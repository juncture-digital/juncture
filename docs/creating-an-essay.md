# Overview

Essays are defined in plain text files that are stored in a Github repository.  These files include narrative text and tags for text formatting and viewer insertion.  The manner in which these text files are created is not important to the display of the generated web page by the Juncture rendering engine.  All that matters is that the formatting and viewer tags are correctly formed.

Some options for creating an essay text file include:

- **Using the Github built-in editor.**  This is a very workable approach and was actually the primary means for creating Juncture essays in the first version.  The drawbacks to this approach are that the editor is exited each time a save is made and previewing changes requires a separate request to the Juncture web server.  While workable it is a cumbersome and inefficient workflow.  Improving this workflow was a key objective in the Juncture rewrite for version 2.  The primary advantage of this approach is that Juncture does not need to be given permission to write to your Github account.
- **Using a text editor on your local computer and uploading the generated files to Github.**  This approach has many of the same trade-offs as the one above.  Juncture does not need write access to your Github account and the authoring workflow is awkward (even more so with the required uploading).  The primary benefit would be the ability to use a familiar text editor on your local computer.
- **Using the Juncture Editor.**  A web-based editor was introduced in Juncture version 2,  It provides an in-browser editor with preview features.  It also provides syntax highlighting of Markdown and Juncture tags.  However, one of the biggest benefits is the automatic creation of Juncture tags using copy-paste and drag-n-drop.  For instance, Juncture media viewer tags are automatically created when dragging an image, video, or audio clip into the editor window from a number of commonly used web sites.

Using the Juncture Editor is the recommended approach for authoring essays, but as mentioned, the Juncture web page rendering engine doesn't care how the source text file was created.  Feel free to use any approach that suits you.  That said, the rest of this _Creating an Essay_ overview and other tutorials in the Juncture documentation assume the Juncture Editor is being used.  Some instructions may need to be adapted to match a different approach.

An overview of the Juncture Editor can be found [here](/tools/editor)

# The Basic Process

This section describes the steps typically performed in the creation of a Juncture essay.  The steps described represent a logical progression from plain, unformatted text, to a completed visual essay with nice formatting, interactive viewers, text interactions, headers and footers, and more.  This is a conceptual workflow.  All of these activities are actually optional and can be performed in any sequence.  In practice the creation of an essay is often an iterative process where aspects of some steps are performed multiple times. 

## Add Text

For essays that contain text, the text is often entered as plain, unformatted text using a text editor.  During this phase of essay development the text is often just organized into paragraphs.  There is nothing special about paragraph formatting in Markdown (and by extension, Juncture).  A paragraph is simply a grouping of one or more sentences separated by one or more blank lines.  The Juncture editor will automatically wrap paragraph text so separating each sentence with a new line is not necessary, or even recommended.  In this digital format it is also a good idea to keep paragraphs relatively small.  

## Format Text with Markdown

Adding Markdown formatting can be done during the initial text entry or added later.  Most often it will be a combination of both.  The Juncture Editor includes a Markdown formatting tool bar in the top-left portion of the editor window.  This can be convenient for most formatting.  The Markdown tags are also quite simple and easy to remember.  Entering the tags manually is often equally fast and convenient.  Below are some links to Markdown resources.

- 
-

## Add Footnotes

In cases where content is reused from another source it is a recommended practice to cite the original source with a footnote (technically, an endnote).  Core Markdown does not include a footnote tag but most of the Markdown implementations provide an extension for this, including the Markdown parser used by Juncture.  More information on Juncture footnote syntax and uses can be found [here](/footnotes).

## Add Entity Popovers

It can be useful to add information popups to text that references entities (people, locations, etc) that may be unfamiliar to the reader.  The information popover provides a short description and image (when available) with a top-level overview of a referenced entity.  The popover will also include a link to the relevant Wikipedia page where the reader can go to learn more.  Using entity popovers can be an effective way for providing context to a reader without disrupting the flow of the narrative.  More information on add entity information popovers can be found [here](/entity-popovers).

A special form of Juncture tagging is provided for creating an information popover for passages in the text portion of an essay.  The passage may be a single word or multi-word phrase.  The passage will typically be associated with an entity such as a person, location, organization, plant, animal, etc.  

