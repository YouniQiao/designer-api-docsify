# ImageAttribute

属性的详细使用指导请参考 [添加属性](../../../ui/arkts-graphics-display.md#添加属性)。除支持通用属性外，还支持以下属性：除支持通用事件外，还支持以下事件：@extends CommonMethod @interface ImageAttribute

**继承/实现关系：** ImageAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## alt

```TypeScript
default alt(value: string | Resource | PixelMap | ImageAlt | undefined): this
```

设置图片加载过程中和加载失败时的占位图。

> **说明：**&gt;
> 通过[ImageAlt](arkts-arkui-image-imagealt-i.md)配置占位图时，
> Image会根据用户配置的加载过程中和加载失败的占位图源生效，未配置时默认不显示。
占位图支持使用[objectFit](#objectfit)设置填充效果，与图片的填充效果一致。当组件的参数类型为 AnimatedDrawableDescriptor时设置该 属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ImageAlt](arkts-arkui-image-imagealt-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## antialiased

```TypeScript
default antialiased(isAntialiased: boolean | undefined): this
```

设置位图图片边缘是否开启抗锯齿。未通过该接口设置时，默认不开启抗锯齿。SVG类型图片不支持该属性。

> **说明：**&gt;
> 如果图片设置了背景色属性(backgroundColor)，
> 图片的抗锯齿属性设置为true不会影响背景
> 色的锯齿效果。&gt;
> 和[resizable](#resizable)一起使用时，该属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isAntialiased | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## autoResize

```TypeScript
default autoResize(value: boolean | undefined): this
```

设置图片解码过程中是否对图源自动缩放。降采样解码时图片的部分信息丢失， 因此可能会导致图片质量的下降（如：出现锯齿）， 这时可以选择把autoResize设为false，按原图尺寸解码，提升显示效果，但会增加内存占用。原图尺寸和显示尺寸不匹配时，图片都会出现些许的失真、模糊。最佳清晰度配置建议：图片缩小显示时：.autoResize(false) + .interpolation(.Medium)图片放大显示时：.interpolation(.High)当组件的参数类型为 AnimatedDrawableDescriptor和SVG 时设置该属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## colorFilter

```TypeScript
default colorFilter(value: ColorFilter | DrawingColorFilter | ResourceColor | undefined): this
```

为图像设置颜色滤镜效果。设置该属性时，[renderMode](#rendermode)属性设置不生效。当值为ResourceColor类型时，它将被转换为带有混合模式的 [DrawingColorFilter](arkts-arkui-drawingcolorfilter-t.md)。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ColorFilter](arkts-arkui-colorfilter-c.md) \| [DrawingColorFilter](arkts-arkui-drawingcolorfilter-t.md) \| [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## contentTransition

```TypeScript
default contentTransition(transition: ContentTransitionEffect | undefined): this
```

图片内容发生变化时，触发过渡动效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| transition | [ContentTransitionEffect](../arkts-components/arkts-arkui-contenttransitioneffect-c.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## copyOption

```TypeScript
default copyOption(value: CopyOptions | undefined): this
```

设置图片是否可复制。当copyOption设置为非CopyOptions.None时，支持使用长按、鼠标右击、 快捷组合键'CTRL+C'等方式进行复制。 SVG图片不支持复制。当组件的参数类型为 AnimatedDrawableDescriptor时设置该 属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CopyOptions](arkts-arkui-copyoptions-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## draggable

```TypeScript
default draggable(value: boolean | undefined): this
```

设置组件默认拖拽效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## dynamicRangeMode

```TypeScript
default dynamicRangeMode(value: DynamicRangeMode | undefined): this
```

设置期望展示的图像动态范围。SVG类型图源不支持该属性。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [DynamicRangeMode](arkts-arkui-image-dynamicrangemode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## enableAnalyzer

```TypeScript
default enableAnalyzer(enable: boolean | undefined): this
```

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能。<!--RP3--><!--RP3End-->不能和overlay属性同时使用，两者同时设置时overlay中 CustomBuilder属性将失效。 该特性依赖设备能力。分析图像要求是静态非矢量图，即svg、gif等图像类型不支持分析，支持传入 [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md)进行分析，目前仅支持 [RGBA_8888](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmapformat-e.md)类型，使用方式见 [示例5（开启图像AI分析）] (../../../reference/apis-arkui/arkui-ts/ts-basic-components-image.md#示例5开启图像ai分析)。  
[alt](#alt)占位图不支持分析，[objectRepeat](#objectrepeat)属性仅在 取值为ImageRepeat.NoRepeat时支持分析，隐私遮罩属性 obscured打开时不支持分析。基于完整原始图像进行分析，设置clip、 margin、 borderRadius、 position和[objectFit](#objectfit)属性导致图像显示不完整， 或使用[renderMode](#rendermode)设置蒙层，仍基于完整原始图像进行分析。 [copyOption](#copyoption) 属性不影响AI分析功能。当组件的参数类型为 AnimatedDrawableDescriptor时设置该 属性不生效。

> **说明：**&gt;
> - 需要配置权限：ohos.permission.INTERNET。&gt;
> - 从API version 12开始，该接口支持在attributeModifier中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## fillColor

```TypeScript
default fillColor(color: ResourceColor | ColorContent | ColorMetrics | undefined): this
```

设置填充颜色，设置后填充颜色会覆盖在图片上。仅对svg图源生效，设置后会替换svg图片中所有可绘制元素的填充颜色。 如需对png图片进行修改颜色，可以使用 [colorFilter](#colorfilter)。 如果想重置填充颜色可以传入[ColorContent](arkts-arkui-image-colorcontent-c.md)类型。 支持通过传入[ColorMetrics](arkts-arkui-graphics-colormetrics-c.md)类型设置P3色域颜色值， 可在支持高色域的设备上获得更丰富的色彩表现。当组件的参数类型为 AnimatedDrawableDescriptor时设置该 属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [ColorContent](arkts-arkui-image-colorcontent-c.md) \| [ColorMetrics](arkts-arkui-colormetrics-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## fitOriginalSize

```TypeScript
default fitOriginalSize(value: boolean | undefined): this
```

设置图片的显示尺寸是否跟随图源尺寸。图片组件已设置width、height属性时，fitOriginalSize属性不生效。当组件的参数类型为 AnimatedDrawableDescriptor时设置该 属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## hdrBrightness

```TypeScript
default hdrBrightness(brightness: double | undefined): this
```

设置组件在显示HDR图片时的亮度。SVG类型图源不支持该属性。该属性与 [dynamicRangeMode](#dynamicrangemode)属性同时设置时，[dynamicRangeMode](#dynamicrangemode)属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| brightness | double \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## imageMatrix

```TypeScript
default imageMatrix(matrix: ImageMatrix | undefined): this
```

设置图片的变换矩阵。通过[ImageMatrix](#imagematrix)对象使用平移、旋转、缩放等函数， 实现宫格缩略图的最佳呈现。 SVG类型图源不支持该属性。设置[resizable](#resizable)、[objectRepeat](#objectrepeat)属性时，该属性设置不生效。 该属性只针对图源做处理，不会触发Image组件的回调事件。该属性与[objectFit](#objectfit)属性强关联，仅在[objectFit](#objectfit)属性设置为ImageFit.MATRIX时生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [ImageMatrix](arkts-arkui-imagematrix-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## interpolation

```TypeScript
default interpolation(value: ImageInterpolation | undefined): this
```

定义图片插值效果。用于优化图片缩放时的锯齿问题。SVG类型图源不支持该属性。当组件的参数类型为 AnimatedDrawableDescriptor时设置该 属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ImageInterpolation](arkts-arkui-image-imageinterpolation-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## matchTextDirection

```TypeScript
default matchTextDirection(value: boolean | undefined): this
```

设置图片是否跟随系统语言方向，在RTL语言环境下显示镜像翻转显示效果。当组件的参数类型为 AnimatedDrawableDescriptor时设置该 属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## objectFit

```TypeScript
default objectFit(value: ImageFit | undefined): this
```

设置图片的填充效果。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ImageFit](arkts-arkui-imagefit-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## objectRepeat

```TypeScript
default objectRepeat(value: ImageRepeat | undefined): this
```

设置图片的重复样式，从中心点向两边重复，剩余空间不足放下一张图片时会截断。SVG类型图源不支持该属性。当组件的参数类型为 AnimatedDrawableDescriptor时设置该 属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ImageRepeat](arkts-arkui-imagerepeat-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## onComplete

```TypeScript
default onComplete(callback: ImageOnCompleteCallback | undefined): this
```

图片数据加载成功和解码成功时均触发该回调，使用callback异步回调，返回成功加载的图片尺寸。当组件的参数类型为 AnimatedDrawableDescriptor时该事件 不触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ImageOnCompleteCallback](arkts-arkui-imageoncompletecallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## onError

```TypeScript
default onError(callback: ImageErrorCallback | undefined): this
```

图片加载异常时触发该回调。当组件的参数类型为 AnimatedDrawableDescriptor时该事件 不触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ImageErrorCallback](arkts-arkui-imageerrorcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## onFinish

```TypeScript
default onFinish(event: VoidCallback | undefined): this
```

当加载的源文件为带动效的SVG格式图片时，SVG动效播放完成时会触发这个回调。 如果动效为无限循环动效，则不会触发这个回调。仅支持SVG格式的图片。当组件的参数类型为 AnimatedDrawableDescriptor 时该事件不触发。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## orientation

```TypeScript
default orientation(orientation: ImageRotateOrientation | undefined): this
```

设置图像内容的显示方向。该属性对[alt](#alt)占位图不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [orientation](#orientation) | [ImageRotateOrientation](arkts-arkui-image-imagerotateorientation-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## privacySensitive

```TypeScript
default privacySensitive(supported: boolean | undefined): this
```

设置是否支持卡片敏感隐私信息。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| supported | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## renderMode

```TypeScript
default renderMode(value: ImageRenderMode | undefined): this
```

设置图片的渲染模式。SVG类型图源不支持该属性。设置ColorFilter时， 该属性设置不生效。当组件的参数类型为 AnimatedDrawableDescriptor时设置该 属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ImageRenderMode](arkts-arkui-image-imagerendermode-e.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## resizable

```TypeScript
default resizable(value: ResizableOptions | undefined): this
```

设置图像拉伸时可调整大小的图像选项。拉伸对拖拽缩略图以及占位图有效。设置合法的 [ResizableOptions](arkts-arkui-image-resizableoptions-i.md) 时， objectRepeat属性、antialiased属性和orientation属性设置不生效。当设置 top +bottom 大于原图的高或者 left + right 大于原图的宽时 [ResizableOptions](arkts-arkui-image-resizableoptions-i.md) 属性设置不生效。当组件的参数类型为 AnimatedDrawableDescriptor和SVG 时设置该属性不生效。

> **说明：**&gt;
> 从API version 20开始，该接口支持在attributeModifier中调用。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResizableOptions](arkts-arkui-image-resizableoptions-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## setImageOptions

```TypeScript
default setImageOptions(
        src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined, 
        imageAIOptions?: ImageAIOptions
    ): this
```

设置加载时显示的占位图片。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-arkui-image-imagecontent-e.md) \| undefined | 是 |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imagecommon-imageaioptions-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## setImageOptions

```TypeScript
default setImageOptions(
        src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined, 
        imageAIOptions?: ImageAIOptions,
        reloadKey?: string
    ): this
```

设置加载时显示的占位图片。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-arkui-image-imagecontent-e.md) \| undefined | 是 |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imagecommon-imageaioptions-i.md) | 否 |
| reloadKey | string | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## setImageOptions

```TypeScript
default setImageOptions(
        src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined, 
        reloadKey?: string
    ): this
```

设置加载时显示的占位图片。

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-arkui-image-imagecontent-e.md) \| undefined | 是 |
| reloadKey | string | 否 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## sourceSize

```TypeScript
default sourceSize(value: ImageSourceSize | undefined): this
```

设置图片解码尺寸。仅在目标尺寸小于图源尺寸时生效。SVG类型图源和PixelMap资源不支持该属性。当组件的参数类型为 AnimatedDrawableDescriptor时设置该 属性不生效。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ImageSourceSize](arkts-arkui-image-imagesourcesize-i.md) \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## supportSvg2

```TypeScript
default supportSvg2(enable: boolean | undefined): this
```

开启或关闭SVG标签解析能力增强功能， 开启后相关SVG图片显示效果会有变化。Image组件创建后，不支持动态修改该属性的值。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## syncLoad

```TypeScript
default syncLoad(value: boolean | undefined): this
```

设置是否同步加载图片。建议加载尺寸较小的本地图片时将syncLoad设为true，因为耗时较短，在主线程上执行即可。当组件的参数类型为 AnimatedDrawableDescriptor时设置该 属性不生效。如果加载图片时出现闪烁，设置syncLoad为true。详情请参见 [并发优化] (https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-click-to-click-response-optimization# section715115119192)。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean \| undefined | 是 |

**返回值：**

| 类型 |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |
