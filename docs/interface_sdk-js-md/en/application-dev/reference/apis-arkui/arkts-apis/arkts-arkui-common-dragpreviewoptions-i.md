# DragPreviewOptions

Defines the preview options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface DragPreviewOptions--><!--Device-unnamed-export declare interface DragPreviewOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## mode

```TypeScript
mode?: DragPreviewMode | Array<DragPreviewMode>
```

Drag preview mode.

**Type:** [DragPreviewMode](arkts-arkui-common-dragpreviewmode-e.md) \| Array&lt;DragPreviewMode&gt;

**Default:** DragPreviewMode.AUTO

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragPreviewOptions-mode?: DragPreviewMode | Array<DragPreviewMode>--><!--Device-DragPreviewOptions-mode?: DragPreviewMode | Array<DragPreviewMode>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## modifier

```TypeScript
modifier?: ImageModifier
```

Drag preview modifier.

**Type:** [ImageModifier](../arkts-components/arkts-arkui-imagemodifier-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragPreviewOptions-modifier?: ImageModifier--><!--Device-DragPreviewOptions-modifier?: ImageModifier-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## numberBadge

```TypeScript
numberBadge?: boolean | long
```

The flag for number showing.

**Type:** boolean \| long

**Default:** true

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragPreviewOptions-numberBadge?: boolean | long--><!--Device-DragPreviewOptions-numberBadge?: boolean | long-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sizeChangeEffect

```TypeScript
sizeChangeEffect?: DraggingSizeChangeEffect
```

Drag start animation effect from drag preview to the handle drag image.

**Type:** [DraggingSizeChangeEffect](arkts-arkui-common-draggingsizechangeeffect-e.md)

**Default:** DraggingSizeChangeEffect.DEFAULT

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragPreviewOptions-sizeChangeEffect?: DraggingSizeChangeEffect--><!--Device-DragPreviewOptions-sizeChangeEffect?: DraggingSizeChangeEffect-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

