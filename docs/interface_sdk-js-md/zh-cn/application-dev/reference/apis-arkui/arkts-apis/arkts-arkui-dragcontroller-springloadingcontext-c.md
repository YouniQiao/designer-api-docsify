# SpringLoadingContext

Context information for the current spring loading trigger. This object is passed to the application in the spring loading callback, allowing it to obtain the current state, dynamically refresh UI effects,and access drag data to determine whether to handle the drag operation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-dragController-export class SpringLoadingContext--><!--Device-dragController-export class SpringLoadingContext-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { dragController } from 'kits/@kit.ArkUI';
```

## abort

```TypeScript
abort(): void
```

Aborts subsequent spring loading triggers.Note: Aborting does not trigger a CANCEL notification, the application must handle state cleanup when aborting.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SpringLoadingContext-abort(): void--><!--Device-SpringLoadingContext-abort(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## updateConfiguration

```TypeScript
updateConfiguration(config: DragSpringLoadingConfiguration): void
```

Updates the spring loading configuration for the current trigger. Only effective during the BEGIN state.This method does not modify the original configuration set during onDragSpringLoading binding.It provides an opportunity for dynamic configuration updates during the current trigger.Typically, applications should use default configurations or set them once during binding.Use this method sparingly, e.g., for different drag data types requiring varied UX timing.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SpringLoadingContext-updateConfiguration(config: DragSpringLoadingConfiguration): void--><!--Device-SpringLoadingContext-updateConfiguration(config: DragSpringLoadingConfiguration): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [DragSpringLoadingConfiguration](../arkts-components/arkts-arkui-dragspringloadingconfiguration-t.md) | 是 |  |

## currentConfig

```TypeScript
currentConfig?: DragSpringLoadingConfiguration
```

Current spring loading configuration. Absent when the state is CANCEL.

**类型：** [DragSpringLoadingConfiguration](../arkts-components/arkts-arkui-dragspringloadingconfiguration-t.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SpringLoadingContext-currentConfig?: DragSpringLoadingConfiguration--><!--Device-SpringLoadingContext-currentConfig?: DragSpringLoadingConfiguration-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## currentNotifySequence

```TypeScript
currentNotifySequence: int
```

Sequence number of the current spring loading state notification. Begins at 0 for BEGIN and increments with each callback.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SpringLoadingContext-currentNotifySequence: int--><!--Device-SpringLoadingContext-currentNotifySequence: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## dragInfos

```TypeScript
dragInfos?: SpringLoadingDragInfos
```

Drag-related information. Absent when the state is CANCEL.

**类型：** [SpringLoadingDragInfos](arkts-arkui-dragcontroller-springloadingdraginfos-i.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SpringLoadingContext-dragInfos?: SpringLoadingDragInfos--><!--Device-SpringLoadingContext-dragInfos?: SpringLoadingDragInfos-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## state

```TypeScript
state: DragSpringLoadingState
```

Current spring loading state. Refer to the DragSpringLoadingState enum for details.

**类型：** [DragSpringLoadingState](arkts-arkui-dragcontroller-dragspringloadingstate-e.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SpringLoadingContext-state: DragSpringLoadingState--><!--Device-SpringLoadingContext-state: DragSpringLoadingState-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

