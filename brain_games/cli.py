#!/usr/bin/env python
import prompt

def welcome_user():
    name = prompt.string("Make I have your name?")
    print(f"Hello,{name}!")


