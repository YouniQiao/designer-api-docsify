# Image属性/事件

Image为图片组件，常用于在应用中显示图片。Image支持加载[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md)、 [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)和[DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md)类型的数据源， 支持png、jpg、jpeg、bmp、 svg、webp、gif、heif和tiff类型的图片格式，不支持apng和svga格式。

> **说明：**

> - 从API version 23开始，图片类型新增支持tiff格式。&gt;
> - 该组件从API版本26.0.0开始支持WithTheme。&gt;
> - 使用快捷组合键对Image组件复制时，Image组件必须处于获焦状态，如何获焦请参考[设置组件是否可获焦]
> (../../../ui/arkts-common-events-focus-event.md#设置组件是否可获焦)。Image组件默认不获焦，
> 需将focusable属性设置为true，即可使用Tab键将焦点切换到组件上，再将
> [focusOnTouch](arkts-arkui-commonmethod-c.md#focusontouch)属性设置为true，即可实现点击获焦。&gt;
> - 图片格式支持SVG图源，SVG标签文档请参考SVG标签说明。&gt;
> - 动图的播放依赖于Image节点的可见性变化，其默认行为是不播放的。当节点可见时，
> 通过回调启动动画，当节点不可见时，停止动画。
> 可见性状态的判断是通过[onVisibleAreaChange]
> [onVisibleAreaChange](arkts-arkui-commonmethod-c.md#onvisibleareachange)
> 事件触发的，当可见阈值ratios大于0时，表明Image处于可见状态。&gt;
> - Image组件播放GIF动图时，帧时长取自GIF文件中各帧的delay time字段。当某帧的时长值小于等于0时，
> 系统会将其修正为100ms；
> 当某帧的时长值大于0时，系统直接使用该原始值，不做最小帧时长限制。&gt;
除支持通用事件外，还支持以下事件：

**继承/实现关系：** ImageAttribute extends CommonMethod<ImageAttribute>

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
```

## alt

```TypeScript
alt(value: string | Resource | PixelMap)
```

设置图片加载过程中显示的占位图。占位图支持使用[objectFit](#objectfit)设置填充效果，与图片的填充效果一致。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时设置该属性不生效。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | string \| Resource \| [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | 是 |

## alt

```TypeScript
alt(src: ResourceStr | PixelMap | ImageAlt)
```

设置图片加载过程中和加载失败时的占位图。

> **说明：**&gt;
> 通过[ImageAlt](arkts-arkui-imagealt-i.md)配置占位图时，Image会根据用户配置的加载过程中和加载失败的占位图源生效，未配置时默认不显示。
> 占位图支持使用[objectFit](#objectfit)设置填充效果，与图片的填充效果一致。
当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时设置该属性不生效。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本22开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| PixelMap \| [ImageAlt](arkts-arkui-imagealt-i.md) | 是 |

## antialiased

```TypeScript
antialiased(isAntialiased: Optional<boolean>)
```

设置位图图片边缘是否开启抗锯齿。未通过该接口设置时，默认不开启抗锯齿。SVG类型图片不支持该属性。

> **说明：**&gt;
> 如果图片设置了背景色属性(backgroundColor)，图片的抗锯齿属性设置为true不会影响背景色的
> 锯齿效果。&gt;
> 和[resizable](#resizable)一起使用时，该属性不生效。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isAntialiased | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | 是 |

## autoResize

```TypeScript
autoResize(value: boolean)
```

设置图片解码过程中是否对图源自动缩放。降采样解码时图片的部分信息丢失，因此可能会导致图片质量的下降（如：出现锯齿），这时可以选择把autoResize设为false，按原图尺寸解码，提升显示效果，但会增加内存占用。原图尺寸和显示尺寸不匹配时，图片都会出现些许的失真、模糊。最佳清晰度配置建议：图片缩小显示时：.autoResize(false) + .interpolation(.Medium)图片放大显示时：.interpolation(.High)当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)和SVG时设置该属性不生 效。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## colorFilter

```TypeScript
colorFilter(value: ColorFilter | DrawingColorFilter)
```

为图像设置颜色滤镜效果。设置该属性时，[renderMode](#rendermode)属性设置不生效。

> **说明：**&gt;
> API version 11及之前，SVG类型图源不支持该属性。从API version 12开始，SVG类型的图源只有设置了stroke属性（无论是否有值）才会生效。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ColorFilter \| [DrawingColorFilter](arkts-arkui-drawingcolorfilter-t.md) | 是 |

## colorFilter

```TypeScript
colorFilter(value: ColorFilter | DrawingColorFilter | ResourceColor)
```

为图像设置颜色滤镜效果。设置该属性时，[renderMode](#rendermode)属性设置不生效。当值为[ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)类型时，它将被转换为带有混合模式的[DrawingColorFilter](arkts-arkui-drawingcolorfilter-t.md)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本26.0.0开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | ColorFilter \| [DrawingColorFilter](arkts-arkui-drawingcolorfilter-t.md) \| [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## contentTransition

```TypeScript
contentTransition(transition: ContentTransitionEffect)
```

图片内容发生变化时，触发过渡动效。

**起始版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| transition | [ContentTransitionEffect](arkts-arkui-contenttransitioneffect-c.md) | 是 |

## copyOption

```TypeScript
copyOption(value: CopyOptions)
```

设置图片是否可复制。当copyOption设置为非CopyOptions.None时，支持使用长按、鼠标右击、快捷组合键'CTRL+C'等方式进行复制。SVG图片不支持复制。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时设置该属性不生效。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [CopyOptions](../arkts-apis/arkts-arkui-copyoptions-e.md) | 是 |

## draggable

```TypeScript
draggable(value: boolean)
```

设置组件默认拖拽效果。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## dynamicRangeMode

```TypeScript
dynamicRangeMode(value: DynamicRangeMode)
```

设置期望展示的图像动态范围。SVG类型图源不支持该属性。该属性与[hdrBrightness](#hdrbrightness)属性同时设置时，该属性不生效。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [DynamicRangeMode](arkts-arkui-dynamicrangemode-e.md) | 是 |

## enableAnalyzer

```TypeScript
enableAnalyzer(enable: boolean)
```

设置组件支持AI分析，当前支持主体识别、文字识别和对象查找等功能。<!--RP3--><!--RP3End-->不能和overlay属性同时使用，两者同时设置时overlay中 [CustomBuilder](arkts-arkui-custombuilder-t.md)属性将失效。该特性依赖设备能力。分析图像要求是静态非矢量图，即svg、gif等图像类型不支持分析，支持传入[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md)进行分析，目前仅支持 [RGBA_8888](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmapformat-e.md)类型，使用方式见 [示例5（开启图像AI分析）](../../../reference/apis-arkui/arkui-ts/ts-basic-components-image.md#示例5开启图像ai分析)。  
[alt](#alt)占位图不支持分析， [objectRepeat](#objectrepeat)属性仅在取值为ImageRepeat.NoRepeat时支持分析，隐私遮罩属性 [obscured](arkts-arkui-commonmethod-c.md#obscured)打开时不支持分析。基于完整原始图像进行分析，设置clip、margin、 borderRadius、 position和[objectFit](#objectfit)属性导致图像显示不完整，或使用 [renderMode](#rendermode)设置蒙层，仍基于完整原始图像进行分析。 [copyOption](#copyoption)属性不影响 AI分析功能。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时设置该属性不生效。

> **说明：**&gt;
> - 需要配置权限：ohos.permission.INTERNET。&gt;
> - 从API version 12开始，该接口支持在attributeModifier中调用。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

## fillColor

```TypeScript
fillColor(value: ResourceColor)
```

设置填充颜色。仅对SVG图源生效，设置后会替换SVG图片中所有可绘制元素的填充颜色。如需对png图片进行修改颜色，可以使用 [colorFilter](#colorfilter)。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时设置该属性不生效。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | 是 |

## fillColor

```TypeScript
fillColor(color: ResourceColor | ColorContent)
```

设置填充颜色。仅对SVG图源生效，设置后会替换SVG图片中所有可绘制元素的填充颜色。如需对png图片进行修改颜色，可以使用 [colorFilter](#colorfilter)。如果想重置填充颜色可以传入 [ColorContent](arkts-arkui-colorcontent-c.md)类型。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时设置该属性不生效。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [ColorContent](arkts-arkui-colorcontent-c.md) | 是 |

## fillColor

```TypeScript
fillColor(color: ResourceColor | ColorContent | ColorMetrics)
```

设置填充颜色。仅对SVG图源生效，设置后会替换SVG图片中所有可绘制元素的填充颜色。如需对png图片进行修改颜色，可以使用 [colorFilter](#colorfilter)。如果想重置填充颜色可以传入 [ColorContent](arkts-arkui-colorcontent-c.md)类型。支持通过传入[ColorMetrics](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md)类型设置P3色域颜色值&lt;!- -Del--&gt;，从API version 24开始，支持BT2020色域颜色值<!--DelEnd-->，可在支持高色域的设备上获得更丰富的色彩表现。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时设置该属性不生效。

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| color | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [ColorContent](arkts-arkui-colorcontent-c.md) \| [ColorMetrics](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md) | 是 |

## fitOriginalSize

```TypeScript
fitOriginalSize(value: boolean)
```

设置图片的显示尺寸是否跟随图源尺寸。图片组件已设置width、height属性时，fitOriginalSize属性不生效。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时设置该属性不生效。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## hdrBrightness

```TypeScript
hdrBrightness(brightness: number)
```

设置组件在显示HDR图片时的亮度。SVG类型图源不支持该属性。该属性与[dynamicRangeMode](#dynamicrangemode)属性同时设置时， [dynamicRangeMode](#dynamicrangemode)属性不生效。

**起始版本：** 19

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| brightness | number | 是 |

## imageMatrix

```TypeScript
imageMatrix(matrix: ImageMatrix)
```

设置图片的变换矩阵。通过[ImageMatrix](#imagematrix)对象使用平移、旋转、缩放等函数，实现宫格缩略图的最佳呈现。SVG类型图源不支持该属性。设置[resizable](#resizable)、[objectRepeat](#objectrepeat)属性时，该属性设置不生效。该属性只针对图 源做处理，不会触发Image组件的回调事件。该属性与[objectFit](#objectfit)属性强关联，仅在[objectFit](#objectfit)属性设置为 ImageFit.MATRIX时生效。

**起始版本：** 15

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| matrix | [ImageMatrix](arkts-arkui-imagematrix-t.md) | 是 |

## interpolation

```TypeScript
interpolation(value: ImageInterpolation)
```

定义图片插值效果。用于优化图片缩放时的锯齿问题。SVG类型图源不支持该属性。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时设置该属性不生效。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ImageInterpolation](arkts-arkui-imageinterpolation-e.md) | 是 |

## matchTextDirection

```TypeScript
matchTextDirection(value: boolean)
```

设置图片是否跟随系统语言方向，在RTL语言环境下显示镜像翻转显示效果。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时设置该属性不生效。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |

## objectFit

```TypeScript
objectFit(value: ImageFit)
```

设置图片的填充效果。未通过该接口设置时，默认为ImageFit.Cover，保持宽高比进行缩小或者放大。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ImageFit](../arkts-apis/arkts-arkui-imagefit-e.md) | 是 |

## objectRepeat

```TypeScript
objectRepeat(value: ImageRepeat)
```

设置图片的重复样式，从中心点向两边重复，剩余空间不足放下一张图片时会截断。SVG类型图源不支持该属性。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时设置该属性不生效。设置合法的[resizable](#resizable)时，该属性不生效。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ImageRepeat](../arkts-apis/arkts-arkui-imagerepeat-e.md) | 是 |

## onComplete

```TypeScript
onComplete(
    callback: (event?: {
      /**
       * The width of the image source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @since 7
       */
      /**
       * The width of the image source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @since 9
       * @form
       */
      /**
       * The width of the image source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @crossplatform
       * @since 10
       * @form
       */
      /**
       * The width of the image source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @crossplatform
       * @atomicservice
       * @since 11
       * @form
       */
      width: number;
      /**
       * The height of the image source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @since 7
       */
      /**
       * The height of the image source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @since 9
       * @form
       */
      /**
       * The height of the image source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @crossplatform
       * @since 10
       * @form
       */
      /**
       * The height of the image source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @crossplatform
       * @atomicservice
       * @since 11
       * @form
       */
      height: number;
      /**
       * The width of the component source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @since 7
       */
      /**
       * The width of the component source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @since 9
       * @form
       */
      /**
       * The width of the component source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @crossplatform
       * @since 10
       * @form
       */
      /**
       * The width of the component source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @crossplatform
       * @atomicservice
       * @since 11
       * @form
       */
      componentWidth: number;
      /**
       * The height of the component source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @since 7
       */
      /**
       * The height of the component source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @since 9
       * @form
       */
      /**
       * The height of the component source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @crossplatform
       * @since 10
       * @form
       */
      /**
       * The height of the component source.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @crossplatform
       * @atomicservice
       * @since 11
       * @form
       */
      componentHeight: number;
      /**
       * The value of the status of the image being loaded successfully.
       * If the returned status value is 0, the image data is successfully loaded.
       * If the returned status value is 1, the image is successfully decoded.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @since 7
       */
      /**
       * The value of the status of the image being loaded successfully.
       * If the returned status value is 0, the image data is successfully loaded.
       * If the returned status value is 1, the image is successfully decoded.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @since 9
       * @form
       */
      /**
       * The value of the status of the image being loaded successfully.
       * If the returned status value is 0, the image data is successfully loaded.
       * If the returned status value is 1, the image is successfully decoded.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @crossplatform
       * @since 10
       * @form
       */
      /**
       * The value of the status of the image being loaded successfully.
       * If the returned status value is 0, the image data is successfully loaded.
       * If the returned status value is 1, the image is successfully decoded.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @crossplatform
       * @atomicservice
       * @since 11
       * @form
       */
      loadingStatus: number;
      /**
       * The width of the picture that is actually drawn.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @stagemodelonly
       * @crossplatform
       * @since 10
       * @form
       */
      /**
       * The width of the picture that is actually drawn.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @stagemodelonly
       * @crossplatform
       * @atomicservice
       * @since 11
       * @form
       */
      contentWidth: number;
      /**
       * The height of the picture that is actually drawn.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @stagemodelonly
       * @crossplatform
       * @since 10
       * @form
       */
      /**
       * The height of the picture that is actually drawn.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @stagemodelonly
       * @crossplatform
       * @atomicservice
       * @since 11
       * @form
       */
      contentHeight: number;
      /**
       * The actual draw is offset from the x-axis of the component itself.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @stagemodelonly
       * @crossplatform
       * @since 10
       * @form
       */
      /**
       * The actual draw is offset from the x-axis of the component itself.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @stagemodelonly
       * @crossplatform
       * @atomicservice
       * @since 11
       * @form
       */
      contentOffsetX: number;
      /**
       * The actual draw is offset from the y-axis of the component itself.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @stagemodelonly
       * @crossplatform
       * @since 10
       * @form
       */
      /**
       * The actual draw is offset from the y-axis of the component itself.
       *
       * @type { number }
       * @syscap SystemCapability.ArkUI.ArkUI.Full
       * @stagemodelonly
       * @crossplatform
       * @atomicservice
       * @since 11
       * @form
       */
      contentOffsetY: number;
    }) => void,
  )
```

Triggered when an image is successfully loaded or decoded. The size of the image source that is successfully loaded is returned, in pixels.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: This event is not triggered if the parameter type of the component is AnimatedDrawableDescriptor. </p>

**起始版本：** 11

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | (event?: {       /**        * The width of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 7        */       /**        * The width of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 9        * @form        */       /**        * The width of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @since 10        * @form        */       /**        * The width of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @atomicservice        * @since 11        * @form        */       width: number;       /**        * The height of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 7        */       /**        * The height of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 9        * @form        */       /**        * The height of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @since 10        * @form        */       /**        * The height of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @atomicservice        * @since 11        * @form        */       height: number;       /**        * The width of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 7        */       /**        * The width of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 9        * @form        */       /**        * The width of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @since 10        * @form        */       /**        * The width of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @atomicservice        * @since 11        * @form        */       componentWidth: number;       /**        * The height of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 7        */       /**        * The height of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 9        * @form        */       /**        * The height of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @since 10        * @form        */       /**        * The height of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @atomicservice        * @since 11        * @form        */       componentHeight: number;       /**        * The value of the status of the image being loaded successfully.        * If the returned status value is 0, the image data is successfully loaded.        * If the returned status value is 1, the image is successfully decoded.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 7        */       /**        * The value of the status of the image being loaded successfully.        * If the returned status value is 0, the image data is successfully loaded.        * If the returned status value is 1, the image is successfully decoded.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 9        * @form        */       /**        * The value of the status of the image being loaded successfully.        * If the returned status value is 0, the image data is successfully loaded.        * If the returned status value is 1, the image is successfully decoded.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @since 10        * @form        */       /**        * The value of the status of the image being loaded successfully.        * If the returned status value is 0, the image data is successfully loaded.        * If the returned status value is 1, the image is successfully decoded.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @atomicservice        * @since 11        * @form        */       loadingStatus: number;       /**        * The width of the picture that is actually drawn.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @since 10        * @form        */       /**        * The width of the picture that is actually drawn.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @atomicservice        * @since 11        * @form        */       contentWidth: number;       /**        * The height of the picture that is actually drawn.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @since 10        * @form        */       /**        * The height of the picture that is actually drawn.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @atomicservice        * @since 11        * @form        */       contentHeight: number;       /**        * The actual draw is offset from the x-axis of the component itself.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @since 10        * @form        */       /**        * The actual draw is offset from the x-axis of the component itself.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @atomicservice        * @since 11        * @form        */       contentOffsetX: number;       /**        * The actual draw is offset from the y-axis of the component itself.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @since 10        * @form        */       /**        * The actual draw is offset from the y-axis of the component itself.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @atomicservice        * @since 11        * @form        */       contentOffsetY: number;     }) = & gt; void | 是 |

## onError

```TypeScript
onError(callback: ImageErrorCallback)
```

图片加载异常时触发该回调。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时该事件不触发。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [ImageErrorCallback](arkts-arkui-imageerrorcallback-t.md) | 是 |

## onFinish

```TypeScript
onFinish(event: () => void)
```

当加载的源文件为带动效的SVG格式图片时，SVG动效播放完成时会触发这个回调。如果动效为无限循环动效，则不会触发这个回调。仅支持SVG格式的图片。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时 该事件不触发。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | () = & gt; void | 是 |

## orientation

```TypeScript
orientation(orientation: ImageRotateOrientation) : ImageAttribute
```

设置图像内容的显示方向。该属性对[alt](#alt)占位图不生效。设置合法的[resizable](#resizable)时，该属性不生效。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [orientation](#orientation) | [ImageRotateOrientation](arkts-arkui-imagerotateorientation-e.md) | 是 |

## privacySensitive

```TypeScript
privacySensitive(supported: boolean)
```

设置是否支持卡片敏感隐私信息。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| supported | boolean | 是 |

## renderMode

```TypeScript
renderMode(value: ImageRenderMode)
```

设置图片的渲染模式。SVG类型图源不支持该属性。设置[ColorFilter](#colorfilter)时，该属性设置不生效。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时设置该属性不生效。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ImageRenderMode](arkts-arkui-imagerendermode-e.md) | 是 |

## resizable

```TypeScript
resizable(value: ResizableOptions)
```

设置图像拉伸时可调整大小的图像选项。拉伸对拖拽缩略图以及占位图有效。设置合法的 [ResizableOptions](arkts-arkui-resizableoptions-i.md) 时，objectRepeat属性、antialiased属性和orientation属性设置不生效。当设置 top +bottom 大于原图的高或者 left + right 大于原图的宽时 [ResizableOptions](arkts-arkui-resizableoptions-i.md) 属性设置不生效。当组件的参数类型为动图、[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)和SVG时设置该属性 不生效。

> **说明：**&gt;
> 从API version 20开始，该接口支持在attributeModifier中调用。

**起始版本：** 11

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ResizableOptions](arkts-arkui-resizableoptions-i.md) | 是 |

## sourceSize

```TypeScript
sourceSize(value: ImageSourceSize)
```

设置图片解码尺寸。仅在目标尺寸小于图源尺寸时生效。SVG类型图源和PixelMap资源不支持该属性。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时设置该属性不生效。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | [ImageSourceSize](arkts-arkui-imagesourcesize-i.md) | 是 |

## supportSvg2

```TypeScript
supportSvg2(enable: boolean) : ImageAttribute
```

开启或关闭SVG标签解析能力增强功能，开启后相关SVG图片显示效果会有变化。Image组件创建后，不支持动态修改该属性的值。

**起始版本：** 21

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本21开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本21开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

## syncLoad

```TypeScript
syncLoad(value: boolean)
```

设置是否同步加载图片。建议加载尺寸较小的本地图片时将syncLoad设为true，因为耗时较短，在主线程上执行即可。不建议对网络图片使用同步加载，应使用异步加载，或将网络下载与Image的显示剥离，避免阻塞UI线程导致 AppFreeze。当组件的参数类型为[AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md)时设置该属性不生效。如果加载图片时出现闪烁，设置syncLoad为true。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | boolean | 是 |
