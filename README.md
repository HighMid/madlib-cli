## LAB - Class 03
- **Project: madlib-cli**

- **Author: DeAndre Ordonez**

### Links and Resources - N/A

### Setup - N/A

### PORT - N/A

### DATABASE_URL - N/A

### How to initialize/run your application - python test_madlib.py

### How to use your library - N/A

### Tests

1. How do you run tests?

    - Using pytest, provided functions in test_madlib.py to test the logic in madlib.py .

    - Tested 
        1. **test_read_template_returns_stripped_string** - returned full template
        2. **test_parse_template** - returned stripped parts
        3. **test_merge** - returned complete template with stripped parts
        4. **test_read_template_raises_exception_with_bad_path** - tested to see if the exception was handled

2. Any tests of note?

    - Had to limit my scope, was getting a little to into the story telling, the tests were pretty straightforward overall.

3. Describe any tests that you did not complete, skipped, etc

    - All tests complete but the story isn't :C