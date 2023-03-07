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

The `.ve-map` tag creates a map viewer that displays a base map with optional map layers.  The map viewer supports zooming and panning.  The base map defaults to [OpenStreetMap](https://www.openstreetmap.org/) but can easily be set to a number of [others](#baselayers).  

The base map can be augmented with one or more optional map layers. Juncture supports 3 types of layers:

- **Location layer** - A location layer contains all of the individual locations defined for a map.  Locations are defined in a list following the _.ve-map_ tag.  Locations may defined with explicit geographic coordinates, a Wikidata entity ID that corresponds to a location, or an IIIF image that contains geographic coordinates in the manifest metadata.  An IIIF manifest created by Juncture will include geographic coordinates if they are found in the [Exif](https://en.wikipedia.org/wiki/Exif) metadata embedded in the source image.  Locations are displayed as map pins.  If the location is specified using a Wikidata ID and the Wikidata entity associated with the location links to a GeoJSON resource the corresponding shape may be displayed instead of the pin by including the `prefer-geojson` attribute in the list item.  By default, all locations are aggregated into a single layer.  the `layer` attribute may be used to organize locations into separate layers.
- **GeoJSON layer** - [GeoJSON](https://en.wikipedia.org/wiki/GeoJSON) is an open standard format designed for representing simple geographical features, along with their non-spatial attributes. It is based on the JSON format.  A GeoJSON layer is added by including a URL to a GeoJSON file in the list following the _.ve-map_ tag.
- **Georeferenced image** - A georeferenced image may also be used as a map layer.  [Georeferencing](https://en.wikipedia.org/wiki/Georeferencing) is a type of coordinate transformation that binds a digital image that represents a geographic space (often a scanned map or aerial photograph) to a spatial reference system, thus locating the digital data in the real world.  One common use of a georeferenced image layer is to create an historic map overlay. Juncture supports the use of georeferenced IIIF images created by [allmaps](https://allmaps.org/).  Adding an allmaps georeferenced image to a Juncture map is accomplished by including the text `allmaps=<ALLMAPS ID>` in a list item following the _.ve-map_ tag.

## Attributes

### Core attributes 

**[basemaps](#basemaps)** (_string_):  The name of an optional base map to be used.  A list of supported base maps can be seen [below](#basemaps)

**[caption](#basic-map-examples)** (_string_):  A caption to use in the viewer caption bar.

**[center](#basic-map-examples)** (_string_):  Defines the initial center of the rendered map.  This can be defined using latitude and longitude coordinates or with a Wikidata QID.

**[marker](#basic-map-examples)** (_boolean_):  If true a Marker will be added to the map center point.

**[popup-on-hover](#basic-map-examples)** (_boolean_):  Show location popup when hovering over the location (marker pin or GeoJSON shape).  The default behavior is to show the popup when clicking on the location.

**[prefer-geojson](#basic-map-examples)** (_boolean_):  Display a GeoJSON shape rather than a pin marker when available.

**[scroll-wheel-zoom](#basic-map-examples)** (_boolean_):  Enable map zoom behavior when scrolling over a map.  This is disabled be default.

**[zoom](#basic-map-examples)** (_number_):  Defines the initial zoom level of the rendered map.

**[zoom-on-click](#basic-map-examples)** (_boolean_):  Increase zoom level on a location after clicking on a location marker pin or shape. 

### Viewer positioning attributes

**[left](/styling/viewer-positioning)** (_boolean_):  Position the viewer in the left half of the viewport and scale the width proportionally.  Text will wrap around the viewer unless the _sticky_ attribute is included.

**[right](/styling/viewer-positioning)** (_boolean_):  Position the viewer in the right half of the viewport and scale the width proportionally. Text will wrap around the viewer unless the _sticky_ attribute is included.

**[full](/styling/viewer-positioning)** (_boolean_):  Use the fill width of the browser viewport for the image.  Scale the image height proportional to the source image.  By default, the image will be auto-sized such that its height is not more than 40% of the viewport height.

**[sticky](/styling/viewer-positioning)** (_boolean_):  The _sticky_ attribute causes the viewer to "stick" to the top of the viewing area when the essay text is scrolled.  The viewer will stick in position until all content in the enclosing section has scrolled through the viewing area.

**[height](/styling/viewer-positioning)** (_string_):  A requested size for the  viewer height.  The default behavior is to use the full width of the available window and scale the viewer height to retain the aspect ratio of the source item (image or video).

**[width](/styling/viewer-positioning)** (_string_):  A requested size for the  viewer width.  The default behavior is to use the full width of the available window.

### Layer attributes

**[allmaps](#layer-examples)** (_string_):  Allmaps ID of a georeferenced image.

**[coords](#layer-examples)** (_string_):  Location coordinates.

**[description](#layer-examples)** (_string_):  Location description used in a popup.

**[disabled](#layer-examples)** (_boolean_):  Location is not displayed initially.  This attribute must be used in conjunction with the `layer` attribute.

**[geojson](#layer-examples)** (_string_):  URL to a GeoJSON file.

**[iiif](#layer-examples)** (_string_):  IIIF manifest URL containing geographic coordinates.

**[image](#layer-examples)** (_string_):  Location image used in a popup thumbnail.

**[label](#layer-examples)** (_string_):  Location label used in a popup.

**[layer](#layer-examples)** (_string_):  Layer name to associate with the location.  Multiple locations can use the same layer name.  When a layer name is specified the layer may be hidden when the map is initially rendered by including the `disabled` attribute on one of the layer locations.

**[marker-type](#layer-examples)** (_string_):  Type of marker to render.  Recognized values are 'circle'.

**[prefer-geojson](#layer-examples)** (_boolean_):  When using a Wikidata ID to define a location a GeoJSON shape may be used rather than a pin marker when available.

**[qid](#layer-examples)** (_string_):  Wikidata entity ID of a location.

**[zoom](#layer-examples)** (_number_):  Location zoom level when `zoom-on-click` behavior is enabled.

## Layers

Map layers are defined in a Markdown list following the `.ve-map` tag.  Items in the layer list may define markers, GeoJSON file URLs or [allmaps](https://allmaps.org/) IDs for georeferenced images.

### Marker layer

A single marker layer is created by aggregating all of the ve-map list items that are not GeoJSON URLs or allmaps references.  A marker can be defined in 3 ways,

- With explicit geographic (latitude and longitude) coordinates.  An optional label may also be specified for the marker.
- With a Wikidata ID that corresponds to an entity associated with a location.
- With an IIIF image that includes geographic coordinates in the manifest metadata

### GeoJSON layer

A GeoJSON layer is defined by including a URL to a GeoJSON file in a .ve-map layer list item. 

### Georeferenced Image layer

A Georeferenced image layer is defined by including an allmaps ID in a .ve-map layer list item. 

##

## Examples

### Basic map examples

<ve-snippet collapsible label="Basic map with default center and zoom">
    .ve-map width=50%
</ve-snippet>

<ve-snippet collapsible label="Basic map with center defined using lat/lng coordinates">
    .ve-map 42.281,-83.748 9 width=50%
</ve-snippet>

<ve-snippet collapsible label="Basic map with center defined using the Wikidata QID for New York City">
    .ve-map Q60 8 width=50%
</ve-snippet>

<ve-snippet collapsible label="Map center defined using a Wikidata QID with marker attribute">
    .ve-map Q60 8 marker width=50%
</ve-snippet>

### Layer examples

<ve-snippet collapsible label="Location defined with coordinates">
    .ve-map 42.281,-83.748 9 width=50%
        - Q12439
</ve-snippet>


<ve-snippet collapsible label="Location defined with coordinates">
    .ve-map 42.281,-83.748 9 width=50%
        - Q12439
</ve-snippet>

<ve-snippet collapsible label="Location defined with coordinates and label">
    .ve-map 42.281,-83.748 10 width=50%
        - 42.281,-83.748 "Ann Arbor, Michigan"
</ve-snippet>

<ve-snippet collapsible label="Location defined with coordinates, label, and description">
    .ve-map 42.281,-83.748 9 width=50%
        - 42.281,-83.748 "Ann Arbor, Michigan" "Ann Arbor is a city in the U.S. state of Michigan and the county seat of Washtenaw County."
        - Q12439
</ve-snippet>

<ve-snippet collapsible label="Location defined with Wikidata ID">
    .ve-map 42.281,-83.748 10 width=50%
        - Q485172
</ve-snippet>

<ve-snippet collapsible label="Location defined with Wikidata ID">
    .ve-map 42.281,-83.748 10 width=50% prefer-geojson
        - Q485172
</ve-snippet>

<ve-snippet collapsible label="Multiple basemaps">
    .ve-map 37.16032,-79.45313 5 width=50% basemaps=OpenStreetMap,Esri_WorldPhysical,Stamen_Watercolor
</ve-snippet>

This example includes a terrain basemap with multiple markers for cities and national parks.  Each location is defined using a Wikidata ID.

<ve-snippet collapsible label="Terrain basemap with multiple locations">
    .ve-map 37.84,-108.92 6 basemaps=Esri_WorldPhysical width=50%
        - Q16554
        - Q49258
        - Q23337
        - Q79842
        - Q777183
        - Q220289
        - Q205325
        - Q219562
        - Q223969
</ve-snippet>

This builds on the previous example by organizing the location markers into two layers, a "Cities" layer and a "National Parks" layer.  The layers may be toggled on and off using the layer control located at the top-right of the map.

<ve-snippet collapsible label="Multiple locations organized into layers">
    .ve-map 37.84,-108.92 6 basemaps=Esri_WorldPhysical width=50%
        - Q16554 layer=Cities
        - Q49258 layer=Cities
        - Q23337 layer=Cities
        - Q79842 layer=Cities
        - Q777183 layer="National Parks"
        - Q220289 layer="National Parks"
        - Q205325 layer="National Parks"
        - Q219562 layer="National Parks"
        - Q223969 layer="National Parks"
</ve-snippet>

<ve-snippet collapsible label="IIIF image as marker">
    .ve-map Q223969 5 right
        - wc:Double-O-Arch_Arches_National_Park_2.jpg

    This example uses [an image from Wikimedia commons](https://commons.wikimedia.org/wiki/File:Double-O-Arch_Arches_National_Park_2.jpg) for a marker.  The image used in this example includes embedded Exif (Exchangeable image file format) data with geographic coordinates.

    Hover over the marker or click here to see the image.

    ==The marker image will also appear when hovering over this text.  Clicking on this text will also cause the map to zoom in on the marker location.=={flyto=wc:Double-O-Arch_Arches_National_Park_2.jpg,14}
</ve-snippet>

#### Georeferenced image layer

<ve-snippet collapsible label="Map with a historic map overlay">
    .ve-map Q507517 13
        - allmaps=911e307b5cecc423
    
    This example uses an image of a historic map of the town of Rochester to overlay on top of the map in Juncture. In order to create a georeferenced image to overlay on top of your map, use the [AllMaps Editor](https://editor.allmaps.org/). You can also refere to [this how-to guide on how to use Historic Map Overlays](/howto/use-historic-maps).
</ve-snippet>

### Basemaps

The table below lists the basemaps recognized by Juncture.  To use these basemaps add the `basemaps=<NAMES>` attribute to the `.ve-map` tag.  Tne basemaps value is one or more basemap names.  Multiple names are comma delimited.  The first name will be the default basemap.

| Name | Min Zoom | Max Zoom |
| --------| -------- | -------- |
| CartoDB_DarkMatter |  | 20 |
| CartoDB_DarkMatterNoLabels |  | 20 |
| CartoDB_DarkMatterOnlyLabels |  | 20 |
| CartoDB_Positron |  | 20 |
| CartoDB_PositronNoLabels |  | 20 |
| CartoDB_PositronOnlyLabels |  | 20 |
| CartoDB_Voyager |  | 20 |
| CartoDB_VoyagerNoLabels |  | 20 |
| CartoDB_VoyagerOnlyLabels |  | 20 |
| CartoDB_VoyagerLabelsUnder |  | 20 |
| Esri_DeLorme | 1 | 11 |
| Esri_NatGeoWorldMap |  | 16 |
| Esri_OceanBasemap |  | 13 |
| Esri_WorldImagery |  |  |
| Esri_WorldPhysical |  | 8 |
| Esri_WorldShadedRelief |  | 13 |
| Esri_WorldStreetMap |  |  |
| Esri_WorldTerrain |  | 13 |
| Esri_WorldTopoMap |  |  |
| MtbMap |  |  |
| OpenStreetMap |  | 18 |
| OpenStreetMap_DE |  | 18 |
| OpenStreetMap_France |  | 18 |
| OpenStreetMap_HOT |  | 19 |
| OpenStreetMap_Mapnik |  | 19 |
| OpenTopoMap |  | 17 |
| OPNVKarte |  | 18 |
| Stadia_AlidadeSmooth |  | 20 |
| Stadia_AlidadeSmoothDark |  | 20 |
| Stadia_OSMBright |  | 20 |
| Stadia_Outdoors |  | 20 |
| Stamen_Terrain | 0 | 18 |
| Stamen_TerrainBackground | 0 | 18 |
| Stamen_TerrainLabels | 0 | 18 |
| Stamen_Toner | 0 | 20 |
| Stamen_TonerBackground | 0 | 20 |
| Stamen_TonerLite | 0 | 20 |
| Stamen_Watercolor | 1 | 16 |
| USGS_USTopo |  | 20 |
| USGS_USImagery |  | 20 |
| USGS_USImageryTopo |  | 20 |

<ve-snippet collapsible label="CartoDB_DarkMatter">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_DarkMatter
</ve-snippet>

<ve-snippet collapsible label="CartoDB_DarkMatterNoLabels">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_DarkMatterNoLabels
</ve-snippet>

<ve-snippet collapsible label="CartoDB_DarkMatterOnlyLabels">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_DarkMatterOnlyLabels
</ve-snippet>

<ve-snippet collapsible label="CartoDB_Positron">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_Positron
</ve-snippet>

<ve-snippet collapsible label="CartoDB_PositronNoLabels">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_PositronNoLabels
</ve-snippet>

<ve-snippet collapsible label="CartoDB_PositronOnlyLabels">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_PositronOnlyLabels
</ve-snippet>

<ve-snippet collapsible label="CartoDB_Voyager">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_Voyager
</ve-snippet>

<ve-snippet collapsible label="CartoDB_VoyagerNoLabels">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_VoyagerNoLabels
</ve-snippet>

<ve-snippet collapsible label="CartoDB_VoyagerOnlyLabels">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_VoyagerOnlyLabels
</ve-snippet>

<ve-snippet collapsible label="CartoDB_VoyagerLabelsUnder">
    .ve-map Q192517 12 width=50% basemaps=CartoDB_VoyagerLabelsUnder
</ve-snippet>

<ve-snippet collapsible label="Esri_DeLorme">
    .ve-map Q192517 12 width=50% basemaps=Esri_DeLorme
</ve-snippet>

<ve-snippet collapsible label="Esri_NatGeoWorldMap">
    .ve-map Q192517 12 width=50% basemaps=Esri_NatGeoWorldMap
</ve-snippet>

<ve-snippet collapsible label="Esri_OceanBasemap">
    .ve-map Q192517 12 width=50% basemaps=Esri_OceanBasemap
</ve-snippet>

<ve-snippet collapsible label="Esri_WorldGrayCanvas">
    .ve-map Q192517 12 width=50% basemaps=Esri_WorldGrayCanvas
</ve-snippet>

<ve-snippet collapsible label="Esri_WorldImagery">
    .ve-map Q192517 12 width=50% basemaps=Esri_WorldImagery
</ve-snippet>

<ve-snippet collapsible label="Esri_WorldPhysical">
    .ve-map Q192517 12 width=50% basemaps=Esri_WorldPhysical
</ve-snippet>

<ve-snippet collapsible label="Esri_WorldShadedRelief">
    .ve-map Q192517 12 width=50% basemaps=Esri_WorldShadedRelief
</ve-snippet>

<ve-snippet collapsible label="Esri_WorldStreetMap">
    .ve-map Q192517 12 width=50% basemaps=Esri_WorldStreetMap
</ve-snippet>

<ve-snippet collapsible label="Esri_WorldTerrain">
    .ve-map Q192517 12 width=50% basemaps=Esri_WorldTerrain
</ve-snippet>

<ve-snippet collapsible label="Esri_WorldTopoMap">
    .ve-map Q192517 12 width=50% basemaps=Esri_WorldTopoMap
</ve-snippet>

<ve-snippet collapsible label="MtbMap">
    .ve-map Q192517 12 width=50% basemaps=MtbMap
</ve-snippet>

<ve-snippet collapsible label="OpenStreetMap">
    .ve-map Q192517 12 width=50% basemaps=OpenStreetMap
</ve-snippet>

<ve-snippet collapsible label="OpenStreetMap_DE">
    .ve-map Q192517 12 width=50% basemaps=OpenStreetMap_DE
</ve-snippet>

<ve-snippet collapsible label="OpenStreetMap_France">
    .ve-map Q192517 12 width=50% basemaps=OpenStreetMap_France
</ve-snippet>

<ve-snippet collapsible label="OpenStreetMap_HOT">
    .ve-map Q192517 12 width=50% basemaps=OpenStreetMap_HOT
</ve-snippet>

<ve-snippet collapsible label="OpenStreetMap_Mapnik">
    .ve-map Q192517 12 width=50% basemaps=OpenStreetMap_Mapnik
</ve-snippet>

<ve-snippet collapsible label="OpenTopoMap">
    .ve-map Q192517 12 width=50% basemaps=OpenTopoMap
</ve-snippet>

<ve-snippet collapsible label="OPNVKarte">
    .ve-map Q192517 12 width=50% basemaps=OPNVKarte
</ve-snippet>

<ve-snippet collapsible label="Stadia_AlidadeSmooth">
    .ve-map Q192517 12 width=50% basemaps=Stadia_AlidadeSmooth
</ve-snippet>

<ve-snippet collapsible label="Stadia_AlidadeSmoothDark">
    .ve-map Q192517 12 width=50% basemaps=Stadia_AlidadeSmoothDark
</ve-snippet>

<ve-snippet collapsible label="Stadia_OSMBright">
    .ve-map Q192517 12 width=50% basemaps=Stadia_OSMBright
</ve-snippet>

<ve-snippet collapsible label="Stadia_Outdoors">
    .ve-map Q192517 12 width=50% basemaps=Stadia_Outdoors
</ve-snippet>

<ve-snippet collapsible label="Stamen_Terrain">
    .ve-map Q192517 12 width=50% basemaps=Stamen_Terrain
</ve-snippet>

<ve-snippet collapsible label="Stamen_TerrainBackground">
    .ve-map Q192517 12 width=50% basemaps=Stamen_TerrainBackground
</ve-snippet>

<ve-snippet collapsible label="Stamen_TerrainLabels">
    .ve-map Q192517 12 width=50% basemaps=Stamen_TerrainLabels
</ve-snippet>

<ve-snippet collapsible label="Stamen_Toner">
    .ve-map Q192517 12 width=50% basemaps=Stamen_Toner
</ve-snippet>

<ve-snippet collapsible label="Stamen_TonerBackground">
    .ve-map Q192517 12 width=50% basemaps=Stamen_TonerBackground
</ve-snippet>

<ve-snippet collapsible label="Stamen_TonerLite">
    .ve-map Q192517 12 width=50% basemaps=Stamen_TonerLite
</ve-snippet>

<ve-snippet collapsible label="Stamen_Watercolor">
    .ve-map Q192517 12 width=50% basemaps=Stamen_Watercolor
</ve-snippet>

<ve-snippet collapsible label="USGS_USTopo">
    .ve-map Q192517 12 width=50% basemaps=USGS_USTopo
</ve-snippet>

<ve-snippet collapsible label="USGS_USImagery">
    .ve-map Q192517 12 width=50% basemaps=USGS_USImagery
</ve-snippet>

<ve-snippet collapsible label="USGS_USImageryTopo">
    .ve-map Q192517 12 width=50% basemaps=USGS_USImageryTopo
</ve-snippet>

