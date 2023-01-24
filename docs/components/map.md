# ve-map
The `.ve-map` tag creates a map viewer that displays a base map with optional map layers.  The map supports zooming and panning.

## .ve-map Attributes
| Syntax | Type                                   | Description                                                         |
|--------|----------------------------------------|---------------------------------------------------------------------|
| **center** | geographic coordinates or Wikidata QID | The _center_ attribute defines the center point of a displayed map. |
| **zoom**   | number                                 | The _zoom_ attribute defines the zoom level of a displayed map.     |


#### Map with zoom level set to 10

<ve-snippet>
    .ve-map Q485172 10
</ve-snippet>

#### Map with zoom level set to 5

<ve-snippet>
    .ve-map Q485172 5
</ve-snippet>
