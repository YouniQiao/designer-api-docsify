# DragStartRequestStatus

Define the status for the application to notify the framework whether to execute drag.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-dragController-const enum DragStartRequestStatus--><!--Device-dragController-const enum DragStartRequestStatus-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## WAITING

```TypeScript
WAITING = 0
```

Notify the framework that the application is not yet ready and needs to temporarily block the start of drag, only effective in onDragStart calls.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragStartRequestStatus-WAITING = 0--><!--Device-DragStartRequestStatus-WAITING = 0-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## READY

```TypeScript
READY = 1
```

Notify the framework that the drag can continue to be started, but only during the start of drag, and will not take effect when the drag is started.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragStartRequestStatus-READY = 1--><!--Device-DragStartRequestStatus-READY = 1-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

