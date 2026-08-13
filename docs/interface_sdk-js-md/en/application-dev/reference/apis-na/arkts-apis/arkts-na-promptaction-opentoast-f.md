# openToast

## openToast

```TypeScript
export function openToast(options: ShowToastOptions): Promise<int>
```

Displays the notification text.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

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
| [100001](../../apis-arkui/errorcode-internal.md#100001-internal-error) | Internal error. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: &lt;br&gt; 1. Mandatory parameters are left unspecified. &lt;br&gt; 2. Incorrect parameters types. &lt;br&gt; 3. Parameter verification failed. |

