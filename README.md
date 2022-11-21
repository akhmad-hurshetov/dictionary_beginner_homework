# Welcome
# Dictionary

Automated grading of homework assignments and tests
- fork this repository
- solve the task
- commit with proper message

# Problems
## count_jobs

  Return the number of users with a given job

**Example 1:**

```Python
Input: ([{'name': 'John', 'job': 'Developer'}, {'name': 'Mary', 'job': 'Developer'}],"Developer")
Output: 2

```
**Constraints:**

  - 0 <= len(data) <= 10^5
  - 0 <= len(data) <= 10^5

## count_users_with_age

  Return the number of users with a given age.

**Example 1:**

```Python
Input: ([{'name': 'John', 'age': 27},{'name':'Mary', 'age': 42}],27)
Output: 1

```
**Constraints:**

  - 0 <= len(data) <= 10^5
  - 0 <= age <= 10^5

## find_int_keys

  Return a list of all keys in a dictionary that are integers.

**Example 1:**

```Python
Input: {'a': 1, 3: 2, 'c': 3,10:'a'}
Output: [3, 10]

```

**Constraints:**

  - 0 <= len(data) <= 10^5

## find_length_of_values

  Return the sum of the length of all values in a dictionary.

**Example 1:**

```Python
Input: {'a': 'abc', 'b': 'def', 'c': 'ghi'}
Output: 9

```

**Example 2:**

```Python
Input: {1: "Khiva", 2: "Namangan", 3: "Samarkand", 4: "Tashkent"}
Output: 30

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## find_max_key

  Return the maximum key in a dictionary.

**Example 1:**

```Python
Input: {1:'a', 2:'b', 3: 'c'}
Output: 3

```
  - 0 <= len(data) <= 10^5

## find_max_value

  Return the maximum value in a dictionary.

**Example 1:**

```Python
Input: {'a': 1, 'b': 2, "c" : 3}
Output: 3

```

**Constraints:**

  - 0 <= len(data) <= 10^5

## get_country_with_least_users

  Return the country with the least users

**Example 1:**

```Python
Input: [{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}]
Output: 'UK'

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## get_country_with_most_users_with_age

  Return the country with the most users with a given age

**Example 1:**

```Python
Input: ([{'name': 'John', 'country': 'USA', 'age': 27}, {'name': 'Mary', 'country': 'UK', 'age': 42}],27)
Output: 'USA'

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## get_country_with_most_users

  Return the country with the most users.

**Example 1:**

```Python
Input:[{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}]
Output: "USA"

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## get_max_age_user_name

  Return the name of the user with the maximum age in a dictionary.

**Example 1:**

```Python
Input: [{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}]
Output: 'Mary'

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## get_min_age_user_name

  Return the name of the user with the minimum age in a dictionary.

**Example 1:**

```Python
Input: [{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}]
Output: 'John'

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## get_user_country

  Return the country of a user with a given name.

**Example 1:**

```Python
Input: ([{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}],"John")
Output: 'USA'

```
**Constraints:**

  - 0 <= len(data) <= 10^5
  - 0 <= len(name) <= 10^5

## get_user_names_with_age_range_and_country

  Return a list of users with a given age range and country

**Example 1:**

```Python
Input: ([{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}],20,30,"USA")
Output: ['John']

```
**Constraints:**

  - 0 <= len(data) <= 10^5
  - 0 <= max_age <= 10^5
  - 0 <= min_age <= 10^5
  - 0 <= len(country) <= 10^5

## get_user_names_with_age_range

  Return a list of users with a given age range

**Example 1:**

```Python
Input: ([{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}],20,30)
Output: ['John']

```
**Constraints:**

  - 0 <= len(data) <= 10^5
  - 0 <= max_age <= 10^5
  - 0 <= min_age <= 10^5

## get_user_names_with_age

  Return a list of users with a given age

**Example 1:**

```Python
Input: ([{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}],27)
Output: ['John']

```
**Constraints:**

  - 0 <= len(data) <= 10^5
  - 0 <= age <= 10^5

## get_user_names

  Return a list of users with a given country

**Example 1:**

```Python
Input: ([{'name': 'John', 'country': 'USA'}, {'name': 'Mary', 'country': 'UK'}],"USA")
Output: ["John"]

```
**Constraints:**

  - 0 <= len(data) <= 10^5
  - 0 <= len(name) <= 10^5

## sum_age_values

  Return the sum of all age values in a dictionary.

**Example 1:**

```Python
Input: [{'name': 'John', 'age': 27}, {'name': 'Mary', 'age': 42}]
Output: 69

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## sum_dict_values

  Return the sum of all values in a dictionary.

**Example 1:**

```Python
Input: {'a': 1, 'b': 2, 'c': 3}
Output: 6

```
**Constraints:**

  - 0 <= len(data) <= 10^5

## sum_even_values

  Return the sum of all even values in a dictionary.
  
**Example 1:**

```Python
Input: {'a': 1, 'b': 2, 'c': 3}
Output: 2

```

**Constraints:**

  - 0 <= len(data) <= 10^5

## sum_float_values

  Return the sum of all float values in dictionary.

**Example 1:**

```Python
Input: {'a': 1, 'b' : 2.5, 'c': 3.0}
Output: 5.5

```

**Constraints:**

  - 0 <= len(data) <= 10^5

# Warning
- don't copy other solutions or any solution
- don't remove comments