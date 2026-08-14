# offDragStateChange (System API)

## Modules to Import

```TypeScript
import { dragInteraction } from 'dragInteraction';
```

## offDragStateChange

```TypeScript
function offDragStateChange(callback?: Callback<DragState>): void
```

Disables listening for dragging state change events.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-dragInteraction-function offDragStateChange(callback?: Callback<DragState>): void--><!--Device-dragInteraction-function offDragStateChange(callback?: Callback<DragState>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Drag

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DragState](arkts-arkui-draginteraction-dragstate-e-sys.md)&gt; | No | Indicates the callback for which listening is disabled. If this <br> parameter is not specified, listening will be disabled for all registered callbacks. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

