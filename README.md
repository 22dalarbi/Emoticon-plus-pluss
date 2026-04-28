<div align="center">
  <h1>Emoticon ++</h1>
</div>
<p align="center">
<img width="720" height="720" alt="image" src="https://github.com/user-attachments/assets/0ea6f6c3-5c52-49cd-baf4-419a85731fc7" />
</p>
<h1>Overview</h1>Emoticon++ is a high-level, interpreted language built on Python. It replaces traditional, rigid syntax with ASCII emoticons to make coding more expressive. Programs are saved with the .emo extension and focus on the "vibe" of the logic rather than just the math.

<h1>Demo Code:</h1>

```
:) greeting OwO +Hello world!+ ~
:) base_number o_o 10 ~
:) adder o_o 5 ~

xD greeting ~

(⊙_⊙) Adding the two integers together (⊙_⊙)
:/ base_number base_number + adder ~

xD +The total is:+ ~
xD base_number ~
```
<h1>Demo Code Output:</h1>

```
Hello world!
The total is:
15

```

<h1>Reserved Words</h1>

| Emoticon | Description              | 
|----------|--------------------------|
| `:)`     | Declare a new variable   | 
| `:/`     | Manipulate a variable    | 
| `:(`     | If statement             | 
| `:|`     | Else statement           | 
| `@@`     | Define loop              |
| `xD`     | Print to screen          | 
| `~`      | End of line              | 
| `[`      | Start code block         | 
| `]`      | End code block           |
| `+`      | String delimiter         | 
|`(⊙_⊙)` | Comment                  |

<h1>Syntax Rules</h1>

-Line Termination: All functional lines must end with the ~ character.

-String Encapsulation: Strings begin and end with the + character.

-Code Blocks: Logic for if statements and loops must be contained within [ and ].

-Comments: Single-line comments are ignored by the interpreter and begin with //.

-The "Vibe" Rule (Unique Feature): The interpreter calculates the "mood" of the file. If there are more happy faces :) than sad faces :(, the program runs in Optimistic Mode, automatically defaulting uninitialized variables to 0 instead of throwing an error.

<h1>Variable Types:</h1>


| Emoticon | Description              | Equivalent Logic |
|----------|--------------------------|------------------|
| `o_o`    | Integer (Number)         |  `int`           |
| `OwO`    | String (Text)            |  `str`           | 
| `^-^`    |Boolean (True/False)      |  `bool`          |



<h1>Valid Grammars</h1>

1. `:) [varName] [varType] [value] ~`  
   *(Standard variable declaration)*

2. `:) [varName] [varType] +[stringValue]+ ~`  
   *(String variable declaration using sparkles)*

3. `:/ [varName] [number] ~`  
   *(Directly updating a variable to a new number)*

4. `:/ [varName] [varName] [mathOperator] [number] ~`  
   *(Variable manipulation with math)*

5. `xD [varName] ~`  
   *(Printing the value of a variable)*

6. `xD +[stringValue]+ ~`  
   *(Printing a raw string)*

7. `@@ [number] [ [code] ]`  
   *(Fixed-count loop)*

8. `@@ [varName] [ [code] ]`  
   *(Looping based on a variable’s value)*

9. `:( [condition] ) [ [code] ]`  
   *(If statement block)*

10. `:| [ [code] ]`  
    *(Else statement block)*

11. `(o_o) [comment text] (o_o)`  
    *(Stunned face comment wrapper)*

12. `:) [varName] [varType] [varName] [mathOperator] [varName] ~`  
    *(Declaring a variable as the result of math between two others)*
