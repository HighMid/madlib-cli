import pytest, os
from madlib_cli.madlib import read_template, parse_template, merge


def test_read_template_returns_stripped_string():
    actual = read_template("madlib_cli/madlib_template.txt")
    expected = """Welcome to the Void of MadLib!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!"""

    assert actual == expected


def test_parse_template():
    template = """Welcome to the Void of MadLib!

I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!"""
    expected_stripped = "Welcome to the Void of MadLib!\n\nI the {} and {} {} have {} {}'s {} sister and plan to steal her {} {}!"
    expected_parts = ("Adjective", "Adjective", "A First Name", "Past Tense Verb", "A First Name", "Adjective", "Adjective", "Plural Noun")

    actual_stripped, actual_parts = parse_template(template)

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts



def test_merge():
    stripped_template = "Welcome to the Void of MadLib!\n\nI the {} and {} {} have {} {}'s {} sister and plan to steal her {} {}!"
    user_inputs = ["scary", "funny", "Bob", "jumped", "Alice", "beautiful", "red", "apples"]
    expected = """Welcome to the Void of MadLib!

I the scary and funny Bob have jumped Alice's beautiful sister and plan to steal her red apples!"""

    actual = merge(stripped_template, user_inputs)
    
    assert actual == expected



def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)
