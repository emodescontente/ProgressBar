class Task:
    def __init__(self, type: str, name: str, complement):
        """_summary_

        Args:
            type ("S", "C", "T"): The type of the task. It can be a S (Single), C (Checklist) or T (Timed). For more information of the tasks types, see above.
            name (str): The name of the task.
            complement (int): The Single task complement is a bool that represents if the task is done. The Checklist complement is a integer > 0 that represents how much checks it needs to be considered Done. The Timed complement is a given number of seconds that the task needs to be considered done. Defaults to None.
        """

        self.__type = type.upper()
        self.name = name
        
        assert type.upper() in ['S', 'C', 'T'], f"The type ({self.__type}) of the inserted task: {self} is not supported."
        assert name.strip() != '', f"The task {self} need to have a name assigned to it."
        assert complement is not None, f"The task {self} need to have a complement."
        
        self.complement = complement

        if self.__type == 'C':
            self.checks = 0

        self.__done = False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__type}', '{self.name}', {self.complement})"
    

    def SetTask(self, setter):
        match self.__type:
            case 'S':
                assert type(setter) == bool, f'The setter of the task {self} has to be a bool.'
                self.complement = setter
                self.__done = bool(self.complement)
            case 'C':
                assert type(setter) == int, f'The setter of the task {self} has to be a int.'
                self.checks = setter
                self.__done = self.checks >= self.complement
            case 'T':
                assert type(setter) == bool, f'The setter of the task {self} has to be a bool.'
                self.__done = setter
    
    
    @property
    def done(self):
        return self.__done
    
    @property
    def type(self):
        return self.__type
    
    def ShowTask(self, complemented = False):
        """Returns the task in a legible way.

        Example:

            >>>print(feed_the_cat.ShowTask())
            "S Feed the cat Unfinished"

            >>>print(feed_the_cat.ShowTask(True))
            "S | Feed the cat: Unfinished"
        """

        if self.__type == 'S':
            task = f"| {self.__type} | {self.name}: {'Done' if self.__done else 'Unfinished'}" 
        elif self.__type == 'C':
            task = f"| {self.__type} | {self.name} | {self.checks}/{self.complement} |: {'Done' if self.__done else 'Unfinished'}" 
        else:
            hours, rest = divmod(self.complement, 3600)
            minutes, seconds = divmod(rest, 60)
            time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            task = f"| {self.__type} | {self.name} | {time} |: {'Done' if self.__done else 'Unfinished'}" 

        return task
    
class TaskList:
    
    def __init__(self, name: str, task):
        """A **Task List** instance is a porter of multiple **Task** instances.

        Args:
            name (str): The name of the Task List.
            task (Task, list with Task instances): Task Instance or a list containing ones to start the Task List (pass a hollow list if you want to start a hollow Task List)
        """
        assert isinstance(task, (list, Task)), f'The given argument: {task} is not a Task or list.'

        self.__tasks = []
        self.total_tasks = 0

        if isinstance(task, Task):
            self.__tasks.append(task)
            self.total_tasks += 1
        else:
            for item in task:
                assert isinstance(item, Task), f'The list given as argument: {task} contain instances that are not Task type.'
                self.__tasks.append(item)

            self.total_tasks += len(task)
        
        self.name = name

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__tasks})"
    
    @property
    def tasks(self):
        return self.__tasks
    
    def AddTask(self, task):
        """Adds a Task instance to the task list.

        Args:
            task (Task, list with Task instances): Task Instance or a list containing ones to add the Task List.
        """
        assert isinstance(task, (list, Task)), f'The given argument: {task} is not a Task or list.'

        if isinstance(task, Task):
            self.__tasks.append(task)
            self.total_tasks += 1
        else:
            for item in task:
                assert isinstance(item, Task), f'The list given as argument: {task} contain instances that are not Task type.'
                self.__tasks.append(item)
                self.total_tasks += 1

    def DeleteTask(self, index: int):
        """Deletes a task from the list.
        
        Args:
        index (int): The index of the task to delete."""
        deleted_task = self.__tasks.pop(index)
        self.total_tasks -= 1
        return deleted_task
    
    def ClearList(self):
        """Clears the tasks from list."""
        self.__tasks = []
        self.total_tasks = 0
    
    def ProgressBar(self, full_bar = True, percentage = False, count_checks = False):
        """Returns the **Tasks Progress** as according to they done state (if its true or not) as a legible **progress bar** or the percentage of tasks done (in decimals).

        Args:
            full_bar (bool, optional): Shows a 100 digits scale bar. If False, it shows a 10 digits scale. That does not affect the percentage option. Defaults to True.
            percentage (bool, optional): Returns the percentage of tasks done instead of a bar. Defaults to False.
            count_checks (bool, optional): If checks in [C] tasks counts to the bar, not the done state in general. Defaults to False.

        Returns:
            str | float: Returns a string if the percentage is set to False, or a float if not.
        """
        done_tasks = 0
        checks = 0

        if not count_checks:
            for task in self.__tasks:
                if task.done:
                    done_tasks += 1
        else:
            for task in self.__tasks:
                if task.type == 'C':
                    done_tasks += task.checks
                    checks += task.complement - 1
                    
                else:
                    if task.done:
                        done_tasks += 1

        done_percentage = done_tasks / len(self.__tasks) if not count_checks else done_tasks / (len(self.__tasks) + checks)

        if percentage:
            return done_percentage
        else:
            if full_bar:
                bar = f"[{'█' * int(done_percentage * 100)}{'▒' * (100 - int(done_percentage * 100))}]"
            else:
                bar = f"[{'█' * int(done_percentage * 10)}{'▒' * (10 - int(done_percentage * 10))}]"

            return bar