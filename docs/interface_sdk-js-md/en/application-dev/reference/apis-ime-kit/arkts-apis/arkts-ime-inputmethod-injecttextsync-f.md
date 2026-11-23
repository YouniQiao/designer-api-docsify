# injectTextSync

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## injectTextSync

```TypeScript
function injectTextSync(text: string): void
```

Inject text into the current focus edit box of the foreground application. <br> <br>  
> **Note:** <br> <br>
> This interface is supported only by PCs.

**Since:** 26.1.0

**Required permissions:** ohos.permission.OPERATE_TEXT_ACROSS_APPLICATION or ohos.permission.CONTROL_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-inputMethod-function injectTextSync(text: string): void--><!--Device-inputMethod-function injectTextSync(text: string): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Text to inject. Maximun 512 bytes. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | permissions check fails. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error,such as null pointer, IPC exception. |
| [12800016](../errorcode-inputmethod-framework.md#12800016-input-method-client-not-in-edit-mode) | input method client is not editable. |
