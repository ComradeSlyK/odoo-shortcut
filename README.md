# odoo-shortcuts

### How to use this tool

Simply enter the repo we're your working and launch the script you need using
Python3.6 (possibly via your custom virtual environment).

For example, let's say I'd like to create a module name `pizza_delivery` into
some repository. All I have to do is:

```
(venv) user:~$ cd ~/path/to/my/repo
(venv) user:~/path/to/my/repo$ python3 ~/path/to/odoo_shortcuts/module_generator.py -m pizza_delivery
```


Done. The module has been created in a matter of seconds.

### Useful info

1. `-m/--module-name` is the only required flag, and it stores the module
   technical name
2. You don't need to move into your repo every time you need to perform some
   operation: you can do that comfortably from within the odoo_shortcut
   directory. The flag `-r/--repo-path` allows you to specify where your
   operations must be executed; using `-r/--repo-path` flag, the command above
   becomes:
```
(venv) user:~/path/to/odoo_shortcuts$ python3 module_generator.py -m pizza_delivery -r ~/path/to/my/repo 
```
3. However, the easiest way to use this tool is to create a bash alias, ie:
```
# A- add the alias within my .bash_profile
alias generate_odoo_module='/path/to/odoo_shortcuts/venv/bin/python3 /path/to/odoo_shortcuts/module_generator.py'

# B- exit the .bash_profile file and activate it
user:~/path/to/my/repo$ source ~/.bash_profile

# C- simply launch the alias
user:~/path/to/my/repo$ generate_odoo_module -m pizza_delivery

# Of course, A and B don't need to be repeated every time. Just once is enough.
```

4. Creating a new module will always create the proper `__init__.py` files and
add the `icon.png` file within the `static/description/` folder; it will also
properly fill some of the `__manifest__.py` info. Moreover, when generating new
`__init__.py` files for existing module, the copyright header (re)generation
will automatically be triggered. This is possible because these scripts call
each other: this will make everything faster, though it may turn into some
unwanted effects if the scripts are not used properly.  Feel free to take your
time and test them as long as you wish!
