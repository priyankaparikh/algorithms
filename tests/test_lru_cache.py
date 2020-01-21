from LRU_cache.lru_cache import dlNode, LRUCache

def testdlNode():
    """ test the Node object of a double linked list"""
    node1 = dlNode(0,0)
    assert not node1.prev
    assert not node1.next
    node2 = dlNode(0,0)
    assert not node2.prev
    assert not node2.next
    node1.next = node2
    node2.prev = node1
    assert node1.next == node2
    assert node2.prev == node1

def test_base_LRU():
    """test the LRU cache ds. It should be instantiated with two nodes and a
    capacity. It should also keep track of it's length ."""

    cache = LRUCache(4)
    assert not cache.head.prev
    assert cache.head.next
    assert cache.head.next.value == 0
    assert cache.tail.prev.value == 0
    assert cache.tail.prev
    assert not cache.tail.next
    assert cache.len == 0
    assert cache.capacity == 4
    assert cache.head
    assert cache.tail


def test_LRU_put():
    cache = LRUCache(4)

    cache.put(1,1)
    assert cache.len == 1
    assert cache.head.next.value == 1
    assert cache.tail.prev.value == 1
    assert cache.tail.value == 0

    cache.put(12, 12)
    assert cache.head.next.value == 12
    assert cache.tail.prev.value == 1
    assert cache.len == 2

#
def test_LRU_get():
    cache = LRUCache(4)
    cache.put(1, 1)
    cache.put(12, 12)

    assert cache.get(12)
    assert cache.get(10) == -1
    assert cache.get(1)
    assert cache.get(4) == -1


def test_pop_least_used():
    cache = LRUCache(4)
    cache.put(1, 1)
    cache.put(12, 12)
    cache.put(10, 10)
    cache.put(899, 899)

    cache.pop_least_used()
    assert cache.tail.prev.value == 12

def test_cache_adjustment():
    cache = LRUCache(4)
    cache.put(1, 1)
    cache.put(12, 12)
    cache.put(10, 10)
    cache.put(899, 899)
    cache.get(1)
    assert cache.head.next.value == 1
    cache.get(12)
    assert cache.head.next.value == 12
    cache.get(10)
    assert cache.head.next.value == 10
