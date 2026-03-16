class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Lnklst:
    def __init__(self):
        self.head=None
    
    def insert_at_begin(self,data):
        node=Node(data,self.head)
        self.head=node
    
    def insert_at_end(self,data):
        if self.head==None:
            self.head=Node(data,None)
        else:
            tmp=self.head
            while tmp.next is not None:
                tmp=tmp.next
            tmp.next=Node(data,None)


    def display(self):
        st=""
        if not self.head:
            print("list is empty")
        else:
            tmp=self.head
            
            while tmp:
                st+=str(tmp.data)+'-->'
                # print(tmp.data,'-->')
                tmp=tmp.next
        print(st)

if __name__=='__main__':
    print('started')
    ll=Lnklst()
    # ll.insert_at_begin(1)
    # ll.insert_at_begin(2)
    # ll.insert_at_begin(3)
    # ll.insert_at_begin(4)
    # ll.display()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.display()