# @ohos.arkui.dragController

This module allows developers to trigger a drag event.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-unnamed-declare namespace dragController--><!--Device-unnamed-declare namespace dragController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { dragController } from 'kits/@kit.ArkUI';
```

## 汇总

### 类

| 名称 | 说明 |
| --- | --- |
| [DragPreview](arkts-arkui-dragcontroller-dragpreview-c.md) | Provides the functions of setting color or updating animation. |
| [SpringLoadingContext](arkts-arkui-dragcontroller-springloadingcontext-c.md) | Context information for the current spring loading trigger. This object is passed to the application in the spring loading callback, allowing it to obtain the current state, dynamically refresh UI effects,and access drag data to determine whether to handle the drag operation. |

### 接口

| 名称 | 说明 |
| --- | --- |
| [AnimationOptions](arkts-arkui-dragcontroller-animationoptions-i.md) | Defines the animation options for drag preview. |
| [DragAction](arkts-arkui-dragcontroller-dragaction-i.md) | One drag action object for drag process |
| [DragAndDropInfo](arkts-arkui-dragcontroller-draganddropinfo-i.md) | Drag and drop information |
| [DragEventParam](arkts-arkui-dragcontroller-drageventparam-i.md) | Define the drag event parameters |
| [DragInfo](arkts-arkui-dragcontroller-draginfo-i.md) | DragInfo object description |
| [DragSpringLoadingConfiguration](arkts-arkui-dragcontroller-dragspringloadingconfiguration-i.md) | Defines parameters affecting spring loading detection. Typically, default system configurations suffice.Customization can be done by specifying the config when binding onDragSpringLoading or dynamically modifying it using the updateConfiguration method during the BEGIN state. |
| [SpringLoadingDragInfos](arkts-arkui-dragcontroller-springloadingdraginfos-i.md) | Defines drag-related information when triggering spring loading callbacks.This interface provides drag data summaries and additional drag information, useful for applications needing to dynamically determine whether to respond to spring loading callbacks based on drag data. |

### 枚举

| 名称 | 说明 |
| --- | --- |
| [DragSpringLoadingState](arkts-arkui-dragcontroller-dragspringloadingstate-e.md) | Defines the drag spring loading state.Under default system configuration, if no CANCEL occurs, the state reporting is as follows: Hover still--500ms-->BEGIN-->100ms-->UPDATE-->100ms-->UPDATE-->100ms-->UPDATE-->100ms-->END |
| [DragStartRequestStatus](arkts-arkui-dragcontroller-dragstartrequeststatus-e.md) | Define the status for the application to notify the framework whether to execute drag. |
| [DragStatus](arkts-arkui-dragcontroller-dragstatus-e.md) | Defines the Drag Status. |

