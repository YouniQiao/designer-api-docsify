# openToast

## Modules to Import

```TypeScript
```

## openToast

```TypeScript
export function openToast(options: ShowToastOptions): Promise<int>
```

Displays the notification text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-promptAction-export function openToast(options: ShowToastOptions): Promise<int>--><!--Device-promptAction-export function openToast(options: ShowToastOptions): Promise<int>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | ShowToastOptions | Yes | Options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | return the toast id that will be used by closeToast. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br> 1. Mandatory parameters are left unspecified. <br> 2. Incorrect parameters types. <br> 3. Parameter verification failed. |
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |

