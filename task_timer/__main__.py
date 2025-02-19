"""
__main__.py
Aaron Cumming
1/22/2025

This Task Timer is able to time tasks.  
The user can start and end a task, see the current tasks, and
see a time sheet of current and past tasks.
"""

import datetime
from rich.console import Console


class Task:
    """ A Task object has a name, time started, and time completed.  
        It can be called to be marked as completed, compute the current time or total time.
    """


    def __init__(self, name):
        """
        Initializes Task with name, 

        name: The name of the task.
        time_started: The time that the task was started.
        time_completed: When the task is initialized, it is set to None, 
                        since we do not know when it will be completed.
        """
        self.name = name
        self.time_started = datetime.datetime.now()
        self.time_completed = None


    def task_completed(self):
        """ Stores the time when the task was completed."""
        self.time_completed = datetime.datetime.now()

    def current_time(self):
        """ Computes the how long the task has currently been running."""
        current_time = datetime.datetime.now() - self.time_started
        return current_time

    def total_time(self):
        """ Computes the how long the task was."""
        total_time = self.time_completed - self.time_started
        return total_time





def start(list_of_tasks, console):
    """Asks for name and makes a task instance and adds to the list"""

    console.print('\nWhat is the name of your task:', style="bold green")
    name = input()

    started_task = Task(name)
    list_of_tasks.append(started_task)
    console.print(f"[bold yellow]{name}[/bold yellow] task timer is starting now." , style="bold magenta")


def end(list_of_tasks, console):
    """ If end command, ask for name and ends tasks."""

    console.print('\nWhat is the name of your task:', style="bold green")
    name = input()

    # Finds the task to end by name
    cur_task = None
    for task in list_of_tasks:
        if task.name == name and task.time_completed == None:
            cur_task = task
            break

    # If task is not in list, say so and break out
    if cur_task == None:
        console.print(f"Task [bold yellow]{name}[/bold yellow] does not exist", style="bold red")
        return

    # If task was in list, complete it and find total_time
    cur_task.task_completed()
    total_time = cur_task.total_time()
    console.print(f"Total time of the [bold yellow]{name}[/bold yellow] task was: [bold yellow]{total_time}[/bold yellow]" , style="bold magenta")




def current(list_of_tasks, console):
    """Gets current tasks by looping through list, finding current tasks, and computes the time."""

    console.print("\nCurrent tasks:",style="bold green")

    for task in list_of_tasks:
        if task.time_completed == None:
            current_time = task.current_time()
            console.print(f"Current time of the [bold yellow]{task.name}[/bold yellow] task is: [bold yellow]{current_time}[/bold yellow]" , style="bold magenta")



def time_sheet(list_of_tasks, console):
    """Gets current tasks by calling current and completed tasks by finding completed tasks, and computes the time"""
    current(list_of_tasks, console)

    console.print("\nCompleted tasks:",style="bold cyan")
    for task in list_of_tasks:
        if task.time_completed != None:
            console.print(f"Total time of the [bold yellow]{task.name}[/bold yellow] task was: [bold yellow]{task.total_time()}[/bold yellow]" , style="bold magenta")



def done(console):
    """Prints the message before the program is closed."""
    console.print("Bye!!! :D", style="blink bold blue on white")


def help(console):
    """Gives descriptions for the other commands."""
    console.print('\nThere are 6 commands that you can run:', style="bold magenta")
    console.print('[bold cyan]start[/bold cyan] -> Asks for the name of the task, then starts timing the task.', style="bold green")
    console.print('[bold cyan]end[/bold cyan] -> Asks for the name of the task, then ends the task'
                    '\n       and gives the time of the task.', style="bold green")            
    console.print('[bold cyan]current[/bold cyan] -> Gives the current time for all of the current running tasks.', style="bold green")
    console.print('[bold cyan]time sheet[/bold cyan] -> Gives the current time for all of the running tasks,'
                    '\n              and the total time for all the completed tasks.', style="bold green")
    console.print('[bold cyan]done[/bold cyan] -> Ends the program.', style="bold green")
    console.print('[bold cyan]help[/bold cyan] -> Gives descriptions for the other commands.', style="bold green")




def main():
    """This is my main cli which is a Task Timer that is able to time tasks."""

    # Initalize the Console for the rich text prints.
    console = Console()

    # Initalize the list for keeping all of the tasks.
    list_of_tasks = []

    console.print("Hello welcome to Task Timer!!!", style="bold purple")

    # This is main loop and the back-bone of the menu-driven program.
    current_request = 'no'
    while current_request != 'done':

        console.print('\nWhat would you like to do? Please select a command:', style="bold green")
        console.print('start, end, current, time sheet, done, help:', style="bold cyan")
        current_request = input()


        # If start command, ask for name and add the time to the list.
        if current_request == 'start':
            start(list_of_tasks, console)
        
        # If end command, ask for name and end the task
        elif current_request == 'end':
            end(list_of_tasks, console)


        # If time_sheet command, get current tasks and completed tasks by looping through the list.
        elif current_request == 'time sheet':
            time_sheet(list_of_tasks, console)
            
        # If current command, get current tasks by looping through the list.
        elif current_request == 'current':
            current(list_of_tasks, console)

        
        # If done command, closes the program.
        # This is the escape.
        elif current_request == 'done':
            done(console)
            break

        # If help command, gives descriptions for the other commands
        elif current_request == 'help':
            help(console)


        # If commmand not typed correctly, give error message and restart the loop.
        else:
            console.print('Sorry but that is not one of the available commands.', style="red")



if __name__=='__main__':
    main()
