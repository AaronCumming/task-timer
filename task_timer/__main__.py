"""
__main__.py
Aaron Cumming
1/22/2025

The output of the project can be edited in this file.
"""
import click
import datetime
from rich.console import Console

@click.command()
def main():
    """This is my main cli"""

    console = Console()


    current_list_of_tasks = {}
    completed_list_of_tasks = {}

    console.print("Hello welcome to Task Timer!!!", style="bold purple")

    current_request = 'no'
    while current_request != 'done':

        console.print('\nWhat would you like to do? Please select a command:', style="bold green")
        console.print('start, end, current, time_sheet, done:', style="bold cyan")
        current_request = input()
        if current_request == 'start':
            console.print('\nWhat is the name of your task:', style="bold green")
            name = input()
            current_time = datetime.datetime.now()
            current_list_of_tasks[name] = current_time
            console.print(f"[bold yellow]{name}[/bold yellow] task timer is starting now." , style="bold magenta")
        
        elif current_request == 'end':
            console.print('\nWhat is the name of your task:', style="bold green")
            name = input()
            end_time = datetime.datetime.now()
            start_time = current_list_of_tasks[name]
            total_time = end_time - start_time
            completed_list_of_tasks[name] = total_time
            console.print(f"Total time of the [bold yellow]{name}[/bold yellow] task was: [bold yellow]{total_time}[/bold yellow]" , style="bold magenta")

            del current_list_of_tasks[name]




        elif current_request == 'time_sheet':
            print("\nCurrent tasks:")
            for key, value in current_list_of_tasks.items():
                end_time = datetime.datetime.now()
                total_time = end_time - value
                print(f"Current time of the {key} task is: {total_time}")

            print("\nCompleted tasks:")
            for key, value in completed_list_of_tasks.items():
                print(f"Total time of the {key} task was: {value}")
            


        elif current_request == 'current':
            print("\nCurrent tasks:")
            for key, value in current_list_of_tasks.items():
                end_time = datetime.datetime.now()
                total_time = end_time - value
                print(f"Current time of the {key} task is: {total_time}")



        elif current_request == 'done':
            print("Bye!!! :D")
            break

        
        else:
            console.print('Sorry but that is not one of the available commands.', style="red")



if __name__=='__main__':
    main()
