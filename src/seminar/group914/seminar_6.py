"""
Write an application that manages a group of students.
Each student has a unique id (string), a name (string) and a grade (integer).
The application will have a menu-driven user interface and will provide the following features:

    1. Add a student
        - adds the student with the given id, name and grade to the list.
        - error if giving existing id, the name or grade fields not given or
        empty

    2. Delete a student
        - deletes the student with the given id from the list
        - error if non-existing id given

    3. Show all students
        - shows all students in descending order of their grade

    4. Show students whose grade is > than given one, ordered in descending order of grade

    5. exit
        - exit the program

    Observations:
        - Add 10 random students at program startup
        - Create a list-based and a dict-based representation of the Student entity
        - Write specifications for non-UI functions
        - Write tests for the non-trivial, non-UI functions
        - Use TypeError and ValueError to handle input and program errors
        - Each function does one thing only, and communicates via parameters and return value
        - The program reports errors to the user. It must also report errors from non-UI functions!
        - Make sure you understand the student's representation
        - Try to reuse functions across functionalities (Less code to write and test)
        - Don't use global variables!
"""

"""
    Student representation functions are below 
"""


def create_student(student_id: int, student_name: str, student_grade: int):
    """
    Create a student entity
    :param student_id: The unique identifier of the student
    :param student_name: The student's name (must have at least 3 character)
    :param student_grade: An integer between 1 and 10
    :return: The student entity represented as a dict
    """
    if len(student_name) < 3:
        raise ValueError("Student name must have at least 3 characters - " + student_name)
    if 1 > student_grade or 10 < student_grade:
        raise ValueError("Student grade must be between 1 and 10, but was given as " + str(student_grade))
    return {"id": student_id, "name": student_name, "grade": student_grade}


def get_id(student) -> int:
    """
    Returns the student's id
    :param student: The student entity
    :return: The id
    """
    return student["id"]


def get_name(student) -> str:
    return student["name"]


def get_grade(student) -> int:
    return student["grade"]


"""
    Test function should take no arguments and return nothing because they need to be independent
    Test functions should be runnable in any order 
"""


def test_student():
    s = create_student(100, "Pop Ioana", 9)
    """
    The assert keyword 101
        assert <condition>
        if <condition> is True than nothing happens ... yay :)
        if <condition> is False an AssertionError is raised :( - we expect it to stop the program
    """
    assert get_id(s) == 100
    assert get_name(s) == "Pop Ioana"
    assert get_grade(s) == 9

    try:
        s = create_student(100, "A", 9)
        """
        In case the line above does not raise the expected ValueError, then the line below runs and will
        generate the AssertionError, failing the test
        """
        assert False
    except ValueError as ve:
        """
        The line below doesn't do anything really, but tells whoever is looking at the code that this is 
        expected behaviour
        """
        assert True
    # TODO Add checks for the student grade ...


test_student()

"""
    What happens in case incorrect data is provided to create_student?
    1. The first check raises ValueError
    2. The create_student function returns immediately with the ValueError exception that was raised
    3. The assignment x = create_student(...) is not executed
    4. All the functions on the call stack return until one of two things happen:
        4.1 If no function can handle the ValueError, the program exits and you get an error message :(
        4.2 In case we have a try ... except that handles the ValueError, then the execution resumes at the
            except ... block
"""

# try:
#     x = create_student(100, "Ana", 80)
#     print(x)
# except ValueError as ve:  # the as keyword creates an alias
#     print(ve)

"""
    Program functionalities (non-UI) are below
"""

"""
    UI code is below
"""
