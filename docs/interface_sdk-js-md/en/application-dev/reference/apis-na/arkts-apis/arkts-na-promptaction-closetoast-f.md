# closeToast

## Modules to Import

```TypeScript
```

## closeToast

```TypeScript
export function closeToast(toastId: int): void
```

Close the notification text.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-promptAction-export function closeToast(toastId: int): void--><!--Device-promptAction-export function closeToast(toastId: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| toastId | int | Yes | the toast id returned by openToast. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [103401](../../apis-arkui/errorcode-promptAction.md#103401-toast-not-found) | Cannot find the toast. |

