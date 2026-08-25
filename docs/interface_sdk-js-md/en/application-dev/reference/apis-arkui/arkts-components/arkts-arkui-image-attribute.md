# Image properties/events

The **Image** component is usually used to display images in applications. It supports data sources of the following types: [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md), [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md), and [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md). Supported image formats include PNG, JPG, JPEG, BMP, SVG, WEBP, GIF, HEIF, and TIFF. Note that the APNG and SVGA formats are not supported.

> **NOTE：**

> - This component supports the TIFF image format since API version 23.&gt;
> - When keyboard shortcuts are used to copy an **Image** component, the **Image** component must be in a focused
> state. For instructions on how to set focus, see
> [Setting Whether a Component Is Focusable](../../../ui/arkts-common-events-focus-event.md#setting-whether-a- component-is-focusable).
> By default, the **Image** component is not focusable. To enable it to gain focus, set both the
> focusable and [focusOnTouch](arkts-arkui-commonmethod-c.md#focusontouch) attributes to
> **true**.&gt;
> - The **Image** component supports SVG image sources. For details about SVG tags, see SVG Tags.&gt;
> - For animated images, animation playback is disabled by default and depends on the visibility of the **Image**
> component. When the component is visible, the animation is started through the callback. When the component is
> invisible, the animation is stopped. The visibility status of the **Image** component can be identified through the&gt;
> [onVisibleAreaChange]
> [onVisibleAreaChange](arkts-arkui-commonmethod-c.md#onvisibleareachange)
> event. If the value of **ratios** is greater than 0, the component is visible.&gt;
> - For details about how to resolve white block issues during image loading, see
> [Solution to White Image Blocks]
> (https://developer.huawei.com/consumer/en/doc/best-practices/bpta-image-white-lump-solution).
> For details about how to address slow image loading, see
> [Optimizing Preset Image Loading](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-texture-&gt; compression-improve-performance#section91526132216).&gt;

**Inheritance/Implementation:** ImageAttribute extends CommonMethod<ImageAttribute>

**Since:** 7

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## alt

```TypeScript
alt(value: string | Resource | PixelMap)
```

Sets the placeholder image displayed during image loading.The placeholder image supports configuration of [objectFit](#objectfit) for setting the fill effect, which is consistent with the fill effect of the image.This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| Resource \| [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | Yes |

## alt

```TypeScript
alt(src: ResourceStr | PixelMap | ImageAlt)
```

Sets the placeholder image displayed during image loading and when image loading fails.

> **NOTE：**&gt;
> When a placeholder image is configured via [ImageAlt](arkts-arkui-imagealt-i.md), **Image** takes effect based on the
> placeholder image sources configured for the loading and load-failure states. If no placeholder image is
> configured, it is not displayed by default.
The placeholder image supports configuration of [objectFit](#objectfit) for setting the fill effect, which is consistent with the fill effect of the image.This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 22

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

**Widget capability:** This API can be used in ArkTS widgets since API version 22.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md) \| PixelMap \| [ImageAlt](arkts-arkui-imagealt-i.md) | Yes |

## antialiased

```TypeScript
antialiased(isAntialiased: Optional<boolean>)
```

Sets whether to enable anti-aliasing for the edges of a pixel map image. If the attribute is not set, anti-aliasing is disabled by default. This attribute is not applicable to SVG images.

> **NOTE：**&gt;
> If the backgroundColor attribute is set for an image,
> setting the **antialiased** attribute of the image to **true** does not affect the aliasing effect of the
> background color.&gt;
> This attribute does not take effect when used together with [resizable](#resizable).

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isAntialiased | [Optional](arkts-arkui-optional-t.md)&lt;boolean&gt; | Yes |

## autoResize

```TypeScript
autoResize(value: boolean)
```

Specifies whether to resize the image source based on the size of the display area during image decoding. As downsampling images results in some loss of information, it may reduce the image quality, causing issues such as aliasing. To retain the original image quality, set **autoResize** to **false**, but this may increase the memory usage.If the original image size does not match the display size, the image may be distorted or blurred. Recommended configuration for the optimal definition:When the image is scaled down: .autoResize(false) + .interpolation(.Medium)When the image is scaled up: .interpolation(.High)This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md) or the image format is SVG.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## colorFilter

```TypeScript
colorFilter(value: ColorFilter | DrawingColorFilter)
```

Sets the color filter for the image.When this attribute is set, [renderMode](#rendermode) is not effective.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | ColorFilter \| [DrawingColorFilter](arkts-arkui-drawingcolorfilter-t.md) | Yes |

## colorFilter

```TypeScript
colorFilter(value: ColorFilter | DrawingColorFilter | ResourceColor)
```

Sets the color filter for the image.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: When this attribute is set, renderMode is not effective. When value is ResourceColor type, it will be converted to ColorFilter with blend mode. </p>

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**Widget capability:** This API can be used in ArkTS widgets since API version 26.0.0.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | ColorFilter \| [DrawingColorFilter](arkts-arkui-drawingcolorfilter-t.md) \| [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## contentTransition

```TypeScript
contentTransition(transition: ContentTransitionEffect)
```

Triggers transition animations when the image content changes.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| transition | [ContentTransitionEffect](arkts-arkui-contenttransitioneffect-c.md) | Yes |

## copyOption

```TypeScript
copyOption(value: CopyOptions)
```

Specifies whether the image can be copied. When **copyOption** is set to a value other than **CopyOptions.None**, the image can be copied through multiple interactions, such as number press, right-click, or Ctrl+C. SVG images cannot be copied.This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CopyOptions](../arkts-apis/arkts-arkui-copyoptions-e.md) | Yes |

## draggable

```TypeScript
draggable(value: boolean)
```

Specifies whether the image is draggable.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## dynamicRangeMode

```TypeScript
dynamicRangeMode(value: DynamicRangeMode)
```

Sets the dynamic range of the image to be displayed. This attribute is not applicable to SVG images.  
**Device behavior difference**: This API takes effect on mobile phones, PCs, 2-in-1 devices, and tablets, but not on other device types.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [DynamicRangeMode](arkts-arkui-dynamicrangemode-e.md) | Yes |

## enableAnalyzer

```TypeScript
enableAnalyzer(enable: boolean)
```

Sets whether to enable the AI image analyzer, which supports subject recognition, text recognition, and object lookup.This attribute cannot be used together with the [overlay](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-overlay.md#overlay) attribute. If they are set at the same time, the [CustomBuilder](../../../reference/apis-arkui/arkui-ts/ts-types.md#custombuilder8) attribute in **overlay** has no effect. This feature also depends on device capabilities.Images to be analyzed must be static, non-vector images. That is, SVG and GIF images cannot be analyzed. [Pixel maps](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) in [RGBA_8888](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmapformat-e.md) format can be passed in for analysis. For details, see [Example 5: Enabling the AI Image Analyzer] (../../../reference/apis-arkui/arkui-ts/ts-basic-components-image.md#example-5-enabling-the-ai-image-analyzer).The [alt](#alt) placeholder image does not support analysis. The [objectRepeat](#objectrepeat) attribute supports analysis only when it is set to **ImageRepeat.NoRepeat**. Analysis is not supported when the [obscured](arkts-arkui-commonmethod-c.md#obscured) attribute is enabled.Analysis is performed based on the complete original image. Even if the settings of the clip, margin, borderRadius, position, and [objectFit](#objectfit) attributes cause incomplete image display, or if a mask layer is set via [renderMode](#rendermode), analysis will still be conducted on the complete original image. The [copyOption](#copyoption) attribute does not affect the AI image analyzer functionality.This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

> **NOTE：**&gt;
> - The **ohos.permission.INTERNET** permission is required.&gt;
> - This API can be called within attributeModifier since API version 12.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## fillColor

```TypeScript
fillColor(value: ResourceColor)
```

Fill color to be superimposed on the image. This attribute applies only to SVG images. Once set, the fill color will replace the fill colors of all drawable elements within the SVG image. To set the fill color for a PNG image, use [colorFilter](#colorfilter).This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes |

## fillColor

```TypeScript
fillColor(color: ResourceColor | ColorContent)
```

Fill color to be superimposed on the image. This attribute applies only to SVG images. Once set, the fill color will replace the fill colors of all drawable elements within the SVG image. To set the fill color for a PNG image, use [colorFilter](#colorfilter). To reset the fill color, pass a value of the [ColorContent](arkts-arkui-colorcontent-c.md) type.This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [ColorContent](arkts-arkui-colorcontent-c.md) | Yes |

## fillColor

```TypeScript
fillColor(color: ResourceColor | ColorContent | ColorMetrics)
```

Fill color to be superimposed on the image. This attribute applies only to SVG images. Once set, the fill color will replace the fill colors of all drawable elements within the SVG image. To set the fill color for a PNG image, use [colorFilter](#colorfilter). To reset the fill color, pass a value of the [ColorContent](arkts-arkui-colorcontent-c.md) type. You can set P3 color gamut values by passing in the [ColorMetrics](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md) type, which can achieve richer color performance on devices that support high color gamut.This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) \| [ColorContent](arkts-arkui-colorcontent-c.md) \| [ColorMetrics](../arkts-apis/arkts-arkui-graphics-colormetrics-c.md) | Yes |

## fitOriginalSize

```TypeScript
fitOriginalSize(value: boolean)
```

Specifies whether the image display size follows the size of the image source.This attribute does not take effect when the component has the **width** and **height** attributes set.This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## hdrBrightness

```TypeScript
hdrBrightness(brightness: number)
```

Sets the brightness of HDR images displayed by the component.This attribute is not applicable to SVG images.If this attribute and the [dynamicRangeMode](#dynamicrangemode) attribute are both set, [dynamicRangeMode](#dynamicrangemode) does not take effect.

**Since:** 19

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| brightness | number | Yes |

## imageMatrix

```TypeScript
imageMatrix(matrix: ImageMatrix)
```

Sets the transformation matrix of the image. This API allows you to use the functions provided by the [ImageMatrix](#imagematrix) object, such as translate, rotate, and scale, to achieve the optimal display of grid thumbnails. This attribute is not applicable to SVG images.This attribute does not take effect when [resizable](#resizable) and [objectRepeat](#objectrepeat) are set. This attribute only processes the image source and does not trigger any callback events of the **Image** component.This attribute is strongly associated with [objectFit](#objectfit) and takes effect only when [objectFit](#objectfit) is set to **ImageFit.MATRIX**.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [matrix](../arkts-apis/arkts-arkui-viewmodel-transformobject-i.md) | [ImageMatrix](arkts-arkui-imagematrix-t.md) | Yes |

## interpolation

```TypeScript
interpolation(value: ImageInterpolation)
```

Defines the image interpolation effect. This attribute mitigates aliasing during image scaling. This attribute is not applicable to SVG images.This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ImageInterpolation](arkts-arkui-imageinterpolation-e.md) | Yes |

## matchTextDirection

```TypeScript
matchTextDirection(value: boolean)
```

Specifies whether the image follows the system language direction, displaying a mirrored effect in a right-to-left (RTL) language environments.This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |

## objectFit

```TypeScript
objectFit(value: ImageFit)
```

Sets how the image is resized to fit its container. If the attribute is not set, the default value is **ImageFit.Cover**, which scales the image up or down while maintaining its aspect ratio.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ImageFit](../arkts-apis/arkts-arkui-imagefit-e.md) | Yes |

## objectRepeat

```TypeScript
objectRepeat(value: ImageRepeat)
```

Sets how the image is repeated. When set to repeat, the image is repeated from the center to edges. The last image will be clipped if it does not fit in the component. This attribute is not applicable to SVG images.This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ImageRepeat](../arkts-apis/arkts-arkui-imagerepeat-e.md) | Yes |

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

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | (event?: {       /**        * The width of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 7        */       /**        * The width of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 9        * @form        */       /**        * The width of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @since 10        * @form        */       /**        * The width of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @atomicservice        * @since 11        * @form        */       width: number;       /**        * The height of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 7        */       /**        * The height of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 9        * @form        */       /**        * The height of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @since 10        * @form        */       /**        * The height of the image source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @atomicservice        * @since 11        * @form        */       height: number;       /**        * The width of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 7        */       /**        * The width of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 9        * @form        */       /**        * The width of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @since 10        * @form        */       /**        * The width of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @atomicservice        * @since 11        * @form        */       componentWidth: number;       /**        * The height of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 7        */       /**        * The height of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 9        * @form        */       /**        * The height of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @since 10        * @form        */       /**        * The height of the component source.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @atomicservice        * @since 11        * @form        */       componentHeight: number;       /**        * The value of the status of the image being loaded successfully.        * If the returned status value is 0, the image data is successfully loaded.        * If the returned status value is 1, the image is successfully decoded.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 7        */       /**        * The value of the status of the image being loaded successfully.        * If the returned status value is 0, the image data is successfully loaded.        * If the returned status value is 1, the image is successfully decoded.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @since 9        * @form        */       /**        * The value of the status of the image being loaded successfully.        * If the returned status value is 0, the image data is successfully loaded.        * If the returned status value is 1, the image is successfully decoded.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @since 10        * @form        */       /**        * The value of the status of the image being loaded successfully.        * If the returned status value is 0, the image data is successfully loaded.        * If the returned status value is 1, the image is successfully decoded.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @crossplatform        * @atomicservice        * @since 11        * @form        */       loadingStatus: number;       /**        * The width of the picture that is actually drawn.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @since 10        * @form        */       /**        * The width of the picture that is actually drawn.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @atomicservice        * @since 11        * @form        */       contentWidth: number;       /**        * The height of the picture that is actually drawn.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @since 10        * @form        */       /**        * The height of the picture that is actually drawn.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @atomicservice        * @since 11        * @form        */       contentHeight: number;       /**        * The actual draw is offset from the x-axis of the component itself.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @since 10        * @form        */       /**        * The actual draw is offset from the x-axis of the component itself.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @atomicservice        * @since 11        * @form        */       contentOffsetX: number;       /**        * The actual draw is offset from the y-axis of the component itself.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @since 10        * @form        */       /**        * The actual draw is offset from the y-axis of the component itself.        *        * @type { number }        * @syscap SystemCapability.ArkUI.ArkUI.Full        * @stagemodelonly        * @crossplatform        * @atomicservice        * @since 11        * @form        */       contentOffsetY: number;     }) = & gt; void | Yes |

## onError

```TypeScript
onError(callback: ImageErrorCallback)
```

Triggered when an error occurs during image loading.This event is not triggered if the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ImageErrorCallback](arkts-arkui-imageerrorcallback-t.md) | Yes |

## onFinish

```TypeScript
onFinish(event: () => void)
```

Triggered when the animation playback in the loaded SVG image is complete. If the animation is an infinite loop, this callback is not triggered.Only images in SVG format are supported. This event is not triggered if the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | () = & gt; void | Yes |

## orientation

```TypeScript
orientation(orientation: ImageRotateOrientation) : ImageAttribute
```

Sets the display orientation of the image content.This attribute does not apply to placeholder images specified by [alt](#alt).

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [orientation](#orientation) | [ImageRotateOrientation](arkts-arkui-imagerotateorientation-e.md) | Yes |

## privacySensitive

```TypeScript
privacySensitive(supported: boolean)
```

Sets whether to secure sensitive information on widgets.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| supported | boolean | Yes |

## renderMode

```TypeScript
renderMode(value: ImageRenderMode)
```

Sets the rendering mode of the image. This attribute is not applicable to SVG images.This attribute does not take effect when [ColorFilter](#colorfilter) is set.This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ImageRenderMode](arkts-arkui-imagerendermode-e.md) | Yes |

## resizable

```TypeScript
resizable(value: ResizableOptions)
```

Sets the resizable image options. Resizing is effective for drag previews and placeholder images.When a valid [ResizableOptions](arkts-arkui-resizableoptions-i.md) is set, the **objectRepeat**, **antialiased**, and **orientation** attributes do not take effect.When the sum of the values of **top** and **bottom** is greater than the source image height, or the sum of the values of **left** and **right** is greater than the source image width, the [ResizableOptions](arkts-arkui-resizableoptions-i.md) attribute does not take effect.This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md) or the image format is SVG.

> **NOTE：**&gt;
> This API can be called in attributeModifier since API version 20.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResizableOptions](arkts-arkui-resizableoptions-i.md) | Yes |

## sourceSize

```TypeScript
sourceSize(value: ImageSourceSize)
```

Sets the decoding size of the image. This attribute works only when the target size is smaller than the source size. This attribute is not applicable to SVG images or **PixelMap** objects.This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ImageSourceSize](arkts-arkui-imagesourcesize-i.md) | Yes |

## supportSvg2

```TypeScript
supportSvg2(enable: boolean) : ImageAttribute
```

Sets whether to enable [enhanced SVG tag parsing](../../../reference/apis-arkui/arkui-ts/ts-image-svg2-capabilities.md). When this feature is enabled, SVG image rendering behavior changes accordingly.After the **Image** component is created, the value of this attribute cannot be dynamically changed.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**Widget capability:** This API can be used in ArkTS widgets since API version 21.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

## syncLoad

```TypeScript
syncLoad(value: boolean)
```

Specifies whether to load the image synchronously. When loading a small local image, you are advised to set **syncLoad** to **true** so that the image loading can be quickly completed on the main thread.This attribute does not take effect when the parameter type of the component is [AnimatedDrawableDescriptor](../arkts-apis/arkts-arkui-arkui-drawabledescriptor-animateddrawabledescriptor-c.md).If image flickering occurs during loading, set **syncLoad** to **true**. For details, see [Optimizing Concurrent Tasks] (https://developer.huawei.com/consumer/en/doc/best-practices/bpta-click-to-click-response- optimization#section715115119192).

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean | Yes |
