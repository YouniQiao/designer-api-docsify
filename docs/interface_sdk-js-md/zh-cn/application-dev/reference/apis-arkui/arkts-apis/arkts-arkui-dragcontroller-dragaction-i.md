# DragAction

One drag action object for drag process

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-dragController-interface DragAction--><!--Device-dragController-interface DragAction-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { dragController } from 'kits/@kit.ArkUI';
```

## offStatusChange

```TypeScript
offStatusChange(callback?: Callback<DragAndDropInfo>): void
```

Deregisters a callback for listening on drag status changes.This callback is not triggered when the drag status change.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragAction-offStatusChange(callback?: Callback<DragAndDropInfo>): void--><!--Device-DragAction-offStatusChange(callback?: Callback<DragAndDropInfo>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DragAndDropInfo&gt; | 否 | with drag event and status information |

## onStatusChange

```TypeScript
onStatusChange(callback: Callback<DragAndDropInfo>): void
```

Registers a callback for listening on drag status changes.This callback is triggered when the drag status change.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragAction-onStatusChange(callback: Callback<DragAndDropInfo>): void--><!--Device-DragAction-onStatusChange(callback: Callback<DragAndDropInfo>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DragAndDropInfo&gt; | 是 | with drag event and status information |

## startDrag

```TypeScript
startDrag(): Promise<void> | null
```

trigger drag action

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-DragAction-startDrag(): Promise<void> | null--><!--Device-DragAction-startDrag(): Promise<void> | null-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | A Promise can indicate the start result is returned, or null is returned if it's failed for some errors, for example: execution environment broken or excess parameters passed in. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 100001 | Internal handling failed. |

