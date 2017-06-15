install selenium

```
pip install selenium
```

Make sure Firefox web browser is installed on the machine, then download (driver)[https://github.com/mozilla/geckodriver/releases] for Firefox.

The driver, geckodriver, needs to accessable from your computer's path.

```
echo $PATH
```

Let's add a new directory to our computer for drivers we manually add.

```
cd
mkdir bin
```

There is now a directory `/Users/<username>/bin` which we should put geckdriver in, but we still need to add this to our path.

```
vim .bash_profle
```
This opens the text editor vim.  (I'll walk students through this.) The goal is to add something that looks like this
```
export PATH=/usr/texbin:/Users/joseph/bin:$PATH
```

Save the file and close it.  Then in the terminal type `source .bash_profile`.

Check to see it's now there `echo $PATH` then `echo geckodriver`.  If it worked we are ready to begin!
