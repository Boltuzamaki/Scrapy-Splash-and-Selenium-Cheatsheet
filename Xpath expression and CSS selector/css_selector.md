## Select a tag
```
tag
```
We can select tag directly

## Class selector
```
.class 
```
defined by "." and after it name of class

## ID selector
```
#id
```
defined by "#" and after it name of id

## Select a tag with specific class
```
tag.class
```
## Select a tag with specific id
```
tag#id
```
## Select element having more tan one class defined 
```
.class1.class2
```
## Selecting on the basis of attribute
```
tag[attribute=value]

or

[attribute=value]
```

## Select on the basis of some string which is present at start of a value for an attribute 

```
a[href^="https"]
tag[attribute^="string"]
```
## Select on the basis of some string which is present at middle of a value for an attribute 
```
a[href*="google"]
tag[attribute*="string"]
```
## Select on the basis of some string which is present at end of a value for an attribute 
```
a[href$="fr"]
tag[attribute$="string"]
```

## Select a tag which is inside other tag 
```
div.intro p

tag.class tag
```
## Select multiple tag which is inside other tag 
```
div.intro p, span#location
```

## Select all the elements that are direct children of other element 
```
div.intro > p
tag.class > tag
```

## Select the element that are placed immediately to other element
```
div.into + p
tag.class + tag
```

## If we want to get a specific number child of a element like li 

example like 
```
   <li data-identifier="7">Item 1</li> 
   <li>Item 2</li> 
   <li>Item 3</li> 
   <li>Item 4</li> 
```
select using 
```
li:nth-child(1)
```
Select more than 1 child 
```
li:nth-child(1), li:nth-child(2)
```
Select element with odd and even positioning 
```
li:nth-child(odd)

li:nth-child(even)
```