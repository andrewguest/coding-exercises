## Build your own `wc` tool

This challenge is to build your own version of the Unix command line tool wc!

The Unix command line tools are a great metaphor for good software engineering and they follow the Unix Philosophies of:

- Writing simple parts connected by clean interfaces - each tool does just one thing and provides a simple CLI that handles text input from either files or file streams.
- Design programs to be connected to other programs - each tool can be easily connected to other tools to create incredibly powerful compositions.

---

### The Challenge - Building `wc`
The functional requirements for wc are concisely described by it’s man page - give it a go in your local terminal now:
```shell
man wc
```
The TL/DR version is: `wc` – word, line, character, and byte count.

---

### Step 1
In this step your goal is to write a simple version of wc, let’s call it `ccwc` (cc for Coding Challenges) that takes the command line option `-c` and outputs the number of bytes in a file.

If you’ve done it right your output should match this:

```shell
>ccwc -c test.txt
342190 test.txt
```

---

### Step 2
In this step your goal is to support the command line option `-l` that outputs the number of lines in a file.

If you’ve done it right your output should match this:

```shell
>ccwc -l test.txt
7145 test.txt
```

---

### Step 3
In this step your goal is to support the command line option `-w` that outputs the number of words in a file. If you’ve done it right your output should match this:

```shell
>ccwc -w test.txt
58164 test.txt
```

---

### Step 4
In this step your goal is to support the command line option `-m` that outputs the number of characters in a file. If the current locale does not support multibyte characters this will match the `-c` option.

For this one your answer will depend on your locale, so if can, use wc itself and compare the output to your solution:

```shell
>wc -m test.txt
339292 test.txt

>ccwc -m test.txt
339292 test.txt
```

---

### Step 5
In this step your goal is to support the default option - i.e. no options are provided, which is the equivalent to the `-c`, `-l` and `-w` options. If you’ve done it right your output should match this:

```shell
>ccwc test.txt
7145   58164  342190 test.txt
```

---

### Final step
In this step your goal is to support being able to read from standard input if no filename is specified. If you’ve done it right your output should match this:

```shell
>cat test.txt | ccwc -l
7145
```

---

## Implementations
|Language| Step 1             |Step 2|Step 3|Step 4|Step 5|Final step|
|---|--------------------|---|---|---|---|---|
|Python| :black_square_button: |:black_square_button:|:black_square_button:|:black_square_button:|:black_square_button:|:black_square_button:|
|Go| :black_square_button:|:black_square_button:|:black_square_button:|:black_square_button:|:black_square_button:|:black_square_button:|