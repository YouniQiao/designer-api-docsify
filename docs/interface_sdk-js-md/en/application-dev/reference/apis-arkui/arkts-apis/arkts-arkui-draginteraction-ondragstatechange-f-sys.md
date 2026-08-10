# onDragStateChange (System API)

## Modules to Import

```TypeScript
import { dragInteraction } from 'kits/@kit.ArkUI';
```

## onDragStateChange

```TypeScript
function onDragStateChange(callback: Callback<DragState>): void
```

Listens for dragging state change events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-dragInteraction-function onDragStateChange(callback: Callback<DragState>): void--><!--Device-dragInteraction-function onDragStateChange(callback: Callback<DragState>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Drag

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DragState&gt; | Yes | Indicates the callback to receive the changed dragging state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Permission verification failed. A non-system application calls a system API. |

