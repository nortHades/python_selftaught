# 1. simple function
def greet():
    """Simple greeting funciton"""
    print("Hello, world!")


# 2. function with parameters
def calculate_area(length, width):
    """Calculate rectangle area"""
    area = length * width
    return area


result = calculate_area(5, 3)
print(f"Area: {result}")


# 3. function with complex parameters
def process_scores(scores):
    """Process a list of scores and return statistics"""
    if not scores:
        return None, None, None

    total = sum(scores)
    average = total / len(scores)
    max_score = max(scores)

    return total, average, max_score


# Usage
student_scores = [85, 92, 78, 96, 87]
total, avg, maximum = process_scores(student_scores)
print(f"Total: {total}, Average: {avg:.2f}, Max: {maximum}")


# 4. parameters and return type
def create_profile(name, age, city="Unknown"):
    """Create user profile"""
    return f"Name: {name}, Age: {age}, City: {city}"


# # Positional arguments
profile1 = create_profile("Alice", 25)

# Keyword arguments
profile2 = create_profile(age=30, name="Bob", city="New York")

# Mixed (positional first, then keyword)
profile3 = create_profile("Charlie", 35, "London")


# *args 和 **kwargs 基础：
def calculate_sum(*numbers):
    """Calculate sum of variable number of arguments"""
    return sum(numbers)


def create_user(**details):
    """Create user with variable keyword arguments"""
    user_info = []
    for key, value in details.items():
        user_info.append(f"{key}: {value}")
    return ", ".join(user_info)


total = calculate_sum(1, 2, 3, 4, 5)  # Result: 15
user = create_user(name="John", age=28, role="developer")


# multiple return values
def analyze_text(text):
    """Analyze text and return multiple statistics"""
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    avg_word_length = sum(len(word) for word in words) / word_count if words else 0

    return word_count, char_count, avg_word_length


# unpacking multiple return values
text = "Python is a powerful programming language"
words, chars, avg_len = analyze_text(text)
print(f"Words: {words}, Characters: {chars}, Avg length: {avg_len:.2f}")
