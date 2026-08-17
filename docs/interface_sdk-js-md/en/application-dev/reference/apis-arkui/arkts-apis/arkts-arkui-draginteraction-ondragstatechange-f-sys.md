# onDragStateChange (System API)

## Modules to Import

```TypeScript
import { dragInteraction } from 'dragInteraction';
```

## onDragStateChange

```TypeScript
function onDragStateChange(callback: Callback<DragState>): void
```

Listens for dragging state change events.

**Since:** 23

<!--Device-dragInteraction-function onDragStateChange(callback: Callback<DragState>): void--><!--Device-dragInteraction-function onDragStateChange(callback: Callback<DragState>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Drag

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DragState](arkts-arkui-draginteraction-dragstate-e-sys.md)&gt; | Yes | Indicates the callback to receive the changed dragging state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

