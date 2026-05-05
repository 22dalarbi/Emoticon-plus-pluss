<div align="center">
  <h1>Emoticon ++</h1>
</div>
<p align="center">
<img width="720" height="720" alt="image" src="https://github.com/user-attachments/assets/0ea6f6c3-5c52-49cd-baf4-419a85731fc7" />
</p>
<h1>Overview</h1>Emoticon++ is a high-level, interpreted language built on Python. It replaces traditional, rigid syntax with ASCII emoticons to make coding more expressive. Programs are saved with the .emo extension and focus on the "vibe" of the logic rather than just the math. Using the extension .emo.

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



<h1>Valid Grammar</h1>

```ebnf
(* High-level program structure *)
program         = { statement } ;
statement       = ( declaration
                  | assignment
                  | print
                  | loop
                  | condition
                  | comment ) "~" ;

(* Variable Declarations *)
declaration     = ":)" , identifier , type , expression ;
type            = "o_o"             (* number  *)
                | "OwO"             (* string  *)
                | "^-^" ;           (* boolean *)

(* Variable Manipulation *)
assignment      = ":/" , identifier , expression ;

(* Output *)
print           = "xD" , ( identifier | string ) ;

(* Control Structures *)
condition       = ":(" , logical_expr , ")" ,
                  "[" , { statement } , "]" ,
                  [ ":|" , "[" , { statement } , "]" ] ;

loop            = "@_@" , ( integer | identifier ) ,
                  "[" , { statement } , "]" ;

(* Expressions *)
expression      = value | ( value , binary_op , value ) ;
logical_expr    = value , comp_op , value ;
value           = identifier | integer | string | boolean ;

(* Operators *)
binary_op       = "+" | "-" | "*" | "/" ;
comp_op         = "==" | "!=" | ">" | "<" | ">=" | "<=" ;

(* Terminals *)
identifier      = letter , { letter | digit } ;
string          = "+" , { character } , "+" ;
integer         = [ "-" ] , digit , { digit } ;
boolean         = "✅" | "❌" ;
comment         = "(⊙_⊙)" , { character } , "(⊙_⊙)" ;
` ` `
```

---



12. `:) [varName] [varType] [varName] [mathOperator] [varName] ~`  
    *(Declaring a variable as the result of math between two others)*
