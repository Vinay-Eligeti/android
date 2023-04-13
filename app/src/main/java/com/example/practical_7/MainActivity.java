package com.example.practical_7;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.annotation.SuppressLint;
import android.os.Bundle;
import android.view.ActionMode;
import android.view.ContextMenu;
import android.view.Menu;
import android.view.MenuInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;
public class MainActivity extends AppCompatActivity {
    TextView text1, text2;
    private ActionMode actionMode;
    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        text1 = findViewById(R.id.t1);
        text2 = findViewById(R.id.t2);
        registerForContextMenu(text1);
        text2.setOnLongClickListener(new View.OnLongClickListener() {
            public boolean onLongClick(View view) {
                if (actionMode != null)
                    return false;
                actionMode =MainActivity.this.startActionMode(actionModeCallback);
                view.setSelected(true);
                return true;
            }
        });
    }
    public ActionMode.Callback actionModeCallback=new ActionMode.Callback() {
        @Override
        public boolean onCreateActionMode(ActionMode mode, Menu menu){
            getMenuInflater().inflate(R.menu.menu3,menu);
            return true;
        }
        @Override
        public boolean onPrepareActionMode(ActionMode mode, Menu menu) {
            return false;
        }
        @Override
        public boolean onActionItemClicked(ActionMode mode, MenuItem item) {
            switch (item.getItemId())
            {
                case R.id.item7:
                    Toast.makeText(MainActivity.this,"Edit CAB selected",Toast.LENGTH_LONG);
                    mode.finish();
                    return true;
                case R.id.item8:
                    Toast.makeText(MainActivity.this,"Share CAB selected",Toast.LENGTH_LONG);
                    mode.finish();
                    return true;
                default:
                    return false;
            }
        }
        @Override
        public void onDestroyActionMode(ActionMode mode)
        {
            actionMode= null;
        }
    };

    @Override
    public void onCreateContextMenu(ContextMenu menu, View v, ContextMenu.ContextMenuInfo menuInfo)
    {
        super.onCreateContextMenu(menu, v, menuInfo);
        getMenuInflater().inflate(R.menu.menu2, menu);
    }

    @Override
    public boolean onContextItemSelected(@NonNull MenuItem item)
    {
        switch (item.getItemId())
        {
            case R.id.item4:
                Toast.makeText(this, "Edit Context menu Selected", Toast.LENGTH_LONG);
                return true;
            case R.id.item5:
                Toast.makeText(this, "Share Context menu Selected", Toast.LENGTH_LONG);
                return true;
            case R.id.item6:
                Toast.makeText(this, "Delete Context menu Selected", Toast.LENGTH_LONG);
                return true;
            default:
                return super.onOptionsItemSelected(item);
        }
    }
    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        super.onCreateOptionsMenu(menu);
        getMenuInflater().inflate(R.menu.menu1, menu);
        return true;
    }
    @Override
    public boolean onOptionsItemSelected(@NonNull MenuItem item)
    {
        switch (item.getItemId())
        {
            case R.id.item1:
                Toast.makeText(this, "Search Option menu Selected", Toast.LENGTH_LONG);
                return true;
            case R.id.item2:
                Toast.makeText(this, "Cart Option menu Selected", Toast.LENGTH_LONG);
                return true;
            case R.id.item3:
                Toast.makeText(this, "Settings Option menu Selected", Toast.LENGTH_LONG);
                return true;
            default:
                return super.onContextItemSelected(item);
        }
    }
}

