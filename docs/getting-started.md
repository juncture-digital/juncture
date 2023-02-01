# Getting Started

## How to use the Juncture documentation

The Juncture documentation index is located in the left sidebar.  The sidebar is closed by default but can easily be opened/closed by clicking on the menu icon located in the top-left corner of the page.

Information boxes are used to draw attention to bits that are particularly useful or important.

?> This is an informational message 

!> This is a message highlighting something important

The documentation also includes a lot of examples demonstrating the use of Markdown and Juncture tag.  Each example includes Markdown snippets showing how a tag would be used in an essay.  An HTML snippet is also provided for each example.  The HTML snippet is valid to use in a Markdown file but is included as a convenience for applications in which a Juncture visualization is used in an HTML page not rendered by a Juncture server.  For example, when adding a Juncture visualization to a WordPress site/page.  In addition to the Markdown and HTML snippets, the examples also rendered version of the snippet.

This is an example that provides Markdown and HTML code snippets and demo of the rendered code.  The snippets are designed to be easily copy-pasted or drag-and-dropped into the Juncture editor.

<ve-snippet>
    .ve-media wc:AmalfiCoast11.jpg width=50%
</ve-snippet>

This is an example that is collapsed by default and must be opened by clicking.  This approach is often used for longer examples.

<ve-snippet collapsible label="A collapsed example snippet - click on me to open">
    # The Amalfi Coast

    .ve-media wc:AmalfiCoast11.jpg right
    
    The Amalfi Coast is a stretch of coastline in southern Italy overlooking the Tyrrhenian Sea and the Gulf of Salerno. It is located south of the Sorrentine Peninsula and north of the Cilentan Coast.

    Celebrated worldwide for its Mediterranean landscape and natural diversity, the Coast is named after the town of Amalfi, which makes up its main historical and political centre. It is a very popular jet set destination, and has been an attraction to upper-class Europeans since the 18th century, when it was a frequent stopover on their Grand Tours. Attracting international tourists of all classes annually, the Amalfi Coast was listed as a UNESCO World Heritage Site in 1997.
</ve-snippet>

## Juncture essay rendering

The primary function performed by Juncture is to turn a plain text file stored in Github into an interactive web page that contains narrative text, deep-zoom images, maps, video, audio, and more.

As an example, consider a Juncture user with the Github username of **snagsby**.  Snagsby has created a Juncture visual essay in his essays repository about his favorite Dickens novel, "Bleak House".  The text for the essay has been created in a file named "bleak-house/README.md" located at the root of his Github essays repository.
- The Github URL for snagsby's essay file is https://github.com/snagsby/essays/blob/main/bleak-house/README.md
- The URL for rendered Juncture essay would be https://juncture-digital.org/snagsby/essays/bleak-house

All Juncture essays are associated with a URL of the form `https://juncture-digital.org/<USERNAME>/<REPOSITORY>/<PATH><ESSAY-ID>`, where:
- `<USERNAME>` and `<REPOSITORY>` are the Github username and repository hosting the file.
- `<PATH>` is an optional path to a Github folder that contains the essay folder or file.  This is not used for essays stored at the root of a repository.
- `<ESSAY-ID>` is an identifier associated with the essay.  By convention, this identifier is lower-case text (characters or numbers) without punctuation and dash characters (`-`) replacing spaces. 

In addition to the `juncture-digital.org` URL that is available for any Juncture essay, an essay may also be associated with a custom domain.  For example, our friend snagsby has obtained the domain `snagsby.net` for a personal site and connected it to his Github essays repository.  With this custom domain, the URL root https://snagsby.net can also be used for his essays, for instance https://snagsby.net/bleak-house.

?> Note that snagsby could have also created his essay in a text file named `bleak-house.md`.  A Juncture essay associated with the identifier bleak-house could be created in either a file named with the desired identifier (bleak-house, in this case) and a `.md` extension, **or** in a file named `README.md` located in a Github folder named with the essay identifier, for instance (`bleak-house/README.md`).  Either of these approaches would result in a Juncture essay accessed by the URL https://juncture-digital.org/snagsby/essays/bleak-house.  The advantage of using the folder-based approach is that this provides a convenient place for storing other files that may eventually be associated with an essay (for instance, image annotations or map overlays).  The folder approach is generally recommended for all but the simplest essays.

