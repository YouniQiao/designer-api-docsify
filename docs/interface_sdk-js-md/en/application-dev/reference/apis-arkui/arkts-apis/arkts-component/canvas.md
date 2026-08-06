# component/canvas

## Summary

### Classes

| Name | Description |
| --- | --- |
| [CanvasGradient](canvas-canvasgradient-c.md) | Opaque objects that describe gradients, created by createLinearGradient() or createRadialGradient() |
| [CanvasPath](canvas-canvaspath-c.md) | Path object, which provides basic methods for drawing paths. |
| [CanvasRenderer](canvas-canvasrenderer-c.md) | Canvas renderer for drawing shapes, text, images and other objects |
| [CanvasRenderingContext2D](canvas-canvasrenderingcontext2d-c.md) | Draw context object for the Canvas component. |
| [DrawingRenderingContext](canvas-drawingrenderingcontext-c.md) | Defines DrawingRenderingContext. |
| [ImageBitmap](canvas-imagebitmap-c.md) | Bitmap image object that can be drawn onto the current Canvas |
| [ImageData](canvas-imagedata-c.md) | Image data object |
| [OffscreenCanvas](canvas-offscreencanvas-c.md) | Draw an object off the screen. The drawing content is not directly displayed on the screen. |
| [OffscreenCanvasRenderingContext2D](canvas-offscreencanvasrenderingcontext2d-c.md) | Draw context object for the OffscreenCanvas component. |
| [Path2D](canvas-path2d-c.md) | 2D path object for path drawing |
| [RenderingContextSettings](canvas-renderingcontextsettings-c.md) | This object allows you to set properties when creating a rendering context |

### Interfaces

| Name | Description |
| --- | --- |
| [CanvasParams](canvas-canvasparams-i.md) | Defines the parameters for creating Canvas. |
| [CanvasPattern](canvas-canvaspattern-i.md) | Describes an opaque object of a template, which is created using the createPattern() method. |
| [RenderingContextOptions](canvas-renderingcontextoptions-i.md) | Defines the options for rendering context. |
| [TextMetrics](canvas-textmetrics-i.md) | Size information of the text |

### Types

| Name | Description |
| --- | --- |
| [CanvasDirection](arkts-arkui-canvasdirection-t.md) | Indicates the attribute of the current text direction. The options are as follows:'inherit': (Default) Inherit current Canvas component settings'ltr': The text direction is left to right.'rtl': The text direction is from right to left. |
| [CanvasFillRule](arkts-arkui-canvasfillrule-t.md) | Filling style algorithm, which determines whether a point is within or outside the path. The following two configurations are supported:'evenodd': odd and even round rule'nonzero': (Default) Non-zero Wrap Rules |
| [CanvasLineCap](arkts-arkui-canvaslinecap-t.md) | Specifies the attribute of drawing the end of each line segment. The following configurations are supported:'butt': (Default) Segment Ends in Square'round': Segment ends in a circle'square': The end of the segment ends in a square, but a rectangular area is added that is the same width as the segment and is half the thickness of the segment. |
| [CanvasLineJoin](arkts-arkui-canvaslinejoin-t.md) | Sets the attribute of how two connected parts (line segments, arcs, and curves) whose length is not 0are connected together. The following three configurations are supported:'bevel': Fill the ends of the connected sections with an additional triangle-base area,each with its own independent rectangular corner.'miter': (Default) An additional diamond region is formed by extending the outer edges of the connected portions so that they intersect at a point.'round': Draw the shape of the corner by filling in an additional sector with the center at the end of the connected section. The radius of the fillet is the width of the segment. |
| [CanvasTextAlign](arkts-arkui-canvastextalign-t.md) | Describes the alignment mode for drawing text. The options are as follows:'center': The text is centered.'end': Where text aligns lines end (Left alignment refers to the local from left to right,and right alignment refers to the local from right to left)'left': (Default) The text is left-aligned.'right': The text is right-aligned.'start': Where the text snap line begins (Left alignment refers to the local from left to right,and right alignment refers to the local from right to left) |
| [CanvasTextBaseline](arkts-arkui-canvastextbaseline-t.md) | Text baseline, which supports the following configurations:'alphabetic': (Default) The text baseline is the standard letter baseline.'bottom': The text baseline is at the bottom of the text block. The difference between the ideographic baseline and the ideographic baseline is that the ideographic baseline does not need to consider downlink letters.'hanging': The text baseline is a hanging baseline.'ideographic': The text baseline is the ideographic baseline; If the character itself exceeds the alphabetic baseline, the ideographic baseline is at the bottom of the character itself.'middle': The text baseline is in the middle of the text block.'top': The text baseline is at the top of the text block. |
| [ImageSmoothingQuality](arkts-arkui-imagesmoothingquality-t.md) | Sets the image smoothness attribute. The options are as follows:'high': height'low': (default)low'medium': medium |

