# DragPreviewOptions

设置拖拽过程中预览图处理模式及数量角标的显示。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface DragPreviewOptions--><!--Device-unnamed-declare interface DragPreviewOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode?: DragPreviewMode | Array<DragPreviewMode>
```

表示拖拽过程中背板图处理模式。

默认值：DragPreviewMode.AUTO

当组件同时设置DragPreviewMode.AUTO和其它枚举值时，以DragPreviewMode.AUTO为准，其它枚举值设置无效。

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

控制数量角标是否显示，或强制设置显示的数量。当设置数量角标时取值范围为[0，2&lt;sup&gt;31&lt;/sup&gt;-1]，超过取值范围时会按默认状态处理。当设置为浮点数时，只显示整数部分。

**说明：**

在多选拖拽场景，需通过该接口设置拖拽对象的数量。

默认值：true。

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

用于选择长按浮起图与拖拽预览图过渡效果。

默认值：DraggingSizeChangeEffect.DEFAULT。

**Type:** [DraggingSizeChangeEffect](../arkts-apis/arkts-arkui-common-draggingsizechangeeffect-e.md)

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-DragPreviewOptions-sizeChangeEffect?: DraggingSizeChangeEffect--><!--Device-DragPreviewOptions-sizeChangeEffect?: DraggingSizeChangeEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

