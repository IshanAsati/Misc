# enCRYtper

A simple Python implementation of the ROT13 cipher.

## What is ROT13?

ROT13 is a letter substitution cipher that replaces each letter with the letter 13 positions after it in the alphabet.

Example:

```text
hello world
```

becomes:

```text
uryyb jbeyq
```

Applying ROT13 twice returns the original text.

## Features

* Encrypts lowercase English letters using ROT13
* Preserves spaces
* Preserves numbers and punctuation
* Lightweight and dependency-free (uses only Python's standard library)

## Usage

Run the script:

```bash
python enCRYtper.py
```

Enter your text when prompted:

```text
Enter Text: hello world!
```

Output:

```text
uryyb jbeyq!
```

## How It Works

The program:

1. Finds the position of each lowercase letter in the alphabet.
2. Shifts it forward by 13 positions.
3. Wraps around to the beginning of the alphabet when necessary.
4. Leaves spaces, numbers, and punctuation unchanged.

## Example

Input:

```text
chatgpt is cool 123!
```

Output:

```text
pungtcg vf pbby 123!
```

## Future Improvements

* Support uppercase letters
* Encrypt entire strings inside the function
* Add a decode mode
* Refactor using modulo arithmetic (`% 26`)

## License

This project is open source and available under the MIT License.
