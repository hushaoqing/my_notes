# Hidden features of Python (from [Stackoverflow](https://stackoverflow.com/questions/101268/hidden-features-of-python))


## Chaining comparison operators
```
x = 5
1 < x < 5
x < 10 < x*10 < 100
10 > x <= 9
5 == x > 4
```
## Get the python regex parse tree to debug your regex
```
re.compile("^\[font(?:=(?P<size>[-+][0-9]{1,2}))?\](.*?)[/font]", re.DEBUG)
```
