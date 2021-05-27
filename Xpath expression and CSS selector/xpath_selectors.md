## Select a tag
```
//tag

# Like
//h1
```


## Class selector
```
//tag[@class="classname"]

# Like 
//div[@class="intro"]
```

## Select an element that is inside a selected class
```
//tag[@class="classname"]/tag

# Like 
//div[@class="intro"]/p
```

## Select more than one element 

```
//tag[@class="classname" or @class="classname2"]

#Like
//div[@class="intro" or @class="outro"]
```

## Select more than one element and their inside element

```
//tag[@class="classname" or @class="classname2"]/tag

#Like
//div[@class="intro" or @class="outro"]/p
```

Note - This all gives along with tage so for getting only text 

## Only select text add /text()

```
//tag[@class="classname" or @class="classname2"]/tag/text()

#Like
//div[@class="intro" or @class="outro"]/p/text()
```
## Select on the basis of some string which is present at start of a value for an attribute 

```
//tag[starts-with(@href, 'string')]

#Like 
//a[starts-with(@href, 'http')]
```

## Select on the basis of some string which is present at end of a value for an attribute 
```
//tag[ends-with(@href, 'string')]

# Like 
//a[ends-with(@href, 'fr')]
```
## Select on the basis of some string which is present at middle of a value for an attribute 
```
//a[contains(@href, 'google')]

# Like 
//tag[contains(@href, 'string')]
```

or

```
//a[contains(text(), 'Google')]
# This is case sensitive

# Like 
//tag[contains(text(), 'string')]
```

## If we want to get a specific number child of a element like li 

example like 
```
    <ul id="items">
        <li data-identifier="7">Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
        <li>Item 4</li>
    </ul>
```
select using 
```
//tag[@id="items"]/tag[1]

# Like 
//ul[@id="items"]/li[1]
```
For first element 

Select more than 1 child
```
//tag[@id="items"]/tag[position()=1 or position()=4]

# Like 
//ul[@id="items"]/li[position()=1 or position()=4]
```

Selecting last item 
```
//tag[@id="items"]/tag[position()=1 or position()=last()]

# Like 
//ul[@id="items"]/li[position()=1 or position()=last()]
```

We can also use operators for selection like greater than or less than 
```
//tag[@id="items"]/tag[position()>1]

# Like 
//ul[@id="items"]/li[position()>1]
```

# Navigating xpath going up 

## Get the parent of an element if know the name of the tag
```
//tag[@id='value']/parent::tag

# Like
//p[@id='unique']/parent::div
```

## Get the parent of an element if not know the name of the tag
```
//tag[@id="value"]/parent::node()

# Like
//p[@id='unique']/parent::node()
```

## Get the grandparents and parents of an element
```
//tag[@id="value"]/ancestor::node()

# Like
//p[@id='unique']/ancestor::node()
```
## Get the grandparents and parents of an element with self
```
//tag[@id="value"]/ancestor-or-self::node()

# Like
//p[@id='unique']/ancestor-or-self::node()
```
## Get all the preceding element of a selected element except the ancestors
```
//tag[@id="value"]/preceding::node()

#Like
//p[@id='unique']/preceding::node()
```

## Get the sibling of the element selected 
```
//tag[@id='outside']/preceding-sibling::node()

# Like
//p[@id='outside']/preceding-sibling::node()
```

# Navigating xpath going down

## Get the child of the given element 
```
//tag[@class="intro"]/child::node()

# Like
//div[@class="intro"]/child::node()
```

## Get all the element followed by the selected element 

```
//tag[@class="intro"]/following::node()

# Like
//div[@class="intro"]/following::node()
```

## Get all the element having same parent of selected element 
```
//tag[@class="intro"]/following-sibling::node()

# Like 
//div[@class="intro"]/following-sibling::node()
```

## Get the children and grandchildren of the selected element 
```
//tag[@class="intro"]/descendant::node()

#Like 
//div[@class="intro"]/descendant::node()
```