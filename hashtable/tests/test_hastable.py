import pytest
from hash_table.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected


def test_contains_method():
    hashtable = Hashtable()
    hashtable.set("Pedro", "Brown-Hair")
    hashtable.set("Karen", "Blond")
    actual = hashtable.contains("Karen")
    expected = True
    assert actual == expected


def test_key_method():
    hashtable = Hashtable()
    hashtable.set("Pedro", "Brown-Hair")
    hashtable.set("Karen", "Blond")
    hashtable.set("Elena", "Red")
    actual = hashtable.keys()
    expected = ["Karen", "Pedro", "Elena"]
    assert actual == expected


def test_key_does_not_exist():
    hashtable = Hashtable()
    hashtable.set("Pedro", "Brown-Hair")
    hashtable.set("Karen", "Blond")
    hashtable.set("Elena", "Red")
    actual = hashtable.contains("Maria")
    expected = False
    assert actual == expected


def test_collision_is_handled():
    hashtable = Hashtable()
    hashtable.set("Pedro", "Brown-Hair")
    hashtable.set("Pedro", "Violet")
    actual = hashtable.get("Pedro")
    expected = "Violet"
    assert actual == expected


def test_retrieve_a_value_from_a_bucket_within_the_hashtable_that_has_a_collision():
    hashtable = Hashtable()
    hashtable.set(" ", "{")
    hashtable.set(" ", "}")
    hashtable.set(" ", "}")
    hashtable.set(" ", "[")
    actual = hashtable.get(" ")
    expected = "["
    assert actual == expected
