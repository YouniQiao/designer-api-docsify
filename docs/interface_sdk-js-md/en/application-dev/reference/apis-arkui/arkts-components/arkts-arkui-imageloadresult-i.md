# ImageLoadResult

Describes the object returned after the callback is triggered when an image is successfully loaded or decoded.

**Since:** 12

<!--Device-unnamed-declare interface ImageLoadResult--><!--Device-unnamed-declare interface ImageLoadResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## componentHeight

```TypeScript
componentHeight: number
```

Height of the component.

Unit: [px](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md)

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageLoadResult-componentHeight: number--><!--Device-ImageLoadResult-componentHeight: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## componentWidth

```TypeScript
componentWidth: number
```

Width of the component.

Unit: [px](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md)

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageLoadResult-componentWidth: number--><!--Device-ImageLoadResult-componentWidth: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentHeight

```TypeScript
contentHeight: number
```

Actual rendered height of the image.

Unit: [px](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md)

**NOTE**

This parameter is valid only when the return value of **loadingStatus** is **1**.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageLoadResult-contentHeight: number--><!--Device-ImageLoadResult-contentHeight: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentOffsetX

```TypeScript
contentOffsetX: number
```

Offset of the rendered content relative to the component on the x-axis.

Unit: [px](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md)

**NOTE**

This parameter is valid only when the return value of **loadingStatus** is **1**.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageLoadResult-contentOffsetX: number--><!--Device-ImageLoadResult-contentOffsetX: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentOffsetY

```TypeScript
contentOffsetY: number
```

Offset of the rendered content relative to the component on the y-axis

Unit: [px](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md)

**NOTE**

This parameter is valid only when the return value of **loadingStatus** is **1**.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageLoadResult-contentOffsetY: number--><!--Device-ImageLoadResult-contentOffsetY: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## contentWidth

```TypeScript
contentWidth: number
```

Actual rendered width of the image.

Unit: [px](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md)

**NOTE**

This parameter is valid only when the return value of **loadingStatus** is **1**.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageLoadResult-contentWidth: number--><!--Device-ImageLoadResult-contentWidth: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## height

```TypeScript
height: number
```

Height of the image.

Unit: [px](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md)

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageLoadResult-height: number--><!--Device-ImageLoadResult-height: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## loadingStatus

```TypeScript
loadingStatus: number
```

Loading status of the image.

**NOTE**

If the return value is **0**, the image is successfully loaded. If the return value is **1**, the image is successfully decoded.

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageLoadResult-loadingStatus: number--><!--Device-ImageLoadResult-loadingStatus: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## width

```TypeScript
width: number
```

Width of the image.

Unit: [px](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md)

**Type:** number

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ImageLoadResult-width: number--><!--Device-ImageLoadResult-width: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

