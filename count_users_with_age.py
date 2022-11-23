def count_users_with_age(data:list, age:int) -> int:
    """
    Return the number of users with a given age

    Args:
        data (dict): A dictionary of values
        age (int): The age to search for
    Returns:
        int: The number of users with the given age
    """
    pass

    count=0
    for i in data:
        if i['age']==age:
            count+=1
    return count

print(count_users_with_age(
    [{'name': 'John', 'age': 27},
    {'name':'Mary', 'age': 42}],42)
)