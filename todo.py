import time

''' This is my Todo List app. you can add, delete, view tasks '''

task_list = {1:'Take out garbage',
             2:'Walk the Dog' }


def banner():
    print('#'*31)
    print('#'*9,' TODO LIST ','#'*9)
    print('#'*31)
    return

def menu():
    print("1: View Tasks")
    print("2: Add Tasks")
    print("3: Delete Tasks")
    print('q: Quit')
    print('\n\n')
    return

def view_tasks(tasks):
    print('#'*31)
    print('#'*9,' View ','#'*9)
    print('#'*31)
    if tasks == {}:
        print("You have no tasks!\n\n")
        return None
    else:
        for key,value in tasks.items():
            print(key, value)
        print('\n\n')
    time.sleep(2)

def get_menu_choice():
    choice = input("1,2,3 or q: ")    
    return choice    

def add_task(tasks):    
    print('#'*31)
    print('#'*9,' ADD ','#'*9)
    print('#'*31)
    if tasks == {}:
        new_task_id = 1
    else:
        new_task_id = (list(tasks)[-1]) + 1
    new_task = input('Enter new task: ')
    tasks[new_task_id] = new_task      
    return print('Task added!\n\n')

def delete_task(tasks):
    print('#'*31)
    print('#'*9,' DELETE ','#'*9)
    if tasks == {}:
        return print('No tasks to delete!')
    else:
        for k,v in tasks.items():
            print(f'{k}: {v}')
        print('#'*31)
        task_num = int(input("Which task to delete: "))
        del tasks[task_num]
        print('Task Deleted')
        print('\n\n')
    return None

    


def main():
    
    while True:
        banner()
        menu()        
        my_choice = get_menu_choice()        
        match my_choice:            
            case '1':
                view_tasks(task_list)                
            case '2':
                add_task(task_list)
            case '3':
                delete_task(task_list)
            case 'q':
                break
                



main()
print("End of Todo")