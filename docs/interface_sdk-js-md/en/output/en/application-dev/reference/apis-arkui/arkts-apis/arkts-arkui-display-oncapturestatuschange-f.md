# onCaptureStatusChange

## onCaptureStatusChange

```TypeScript
function onCaptureStatusChange(callback: Callback<boolean>): void
```

Register the callback for device capture, casting, or recording status changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-display-function onCaptureStatusChange(callback: Callback<boolean>): void--><!--Device-display-function onCaptureStatusChange(callback: Callback<boolean>): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;boolean&gt; | Yes | Callback used to return the device capture, casting, or recording status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [1400003](../errorcode-display.md#1400003-abnormal-display-manager-service) | This display manager service works abnormally. |

