### Attributes to watch out for
#### hand
Indicates a Vanguard type. I generally want to exclude cards with this attribute.
#### alternate cards
A lot of cards have duplicates in the same set that just have different art or a different style. These can be excluded by checking for isAlternative.
#### flavorName and faceFlavorName 
These should be treated like alternate cards, and they can be excluded in the same way.
#### Availability
Cards that only have the availability 'shandalar' or 'dreamcast' are not canonical magic cards; they only exist in forgotten, old digital sets. These should be excluded from most analyses.
#### isFunny
This is another one that might be excluded from a lot of analyses, though cards from these sets are not necessarily banned in all formats.
#### isOnlineOnly
Seems like an alternative to filtering by whether or not 'paper' is in card['availability']
#### isOversized
This is a novelty, something I'll almost always want to exclude.
