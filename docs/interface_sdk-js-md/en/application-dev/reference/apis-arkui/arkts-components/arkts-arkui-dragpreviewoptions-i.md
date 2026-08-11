# DragPreviewOptions

Preview image processing mode and badge count during dragging.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface DragPreviewOptions--><!--Device-unnamed-declare interface DragPreviewOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode?: DragPreviewMode | Array<DragPreviewMode>
```

How the background image is processed when the component is dragged.

Default value: **DragPreviewMode.AUTO**

If **DragPreviewMode.AUTO** is set concurrently with other enumerated values, **DragPreviewMode.AUTO** takes precedence and the other values are ignored.

**Type:** [DragPreviewMode](../arkts-apis/arkts-arkui-common-dragpreviewmode-e.md) \| Array&lt;DragPreviewMode&gt;

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DragPreviewOptions-mode?: DragPreviewMode | Array<DragPreviewMode>--><!--Device-DragPreviewOptions-mode?: DragPreviewMode | Array<DragPreviewMode>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## numberBadge

```TypeScript
numberBadge?: boolean | number
```

Whether to display the number badge or the number displayed on the badge. For a number badge, the value range is  
[0, 2&lt;sup&gt;31&lt;/sup&gt;-1]. Values outside this range will be processed as the default state. If the value specified is a floating-point number, only the integer part is displayed.

**NOTE：**

When multiple items are dragged, use this API to set the number of items dragged.

Default value: **true**.

**Type:** boolean \| number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-DragPreviewOptions-numberBadge?: boolean | number--><!--Device-DragPreviewOptions-numberBadge?: boolean | number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sizeChangeEffect

```TypeScript
sizeChangeEffect?: DraggingSizeChangeEffect
```

Transition effect between the floating image and drag preview.

Default value: **DraggingSizeChangeEffect.DEFAULT**.

**Type:** [DraggingSizeChangeEffect](../arkts-apis/arkts-arkui-common-draggingsizechangeeffect-e.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-DragPreviewOptions-sizeChangeEffect?: DraggingSizeChangeEffect--><!--Device-DragPreviewOptions-sizeChangeEffect?: DraggingSizeChangeEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

