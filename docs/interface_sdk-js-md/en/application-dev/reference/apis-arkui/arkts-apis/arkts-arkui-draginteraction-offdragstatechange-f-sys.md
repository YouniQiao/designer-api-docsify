# offDragStateChange (System API)

## Modules to Import

```TypeScript
import { dragInteraction } from 'kits/@kit.ArkUI';
```

## offDragStateChange

```TypeScript
function offDragStateChange(callback?: Callback<DragState>): void
```

Disables listening for dragging state change events.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-dragInteraction-function offDragStateChange(callback?: Callback<DragState>): void--><!--Device-dragInteraction-function offDragStateChange(callback?: Callback<DragState>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Drag

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DragState&gt; | No | Indicates the callback for which listening is disabled. If this &lt;br&gt; parameter is not specified, listening will be disabled for all registered callbacks. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 202 | Permission verification failed. A non-system application calls a system API. |

