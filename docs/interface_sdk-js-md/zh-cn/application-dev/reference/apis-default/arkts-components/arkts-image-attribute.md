# ImageAttribute

属性的详细使用指导请参考 [添加属性](../../../ui/arkts-graphics-display.md#添加属性)。除支持通用属性外，还支持以下属性：

除支持通用事件外，还支持以下事件：

@extends CommonMethod @interface ImageAttribute

**继承/实现关系：** ImageAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-unnamed-export declare interface ImageAttribute--><!--Device-unnamed-export declare interface ImageAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## alt

```TypeScript
alt(value: string | Resource | PixelMap | ImageAlt | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-alt(value: string | Resource | PixelMap | ImageAlt | undefined): this--><!--Device-ImageAttribute-alt(value: string | Resource | PixelMap | ImageAlt | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ImageAlt](arkts-image-imagealt-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## analyzerConfig

```TypeScript
analyzerConfig(config: ImageAnalyzerConfig | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-analyzerConfig(config: ImageAnalyzerConfig | undefined): this--><!--Device-ImageAttribute-analyzerConfig(config: ImageAnalyzerConfig | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [ImageAnalyzerConfig](../../apis-arkui/arkts-apis/arkts-arkui-imagecommon-imageanalyzerconfig-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## antialiased

```TypeScript
antialiased(isAntialiased: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-antialiased(isAntialiased: boolean | undefined): this--><!--Device-ImageAttribute-antialiased(isAntialiased: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isAntialiased | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## autoResize

```TypeScript
autoResize(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-autoResize(value: boolean | undefined): this--><!--Device-ImageAttribute-autoResize(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## colorFilter

```TypeScript
colorFilter(value: ColorFilter | DrawingColorFilter | ResourceColor | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-colorFilter(value: ColorFilter | DrawingColorFilter | ResourceColor | undefined): this--><!--Device-ImageAttribute-colorFilter(value: ColorFilter | DrawingColorFilter | ResourceColor | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ColorFilter](../../apis-arkui/arkts-apis/arkts-arkui-colorfilter-c.md) \| [DrawingColorFilter](arkts-drawingcolorfilter-t.md) \| [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## contentTransition

```TypeScript
contentTransition(transition: ContentTransitionEffect | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-contentTransition(transition: ContentTransitionEffect | undefined): this--><!--Device-ImageAttribute-contentTransition(transition: ContentTransitionEffect | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transition | [ContentTransitionEffect](../../apis-arkui/arkts-components/arkts-arkui-contenttransitioneffect-c.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## copyOption

```TypeScript
copyOption(value: CopyOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-copyOption(value: CopyOptions | undefined): this--><!--Device-ImageAttribute-copyOption(value: CopyOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CopyOptions](../../apis-arkui/arkts-apis/arkts-arkui-copyoptions-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## draggable

```TypeScript
draggable(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-draggable(value: boolean | undefined): this--><!--Device-ImageAttribute-draggable(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## dynamicRangeMode

```TypeScript
dynamicRangeMode(value: DynamicRangeMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-dynamicRangeMode(value: DynamicRangeMode | undefined): this--><!--Device-ImageAttribute-dynamicRangeMode(value: DynamicRangeMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [DynamicRangeMode](arkts-image-dynamicrangemode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## edgeAntialiasing

```TypeScript
edgeAntialiasing(value: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-edgeAntialiasing(value: double | undefined): this--><!--Device-ImageAttribute-edgeAntialiasing(value: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enableAnalyzer

```TypeScript
enableAnalyzer(enable: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-enableAnalyzer(enable: boolean | undefined): this--><!--Device-ImageAttribute-enableAnalyzer(enable: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## enhancedImageQuality

```TypeScript
enhancedImageQuality(imageQuality: ResolutionQuality | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-enhancedImageQuality(imageQuality: ResolutionQuality | undefined): this--><!--Device-ImageAttribute-enhancedImageQuality(imageQuality: ResolutionQuality | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| imageQuality | [ResolutionQuality](arkts-resolutionquality-t-sys.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fillColor

```TypeScript
fillColor(color: ResourceColor | ColorContent | ColorMetrics | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-fillColor(color: ResourceColor | ColorContent | ColorMetrics | undefined): this--><!--Device-ImageAttribute-fillColor(color: ResourceColor | ColorContent | ColorMetrics | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| [ColorContent](arkts-image-colorcontent-c.md) \| [ColorMetrics](../../apis-arkui/arkts-apis/arkts-arkui-colormetrics-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## fitOriginalSize

```TypeScript
fitOriginalSize(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-fitOriginalSize(value: boolean | undefined): this--><!--Device-ImageAttribute-fitOriginalSize(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## hdrBrightness

```TypeScript
hdrBrightness(brightness: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-hdrBrightness(brightness: double | undefined): this--><!--Device-ImageAttribute-hdrBrightness(brightness: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| brightness | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## imageMatrix

```TypeScript
imageMatrix(matrix: ImageMatrix | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-imageMatrix(matrix: ImageMatrix | undefined): this--><!--Device-ImageAttribute-imageMatrix(matrix: ImageMatrix | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matrix | [ImageMatrix](arkts-imagematrix-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## interpolation

```TypeScript
interpolation(value: ImageInterpolation | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-interpolation(value: ImageInterpolation | undefined): this--><!--Device-ImageAttribute-interpolation(value: ImageInterpolation | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageInterpolation](arkts-image-imageinterpolation-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## matchTextDirection

```TypeScript
matchTextDirection(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-matchTextDirection(value: boolean | undefined): this--><!--Device-ImageAttribute-matchTextDirection(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## objectFit

```TypeScript
objectFit(value: ImageFit | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-objectFit(value: ImageFit | undefined): this--><!--Device-ImageAttribute-objectFit(value: ImageFit | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageFit](../../apis-arkui/arkts-apis/arkts-arkui-imagefit-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## objectRepeat

```TypeScript
objectRepeat(value: ImageRepeat | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-objectRepeat(value: ImageRepeat | undefined): this--><!--Device-ImageAttribute-objectRepeat(value: ImageRepeat | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageRepeat](../../apis-arkui/arkts-apis/arkts-arkui-imagerepeat-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onComplete

```TypeScript
onComplete(callback: ImageOnCompleteCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-onComplete(callback: ImageOnCompleteCallback | undefined): this--><!--Device-ImageAttribute-onComplete(callback: ImageOnCompleteCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ImageOnCompleteCallback](arkts-imageoncompletecallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onError

```TypeScript
onError(callback: ImageErrorCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-onError(callback: ImageErrorCallback | undefined): this--><!--Device-ImageAttribute-onError(callback: ImageErrorCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [ImageErrorCallback](arkts-imageerrorcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## onFinish

```TypeScript
onFinish(event: VoidCallback | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-onFinish(event: VoidCallback | undefined): this--><!--Device-ImageAttribute-onFinish(event: VoidCallback | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## orientation

```TypeScript
orientation(orientation: ImageRotateOrientation | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-orientation(orientation: ImageRotateOrientation | undefined): this--><!--Device-ImageAttribute-orientation(orientation: ImageRotateOrientation | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| orientation | [ImageRotateOrientation](arkts-image-imagerotateorientation-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## pointLight

```TypeScript
pointLight(value: PointLightStyle | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-pointLight(value: PointLightStyle | undefined): this--><!--Device-ImageAttribute-pointLight(value: PointLightStyle | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [PointLightStyle](../../apis-arkui/arkts-components/arkts-arkui-pointlightstyle-i-sys.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## privacySensitive

```TypeScript
privacySensitive(supported: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-privacySensitive(supported: boolean | undefined): this--><!--Device-ImageAttribute-privacySensitive(supported: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| supported | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## renderMode

```TypeScript
renderMode(value: ImageRenderMode | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-renderMode(value: ImageRenderMode | undefined): this--><!--Device-ImageAttribute-renderMode(value: ImageRenderMode | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageRenderMode](arkts-image-imagerendermode-e.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## resizable

```TypeScript
resizable(value: ResizableOptions | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-resizable(value: ResizableOptions | undefined): this--><!--Device-ImageAttribute-resizable(value: ResizableOptions | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ResizableOptions](arkts-image-resizableoptions-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setImageOptions

```TypeScript
setImageOptions(
        src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined, 
        imageAIOptions?: ImageAIOptions
    ): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-setImageOptions(        src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,         imageAIOptions?: ImageAIOptions    ): this--><!--Device-ImageAttribute-setImageOptions(        src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,         imageAIOptions?: ImageAIOptions    ): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../arkts-apis/arkts-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-image-imagecontent-e.md) \| undefined | 是 |  |
| imageAIOptions | [ImageAIOptions](../../apis-arkui/arkts-apis/arkts-arkui-imagecommon-imageaioptions-i.md) | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setImageOptions

```TypeScript
setImageOptions(
        src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined, 
        imageAIOptions?: ImageAIOptions,
        reloadKey?: string
    ): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-setImageOptions(        src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,         imageAIOptions?: ImageAIOptions,        reloadKey?: string    ): this--><!--Device-ImageAttribute-setImageOptions(        src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,         imageAIOptions?: ImageAIOptions,        reloadKey?: string    ): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../arkts-apis/arkts-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-image-imagecontent-e.md) \| undefined | 是 |  |
| imageAIOptions | [ImageAIOptions](../../apis-arkui/arkts-apis/arkts-arkui-imagecommon-imageaioptions-i.md) | 否 |  |
| reloadKey | string | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setImageOptions

```TypeScript
setImageOptions(
        src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined, 
        reloadKey?: string
    ): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-setImageOptions(        src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,         reloadKey?: string    ): this--><!--Device-ImageAttribute-setImageOptions(        src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined,         reloadKey?: string    ): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | [PixelMap](../../apis-arkui/arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](../../apis-arkui/arkts-apis/arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](../arkts-apis/arkts-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-image-imagecontent-e.md) \| undefined | 是 |  |
| reloadKey | string | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## sourceSize

```TypeScript
sourceSize(value: ImageSourceSize | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-sourceSize(value: ImageSourceSize | undefined): this--><!--Device-ImageAttribute-sourceSize(value: ImageSourceSize | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ImageSourceSize](arkts-image-imagesourcesize-i.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## supportSvg2

```TypeScript
supportSvg2(enable: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-supportSvg2(enable: boolean | undefined): this--><!--Device-ImageAttribute-supportSvg2(enable: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## syncLoad

```TypeScript
syncLoad(value: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为-1。

<!--Device-ImageAttribute-syncLoad(value: boolean | undefined): this--><!--Device-ImageAttribute-syncLoad(value: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置位图图片边缘是否开启抗锯齿。未通过该接口设置时，默认不开启抗锯齿。SVG类型图片不支持该属性。

> **说明：**
> 
> 如果图片设置了背景色属性(backgroundColor)， &gt; 图片的抗锯齿属性设置为true不会影响背景 &gt; 色的锯齿效果。
> 
> 和[resizable](#resizable)一起使用时，该属性不生效。

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageAttribute-default--><!--Device-ImageAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

