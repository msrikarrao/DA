### WORKING WITH NUMBERS
- Floating point numbers have limit significant digits.
- Floating point numbers is an approximate value that can yeild unexpected results known as floating point errors.

### Math module
- Students should explore this module
- The math module function
    pow()
    sqrt()
    ceil()
    floor()
    pi

### Formating numbers
- The `format()` method of string is used to format a single value or a series of values by converting them to strings.

### The format method
Syntax:
```
"...{:format>specifier}...".format(data_item, ...)
```

### The syntax for the format_specification
[field_width][comma][.decimal_places][type_code]

- command type codes
    - d (integers)
    - f (floating point)
    - s (strings)
    - % (percentage)
    - e (exponential)

< is for left allignment
> is for right allignment
^ is for 

### WORKING WITH DECIMAL NUMBERS
- Use the `decimal` module to create decimal numbers that are exact when and don't yield unexpected results
- We use `Decimal` class from `decimal` module to create decimal numbers, and also we import rounding constants that we need from the decimal module.
- To create a Decimal object that stores a decimal numbers, pass a string for the decimal number to the constructor ('Decimal(string)') of the Decimal class.
- It's illegal to code expressions with mixing Decimal with int values. However, it's illegal to code expressions that mix Decimal objects with float values.
