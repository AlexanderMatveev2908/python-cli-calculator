## Requirements

Build a CLI calculator that:

- Displays a menu with operations: Addition, Subtraction, Multiplication, Division, Exit
- Accepts two numbers from the user
- Validates input (re-prompt on errors)
- Handles division by zero
- Allows multiple calculations until user exits

## Implementation

### Addition

```
Enter your choice: 1
Enter first number: 15.5
Enter second number: 7.3
Result: 22.8
```

### Subtraction

```
Enter your choice: 2
Enter first number: 100
Enter second number: 45
Result: 55.0
```

### Multiplication

```
Enter your choice: 3
Enter first number: 6.5
Enter second number: 8
Result: 52.0
```

### Division

```
Enter your choice: 4
Enter first number: 100
Enter second number: 4
Result: 25.0
```

### Division by Zero

```
Enter your choice: 4
Enter first number: 50
Enter second number: 0
Error: Cannot divide by zero!
```

### Invalid Input

```
Enter first number: abc
Invalid input! Please enter a valid number.
Enter first number: 10
```

### Multiple Calculations

```
Enter your choice: 2
Enter first number: 100
Enter second number: 45
Result: 55.0

Do you want to perform another calculation? (yes/no): yes

Enter your choice: 3
Enter first number: 6.5
Enter second number: 8
Result: 52.0
```

### Exit

```
Enter your choice: 5
Thank you for using Calculator CLI!
```
