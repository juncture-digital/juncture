<script src="https://cdn.jsdelivr.net/npm/prismjs@1.29.0/components/prism-markdown.min.js"></script>

# ve-header

The `.ve-header` tag is used to define an optional header that appears at the start of the essay.  The header can be used to:

- Define a title and subtitle for the essay
- Display a banner image
- Create a navigation menu for linking to sections within the current essay, to other essays, or to arbitrary web pages

As with the images displayed by the `.ve-image` tag, the banner image used by the `.ve-header` tag is a IIIF image and can be cropped or otherwise manipulated when displayed in the header.

## .ve-header Attributes

- **label** (_text string_):  The text to use for the essay title. 
- **subtitle** (_text string_):  The text to use for the essay subtitle.
- **height** (_height in pixels_):  The height of the header (before collapsing when in _sticky_ mode).
- **background** (_IIIF manifest URL_):  The URL to the IIIF manifest for the image to display as a banner image in the header.
- **logo** (_logo image URL_): A URL to a logo image.
- **url** (_URL associated with logo image_):  The URL that is invoked when the logo image is clicked.
- **options** (_IIIF image options_):  The _options_ attribute is used to define the [IIIF image request parameters](https://iiif.io/api/image/2.1/#image-request-parameters) for an image.  This attribute is most commonly used to define a coordinates for displaying an image region.   
- **position** ("_top_", "_center_" or "_bottom_"):  The portion of a cropped banner image to display.  The default is _center_.  Other recognized values are _top_ and _bottom_.
- **sticky** ("_true_" or "_false_"):  If set to "_true_" the header will collapse into a condensed form and remain fixed at the top of the page.

## Examples

### Basic header

A basic header with a title.

<ve-snippet>
    .ve-header "Essay Title"
</ve-snippet>

### Basic header with custom color

This examples shows the use of a basic header with a title and custom background color.  In this example the custom background color `LightCoral` is used.  Any valid HTML color name or hex code may be used for a background color.  HTML supports 140 [standard color names](https://www.w3schools.com/colors/colors_names.asp).  The full range of colors can be at a number of online sites, including  [https://htmlcolorcodes.com](https://htmlcolorcodes.com/)

<ve-snippet>
    .ve-header "Essay Title" background=LightCoral
</ve-snippet>

### Sticky header

A sticky header defined with positional attributes and navigation menu options in a nested Markdown list.

<ve-snippet fill>
    .ve-header "Essay Title" wc:Zelfportret_met_strohoed_-_s0164V1962_-_Van_Gogh_Museum.jpg "Essay subtitle" pct:3,23,80,20 center sticky
        - [Home](/)
        - [About](/about)
</ve-snippet>