# ImageAttachmentInterface

Defines the ImageAttachmentInterface.

**Since:** 12

<!--Device-unnamed-declare interface ImageAttachmentInterface--><!--Device-unnamed-declare interface ImageAttachmentInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## colorFilter

```TypeScript
colorFilter?: ColorFilterType
```

Image color filter of the styled string.

**Type:** ColorFilterType

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-ImageAttachmentInterface-colorFilter?: ColorFilterType--><!--Device-ImageAttachmentInterface-colorFilter?: ColorFilterType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## layoutStyle

```TypeScript
layoutStyle?: ImageAttachmentLayoutStyle
```

Image layout.

**Type:** ImageAttachmentLayoutStyle

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageAttachmentInterface-layoutStyle?: ImageAttachmentLayoutStyle--><!--Device-ImageAttachmentInterface-layoutStyle?: ImageAttachmentLayoutStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## objectFit

```TypeScript
objectFit?: ImageFit
```

Image scaling type. The **ImageFit.MATRIX** enum value is not supported.

Default value: **ImageFit.Cover**

**Type:** ImageFit

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageAttachmentInterface-objectFit?: ImageFit--><!--Device-ImageAttachmentInterface-objectFit?: ImageFit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## size

```TypeScript
size?: SizeOptions
```

Image size, which does not support percentage values.

The default value of **size** depends on the value of **objectFit**. For example, if the value of **objectFit** is **Cover**, the image height is the component height minus the top and bottom paddings, and the image width is the component width minus the left and right paddings.

**Type:** SizeOptions

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageAttachmentInterface-size?: SizeOptions--><!--Device-ImageAttachmentInterface-size?: SizeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## value

```TypeScript
value: PixelMap
```

Image data source.

**Type:** PixelMap

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageAttachmentInterface-value: PixelMap--><!--Device-ImageAttachmentInterface-value: PixelMap-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## verticalAlign

```TypeScript
verticalAlign?: ImageSpanAlignment
```

Alignment mode of the image with the text.

Default value: **ImageSpanAlignment.BOTTOM**

**Type:** ImageSpanAlignment

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageAttachmentInterface-verticalAlign?: ImageSpanAlignment--><!--Device-ImageAttachmentInterface-verticalAlign?: ImageSpanAlignment-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

