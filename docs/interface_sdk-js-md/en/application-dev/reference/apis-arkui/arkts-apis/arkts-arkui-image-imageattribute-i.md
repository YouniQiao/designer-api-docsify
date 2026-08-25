# ImageAttribute

Defines the Image component attributes.@extends CommonMethod @interface ImageAttribute

**Inheritance/Implementation:** ImageAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## alt

```TypeScript
default alt(value: string | Resource | PixelMap | ImageAlt | undefined): this
```

Sets the placeholder image displayed during loading.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute does not take effect when the parameter type of the component is AnimatedDrawableDescriptor. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ImageAlt](arkts-arkui-image-imagealt-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## antialiased

```TypeScript
default antialiased(isAntialiased: boolean | undefined): this
```

Anti-aliasing of image edges.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| isAntialiased | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ImageAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ImageAttribute](arkts-arkui-image-imageattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## autoResize

```TypeScript
default autoResize(value: boolean | undefined): this
```

Specifies whether to resize the image source based on the size of the display area during image decoding.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute does not take effect when the parameter type of the component is AnimatedDrawableDescriptor or SVG. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## colorFilter

```TypeScript
default colorFilter(value: ColorFilter | DrawingColorFilter | ResourceColor | undefined): this
```

Sets the color filter for the image.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>When this attribute is set, renderMode is not effective. </p>

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ColorFilter](arkts-arkui-colorfilter-c.md) \| [DrawingColorFilter](arkts-arkui-drawingcolorfilter-t.md) \| [ResourceColor](arkts-arkui-resourcecolor-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## contentTransition

```TypeScript
default contentTransition(transition: ContentTransitionEffect | undefined): this
```

Animation effect when the image content changes.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| transition | [ContentTransitionEffect](../arkts-components/arkts-arkui-contenttransitioneffect-c.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## copyOption

```TypeScript
default copyOption(value: CopyOptions | undefined): this
```

Whether the image can be copied.&lt;strong&gt;NOTE&lt;/strong&gt;: <br>SVG images cannot be copied. <br>This attribute does not take effect when the parameter type of the component is AnimatedDrawableDescriptor. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [CopyOptions](arkts-arkui-copyoptions-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## draggable

```TypeScript
default draggable(value: boolean | undefined): this
```

Specifies whether the image is draggable.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute cannot be used together with the onDragStart event. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## dynamicRangeMode

```TypeScript
default dynamicRangeMode(value: DynamicRangeMode | undefined): this
```

Sets the dynamic range of the image to be displayed.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute is not applicable to SVG images. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [DynamicRangeMode](arkts-arkui-image-dynamicrangemode-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## enableAnalyzer

```TypeScript
default enableAnalyzer(enable: boolean | undefined): this
```

Sets whether to enable the AI analyzer<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute cannot be used together with the overlay attribute. If they are set at the same time, the CustomBuilder attribute in overlay has no effect. This attribute depends on device capabilities. <br>Images to be analyzed must be static, non-vector images. That is, SVG and GIF images cannot be analyzed. Pixel maps in RGBA_8888 format can be passed in for analysis. <br>The placeholder images (specified by alt) cannot be analyzed. An image can be analyzed only when objectRepeat is set to ImageRepeat.NoRepeat and obscured is disabled. <br>Analysis is performed based on the complete original image. If the clip, margin, borderRadius, position, or objectFit attribute is set, the image is not displayed completely. If renderMode is used to apply a mask, analysis is still performed based on the complete original image. The copyOption attribute does not affect the AI analyzer. <br>This attribute does not take effect when the parameter type of the component is AnimatedDrawableDescriptor. <br>The ohos.permission.INTERNET permission must be declared. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## fillColor

```TypeScript
default fillColor(color: ResourceColor | ColorContent | ColorMetrics | undefined): this
```

Sets the fill color to be superimposed on the image. By default, no fill color is applied. If an invalid value is passed, the system uses the default theme color: black in light mode and white in dark mode.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute applies only to SVG images. <br>This attribute does not take effect when the parameter type of the component is AnimatedDrawableDescriptor. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| color | [ResourceColor](arkts-arkui-resourcecolor-t.md) \| [ColorContent](arkts-arkui-image-colorcontent-c.md) \| [ColorMetrics](arkts-arkui-colormetrics-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## fitOriginalSize

```TypeScript
default fitOriginalSize(value: boolean | undefined): this
```

Sets whether the display size of the image follows the source size.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute does not take effect when the parameter type of the component is AnimatedDrawableDescriptor. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## hdrBrightness

```TypeScript
default hdrBrightness(brightness: double | undefined): this
```

Set hdrBrightness for Image.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| brightness | double \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## imageMatrix

```TypeScript
default imageMatrix(matrix: ImageMatrix | undefined): this
```

Sets the transformation matrix of the image.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [matrix](arkts-arkui-viewmodel-transformobject-i.md) | [ImageMatrix](arkts-arkui-imagematrix-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## interpolation

```TypeScript
default interpolation(value: ImageInterpolation | undefined): this
```

Sets the interpolation effect of the image, which can alleviate aliasing that occurs when the image is zoomed.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute is not applicable to SVG images. <br>This attribute does not take effect when the parameter type of the component is AnimatedDrawableDescriptor. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ImageInterpolation](arkts-arkui-image-imageinterpolation-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## matchTextDirection

```TypeScript
default matchTextDirection(value: boolean | undefined): this
```

Specifies whether to display the image in the system language direction.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute does not take effect when the parameter type of the component is AnimatedDrawableDescriptor. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## objectFit

```TypeScript
default objectFit(value: ImageFit | undefined): this
```

Sets how the image is resized to fit its container.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ImageFit](arkts-arkui-imagefit-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## objectRepeat

```TypeScript
default objectRepeat(value: ImageRepeat | undefined): this
```

Set the repeat style of the picture<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute is not applicable to SVG images. <br>This attribute does not take effect when the parameter type of the component is AnimatedDrawableDescriptor. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ImageRepeat](arkts-arkui-imagerepeat-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## onComplete

```TypeScript
default onComplete(callback: ImageOnCompleteCallback | undefined): this
```

This callback is triggered when an image is successfully loaded. The size of the image source that is successfully loaded is returned, in pixels.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ImageOnCompleteCallback](arkts-arkui-imageoncompletecallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## onError

```TypeScript
default onError(callback: ImageErrorCallback | undefined): this
```

Triggered when an error occurs during image loading. The field of "message" carries the detailed information of failed image loading.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This event is not triggered if the parameter type of the component is AnimatedDrawableDescriptor. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ImageErrorCallback](arkts-arkui-imageerrorcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## onFinish

```TypeScript
default onFinish(event: VoidCallback | undefined): this
```

When the loaded source file is a svg image, this callback is triggered when the playback of the svg image is complete. If the svg image is a wireless loop image, this callback is not triggered.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Only SVG images are supported. <br>This event is not triggered if the parameter type of the component is AnimatedDrawableDescriptor. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## orientation

```TypeScript
default orientation(orientation: ImageRotateOrientation | undefined): this
```

Sets the display orientation of the image content.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [orientation](#orientation) | [ImageRotateOrientation](arkts-arkui-image-imagerotateorientation-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## privacySensitive

```TypeScript
default privacySensitive(supported: boolean | undefined): this
```

Set the quality enhancement level of image.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| supported | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## renderMode

```TypeScript
default renderMode(value: ImageRenderMode | undefined): this
```

Sets the rendering mode of the image.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute is not applicable to SVG images. <br>When ColorFilter is set, this attribute is not effective. <br>This attribute does not take effect when the parameter type of the component is AnimatedDrawableDescriptor. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ImageRenderMode](arkts-arkui-image-imagerendermode-e.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## resizable

```TypeScript
default resizable(value: ResizableOptions | undefined): this
```

Sets the resizable image options.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>Resizing is effective for drag previews and placeholder images. <br>When ResizableOptions is set to a valid value, the objectRepeat attribute does not take effect. <br>When the sum of the values of top and bottom is greater than the source image height, or the sum of the values of left and right is greater than the source image width, the ResizableOptions attribute does not take effect. <br>This attribute does not take effect when the parameter type of the component is AnimatedDrawableDescriptor or SVG. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ResizableOptions](arkts-arkui-image-resizableoptions-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## setImageOptions

```TypeScript
default setImageOptions(
        src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined, 
        imageAIOptions?: ImageAIOptions
    ): this
```

Sets the placeholder image displayed during loading.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-arkui-image-imagecontent-e.md) \| undefined | Yes |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imagecommon-imageaioptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
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

Sets the placeholder image displayed during loading.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-arkui-image-imagecontent-e.md) \| undefined | Yes |
| imageAIOptions | [ImageAIOptions](arkts-arkui-imagecommon-imageaioptions-i.md) | No |
| reloadKey | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## setImageOptions

```TypeScript
default setImageOptions(
        src: PixelMap | ResourceStr | DrawableDescriptor | ImageContent | undefined, 
        reloadKey?: string
    ): this
```

Sets the placeholder image displayed during loading.

**Since:** 26.1.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| src | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) \| [ResourceStr](arkts-arkui-resourcestr-t.md) \| [DrawableDescriptor](arkts-arkui-arkui-drawabledescriptor-drawabledescriptor-c.md) \| [ImageContent](arkts-arkui-image-imagecontent-e.md) \| undefined | Yes |
| reloadKey | string | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## sourceSize

```TypeScript
default sourceSize(value: ImageSourceSize | undefined): this
```

Sets the decoding size of the image. The original picture is decoded into a picture of a specified size. The unit of the number type is px. Anonymous Object Rectification.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute works only when the target size is smaller than the source size. <br>This attribute is not applicable to SVG images or PixelMap objects. <br>This attribute does not take effect when the parameter type of the component is AnimatedDrawableDescriptor. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [ImageSourceSize](arkts-arkui-image-imagesourcesize-i.md) \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## supportSvg2

```TypeScript
default supportSvg2(enable: boolean | undefined): this
```

Set the range of SVG parsing capabilities supported through enable switch.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |

## syncLoad

```TypeScript
default syncLoad(value: boolean | undefined): this
```

Specifies whether to load the image synchronously.<p>&lt;strong&gt;NOTE&lt;/strong&gt;: <br>This attribute does not take effect when the parameter type of the component is AnimatedDrawableDescriptor. </p>

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | boolean \| undefined | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ImageAttribute](arkts-arkui-image-imageattribute-i.md) |