?> Juncture essay text files must include a `.md` file extension.  While the file is a plain text the .md extension signals that it contains  [Markdown](https://www.markdownguide.org/) text formatting tags.  When using the folder-based approach for creating a Juncture essay text file, the file must be named `README.md`, following the Github convention for naming a primary file in a folder.

## More about Github...

Github is a **free** Internet hosting service commonly used for software development projects.  It provides sophisticated features for version control and workflow management for distributed teams.  Juncture primarily uses Github as a file hosting service, similar to how one might use Dropbox or Google Drive.  When using the Juncture Editor and Media Tool for essay authoring and management the Github interactions (file creation, saving, deletion, etc) are handled by the tools.  

?> A Juncture essay author will not typically need to interact with Github directly after signing up for an account and linking it to Juncture (using the "Login with Github" button located in the left sidebar).  

A visual essay text file stored in Github will be associated with a Github account (Github username), repository, and file path.  Github hosted content is organized into one or more repositories.  Users unfamiliar with Github can think of a repository as a workspace, or simply as a collection of folders holding one or more files.  This isimilar to how content is stored on most computers.  Github supports the creation and use of multiple repositories for organizing content.  When Juncture is initially linked to a Github account it creates 2 repositories, named `essays` and  `media`.

- The `essays` repository is the default repository for storing visual essays text files.  While the `essays` repository is the Juncture default location for visual essay text files, any repository may be used.  The Github explorer widget used by the Juncture Editor and Media Tool use any public Github repository.  It can also be used to create new repositories if desired.  This can also be done through the Github web interface,
- The `media` repository is the default for building a personal collection of image, video, and audio files for use in a visual essay, or just sharing generally.  Juncture visual essays typically use media content hosted on sites like Wikimedia Commons, Flickr, and the JSTOR Community Collections, among others.  In situations where a user wants to use their own content hosting it in the same Github account is a convenient option.  The `media` repository was created for this purpose.  A Media Tool is provided by Juncture for browsing the contents of a Github-hosted media collection.  The Juncture Media Tool is also convenient for uploading content from a personal computer or smartphone into a Github repository.

Essays are defined in plain text files that are stored in a Github repository.  These files include narrative text and tags for text formatting and viewer rendering.  The manner in which these text files are created is not important to the display of the generated web page by Juncture.  All that matters is that the formatting and viewer tags are correctly formed.

- A Github repository will be associated with a URL of the form `https://github.com/<USERNAME>/<REPOSITORY>`, where `<USERNAME>` is the Github username associated with your Github account and `REPOSITORY` is the name of a repository in the account.  By convention the repository name is often `essays`, but any repository name can be used.  

Some options for creating an essay text file include:

- **Using the Github built-in editor.**  This is a very workable approach and was actually the primary means for creating Juncture essays in the first version.  The drawbacks to this approach are that the editor is exited each time a save is made and previewing changes requires a separate request to the Juncture web server.  While workable it is a cumbersome and inefficient workflow.  Improving this workflow was a key objective in the Juncture rewrite for version 2.  The primary advantage of this approach is that Juncture does not need to be given permission to write to your Github account.
- **Using a text editor on your local computer and uploading the generated files to Github.**  This approach has many of the same trade-offs as the one above.  Juncture does not need write access to your Github account and the authoring workflow is awkward (even more so with the required uploading).  The primary benefit would be the ability to use a familiar text editor on your local computer.
- **Using the Juncture Editor.**  A web-based editor was introduced in Juncture version 2,  It provides an in-browser editor with preview features.  It also provides syntax highlighting of Markdown and Juncture tags.  However, one of the biggest benefits is the automatic creation of Juncture tags using copy-paste and drag-n-drop.  For instance, Juncture media viewer tags are automatically created when dragging an image, video, or audio clip into the editor window from a number of commonly used web sites.

Using the Juncture Editor is the recommended approach for authoring essays, but as mentioned, the Juncture web page rendering engine doesn't care how the source text file was created.  Feel free to use any approach that suits you.  That said, the rest of this _Creating an Essay_ overview and other tutorials in the Juncture documentation assume the Juncture Editor is being used.  Some instructions may need to be adapted to match a different approach.

After logging in with Github the Juncture editor can be used in one of two ways:
    
- As a **separate window** launched from a button found in the left sidebar.  The advantage of this approach is that the various code snippets found in the documentation can be easily added to the editor using drag-and-drop.
- An **embedded viewer** found on [this page](/embedded-editor).  This approach has the advantage of reducing desktop clutter with one less window.

!> The editor works identically in either mode.  One caution though - **try to avoid using both simultaneously as divergent edits may result in Github merge conflicts when saving.**

An overview on using the Juncture Editor can be found [here](/tools/editor)

# Creating an essay

This section describes the steps typically performed in the creation of a Juncture essay.  The steps described represent a logical progression from plain, unformatted text, to a completed visual essay with nice formatting, interactive viewers, text interactions, headers and footers, and more.  This is a conceptual workflow.  All of these activities are actually optional and can be performed in any sequence.  In practice the creation of an essay is often an iterative process where aspects of some steps are performed multiple times. 

## Add Text

For essays that contain text, the text is often entered as plain, unformatted text using a text editor.  During this phase of essay development the text is often just organized into paragraphs.  There is nothing special about paragraph formatting in Markdown (and by extension, Juncture).  A paragraph is simply a grouping of one or more sentences separated by one or more blank lines.  The Juncture editor will automatically wrap paragraph text so separating each sentence with a new line is not necessary, or even recommended.  In this digital format it is also a good idea to keep paragraphs relatively small.  

## Format Text with Markdown

Adding Markdown formatting can be done during the initial text entry or added later.  Most often it will be a combination of both.  The Juncture Editor includes a Markdown formatting tool bar in the top-left portion of the editor window.  This can be convenient for most formatting.  The Markdown tags are also quite simple and easy to remember.  Entering the tags manually is often equally fast and convenient.  Below are some links to Markdown resources.

- [Markdown Guide](https://www.markdownguide.org/)
- [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Short (12min) Markdown tutorial on YouTube](https://www.youtube.com/watch?v=6A5EpqqDOdk)

## Add Footnotes

In cases where content is reused from another source it is a recommended practice to cite the original source with a footnote (technically, an endnote).  Core Markdown does not include a footnote tag but most of the Markdown implementations provide an extension for this, including the Markdown parser used by Juncture.  More information on Juncture footnote syntax and uses can be found [here](/footnotes).

## Add Entity Popovers

It can be useful to add information popups to text that references entities (people, locations, etc) that may be unfamiliar to the reader.  The information popover provides a short description and image (when available) with a top-level overview of a referenced entity.  The popover will also include a link to the relevant Wikipedia page where the reader can go to learn more.  Using entity popovers can be an effective way for providing context to a reader without disrupting the flow of the narrative.  More information on add entity information popovers can be found [here](/entity-popovers).

A special form of Juncture tagging is provided for creating an information popover for passages in the text portion of an essay.  The passage may be a single word or multi-word phrase.  The passage will typically be associated with an entity such as a person, location, organization, plant, animal, etc.  

The information popover is created from open data and text retrieved from Wikipedia and [Wikidata](https://www.wikidata.org).  Wikidata is an open database containing entries for more than 100 million entities.  Each of these entities is associated with a unique identifier, also know as a `QID` since each identifier starts with the capital letter `Q` follow by a number.  As an example, the Wikidata identifier for Barcelona is [Q1492](https://www.wikidata.org/wiki/Q1492).

More background on Wikidata and how Juncture uses it can be found [here](/wikidata). 

In the snippet below, the text `Barcelona` and `Mediterranean Sea` are tagged with their relative QIDs.  The effect of this is to generate an information popover when a cursor hovers over the wrapped ("marked") text.

<ve-snippet collapsible label="Creating an information popover">
    Barcelona is a city on the coast of northeastern Spain. It is the capital and largest city of the autonomous community of Catalonia, as well as the second most populous municipality of Spain. With a population of 1.6 million within city limits, its urban area extends to numerous neighbouring municipalities within the Province of Barcelona and is home to around 4.8 million people, making it the fifth most populous urban area in the European Union after Paris, the Ruhr area, Madrid, and Milan. 

    ==Barcelona=={Q1492} is one of the largest metropolises on the ==Mediterranean Sea=={Q4918}, located on the coast between the mouths of the rivers Llobregat and Besòs, and bounded to the west by the Serra de Collserola mountain range, the tallest peak of which is 512 metres (1,680 feet) high.
</ve-snippet>

## Add Juncture Viewer Tags

This is where a text narrative starts to become an interactive and engaging visual essay.  High resolution images, maps, videos, and other visualizations can bring a text narrative to life while also providing details and context that can often be difficult to convey in text alone.  Juncture's media viewer is great at providing visual appeal, especially when using high resolution images.  Videos and interactive maps are other visualizations often used in a visual essay.

Juncture tags are used to add viewers to an essay.  The media and map viewers are a couple that are commonly used.  Others are available and more will be added in future versions.  Juncture tags include a `.ve-` prefix and must be located at the beginning of a new line in the essay.  One or more additional attributes will often be required after the tag.  These attributes can be expressed as single values or as key-value pairs, for instance `fit=cover` is an attribute used by the Juncture `.ve-media` tag.  The key in this string is `fit` and the value is `cover`.  This is an attribute that tells the media viewer how to display an image that has a different aspect ratio than the viewers.  Many attributes can be expressed as single values as Juncture can usually infer the purpose of the attribute by its position in the tag string or the value itself.  

Below is an example of a Juncture `.ve-image` tag with the `src` attribute specified with key-value notation.

<ve-snippet collapsible label="Juncture attribute in key-value notation">
.ve-media src=wc:The_Bug_Peek.jpg
</ve-snippet>

This next example uses the `.ve-image` tag to display the same image, this time just using the attribute value.  

<ve-<ve-snippet collapsible label="Juncture attribute with value only">
.ve-media wc:The_Bug_Peek.jpg
</ve-snippet>

Note that in the HTML version of the tag seen in the snippet above, the `src` key has been added by the Markdown-to-HTML conversion that Juncture performs.  The Markdown versions of the Juncture tags are easier to write but ultimately these are converted to HTML for use by a browser.  The HTML version of the Juncture tags are provided in the snippets in the Juncture documentation.  These are provided as a convenience for uses that may be using Juncture viewers in web pages not rendered by Juncture, in a vanilla HTML document or in WordPress site for instance.  The HTML version of the tag could be used in the essay text file Juncture Editor but the Markdown version is always more concise and readable.

## Add Interactions

After adding Juncture viewers to an essay it can often be useful to connect the viewer to associated sections of the text with one or more interactions.  These interactions include `zoom to`, `fly to` and `play at` actions for images, maps, and audio/video clips.  The interactions are triggered by a user gesture, clicking or hovering over a marked passage in the text.

One of Juncture's key features is the ability to connect text passages to viewer actions.  These actions include zooming in on a particular region of an image, positioning a map over a specific location and playing an audio or video clip at a specific time stamp.  Actions may be triggered by clicking on marked passages or by scrolling marked paragraphs into the active portion of the browser window. 

In the snippet below a few `zoom to` actions are defined for an image displayed by the `.ve-media` viewer.

<ve-snippet collapsible label="Juncture 'zoom to' interactions on an image">
    .ve-media wc:The_Bug_Peek.jpg right

    Click on the text below to trigger an image `zoom to` action.
    - ==A close-up of the bug=={1131,639,1358,904}
    - ==Some kind of fungus on the leaf?=={1229,2533,928,618}
    - ==Full image view=={pct:0,0,100,100}
</ve-snippet>

This next snippet shows the use of `fly to` actions with a `.ve-map` viewer.

<ve-snippet collapsible label="Juncture 'fly to' interactions on an map">
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
