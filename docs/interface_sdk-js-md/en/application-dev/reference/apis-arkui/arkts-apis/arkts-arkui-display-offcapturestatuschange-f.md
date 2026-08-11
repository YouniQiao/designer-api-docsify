# offCaptureStatusChange

## Modules to Import

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## offCaptureStatusChange

```TypeScript
function offCaptureStatusChange(callback?: Callback<boolean>): void
```

Unregister the callback for the status of the device's screen content is being captured.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-display-function offCaptureStatusChange(callback?: Callback<boolean>): void--><!--Device-display-function offCaptureStatusChange(callback?: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | No | Unregister the callback function. If not provided, all callbacks for the given event type will be removed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

