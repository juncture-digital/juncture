<style> 
    .markdown-section h3 ~ p > strong > a { color: crimson; font-size: 110%; text-decoration: none; }
    .markdown-section table { 
        margin-left:3rem; 
        width: calc(100% - 6rem); 
        border:1px solid #555;
    }
    .markdown-section td, .markdown-section th {
        border:1px solid #555;
        padding: 8px;
        line-height: 1.2;
    }
    .markdown-section th {
        background-color:#E2F0F7;
        font-weight:bold !important;
        text-align:center !important;
    }
</style>

# The Juncture Actions Framework

## Overview

The Juncture actions framework provides a way to trigger actions in a viewer component from essay text.  A text-to-viewer interaction is created by marking the text to use as a trigger and adding a specific attribute that is recognized by the target viewer component.  The interaction is typically triggered by clicking the marked text, but some interactions may also be triggered by hovering over marked text, or by scrolling a marked paragraph into the active portion of the browser window.

The example below demonstrates a simple `zoomto` action which is commonly used with the media viewer.  In this example the text "leaf beetle" is marked and associated with an image region.  This action is triggered when a user clicks on the marked text (`leaf beetle`).  When the action is triggered the viewer will zoom in on the specified region. 

<ve-snippet>
    .ve-media wc:The_Bug_Peek.jpg right
    In the image at the right, zoom in on the region containing the ==leaf beetle=={zoomto=1005,507,1676,1117}
</ve-snippet>

THe `flyto` action performed by the map viewer works similarly.  Instead of specifying an image region, in the map viewer `flyto` action a location and zoom level is provided.  For example,

<ve-snippet>
    .ve-map right
    In the map at the right, "fly to" ==Miami=={flyto=25.783,-80.217,10}
</ve-snippet>

## Viewer actions

| Viewer | Key | Value | Behavior |
| ------ | --- | ----- | -------- |
| Media  | `zoomto` | Image region bounding box | Zooms the image to the specified image region |
| Media  | `anno` | Annotation ID | Opens an annotation text box |
| Media  | `zoomto` | Image region bounding box **and** Annotation ID | Zooms the image to the specified image region **and** opens an annotation text box |
| Media  | `play` | Time to start (and optionally stop) an audio or video | Plays an audio or video clip from the specified time |
| Map  | `flyto` | Geographic coordinates and optional zoom level | Centers a map at the specified coordinates and sets zoom level |
| Map  | `flyto` | Wikidata QID | Centers a map at the coordinates associated with entity identified by the provided QID |

## Marking text

### Marking a word or phrase

Essay text to be used as an action trigger is wrapped with double equal signs `==`.  The action to be performed is then defined in an attribute that is connected to the wrapped text.  The actions may be defined using either key-value notation or as a single value.  The keys and values used are specific to each viewer. 

### Marking an entire paragraph

Using paragraph position as an action trigger is typically used in combination with a viewer that has been set to `sticky`.  When a viewer is set to `sticky` and positioned with a `left` or `right` attribute a 2-column layout is created for the parent section.  In this 2-column layout the viewer will stick to the top of the viewer window and the paragraphs will scroll in the other column.  As each paragraph enters the active portion of the window the associated action is triggered.  The "active" portion of the screen is defined as section near the top of the screen such the the majority of a paragraph is visible.

A paragraph is "marked" by appending an attributes block to the paragraph.  The attributes block can include `enter` and `exit` attributes to trigger actions when the paragraph enters or leaves the active area of the screen.

In the example below a map and 3 paragraphs are defined.  Each of the paragraphs correspond to a location - New York, Paris, and London.  As each of these paragraphs are scrolled into the "active" portion of the browser window a `flyto` action is triggered to reposition the map to the associated location.  In this example the `show-active` class is added to the section containing the sticky map and text paragraphs.  The `show-active` class adds a gray border to the left side of active paragraph as a visual indicator.  The example also uses Wikidata QIDs for the `flyto` actions.  Lat/Lng coordinates could have also been used.

