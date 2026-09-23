# ImageLoadResult

```TypeScript
declare interface ImageLoadResult
```

Describes the object returned after the callback is triggered when an image is successfully loaded or decoded.

**Since:** 12

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## componentHeight

```TypeScript
componentHeight: number
```

Height of the component.

Unit: [px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#basic-pixel-units)

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## componentWidth

```TypeScript
componentWidth: number
```

Width of the component.

Unit: [px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#basic-pixel-units)

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentHeight

```TypeScript
contentHeight: number
```

Height of the image actually drawn.

Unit: [px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#basic-pixel-units)

**NOTE:** 

Valid only when loadingStatus returns 1.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentOffsetX

```TypeScript
contentOffsetX: number
```

X-axis offset of the actually drawn content relative to the component itself.

Unit: [px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#basic-pixel-units)

**NOTE:** 

Valid only when loadingStatus returns 1.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentOffsetY

```TypeScript
contentOffsetY: number
```

Y-axis offset of the actually drawn content relative to the component itself.

Unit: [px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#basic-pixel-units)

**NOTE:** 

Valid only when loadingStatus returns 1.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentWidth

```TypeScript
contentWidth: number
```

Width of the image actually drawn.

Unit: [px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#basic-pixel-units)

**NOTE:** 

Valid only when loadingStatus returns 1.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height: number
```

Height of the image.

Unit: [px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#basic-pixel-units)

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## loadingStatus

```TypeScript
loadingStatus: number
```

Status value of image loading success.

**NOTE:** 

When the returned status value is 0, it indicates image data load success. When the returned status value is 1, it indicates image decoding success.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width: number
```

Width of the image.

Unit: [px](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#basic-pixel-units)

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
