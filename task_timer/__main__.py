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

def main():
    """This is my main cli"""

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
        console.print('start, end, current, time sheet, done:', style="bold cyan")
        current_request = input()


        # If start command, ask for name and add the time to the current task dict.
        if current_request == 'start':
            console.print('\nWhat is the name of your task:', style="bold green")
            name = input()

            current_time = datetime.datetime.now()
            current_list_of_tasks[name] = current_time
            console.print(f"[bold yellow]{name}[/bold yellow] task timer is starting now." , style="bold magenta")
        

        # If end command, ask for name and add the total time to the completed task dict.
        # And remove this task from current tasks dict.
        elif current_request == 'end':
            console.print('\nWhat is the name of your task:', style="bold green")
            name = input()

            end_time = datetime.datetime.now()
            start_time = current_list_of_tasks[name]
            total_time = end_time - start_time
            completed_list_of_tasks[name] = total_time
            del current_list_of_tasks[name]
            console.print(f"Total time of the [bold yellow]{name}[/bold yellow] task was: [bold yellow]{total_time}[/bold yellow]" , style="bold magenta")



        # If time_sheet command, get current tasks and completed tasks by looping through both dicts.
        elif current_request == 'time sheet':
            console.print("\nCurrent tasks:",style="bold green")
            for key, value in current_list_of_tasks.items():
                current_time = datetime.datetime.now()
                total_time = current_time - value
                console.print(f"Current time of the [bold yellow]{key}[/bold yellow] task is: [bold yellow]{total_time}[/bold yellow]" , style="bold magenta")

            console.print("\nCompleted tasks:",style="bold cyan")
            for key, value in completed_list_of_tasks.items():
                console.print(f"Total time of the [bold yellow]{key}[/bold yellow] task was: [bold yellow]{value}[/bold yellow]" , style="bold magenta")

            

        # If current command, get current tasks by looping through current task dict.
        elif current_request == 'current':
            console.print("\nCurrent tasks:",style="bold green")
            for key, value in current_list_of_tasks.items():
                current_time = datetime.datetime.now()
                total_time = current_time - value
                console.print(f"Current time of the [bold yellow]{key}[/bold yellow] task is: [bold yellow]{total_time}[/bold yellow]" , style="bold magenta")


        # If done command, closes the program.
        # This is the escape.
        elif current_request == 'done':
            console.print("Bye!!! :D", style="blink bold blue on white")
            break

        # If commmand not typed correctly, give error message and restart the loop.
        else:
            console.print('Sorry but that is not one of the available commands.', style="red")



if __name__=='__main__':
    main()
