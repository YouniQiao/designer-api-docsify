# @ohos.graphics.drawing

During application development, you often need to draw different elements. Typically, you can use ArkUI components to draw the desired elements or effects. However, sometimes these components cannot meet the needs for custom graphics or effects. In such cases, you can turn to the Drawing module for flexible custom drawing. This module provides basic drawing capabilities, such as drawing rectangles, circles, points, straight lines, custom paths, and fonts.

> **NOTE：**&gt;
> - This module uses the physical pixel unit, px.&gt;
> - The module operates under a single-threaded model. The caller needs to manage thread safety and context state
> transitions.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## Summary

### Classes

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Brush](arkts-arkgraphics2d-drawing-brush-c.md) |
| [Canvas](arkts-arkgraphics2d-drawing-canvas-c.md) |
| [ColorFilter](arkts-arkgraphics2d-drawing-colorfilter-c.md) |
| [Font](arkts-arkgraphics2d-drawing-font-c.md) |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) |
| [Lattice](arkts-arkgraphics2d-drawing-lattice-c.md) |
| [MaskFilter](arkts-arkgraphics2d-drawing-maskfilter-c.md) |
| [Matrix](arkts-arkgraphics2d-drawing-matrix-c.md) |
| [Path](arkts-arkgraphics2d-drawing-path-c.md) |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) |
| [PathIterator](arkts-arkgraphics2d-drawing-pathiterator-c.md) |
| [Pen](arkts-arkgraphics2d-drawing-pen-c.md) |
| [PointUtils](arkts-arkgraphics2d-drawing-pointutils-c.md) |
| [RectUtils](arkts-arkgraphics2d-drawing-rectutils-c.md) |
| [Region](arkts-arkgraphics2d-drawing-region-c.md) |
| [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) |
| [SamplingOptions](arkts-arkgraphics2d-drawing-samplingoptions-c.md) |
| [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) |
| [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) |
| [TextBlob](arkts-arkgraphics2d-drawing-textblob-c.md) |
| [Tool](arkts-arkgraphics2d-drawing-tool-c.md) |
| [Typeface](arkts-arkgraphics2d-drawing-typeface-c.md) |
| [TypefaceArguments](arkts-arkgraphics2d-drawing-typefacearguments-c.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [FontFeature](arkts-arkgraphics2d-drawing-fontfeature-i.md) |
| [FontMetrics](arkts-arkgraphics2d-drawing-fontmetrics-i.md) |
| [TextBlobRunBuffer](arkts-arkgraphics2d-drawing-textblobrunbuffer-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [BlendMode](arkts-arkgraphics2d-drawing-blendmode-e.md) |
| [BlurType](arkts-arkgraphics2d-drawing-blurtype-e.md) | Enumerates the blur types of a mask filter. \| Name \| Value\| Description \| Diagram \| \| ------ \| - \| ------------------ \| -------- \| \| NORMAL \| 0 \| Both the outer edges and the inner solid parts are blurred.\|\| \| SOLID \| 1 \| The inner solid part remains unchanged, while only the outer edges are blurred.\|\| \| OUTER \| 2 \| Only the outer edges are blurred, with the inner solid part being fully transparent.\|\| \| INNER \| 3 \| Only the inner solid part is blurred, while the outer edges remain sharp.\|\|
| [CapStyle](arkts-arkgraphics2d-drawing-capstyle-e.md) |
| [ClipOp](arkts-arkgraphics2d-drawing-clipop-e.md) |
| [CornerPos](arkts-arkgraphics2d-drawing-cornerpos-e.md) |
| [FilterMode](arkts-arkgraphics2d-drawing-filtermode-e.md) |
| [FontEdging](arkts-arkgraphics2d-drawing-fontedging-e.md) |
| [FontHinting](arkts-arkgraphics2d-drawing-fonthinting-e.md) |
| [FontMetricsFlags](arkts-arkgraphics2d-drawing-fontmetricsflags-e.md) |
| [JoinStyle](arkts-arkgraphics2d-drawing-joinstyle-e.md) |
| [PathDashStyle](arkts-arkgraphics2d-drawing-pathdashstyle-e.md) | Enumerates the drawing styles for path effects. \| Name \| Value\| Description \| \| ------ \| - \| ------------------ \| \| TRANSLATE \| 0 \| Translates only, not rotating with the path.\| \| ROTATE \| 1 \| Rotates with the path.\| \| MORPH \| 2 \| Rotates with the path and stretches or compresses at turns to enhance smoothness.\|
| [PathDirection](arkts-arkgraphics2d-drawing-pathdirection-e.md) |
| [PathFillType](arkts-arkgraphics2d-drawing-pathfilltype-e.md) |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) |
| [PathMeasureMatrixFlags](arkts-arkgraphics2d-drawing-pathmeasurematrixflags-e.md) |
| [PathOp](arkts-arkgraphics2d-drawing-pathop-e.md) |
| [PointMode](arkts-arkgraphics2d-drawing-pointmode-e.md) |
| [RectType](arkts-arkgraphics2d-drawing-recttype-e.md) |
| [RegionOp](arkts-arkgraphics2d-drawing-regionop-e.md) |
| [ScaleToFit](arkts-arkgraphics2d-drawing-scaletofit-e.md) |
| [ShadowFlag](arkts-arkgraphics2d-drawing-shadowflag-e.md) |
| [SrcRectConstraint](arkts-arkgraphics2d-drawing-srcrectconstraint-e.md) |
| [TextEncoding](arkts-arkgraphics2d-drawing-textencoding-e.md) |
| [TileMode](arkts-arkgraphics2d-drawing-tilemode-e.md) |
| [VertexMode](arkts-arkgraphics2d-drawing-vertexmode-e.md) |
