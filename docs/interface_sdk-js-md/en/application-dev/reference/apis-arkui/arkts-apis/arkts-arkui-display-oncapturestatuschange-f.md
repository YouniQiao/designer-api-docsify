# onCaptureStatusChange

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## onCaptureStatusChange

```TypeScript
function onCaptureStatusChange(callback: Callback<boolean>): void
```

Register the callback for the status of the device's screen content is being captured.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-display-function onCaptureStatusChange(callback: Callback<boolean>): void--><!--Device-display-function onCaptureStatusChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;boolean&gt; | Yes | Callback used to return the device capture, casting, or recording status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-arkui/errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

