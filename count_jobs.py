def count_jobs(data:list, job:str) -> int:
    """
    Return the number of users with a given job

    Args:
        data (dict): A dictionary of values
        job (str): The job to search for
    Returns:
        int: The number of users with the given job
    """
    
    pass

    x=0
    for i in data:
        if i['job']==job:
            x+=1
    return x


print(count_jobs([
    {'name': 'John', 'job': 'Developer'},
    {'name': 'Mary', 'job': 'Developer'},
    {'name': 'Akhmad', 'job': 'Student'},
    {'name': 'Ulugbek', 'job': 'Developer'}], 
    "Developer"
    ))