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


def start(current_list_of_tasks1, console):
    """Asks for name and adds the time to the current task dict"""
    console.print('\nWhat is the name of your task:', style="bold green")
    name = input()

    current_time = datetime.datetime.now()
    current_list_of_tasks1[name] = current_time
    console.print(f"[bold yellow]{name}[/bold yellow] task timer is starting now." , style="bold magenta")


def end(current_list_of_tasks, completed_list_of_tasks, console):
    """ If end command, ask for name and ends tasks.
    
        It does this by seeing if the name exists in the current dict,
        then if it does adds the total time to the completed task dict,
        and removes this task from current tasks dict.
        If name does not exists, says that it does not and exits the function.
    """
    console.print('\nWhat is the name of your task:', style="bold green")
    name = input()

    # Sees if the task exists in the current dict
    try:
        current_list_of_tasks[name]
    # If not, prints out that it does not exist
    except:
        console.print(f'Sorry but [bold yellow]{name}[/bold yellow] task does not exist.', style="red")
    # If it does exist, adds the total time to the completed task dict
    # and removes the task from current tasks dict
    else:
        end_time = datetime.datetime.now()
        start_time = current_list_of_tasks[name]
        total_time = end_time - start_time
        completed_list_of_tasks[name] = total_time

        current_list_of_tasks.pop(name)
        console.print(f"Total time of the [bold yellow]{name}[/bold yellow] task was: [bold yellow]{total_time}[/bold yellow]" , style="bold magenta")



def current(current_list_of_tasks, console):
    """Gets current tasks by looping through current task dict"""
    console.print("\nCurrent tasks:",style="bold green")
    for key, value in current_list_of_tasks.items():
        current_time = datetime.datetime.now()
        total_time = current_time - value
        console.print(f"Current time of the [bold yellow]{key}[/bold yellow] task is: [bold yellow]{total_time}[/bold yellow]" , style="bold magenta")


def time_sheet(current_list_of_tasks, completed_list_of_tasks, console):
    """Gets current tasks by calling current and completed tasks by looping through completed dict."""
    current(current_list_of_tasks, console)

    console.print("\nCompleted tasks:",style="bold cyan")
    for key, value in completed_list_of_tasks.items():
        console.print(f"Total time of the [bold yellow]{key}[/bold yellow] task was: [bold yellow]{value}[/bold yellow]" , style="bold magenta")


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

    # Initalize the dicts for keeping the current and completed tasks.
    current_list_of_tasks = {}
    completed_list_of_tasks = {}

    console.print("Hello welcome to Task Timer!!!", style="bold purple")

    # This is main loop and the back-bone of the menu-driven program.
    current_request = 'no'
    while current_request != 'done':

        console.print('\nWhat would you like to do? Please select a command:', style="bold green")
        console.print('start, end, current, time sheet, done, help:', style="bold cyan")
        current_request = input()


        # If start command, ask for name and add the time to the current task dict.
        if current_request == 'start':
            start(current_list_of_tasks, console)
        
        # If end command, ask for name and add the total time to the completed task dict.
        # And remove this task from current tasks dict.
        elif current_request == 'end':
            end(current_list_of_tasks, completed_list_of_tasks, console)


        # If time_sheet command, get current tasks and completed tasks by looping through both dicts.
        elif current_request == 'time sheet':
            time_sheet(current_list_of_tasks, completed_list_of_tasks, console)
            
        # If current command, get current tasks by looping through current task dict.
        elif current_request == 'current':
            current(current_list_of_tasks, console)

        
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
