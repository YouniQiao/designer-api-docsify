# ImageFilter

图像滤波器，用于对图像应用各种滤波效果，支持创建模糊、颜色混合、级联组合、偏移、基于着色器等多种图像滤波器。

> **说明：**
> 
> - 本Class首批接口从API version 12开始支持。
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 12

<!--Device-drawing-class ImageFilter--><!--Device-drawing-class ImageFilter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## createBlendImageFilter

```TypeScript
static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter
```

按照指定的混合模式对两个滤波器进行叠加，生成一个新的滤波器。

**起始版本：** 20

<!--Device-ImageFilter-static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter--><!--Device-ImageFilter-static createBlendImageFilter(mode: BlendMode, background: ImageFilter, foreground: ImageFilter): ImageFilter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| mode | [BlendMode](../../apis-arkui/arkts-components/arkts-arkui-blendmode-e.md) | 是 |
| background | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 是 |
| foreground | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [25900001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-arkgraphics2d/errorcode-drawing.md#25900001-参数值异常) |

## createBlurImageFilter

```TypeScript
static createBlurImageFilter(sigmaX: number, sigmaY: number,
        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter
```

创建具有模糊效果的图像滤波器。

**起始版本：** 12

<!--Device-ImageFilter-static createBlurImageFilter(sigmaX: number, sigmaY: number,        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter--><!--Device-ImageFilter-static createBlurImageFilter(sigmaX: number, sigmaY: number,        tileMode: TileMode, imageFilter?: ImageFilter | null): ImageFilter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sigmaX | number | 是 |
| sigmaY | number | 是 |
| tileMode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |
| imageFilter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## createComposeImageFilter

```TypeScript
static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter
```

将两个图像滤波器进行级联，生成新的图像滤波器，级联时会将第一级滤波器的输出作为第二级滤波器的输入，经过第二级滤波器处理后，输出最终的滤波结果。

**起始版本：** 20

<!--Device-ImageFilter-static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter--><!--Device-ImageFilter-static createComposeImageFilter(cOuter: ImageFilter, cInner: ImageFilter): ImageFilter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cOuter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 是 |
| cInner | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) |

## createFromColorFilter

```TypeScript
static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter
```

创建一个图像滤波器，将指定的颜色滤波器应用于输入的图像滤波器。

**起始版本：** 12

<!--Device-ImageFilter-static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter--><!--Device-ImageFilter-static createFromColorFilter(colorFilter: ColorFilter, imageFilter?: ImageFilter | null): ImageFilter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorFilter | [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) | 是 |
| imageFilter | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

## createFromImage

```TypeScript
static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter
```

基于给定的图像创建一个图像滤波器。此接口不建议用于录制类型的画布（即用于记录绘制指令而非直接渲染的Canvas对象），会影响性能。

**起始版本：** 20

<!--Device-ImageFilter-static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter--><!--Device-ImageFilter-static createFromImage(pixelmap: image.PixelMap, srcRect?: common2D.Rect | null, dstRect?: common2D.Rect | null): ImageFilter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelmap | image.PixelMap | 是 |
| srcRect | common2D.Rect \| null | 否 |
| dstRect | common2D.Rect \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) |

## createFromShaderEffect

```TypeScript
static createFromShaderEffect(shader: ShaderEffect): ImageFilter
```

基于着色器创建一个图像滤波器。

**起始版本：** 20

<!--Device-ImageFilter-static createFromShaderEffect(shader: ShaderEffect): ImageFilter--><!--Device-ImageFilter-static createFromShaderEffect(shader: ShaderEffect): ImageFilter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| shader | [ShaderEffect](arkts-arkgraphics2d-drawing-shadereffect-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) |

## createOffsetImageFilter

```TypeScript
static createOffsetImageFilter(dx: number, dy: number, input?: ImageFilter | null): ImageFilter
```

创建一个偏移滤波器，将输入的滤波器按照指定向量进行平移。

**起始版本：** 20

<!--Device-ImageFilter-static createOffsetImageFilter(dx: number, dy: number, input?: ImageFilter | null): ImageFilter--><!--Device-ImageFilter-static createOffsetImageFilter(dx: number, dy: number, input?: ImageFilter | null): ImageFilter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dx | number | 是 |
| dy | number | 是 |
| input | [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageFilter](arkts-arkgraphics2d-drawing-imagefilter-c.md) |
