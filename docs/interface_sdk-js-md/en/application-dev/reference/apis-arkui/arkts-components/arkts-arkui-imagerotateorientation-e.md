# ImageRotateOrientation

Describes the desired display orientation for image content.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

<!--Device-unnamed-declare enum ImageRotateOrientation--><!--Device-unnamed-declare enum ImageRotateOrientation-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AUTO

```TypeScript
AUTO = 0
```

Use EXIF metadata for display orientation, with support for rotation and mirroring.

Images of the [PixelMap]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ and  
[DrawableDescriptor]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ types do not contain header information. When this API is called,the image display effect remains unchanged.

!\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-AUTO = 0--><!--Device-ImageRotateOrientation-AUTO = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## UP

```TypeScript
UP = 1
```

Display original pixel data without transformation.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-UP = 1--><!--Device-ImageRotateOrientation-UP = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RIGHT

```TypeScript
RIGHT = 2
```

Display the image after rotating it 90 degrees clockwise.

!\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-RIGHT = 2--><!--Device-ImageRotateOrientation-RIGHT = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DOWN

```TypeScript
DOWN = 3
```

Display the image after rotating it 180 degrees clockwise.

!\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-DOWN = 3--><!--Device-ImageRotateOrientation-DOWN = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LEFT

```TypeScript
LEFT = 4
```

Display the image after rotating it 270 degrees clockwise.

!\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-LEFT = 4--><!--Device-ImageRotateOrientation-LEFT = 4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## UP_MIRRORED

```TypeScript
UP_MIRRORED = 5
```

Display the image after flipping it horizontally.

!\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-UP_MIRRORED = 5--><!--Device-ImageRotateOrientation-UP_MIRRORED = 5-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RIGHT_MIRRORED

```TypeScript
RIGHT_MIRRORED = 6
```

Display the image after flipping it horizontally and then rotating it 90 degrees clockwise.

!\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-RIGHT_MIRRORED = 6--><!--Device-ImageRotateOrientation-RIGHT_MIRRORED = 6-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DOWN_MIRRORED

```TypeScript
DOWN_MIRRORED = 7
```

Display the image after flipping it vertically.

!\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-DOWN_MIRRORED = 7--><!--Device-ImageRotateOrientation-DOWN_MIRRORED = 7-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LEFT_MIRRORED

```TypeScript
LEFT_MIRRORED = 8
```

Display the image after flipping it horizontally and then rotating it 270 degrees clockwise.

!\_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

<!--Device-ImageRotateOrientation-LEFT_MIRRORED = 8--><!--Device-ImageRotateOrientation-LEFT_MIRRORED = 8-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

