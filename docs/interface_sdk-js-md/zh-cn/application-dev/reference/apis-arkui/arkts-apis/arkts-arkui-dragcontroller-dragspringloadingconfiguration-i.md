# DragSpringLoadingConfiguration

Defines parameters affecting spring loading detection. Typically, default system configurations suffice.Customization can be done by specifying the config when binding onDragSpringLoading or dynamically modifying it using the updateConfiguration method during the BEGIN state.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-dragController-export interface DragSpringLoadingConfiguration--><!--Device-dragController-export interface DragSpringLoadingConfiguration-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { dragController } from 'kits/@kit.ArkUI';
```

## stillTimeLimit

```TypeScript
stillTimeLimit?: int
```

Time interval to maintain a stationary state before entering spring loading. Default: 500 ms.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragSpringLoadingConfiguration-stillTimeLimit?: int--><!--Device-DragSpringLoadingConfiguration-stillTimeLimit?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## updateInterval

```TypeScript
updateInterval?: int
```

Interval between update notifications after entering the spring loading state. Default: 100ms.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragSpringLoadingConfiguration-updateInterval?: int--><!--Device-DragSpringLoadingConfiguration-updateInterval?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## updateNotifyCount

```TypeScript
updateNotifyCount?: int
```

Maximum number of update notifications to report while in the spring loading state. Default: 3.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragSpringLoadingConfiguration-updateNotifyCount?: int--><!--Device-DragSpringLoadingConfiguration-updateNotifyCount?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## updateToFinishInterval

```TypeScript
updateToFinishInterval?: int
```

Maximum wait time from the last UPDATE state to the end of spring loading. Default: 100ms.

**类型：** int

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragSpringLoadingConfiguration-updateToFinishInterval?: int--><!--Device-DragSpringLoadingConfiguration-updateToFinishInterval?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

