class ToDoList:
    def __init__(self):
        self.tasks = []
    def add_task(self,something):
        self.tasks.append(something)
    def remove_task(self,something):
        if not self.tasks:
            raise Exception('No tasks')
        if not something in self.tasks:
            raise Exception('No such task')
        self.tasks.remove(something)
    def remove_task_by_index(self,index):
        if not self.tasks:
            raise Exception('No tasks')
        if index <1 or index > len(self.tasks):
            raise Exception('Index out of range')
        self.tasks.remove(self.tasks[index-1])
    def length(self):
        return len(self.tasks)
    def print_tasks(self):
        if self.length()==0:
            print("No tasks yet")
            return
        for i,task in enumerate(self.tasks,start=1):
            print(i,task)
    def print_task_by_index(self,index):
        if self.length()==0:
            print("No tasks yet")
            return
        if type(index)!=int or index<1 or index>self.length():
            raise Exception('Index out of range')
        print(self.tasks[index-1])
    def check_task(self,task):
        if self.length()==0:
            print("No tasks yet")
            return

        if task in self.tasks:
            i=self.tasks.index(task)
            self.tasks[i]="[x]"+task
            return
        else:
            raise Exception('Task not found')


if __name__ == '__main__':
    td=ToDoList()
    while True:
        print('\n1. Add task')
        print('2. View task by index')
        print('3. Remove task by index')
        print('4. Remove task')
        print('5. Check off task')
        print('6. View all tasks')
        print('7. Exit')

        choice=input('Choose an option: ')
        if choice=='1':
            task=input('Enter task to add: ')
            td.add_task(task)
        elif choice=='2':
            try:
                index=int(input('Enter index of task to display: '))
                td.print_task_by_index(index)
            except ValueError:
                print('Please enter a valid index')
            except Exception as e:
                print(e)
        elif choice=='3':
            try:
                index=int(input('Enter index of task to remove: '))
                td.remove_task_by_index(index)
            except ValueError:
                print('Please enter a valid index')
            except Exception as e:
                print(e)

        elif choice=='4':
            task=input('Enter task to remove: ')
            td.remove_task(task)
        elif choice=='5':
            task=input('Enter task to check: ')
            td.check_task(task)
        elif choice=='6':
            td.print_tasks()
        elif choice=='7':
            break