The information popover is created from open data and text retrieved from Wikipedia and [Wikidata](https://www.wikidata.org).  Wikidata is an open database containing entries for more than 100 million entities.  Each of these entities is associated with a unique identifier, also know as a `QID` since each identifier starts with the capital letter `Q` follow by a number.  As an example, the Wikidata identifier for Barcelona is [Q1492](https://www.wikidata.org/wiki/Q1492).

More background on Wikidata and how Juncture uses it can be found [here](/wikidata). 

In the snippet below, the text `Barcelona` and `Mediterranean Sea` are tagged with their relative QIDs.  The effect of this is to generate an information popover when a cursor hovers over the wrapped ("marked") text.

<ve-snippet>
    Barcelona is a city on the coast of northeastern Spain. It is the capital and largest city of the autonomous community of Catalonia, as well as the second most populous municipality of Spain. With a population of 1.6 million within city limits, its urban area extends to numerous neighbouring municipalities within the Province of Barcelona and is home to around 4.8 million people, making it the fifth most populous urban area in the European Union after Paris, the Ruhr area, Madrid, and Milan. 

    ==Barcelona=={Q1492} is one of the largest metropolises on the ==Mediterranean Sea=={Q4918}, located on the coast between the mouths of the rivers Llobregat and Besòs, and bounded to the west by the Serra de Collserola mountain range, the tallest peak of which is 512 metres (1,680 feet) high.
</ve-snippet>

## Add Juncture Viewer Tags

This is where a text narrative starts to become an interactive and engaging visual essay.  High resolution images, maps, videos, and other visualizations can bring a text narrative to life while also providing details and context that can often be difficult to convey in text alone.  Juncture's media viewer is great at providing visual appeal, especially when using high resolution images.  Videos and interactive maps are other visualizations often used in a visual essay.

Juncture tags are used to add viewers to an essay.  The media and map viewers are a couple that are commonly used.  Others are available and more will be added in future versions.  Juncture tags include a `.ve-` prefix and must be located at the beginning of a new line in the essay.  One or more additional attributes will often be required after the tag.  These attributes can be expressed as single values or as key-value pairs, for instance `fit=cover` is an attribute used by the Juncture `.ve-media` tag.  The key in this string is `fit` and the value is `cover`.  This is an attribute that tells the media viewer how to display an image that has a different aspect ratio than the viewers.  Many attributes can be expressed as single values as Juncture can usually infer the purpose of the attribute by its position in the tag string or the value itself.  

Below is an example of a Juncture `.ve-image` tag with the `src` attribute specified with key-value notation.

<ve-snippet>
.ve-media src=wc:The_Bug_Peek.jpg
</ve-snippet>

This next example uses the `.ve-image` tag to display the same image, this time just using the attribute value.  

<ve-snippet>
.ve-media wc:The_Bug_Peek.jpg
</ve-snippet>

Note that in the HTML version of the tag seen in the snippet above, the `src` key has been added by the Markdown-to-HTML conversion that Juncture performs.  The Markdown versions of the Juncture tags are easier to write but ultimately these are converted to HTML for use by a browser.  The HTML version of the Juncture tags are provided in the snippets in the Juncture documentation.  These are provided as a convenience for uses that may be using Juncture viewers in web pages not rendered by Juncture, in a vanilla HTML document or in WordPress site for instance.  The HTML version of the tag could be used in the essay text file Juncture Editor but the Markdown version is always more concise and readable.

## Add Interactions

After adding Juncture viewers to an essay it can often be useful to connect the viewer to associated sections of the text with one or more interactions.  These interactions include `zoom to`, `fly to` and `play at` actions for images, maps, and audio/video clips.  The interactions are triggered by a user gesture, clicking or hovering over a marked passage in the text.

One of Juncture's key features is the ability to connect text passages to viewer actions.  These actions include zooming in on a particular region of an image, positioning a map over a specific location and playing an audio or video clip at a specific time stamp.  Actions may be triggered by clicking on marked passages or by scrolling marked paragraphs into the active portion of the browser window. 

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

More information on the Juncture interactions framework can be found [here](/actions/overview).

## Add Header and Footer

Custom headers and/or footers can be a nice addition to an essay.  A Header can be a good location for a title and subtitle or author name.  Headers can be very useful, or even essential, when building a web site consisting of multiple interlinked essays.  The header provides navigation capabilities that can be used for linking key areas of a site as well as providing access to documentation and a contact form.  Headers also support the use of a banner image which can add to the visual appeal of an essay.

More information on the Juncture header component can be found [here](/components/header).  Footer info is found [here](/components/footer).

## Enable Annotations

Depending on the purpose of an essay, enabling annotations may be desired.  This can be done easily with a simple Juncture tag.