<ve-snippet collapsible label="Using paragraph position as an action trigger" height="600px">
    # Using paragraph position as an action trigger {.show-active}

    .ve-map Q60 8 sticky right

    **New York**, often called New York City or NYC, is the most populous city in the United States. With a 2020 population of 8,804,190 distributed over 300.46 square miles (778.2 km2), New York City is also the most densely populated major city in the United States, and is more than twice as populous as second-place Los Angeles. New York City lies at the southern tip of New York State, and constitutes the geographical and demographic center of both the Northeast megalopolis and the New York metropolitan area, the largest metropolitan area in the United States both by population and by urban landmass. 
    {enter=flyto:Q60}

    **Paris** is the capital and most populous city of France, with an estimated population of 2,165,423 residents in 2019 in an area of more than 105 km² (41 sq mi), making it the 30th most densely populated city in the world in 2020. Since the 17th century, Paris has been one of the world's major centres of finance, diplomacy, commerce, fashion, gastronomy, and science. For its leading role in the arts and sciences, as well as its very early system of street lighting, in the 19th century it became known as "the City of Light". Like London, prior to the Second World War, it was also sometimes called the capital of the world.
    {enter=flyto:Q90}

    **London** is the capital and largest city of England and the United Kingdom, with a population of just under 9 million. It stands on the River Thames in south-east England at the head of a 50-mile (80 km) estuary down to the North Sea, and has been a major settlement for two millennia. The City of London, its ancient core and financial centre, was founded by the Romans as Londinium and retains its medieval boundaries.[note 1] The City of Westminster, to the west of the City of London, has for centuries hosted the national government and parliament. Since the 19th century, the name "London" has also referred to the metropolis around this core, historically split between the counties of Middlesex, Essex, Surrey, Kent, and Hertfordshire, which since 1965 has largely comprised Greater London, which is governed by 33 local authorities and the Greater London Authority.
    {enter=flyto:Q84}

    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
</ve-snippet>


## Media viewer actions

### Zoom to image region

<ve-snippet collapsible label="Zoom to image region (using key-value notation)">
.ve-media wc:The_Bug_Peek.jpg right
The image depicts a ==leaf beetle=={zoomto=1005,507,1676,1117} looking out from a leaf hole of Alnus nepalensis tree. Adult leaf beetles make holes in host plant leaves while feeding. They camouflage themselves with these holes.
</ve-snippet>

<ve-snippet collapsible label="Zoom to image region (using value only)">
.ve-media wc:The_Bug_Peek.jpg right
The image depicts a ==leaf beetle=={1005,507,1676,1117} looking out from a leaf hole of Alnus nepalensis tree. Adult leaf beetles make holes in host plant leaves while feeding. They camouflage themselves with these holes.
</ve-snippet>

### Show annotation

<ve-snippet collapsible label="Show annotation (using key-value notation)">
.ve-media wc:The_Bug_Peek.jpg right base=juncture-digital/juncture/examples/hello-juncture
The image depicts a ==leaf beetle=={anno=386db45b} looking out from a leaf hole of Alnus nepalensis tree. Adult leaf beetles make holes in host plant leaves while feeding. They camouflage themselves with these holes.
</ve-snippet>

<ve-snippet collapsible label="Show annotation (using value only)">
.ve-media wc:The_Bug_Peek.jpg right base=juncture-digital/juncture/examples/hello-juncture
The image depicts a ==leaf beetle=={386db45b} looking out from a leaf hole of Alnus nepalensis tree. Adult leaf beetles make holes in host plant leaves while feeding. They camouflage themselves with these holes.
</ve-snippet>

### Zoom to image region and show annotation

<ve-snippet collapsible label="Zoom to image region and show annotation (using key-value notation)">
.ve-media wc:The_Bug_Peek.jpg right base=juncture-digital/juncture/examples/hello-juncture
The image depicts a ==leaf beetle=={zoomto=167,1,3352,2233,386db45b} looking out from a leaf hole of Alnus nepalensis tree. Adult leaf beetles make holes in host plant leaves while feeding. They camouflage themselves with these holes.
</ve-snippet>

<ve-snippet collapsible label="Zoom to image region and show annotation (using value only)">
.ve-media wc:The_Bug_Peek.jpg right base=juncture-digital/juncture/examples/hello-juncture
The image depicts a ==leaf beetle=={167,1,3352,2233,386db45b} looking out from a leaf hole of Alnus nepalensis tree. Adult leaf beetles make holes in host plant leaves while feeding. They camouflage themselves with these holes.
</ve-snippet>

### Play at time

<ve-snippet collapsible label="Play at time (using key-value notation)">
.ve-media https://www.youtube.com/watch?v=Zy3K2Lcw7hQ right
Start playing video at ==time=={play=10}
</ve-snippet>

<ve-snippet collapsible label="Play at time (using value only)">
.ve-media https://www.youtube.com/watch?v=Zy3K2Lcw7hQ right
Start playing video at ==time=={10}
</ve-snippet>

## Map viewer actions

<ve-snippet collapsible label="Fly to location using lat/lng coordinates">
.ve-map Q60 8 right
Fly to ==Paris=={flyto:48.857,2.352}
</ve-snippet>

<ve-snippet collapsible label="Fly to location using Wikidata ID">
.ve-map Q60 8 right
Fly to ==Paris=={flyto:Q90}
</ve-snippet>

<ve-snippet collapsible label="Fly to location with specified zoom level">
.ve-map Q60 8 right
    - Q60
    - Q90
Fly to ==Paris=={flyto:Q90,7}
</ve-snippet>