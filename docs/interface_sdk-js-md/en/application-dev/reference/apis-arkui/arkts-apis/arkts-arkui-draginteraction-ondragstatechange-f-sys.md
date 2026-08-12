# onDragStateChange (System API)

## Modules to Import

```TypeScript
import { dragInteraction } from '@kit.ArkUI';
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
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DragState](arkts-arkui-draginteraction-dragstate-e-sys.md)&gt; | Yes | Indicates the callback to receive the changed dragging state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

