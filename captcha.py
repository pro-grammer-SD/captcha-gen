"""

MIT License

Copyright (C) 2025 Soumalya Das

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""

from random import (choice,randint,) # imports

""" The `CaptchaEntity` class """

class CaptchaEntity: # instantiating the `CaptchaEntity` object

    def __init__(self,wm: bool): # __init__ method for a default action to the program
        if wm == True:
            print("Hello from Captcha library!")
        
        elif wm == False:
            pass
        
        else:
            print("Invalid argument was passed to the \"wm\" parameter! It can be either True or False.")

    """Generates the captcha. `kind` parameter can be used to set the type of the captcha. There are 3 kinds: `numeric`, `lettered`, `mixed`"""
    def generate(self, kind: str) -> str: # `generate` function used to generate thee

        lettered_list = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]

        numeric_list = [str(i) for i in range(10)]

        if kind == "numeric":
            return "".join(choice(numeric_list) for _ in range(10))
        
        elif kind == "lettered":
            return "".join(choice(lettered_list) for _ in range(10))
        
        elif kind == "mixed":
            mixed_list = lettered_list + numeric_list
            return "".join(choice(mixed_list) for _ in range(10))
        
        else:
            print("Invalid kind! Please select between `numeric`, `lettered` and `mixed`. ")

"""The END"""