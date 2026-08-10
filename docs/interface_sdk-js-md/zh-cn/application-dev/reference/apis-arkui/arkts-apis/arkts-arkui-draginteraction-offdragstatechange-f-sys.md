# offDragStateChange（系统接口）

## 导入模块

```TypeScript
import { dragInteraction } from 'kits/@kit.ArkUI';
```

## offDragStateChange

```TypeScript
function offDragStateChange(callback?: Callback<DragState>): void
```

Disables listening for dragging state change events.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-dragInteraction-function offDragStateChange(callback?: Callback<DragState>): void--><!--Device-dragInteraction-function offDragStateChange(callback?: Callback<DragState>): void-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Drag

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DragState&gt; | 否 | Indicates the callback for which listening is disabled. If this &lt;br&gt; parameter is not specified, listening will be disabled for all registered callbacks. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 202 | Permission verification failed. A non-system application calls a system API. |

