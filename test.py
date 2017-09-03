from example import add, Pet


def test_add():
    assert add(2, 3) == 5


def test_pet():
    my_dog = Pet('Pluto', 5)
    assert my_dog.get_name() == 'Pluto'
    assert my_dog.get_hunger() == 5
    my_dog.go_for_a_walk()
    assert my_dog.get_hunger() == 6