/*
Practical-1
def matrix_multiplication(array1,array2):
    m=len(array1)
    n=len(array1[0])
    p=len(array2)
    q=len(array2[0])
    l=[[0 for i in range(m)]for i in range(q)]
    if n==p:
        for i in range(m):
            for j in range(q):
                for k in range(n):
                    l[i][j]=l[i][j]+array1[i][k]*array2[k][j]
        print(l)
    else:
        print("*-*__Sorry__ can't invalid??")        
matrix_multiplication([[1,2],[3,4]],[[5,6],[5,6]])

Practical-2
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]
    # pointer for greater element
    i = low - 1
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    # Return the position from where partition is done
    return i + 1
# function to perform quicksort
def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)

        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
data = [1, 7, 4,5,7]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)

Practical-3
def mergesort(mylist):
    print("dividing:",mylist)
    if(len(mylist)>1):
        mid=len(mylist)//2
        leftlist=mylist[:mid]
        rightlist=mylist[mid:]
        mergesort(leftlist)
        mergesort(rightlist)
        i=j=k=0
        while i<len(leftlist) and j<len(rightlist):
            if leftlist[i]<=rightlist[j]:
                mylist[k]=leftlist[i]
                i=i+1
            else:
                mylist[k]=rightlist[j]
                j=j+1
                k=k+1
        while i<len(leftlist):
            mylist[k]=leftlist[i]
            i=i+1
            k=k+1
        while j<len(rightlist):
            mylist[k]=rightlist[j]
            j=j+1
            k=k+1
    print("merging:",mylist)
    return mylist
num=int(input("how many no you want in list:")) 
list1=[int(input())for x in range(num)] 
mergesort(list1)
print("sorted list:",list1)

Practical-4
linear search

Practical-5
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = [1, 3, 5, 7, 9]
target = 7
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} is present at index {result}")
else:
    print(f"Element {target} is not present in the array")

Practical-6
class Node:
    def __init__(self,index):
        self.left=None
        self.right=None
        self.val=index
def insert(root,newnode):
    if root is None:
        root=newnode
    else:
        if root.val<newnode.val:
            if root.right is None:
                root.right=newnode
            else:
                insert(root.right,newnode)
        elif root.val==newnode.val:
            print("Already present",newnode.val)
        else:
            if root.left is None:
                root.left=newnode
            else:
                insert(root.left,newnode)
def inorder(root):
    if root:
        if root.val==None:
            print(end="")
        else:
            inorder(root.left)
            print(root.val,end=" ")
            inorder(root.right)
def preorder(root):
    if root:
        if root.val==None:
            print(end="")
        else:
            preorder(root.left)
            print(root.val)
            preorder(root.right)
def postorder(root):
    if root:
        if root.val==None:
            print(end="")
        else:
            postorder(root.left)
            print(root.val)
            postorder(root.right)
def delete(root,node1):
    if root is None:
        print("Empty tree")
    elif root.val<node1:
        delete(root.right,node1)
    elif root.val>node1:
        delete(root.left,node1)
    else:
        root.val=None
r=Node(10)
insert(r,Node(60))
insert(r,Node(50))
insert(r,Node(40))
insert(r,Node(53))
insert(r,Node(120))
insert(r,Node(120))
delete(r,40)
print("inorder Traversal:")
inorder(r)
# print("preorder Traversal:")
# preorder(r)
# print("postorder Traversal:")
# postorder(r)

Practical-7
class Node:
    def __init__(self,index):
        self.index=index
        self.left=None
        self.right=None
def insert(node,index):
    if node is None:
        return Node(index)
    if index<node.index:
        node.left=insert(node.left,index)
    else:
        node.right=insert(node.right,index)
    return node
def searchminode(node):
    current=node
    while current.left is not None:
        current=current.left
    return current
    
def deletenode(root,index):
    if root is None:
        print("Empty tree")
    if index<root.index:
        root.left=deletenode(root.left,index)
    elif index>root.index:
        root.right=deletenode(root,right,index)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=searchminode(root.right)
        root.index=temp.index
        root.right=deletenode(root.right,temp.index)
    return root
def inorder(root):
    if root:
        if root.index==None:
            print(end="")
        else:
            inorder(root.left)
            print(root.index)
            inorder(root.right)
r=None
r=insert(r,60)
r=insert(r,50)
r=insert(r,90)
r=insert(r,40)
r=insert(r,53)
r=insert(r,120)
r=insert(r,95)
r=insert(r,1200)
r=insert(r,120)
print("Inorder Traversal of a tree is:")
inorder(r)
r=deletenode(r,40)
print("Inorder Traversal of a tree is:")
inorder(r)

Practical-8
graph = {
    '1' : ['2','4','7'],
    '2' : ['3','6'],
    '3' : ['7','4','5'],
    '4' : ['5'],
    '5' : ['7','6'],
    '6' : ['7'],
    '7' : []
    }
visited = []
queue = []

def bfs(visisted, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print (m, end = " ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("Following is the Breadth-First Search")
bfs(visited, graph, '1')

Practical-9
graph = {
    '1' : ['2','4','7'],
    '2' : ['3','6'],
    '3' : ['7','4','5'],
    '4' : ['5'],
    '5' : ['7','6'],
    '6' : ['7'],
    '7' : []
    }

visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("Following is the Depth-First Search")
dfs(visited, graph, '1')

Practical-10
#Write a Python Program for checking whether a given graph g has a simple path from source s to destination d.
graph={'A':['B','C'],'B':['C','D'],'C':[],'D':['C'],'E':['F'],'F':['C']}
def find_all_paths(graph,start,end,path=[]):
    path=path+[start]
    if start==end:
        return [path]
    if start not in graph:
        print("start vertex is not present in the graph")
        return None
    paths=[]
    for node in graph[start]:
        if node not in path:
            newpaths=find_all_paths(graph,node,end,path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
c=find_all_paths(graph,'A','C')
print(c)
count=0
for i in c:
    count+=1
    print("Path",count,"= "+"-->".join(i))

Practical-11
def Selection(array):
    count=0
    for i in range(len(array)):
        index=i
        for j in range(i+1,len(array)):
            if array[index]>array[j]:
                index=j
            count+=1
        array[i],array[index]=array[index],array[i]
    print(count)
    return array
obj=Selection([9,8,7,6,5,4,3,2,1,0])
print(obj)

Practical-12
groups=[]
def largest(list1):
    global groups
    if len(list1)==1:
        return list1[0]
    else:
        left=largest(list1[:len(list1)//2])
        right=largest(list1[len(list1)//2:])
      # print("left",left,"right",right)
        groups.append((left,right))
      # print(groups)
        return max(left,right)
l1=largest([241,1343,315,315])
print("Frist largest is :",l1)
s=[]
for item in groups:
    if l1 in item:
        s.append(min(item))
      # print(s)
print("Second largest is :",max(s))

*/
