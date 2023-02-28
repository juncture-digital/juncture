# ve-map

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

The `.ve-map` tag creates a map viewer that displays a base map with optional map layers.  The map supports zooming and panning.

## Attributes

### Core attributes 

**[center](#basic)** (_string_):  Defines the initial center of the rendered map.  This can be defined using latitude and longitude coordinates or with a Wikidata QID.

**[zoom](#basic)** (_number_):  Defines the initial zoom level of the rendered map.

**[marker](#basic)** (_boolean_):  If true a Marker will be added to the map center point.

**[caption](#basic)** (_string_):  A caption to use in the viewer caption bar.

### Viewer positioning attributes

**[left](/styling/viewer-positioning)** (_boolean_):  Position the viewer in the left half of the viewport and scale the width proportionally.  Text will wrap around the viewer unless the _sticky_ attribute is included.

**[right](/styling/viewer-positioning)** (_boolean_):  Position the viewer in the right half of the viewport and scale the width proportionally. Text will wrap around the viewer unless the _sticky_ attribute is included.

**[full](/styling/viewer-positioning)** (_boolean_):  Use the fill width of the browser viewport for the image.  Scale the image height proportional to the source image.  By default, the image will be auto-sized such that its height is not more than 40% of the viewport height.

**[sticky](/styling/viewer-positioning)** (_boolean_):  The _sticky_ attribute causes the viewer to "stick" to the top of the viewing area when the essay text is scrolled.  The viewer will stick in position until all content in the enclosing section has scrolled through the viewing area.

**[height](/styling/viewer-positioning)** (_string_):  A requested size for the  viewer height.  The default behavior is to use the full width of the available window and scale the viewer height to retain the aspect ratio of the source item (image or video).

**[width](/styling/viewer-positioning)** (_string_):  A requested size for the  viewer width.  The default behavior is to use the full width of the available window.

## Overlays

Map overlays are defined in a Markdown list following the `.ve-map` tag.

### Overlay attributes

**[location](/styling/overlays)** (_string_):  Location for a marker.  A location may be defined using latitude/longitude coordinates or a Wikidata QID. 

**[geojson](/styling/overlays)** (_string_):  A GeoJSON overlay be defined with a URL to a GeoJSON file or a Wikidata QID.

**[label](/styling/overlays)** (_string_):  Optional label for marker or GeoJSON overlay. 

## Examples

### Basic

<ve-snippet collapsible label="Basic map with default center and zoom">
    .ve-map
</ve-snippet>

<ve-snippet collapsible label="Basic map with center defined using lat/lng coordinates">
    .ve-map 42.281,-83.748 9
</ve-snippet>

<ve-snippet collapsible label="Basic map with center defined using the Wikidata QID for New York City">
    .ve-map Q60 8
</ve-snippet>

<ve-snippet collapsible label="Map with image as marker">
    .ve-map Q223969 5 right
        - wc:Double-O-Arch_Arches_National_Park_2.jpg

    This example uses [an image from Wikimedia commons](https://commons.wikimedia.org/wiki/File:Double-O-Arch_Arches_National_Park_2.jpg) for a marker.  The image used in this example includes embedded Exif (Exchangeable image file format) data with geographic coordinates.

    Hover over the marker or click here to see the image.

    ==The marker image will also appear when hovering over this text.  Clicking on this text will also cause the map to zoom in on the marker location.=={flyto=wc:Double-O-Arch_Arches_National_Park_2.jpg,14}
</ve-snippet>

### Overlays
