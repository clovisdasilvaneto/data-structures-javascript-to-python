def linkedList():
    head = {}
    tail = {}

    def initializeList(node):
        nonlocal head
        nonlocal tail
        head = node
        tail = head

    def createNode(value):
        return {
            'next': dict(),
            'value': value
        }

    def addNode(value):
        nonlocal head
        nonlocal tail
        node = createNode(value)

        if bool(head) == False:
            initializeList(node)
            return

        tail['next'] = node
        tail = tail['next']

    def prependNode(value):
        nonlocal head
        nonlocal tail
        node = createNode(value)

        if bool(head) == False:
            initializeList(node)
            return
        
        node['next'] = head
        head = node

    def getList():
        return { 
            'head': head,
            'tail': tail
         }

    def search(value):
        nonlocal head

        if bool(head) == False:
            return
        
        current = head
        result = None

        while result == None and bool(current) == True:
            if current['value'] == value:
                result = current
            
            current = current['next']
        
        return result

    def traverse(_callback = None):
        nonlocal head
        current = head

        while bool(current) == True:
            if _callback:
                _callback(current)
            
            current = current['next']

    def reverseTraversal(_callback = None):
        nonlocal tail
        nonlocal head
        current = tail

        while current['value'] != head['value']:
            prev = head

            while prev['next']['value'] != current['value']:
                prev = prev['next']
            
            if _callback:
                _callback(current)

            current = prev
        
        _callback(current)

    return {
        'getList': getList,
        'createNode': createNode,
        'prependNode': prependNode,
        'addNode': addNode,
        'traverse': traverse,
        'reverseTraversal': reverseTraversal,
        'search': search
    }

myList = linkedList()
myList['addNode'](2)
myList['addNode'](3)
myList['prependNode'](1)


def printListValues(item):
    print('printed value: ', item['value'])

# myList['traverse'](printListValues)
myList['reverseTraversal'](printListValues)

print('Founded valued:')
print(myList['search'](21))