# Overview

An essay is defined in plain text files that are stored in a Github repository.  These files include the essay narrative text and tags for text formatting and viewer insertion.  The manner in which these text files are created is not important to the display of the generated web page by the Juncture rendering engine.  All that matters is that the formatting and viewer tags are correctly formed.

Some options for creating an essay text file include:

- **Using the Github built-in editor.**  This is a very workable approach and was actually the primary means for creating Juncture essays in the first version.  The drawbacks to this approach are that the editor is exited each time a save is made and previewing changes requires a separate request to the Juncture web server.  While workable it is a cumbersome and inefficient workflow.  Improving this workflow was a key objective in the Juncture rewrite for version 2.  The primary advantage of this approach is that Juncture does not need to be given permission to write to your Github account.
- **Using a text editor on your local computer and uploading the generated files to Github.**  This approach has may of the same trade-offs as the one above.  Juncture does not need write access to your Github account and the authoring workflow is awkward, even more so with the required uploading.  The primary benefit would be the ability to use a familiar text editor.
- **Using the Juncture Editor.**  The Juncture web-based editor was introduced in version 2,  It provides an in-browser editor with preview features.  It also provides syntax highlighting of Markdown and Juncture tags.  One of the biggest benefits in using the Juncture editor is the automatic creation of tags using copy-paste and drag-n-drop.  Media viewer tags are automatically created when dragging an image, video, or audio clip into the editor window from a number of popular web sites.

Using the Juncture Editor is the recommended approach for authoring essays but as mentioned, the Juncture web page rendering engine doesn't care how the source text file was created so feel free to use any approach that suits you.  The tutorials in the Juncture documentation assume the Juncture Editor is used.  Some instructions may need to be adapted to match a different approach.

A tutorial for using the Juncture Editor can be found [here](/editor)

# Markdown

...

# Juncture Tags

Juncture tags are used to add viewers to an essay.  The Media and Map viewers are a couple that are commonly used.  Others are available and more will be added in future versions.  Juncture tags include a `.ve-` prefix and must be located at the beginning of a new line in the essay.  One or more additional attributes will often be required after the tag.  These attributes can be expressed as single values or as key-value pairs, for instance `fit=cover` is an attribute used by the Juncture `.ve-media` tag.  The key in this string is `fit` and the value is `cover`.  This is an attribute that tells the media viewer how to display an image that has a different aspect ratio than the viewers.  Many attributes can be expressed as single values as Juncture can usually infer the purpose of the attribute by its position in the tag string or the value itself.  

Below is an example of a Juncture `.ve-image` tag with the `src` attribute specified with key-value notation.

<ve-snippet>
.ve-media src=wc:The_Bug_Peek.jpg
</ve-snippet>

This next example uses the `.ve-image` tag to display the same image, this time just using the attribute value.  

<ve-snippet>
.ve-media wc:The_Bug_Peek.jpg
</ve-snippet>

Note that in the HTML version of the tag seen in the snippet above, the `src` key has been added by the Markdown-to-HTML conversion that Juncture performs.  The Markdown versions of the Juncture tags are easier to write but ultimately these are converted to HTML for use by a browser.  The HTML version of the Juncture tags are provided in the snippets in the Juncture documentation.  These are provided as a convenience for uses that may be using Juncture viewers in web pages not rendered by Juncture, in a vanilla HTML document or in WordPress site for instance.  The HTML version of the tag could be used in the essay text file Juncture Editor but the Markdown version is always more concise and readable.

# Entity Information Popups

A special form of Juncture tagging is provided for creating an information popup for passages in the text portion of an essay.  The passage may be a single word or multi-word phrase.  The passage will typically be associated with an entity such as a person, location, organization, plant, animal, etc.  

The information popup is created from open data and text retrieved from Wikipedia and [Wikidata](https://www.wikidata.org).  Wikidata is an open database containing entries for more than 100 million entities.  Each of these entities is associated with a unique identifier, also know as a `QID` since each identifier starts with the capital letter `Q` follow by a number.  As an example, the Wikidata identifier for Barcelona is [Q1492](https://www.wikidata.org/wiki/Q1492).

More background on Wikidata and how Juncture uses it can be found [here](/wikidata). 

In the snippet below, the text `Barcelona` and `Mediterranean Sea` are tagged with their relative QIDs.  The effect of this is to generate an information popup when a cursor hovers over the wrapped ("marked") text.

<ve-snippet>
    Barcelona is a city on the coast of northeastern Spain. It is the capital and largest city of the autonomous community of Catalonia, as well as the second most populous municipality of Spain. With a population of 1.6 million within city limits, its urban area extends to numerous neighbouring municipalities within the Province of Barcelona and is home to around 4.8 million people, making it the fifth most populous urban area in the European Union after Paris, the Ruhr area, Madrid, and Milan. 

    ==Barcelona=={Q1492} is one of the largest metropolises on the ==Mediterranean Sea=={Q4918}, located on the coast between the mouths of the rivers Llobregat and Besòs, and bounded to the west by the Serra de Collserola mountain range, the tallest peak of which is 512 metres (1,680 feet) high.
</ve-snippet>

# Text and Viewer Interactions

One of Juncture's key features is the ability to connect text passages to viewer actions.  These actions include zooming in on a particular region of an image, positioning a map over a specific location and playing an audio or video clip at a specific time stamp.  Actions may be triggered by clicking on marked passages or by scrolling tagged paragraph into the active portion of the browser window.  More information on Juncture Actions can be found [here](/juncture-actions).

In the snippet below a few `zoom to` actions are defined for an image displayed by the `.ve-media` viewer.

<ve-snippet>
    .ve-media wc:The_Bug_Peek.jpg right

    Click on the text below to trigger an image `zoom to` action.
    - ==A close-up of the bug=={1131,639,1358,904}
    - ==Some kind of fungus on the leaf?=={1229,2533,928,618}
    - ==Full image view=={pct:0,0,100,100}
</ve-snippet>

This next snippet shows the use of `fly to` actions with a `.ve-map` viewer.

<ve-snippet>
    .ve-map 11.18,-27.77 2 right
        - Q60
        - Q90
        - Q5465

    Click on the text below to trigger a `fly to` action.
    - ==New York=={40.7,-74,10}
    - ==Paris=={48.856944,2.351389,10}
    - ==Cape Town=={-33.925,18.425,10}
    - ==Overview=={11.18,-27.77,2}
</ve-snippet>