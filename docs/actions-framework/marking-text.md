# Marking Text
Essay text is "marked" by surrounding the applicable text with double equal signs (`==`) followed by an element attributes definition with the action to be performed.  Element attributes are defined by text enclosed with `{` and `}` characters.  For example:

```Markdown
Lorem ipsum ==dolor=={100,100,400,400} sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
```

In the example above the text `dolor` is marked and associated with the attribute `100,100,400,400`.  This has the effect of highlighting the `dolor` text in the rendered essay and creating a `zoom` interaction when the text is selected (clicked or tapped).  The `zoom` interaction causes the closest image to zoom into the region specified by the coordinates in the  attribute.

## Marked Text
Marked text is used to create a essay interactions such as zooming into an image region or playing a specific segment of a video.  The text to trigger the interaction is marked by surrounding a word or phrase with double equal signs and enclosing a value for the desired behavior in brace characters (`{`,`}`).  Below are a few examples of some commonly used marked text behaviors.  These are explained in more detail the following sections.

- [**Image region zoom**](/actions/zoom-to) - `==click to zoom=={100,100,400,400}`
- [**Play multimedia (video or audio) segment**](/actions/play-at) - `==click to play=={1:30,1:45}`
- [**Fly to region**](/actions/fly-to)
- [**Show entity information popup**](/actions/infobox-hover) - `==Vincent van Gogh=={Q5582}`
