# @ohos.graphics.drawing

开发者在绘制界面元素时，若ArkUI组件无法满足自定义图形需求，可使用Drawing模块实现灵活的自定义绘制效果。Drawing模块提供基础的图形绘制能力，包括绘制矩形、圆形、点、直线、自定义Path和字体等。

> **说明：**
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 11

<!--Device-unnamed-declare namespace drawing--><!--Device-unnamed-declare namespace drawing-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## 汇总

### 类

| 名称 |
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

### 接口

| 名称 |
| --- |
| [FontFeature](arkts-arkgraphics2d-drawing-fontfeature-i.md) |
| [FontMetrics](arkts-arkgraphics2d-drawing-fontmetrics-i.md) |
| [TextBlobRunBuffer](arkts-arkgraphics2d-drawing-textblobrunbuffer-i.md) |

### 枚举

| 名称 |
| --- |
| [BlendMode](arkts-arkgraphics2d-drawing-blendmode-e.md) |
| [BlurType](arkts-arkgraphics2d-drawing-blurtype-e.md) | 定义蒙版滤镜模糊中操作类型的枚举。蒙版用于定义图像的可绘制区域，滤镜用于应用模糊等视觉效果。该枚举控制模糊效果如何应用到蒙版定义的区域内。  \| 名称 \| 值 \| 说明 \| 示意图 \|  \| ------ \| - \| ------------------ \| -------- \|  \| NORMAL \| 0 \| 全面模糊，外圈和内部实体一起模糊。 \| ![NORMAL](../../../reference/apis-arkgraphics2d/figures/BlurType-Normal.png) \|  \| SOLID \| 1 \| 内部实体不变，只模糊外圈边缘部分。 \| ![SOLID](../../../reference/apis-arkgraphics2d/figures/BlurType-Solid.png) \|  \| OUTER \| 2 \| 只有外圈边缘模糊，内部实体完全透明。 \| ![OUTER](../../../reference/apis-arkgraphics2d/figures/BlurType-Outer.png) \|  \| INNER \| 3 \| 只有内部实体模糊，外圈边缘清晰。 \| ![INNER](../../../reference/apis-arkgraphics2d/figures/BlurType-Inner.png) \|
| [CapStyle](arkts-arkgraphics2d-drawing-capstyle-e.md) |
| [ClipOp](arkts-arkgraphics2d-drawing-clipop-e.md) |
| [CornerPos](arkts-arkgraphics2d-drawing-cornerpos-e.md) |
| [FilterMode](arkts-arkgraphics2d-drawing-filtermode-e.md) |
| [FontEdging](arkts-arkgraphics2d-drawing-fontedging-e.md) |
| [FontHinting](arkts-arkgraphics2d-drawing-fonthinting-e.md) |
| [FontMetricsFlags](arkts-arkgraphics2d-drawing-fontmetricsflags-e.md) |
| [JoinStyle](arkts-arkgraphics2d-drawing-joinstyle-e.md) |
| [PathDashStyle](arkts-arkgraphics2d-drawing-pathdashstyle-e.md) | 路径效果的绘制样式枚举。  \| 名称 \| 值 \| 说明 \|  \| ------ \| - \| ------------------ \|  \| TRANSLATE \| 0 \| 不会随着路径旋转，只会平移。 \|  \| ROTATE \| 1 \| 随着路径的旋转而旋转。 \|  \| MORPH \| 2 \| 随着路径的旋转而旋转，并在转折处进行拉伸或压缩等操作以增加平滑度。 \|
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
