import pandas as pd
import random

# Generate random numbers
random_numbers_1 = [random.randint(1, 100) for _ in range(10)]  # Generates 10 random integers between 1 and 100
random_numbers_2=[random.randint(1,100) for _ in range(10)]
random_numbers_3=[random.randint(1,100) for _ in range(10)]
random_numbers_4=[random.randint(1,100) for _ in range(10)]
# Create a DataFrame from the random numbers
df = pd.DataFrame({'Column 1': random_numbers_1, 'Column 2': random_numbers_2, 'column 3': random_numbers_3, 'Column 4': random_numbers_4})

# Export DataFrame to Excel
df.to_excel('random_numbers.xlsx', index=False)
print(df.to_string())
