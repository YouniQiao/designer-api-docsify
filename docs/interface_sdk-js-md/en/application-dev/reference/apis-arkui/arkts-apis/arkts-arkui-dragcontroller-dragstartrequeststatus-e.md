# DragStartRequestStatus

Define the status for the application to notify the framework whether to execute drag.

@enum { number }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-dragController-const enum DragStartRequestStatus--><!--Device-dragController-const enum DragStartRequestStatus-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## WAITING

```TypeScript
WAITING = 0
```

Notify the framework that the application is not yet ready and needs to temporarily block the start of drag, only effective in onDragStart calls.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragStartRequestStatus-WAITING = 0--><!--Device-DragStartRequestStatus-WAITING = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## READY

```TypeScript
READY = 1
```

Notify the framework that the drag can continue to be started, but only during the start of drag, and will not take effect when the drag is started.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DragStartRequestStatus-READY = 1--><!--Device-DragStartRequestStatus-READY = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

