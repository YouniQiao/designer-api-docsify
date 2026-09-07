# ImageRotateOrientation

Describes the desired display orientation for image content.

**Since:** 14

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## AUTO

```TypeScript
AUTO = 0
```

Use EXIF metadata for display orientation, with support for rotation and mirroring.

Images of the [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) and [DrawableDescriptor](arkts-arkui-drawabledescriptor-t.md) types do not contain header information. When this API is called, the image display effect remains unchanged.



**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## UP

```TypeScript
UP = 1
```

Display original pixel data without transformation.

**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RIGHT

```TypeScript
RIGHT = 2
```

Display the image after rotating it 90 degrees clockwise.



**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DOWN

```TypeScript
DOWN = 3
```

Display the image after rotating it 180 degrees clockwise.



**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LEFT

```TypeScript
LEFT = 4
```

Display the image after rotating it 270 degrees clockwise.



**Since:** 14

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 14.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## UP_MIRRORED

```TypeScript
UP_MIRRORED = 5
```

Display the image after flipping it horizontally.



**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## RIGHT_MIRRORED

```TypeScript
RIGHT_MIRRORED = 6
```

Display the image after flipping it horizontally and then rotating it 90 degrees clockwise.



**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DOWN_MIRRORED

```TypeScript
DOWN_MIRRORED = 7
```

Display the image after flipping it vertically.



**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## LEFT_MIRRORED

```TypeScript
LEFT_MIRRORED = 8
```

Display the image after flipping it horizontally and then rotating it 270 degrees clockwise.



**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

**Widget capability:** This API can be used in ArkTS widgets since API version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
