# DragResult

定义拖拽操作的结果及组件的落入选定状态。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare enum DragResult--><!--Device-unnamed-declare enum DragResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## UNKNOWN

```TypeScript
UNKNOWN = -1
```

拖拽结果尚未设置，在[onDragStart](arkts-arkui-commonmethod-c.md#ondragstart)，[onDragEnter](arkts-arkui-commonmethod-c.md#ondragenter)，  
[onDragMove](arkts-arkui-commonmethod-c.md#ondragmove)，[onDragLeave](arkts-arkui-commonmethod-c.md#ondragleave)，  
[onDrop](arkts-arkui-commonmethod-c.md#ondrop)中使用。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-DragResult-UNKNOWN = -1--><!--Device-DragResult-UNKNOWN = -1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DRAG_SUCCESSFUL

```TypeScript
DRAG_SUCCESSFUL = 0
```

拖拽成功，在[onDrop](arkts-arkui-commonmethod-c.md#ondrop)中使用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragResult-DRAG_SUCCESSFUL = 0--><!--Device-DragResult-DRAG_SUCCESSFUL = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DRAG_FAILED

```TypeScript
DRAG_FAILED = 1
```

拖拽失败，在[onDrop](arkts-arkui-commonmethod-c.md#ondrop)中使用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragResult-DRAG_FAILED = 1--><!--Device-DragResult-DRAG_FAILED = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DRAG_CANCELED

```TypeScript
DRAG_CANCELED = 2
```

拖拽取消，在[onDrop](arkts-arkui-commonmethod-c.md#ondrop)中使用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragResult-DRAG_CANCELED = 2--><!--Device-DragResult-DRAG_CANCELED = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DROP_ENABLED

```TypeScript
DROP_ENABLED = 3
```

组件允许落入，在[onDragEnter](arkts-arkui-commonmethod-c.md#ondragenter)，[onDragMove](arkts-arkui-commonmethod-c.md#ondragmove)，  
[onDragLeave](arkts-arkui-commonmethod-c.md#ondragleave)中使用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragResult-DROP_ENABLED = 3--><!--Device-DragResult-DROP_ENABLED = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## DROP_DISABLED

```TypeScript
DROP_DISABLED = 4
```

组件不允许落入，在[onDragEnter](arkts-arkui-commonmethod-c.md#ondragenter)，[onDragMove](arkts-arkui-commonmethod-c.md#ondragmove)，  
[onDragLeave](arkts-arkui-commonmethod-c.md#ondragleave)中使用。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-DragResult-DROP_DISABLED = 4--><!--Device-DragResult-DROP_DISABLED = 4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

