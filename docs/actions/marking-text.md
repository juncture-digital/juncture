# Marking Text
Essay text is "marked" by surrounding the applicable text with double equal signs (`==`) followed by an element attributes definition with the action to be performed.  Element attributes are defined by text enclosed with `{` and `}` characters.  For example:

```Markdown
Lorem ipsum ==dolor=={100,100,400,400} sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam
```

In the example above the text `dolor` is marked and associated with the attribute `100,100,400,400`.  This has the effect of highlighting the `dolor` text in the rendered essay and creating a `zoom` interaction when the text is selected (clicked or tapped).  The `zoom` interaction causes the closest image to zoom into the region specified by the coordinates in the  attribute.

## Marked Text
Marked text is used to create a essay interactions such as zooming into an image region or playing a specific segment of a video.  The text to trigger the interaction is marked by surrounding a word or phrase with double equal signs and enclosing a value for the desired behavior in brace characters (`{`,`}`).  Below are a few examples of some commonly used marked text behaviors.  These are explained in more detail the following sections.

- [**Image region zoom**](zoom) - `==click to zoom=={100,100,400,400}`
- **Play multimedia (video or audio) segment** - `==click to play=={1:30,1:45}`
- **Show entity information popup** - `==Vincent van Gogh=={Q5582}`

### Image zoom {#zoom}

.ve-media gh:juncture-digital/media/videos/Image_Zoom_Example.mp4 right

The image zoom behavior causes the `.ve-media` viewer to zoom to a specific region of an image.  The region of interest is specified using a set of 4 coordinates defining a rectangular bounding box.  The coordinates are the `x-position`, `y-position`, `width`, and `height`.  The coordinate values may be defined as absolute pixel values or as a percentage relative to the full size of the source image.[^iiif-region]

- **x,y,w,h**: The region of the full image to be returned is specified in terms of absolute pixel values. The value of x represents the number of pixels from the 0 position on the horizontal axis. The value of y represents the number of pixels from the 0 position on the vertical axis. Thus the x,y position 0,0 is the upper left-most pixel of the image. w represents the width of the region and h represents the height of the region in pixels.
- **pct:x,y,w,h**: The region to be returned is specified as a sequence of percentages of the full image’s dimensions, as reported in the image information document. Thus, x represents the number of pixels from the 0 position on the horizontal axis, calculated as a percentage of the reported width. w represents the width of the region, also calculated as a percentage of the reported width. The same applies to y and h respectively. These may be floating point numbers.

### [⇧](#top) Play video or audio segment {#play-at}

The play behavior causes the `.ve-media` viewer to play a video or audio clip starting at a specified time.  A second time value may optionally be used to define a stop time.  If a stop time is not provided the clip will play from the start time to the end.  The values for the start and end times are specified in **hh:mm:ss** notation.  The **hh** and **mm** values are optional.  For example:

- **30**: `==start playing 30 seconds into clip=={30}`
- **1:30**: `==start playing 90 seconds into clip=={1:30}`
- **15:00**: `==start playing 15 minutes into clip=={15:00}`
- **1:10:00**: `==start playing 1 hour and 10 minutes into clip=={1:10:00}`
- **5:30,6:00**: `==play from 5:30 to 6:00=={5:30,6:00}`

### [⇧](#top) Show entity info-box on hover {#entity-popup}

This behavior causes an entity information popup to be display when the cursor hovers over marked text associated with an entity (person, place, etc) identifier.  Juncture uses [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page) for entity data.  Wikidata is a free and open knowledge base that can be read and edited by both humans and machines.  Wikidata acts as central storage for the structured data of its Wikimedia sister projects including Wikipedia, Wikivoyage, Wiktionary, Wikisource, and others.  The textual information displayed in a Juncture entity popup is retrieved from Wikidata and Wikipedia.  When available, thumbnail images are retrieved from Wikimedia Commons.

Wikidata entity identifiers ("Q" IDs) can be obtained by querying Wikidata or by visiting the Wikipedia page associated with the entity of interest.  When viewing a Wikipedia page the Wikidata link in the left navigation panel can be used to easily obtain the entity `QID`.  Clicking on the Wikidata link will open the associated Wikidata page where the QID can be copied from the title displayed at the top of the page.  For example, the [Wikidata page for Vincent van Gogh](https://www.wikidata.org/wiki/Q5582) reveals the QID `Q5582`.  Adding this QID to a marked text segment will cause an entity popup to appear when hovering over the text.  A working example of this can be seen in the paragraph below.

> ==Vincent Willem van Gogh=={Q5582} was a Dutch Post-Impressionist painter who posthumously became one of the most famous and influential figures in Western art history. In a decade, he created about 2,100 artworks, including around 860 oil paintings, most of which date from the last two years of his life.
