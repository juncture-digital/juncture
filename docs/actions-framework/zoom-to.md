# Zoom To

.ve-media gh:juncture-digital/media/videos/Image_Zoom_Example.mp4 right

The image zoom behavior causes the `.ve-media` viewer to zoom to a specific region of an image.  The region of interest is specified using a set of 4 coordinates defining a rectangular bounding box.  The coordinates are the `x-position`, `y-position`, `width`, and `height`.  The coordinate values may be defined as absolute pixel values or as a percentage relative to the full size of the source image.[^iiif-region]

- **x,y,w,h**: The region of the full image to be returned is specified in terms of absolute pixel values. The value of x represents the number of pixels from the 0 position on the horizontal axis. The value of y represents the number of pixels from the 0 position on the vertical axis. Thus the x,y position 0,0 is the upper left-most pixel of the image. w represents the width of the region and h represents the height of the region in pixels.
- **pct:x,y,w,h**: The region to be returned is specified as a sequence of percentages of the full image’s dimensions, as reported in the image information document. Thus, x represents the number of pixels from the 0 position on the horizontal axis, calculated as a percentage of the reported width. w represents the width of the region, also calculated as a percentage of the reported width. The same applies to y and h respectively. These may be floating point numbers.
