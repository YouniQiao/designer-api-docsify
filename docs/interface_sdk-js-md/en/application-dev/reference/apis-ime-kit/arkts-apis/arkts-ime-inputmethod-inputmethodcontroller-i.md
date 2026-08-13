# InputMethodController

A control class that encapsulates APIs for input method management, which can only be invoked after an **InputMethodController** instance is obtained via [getController](arkts-ime-inputmethod-getcontroller-f.md#getController).

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-inputMethod-interface InputMethodController--><!--Device-inputMethod-interface InputMethodController-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from '@kit.IMEKit';
```

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void
```

Attach application to the input method service.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void--><!--Device-InputMethodController-attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| showKeyboard | boolean | Yes | show the keyboard or not when attach the input method. |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | Yes | indicates the config of the textInput. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of attach. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
inputMethod.getController().attach(true, textConfig, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in attaching the inputMethod.');
});
```

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>
```

Attach application to the input method service.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>--><!--Device-InputMethodController-attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| showKeyboard | boolean | Yes | show the keyboard or not when attach the input method. |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | Yes | indicates the config of the textInput. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
inputMethod.getController().attach(true, textConfig).then(() => {
  console.info('Succeeded in attaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
});
```

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>
```

Attach application to the input method service.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>--><!--Device-InputMethodController-attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| showKeyboard | boolean | Yes | show the keyboard or not when attach the input method. |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | Yes | indicates the config of the textInput. |
| requestKeyboardReason | RequestKeyboardReason | Yes | requestKeyboardReason of show the keyboard . |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
let requestKeyboardReason: inputMethod.RequestKeyboardReason = inputMethod.RequestKeyboardReason.MOUSE;

inputMethod.getController().attach(true, textConfig, requestKeyboardReason).then(() => {
  console.info('Succeeded in attaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
});
```

## attachWithUIContext

```TypeScript
attachWithUIContext(uiContext: UIContext, textConfig: TextConfig, attachOptions?: AttachOptions): Promise<void>
```

Attach application to the input method service with UI context.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodController-attachWithUIContext(uiContext: UIContext, textConfig: TextConfig, attachOptions?: AttachOptions): Promise<void>--><!--Device-InputMethodController-attachWithUIContext(uiContext: UIContext, textConfig: TextConfig, attachOptions?: AttachOptions): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | indicates the ui context where the attachment will be performed. |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | Yes | indicates the config of the textInput. |
| attachOptions | AttachOptions | No | indicates the attach options. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { UIContext } from '@kit.ArkUI';

let uiContext: UIContext | undefined = UIContext.getCallingScopeUIContext();
let inputAttribute: inputMethod.InputAttribute = {
  textInputType: inputMethod.TextInputType.TEXT,
  enterKeyType: inputMethod.EnterKeyType.GO
}
let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
let attachOptions: inputMethod.AttachOptions = { showKeyboard: true };
inputMethod.getController().attachWithUIContext(uiContext, textConfig, attachOptions).then(() => {
  console.info('Succeeded in attaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
});
```

## changeSelection

```TypeScript
changeSelection(text: string, start: int, end: int, callback: AsyncCallback<void>): void
```

Notify the input method the selected text and the selection range of the current application text has changed.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-changeSelection(text: string, start: int, end: int, callback: AsyncCallback<void>): void--><!--Device-InputMethodController-changeSelection(text: string, start: int, end: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | the whole input text. |
| start | int | Yes | start position of selected text. |
| end | int | Yes | end position of selected text. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of changeSelection. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().changeSelection('text', 0, 5, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to changeSelection, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in changing selection.');
});
```

## changeSelection

```TypeScript
changeSelection(text: string, start: int, end: int): Promise<void>
```

Notify the input method the selected text and the selection range of the current application text has changed.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-changeSelection(text: string, start: int, end: int): Promise<void>--><!--Device-InputMethodController-changeSelection(text: string, start: int, end: int): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | the selected text. |
| start | int | Yes | start position of selected text. |
| end | int | Yes | end position of selected text. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().changeSelection('test', 0, 5).then(() => {
  console.info('Succeeded in changing selection.');
}).catch((err: BusinessError) => {
  console.error(`Failed to changeSelection, code: ${err.code}, message: ${err.message}`);
});
```

## detach

```TypeScript
detach(callback: AsyncCallback<void>): void
```

Detach the applications from the input method manager service.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-detach(callback: AsyncCallback<void>): void--><!--Device-InputMethodController-detach(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of detach. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().detach((err: BusinessError) => {
  if (err) {
    console.error(`Failed to detach, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in detaching inputMethod.');
});
```

## detach

```TypeScript
detach(): Promise<void>
```

Detach the applications from the input method manager service.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-detach(): Promise<void>--><!--Device-InputMethodController-detach(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().detach().then(() => {
  console.info('Succeeded in detaching inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to detach, code: ${err.code}, message: ${err.message}`);
});
```

## discardTypingText

```TypeScript
discardTypingText(): Promise<void>
```

Discard the typing text

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-discardTypingText(): Promise<void>--><!--Device-InputMethodController-discardTypingText(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800015](../errorcode-inputmethod-framework.md#12800015-message-receiver-unable-to-receive-custom-communication-data) | the other side does not accept the request. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().discardTypingText().then(() => {
  console.info('Succeeded discardTypingText.');
}).catch((err: BusinessError) => {
  console.error(`Failed to discardTypingText, code: ${err.code}, message: ${err.message}`);
});
```

## hideSoftKeyboard

```TypeScript
hideSoftKeyboard(callback: AsyncCallback<void>): void
```

Hide soft keyboard. This API can be called only by system applications.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

<!--Device-InputMethodController-hideSoftKeyboard(callback: AsyncCallback<void>): void--><!--Device-InputMethodController-hideSoftKeyboard(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of hideSoftKeyboard. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [201](../../errorcode-universal.md#201-permission-denied) | permissions check fails. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideSoftKeyboard((err: BusinessError) => {
  if (!err) {
    console.info('Succeeded in hiding softKeyboard.');
  } else {
    console.error(`Failed to hide softKeyboard, code: ${err.code}, message: ${err.message}`);
  }
})
```

## hideSoftKeyboard

```TypeScript
hideSoftKeyboard(): Promise<void>
```

Hide soft keyboard. This API can be called only by system applications.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

<!--Device-InputMethodController-hideSoftKeyboard(): Promise<void>--><!--Device-InputMethodController-hideSoftKeyboard(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [201](../../errorcode-universal.md#201-permission-denied) | permissions check fails. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideSoftKeyboard().then(() => {
  console.info('Succeeded in hiding softKeyboard.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hide softKeyboard, code: ${err.code}, message: ${err.message}`);
});
```

## hideTextInput

```TypeScript
hideTextInput(callback: AsyncCallback<void>): void
```

Hide the text input and stop typing.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-hideTextInput(callback: AsyncCallback<void>): void--><!--Device-InputMethodController-hideTextInput(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of hideTextInput. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideTextInput((err: BusinessError) => {
  if (err) {
    console.error(`Failed to hideTextInput, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in hiding text input.');
});
```

## hideTextInput

```TypeScript
hideTextInput(): Promise<void>
```

Hide the text input and stop typing.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-hideTextInput(): Promise<void>--><!--Device-InputMethodController-hideTextInput(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().hideTextInput().then(() => {
  console.info('Succeeded in hiding inputMethod.');
}).catch((err: BusinessError) => {
  console.error(`Failed to hideTextInput, code: ${err.code}, message: ${err.message}`);
})
```

## offDeleteLeft

```TypeScript
offDeleteLeft(callback?: Callback<int>): void
```

Unregister the callback of deleteLeft.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-offDeleteLeft(callback?: Callback<int>): void--><!--Device-InputMethodController-offDeleteLeft(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | No | the callback called when the input method deletes text to the left of the cursor. |

## offDeleteRight

```TypeScript
offDeleteRight(callback?: Callback<int>): void
```

Unregister the callback of deleteRight.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-offDeleteRight(callback?: Callback<int>): void--><!--Device-InputMethodController-offDeleteRight(callback?: Callback<int>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | No | the callback called when the input method deletes text to the right of the cursor. |

## offFinishTextPreview

```TypeScript
offFinishTextPreview(callback?: Callback<void>): void
```

Unsubscribe 'finishTextPreview' event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-offFinishTextPreview(callback?: Callback<void>): void--><!--Device-InputMethodController-offFinishTextPreview(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | optional, the callback called when the input method finishes text preview. |

## offGetLeftTextOfCursor

```TypeScript
offGetLeftTextOfCursor(callback?: GetTextCallback): void
```

Unregister the callback of getLeftTextofCursor event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-offGetLeftTextOfCursor(callback?: GetTextCallback): void--><!--Device-InputMethodController-offGetLeftTextOfCursor(callback?: GetTextCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) | No | the callback called when the input method gets text to the left of the cursor. The callback must be a synchronization method and will block the input method application. |

## offGetRightTextOfCursor

```TypeScript
offGetRightTextOfCursor(callback?: GetTextCallback): void
```

Unregister the callback of getRightTextOfCursor event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-offGetRightTextOfCursor(callback?: GetTextCallback): void--><!--Device-InputMethodController-offGetRightTextOfCursor(callback?: GetTextCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) | No | the callback called when the input method gets text to the right of the cursor. The callback must be a synchronization method and will block the input method application. |

## offGetTextIndexAtCursor

```TypeScript
offGetTextIndexAtCursor(callback?:GetTextIndexAtCursorCallback): void
```

Unregister the callback of getTextIndexAtCursor.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodController-offGetTextIndexAtCursor(callback?:GetTextIndexAtCursorCallback): void--><!--Device-InputMethodController-offGetTextIndexAtCursor(callback?:GetTextIndexAtCursorCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [GetTextIndexAtCursorCallback](arkts-ime-inputmethod-gettextindexatcursorcallback-t.md) | No | the callback called when the input method gets cursor index. |

## offHandleExtendAction

```TypeScript
offHandleExtendAction(callback?: Callback<ExtendAction>): void
```

Unregister the callback of handleExtendAction.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-offHandleExtendAction(callback?: Callback<ExtendAction>): void--><!--Device-InputMethodController-offHandleExtendAction(callback?: Callback<ExtendAction>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ExtendAction&gt; | No | the callback called when the input method sends extend action. |

## offInsertText

```TypeScript
offInsertText(callback?: Callback<string>): void
```

Unregister the callback of insertText.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-offInsertText(callback?: Callback<string>): void--><!--Device-InputMethodController-offInsertText(callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No | the callback called when the input method inserts text. |

## offMoveCursor

```TypeScript
offMoveCursor(callback?: Callback<Direction>): void
```

Unregister the callback of moveCursor.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-offMoveCursor(callback?: Callback<Direction>): void--><!--Device-InputMethodController-offMoveCursor(callback?: Callback<Direction>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Direction&gt; | No | the callback called when the input method moves cursor. |

## offSelectByMovement

```TypeScript
offSelectByMovement(callback?: Callback<Movement>): void
```

Unregister the callback of selectedByMovement.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-offSelectByMovement(callback?: Callback<Movement>): void--><!--Device-InputMethodController-offSelectByMovement(callback?: Callback<Movement>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | No | the callback called when the input method selects text by movement. |

## offSelectByRange

```TypeScript
offSelectByRange(callback?: Callback<Range>): void
```

Unregister the callback of selectedByRange.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-offSelectByRange(callback?: Callback<Range>): void--><!--Device-InputMethodController-offSelectByRange(callback?: Callback<Range>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | No | the callback called when the input method selects text by range. |

## offSendFunctionKey

```TypeScript
offSendFunctionKey(callback?: Callback<FunctionKey>): void
```

Unregister the callback of sendFunctionKey.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-offSendFunctionKey(callback?: Callback<FunctionKey>): void--><!--Device-InputMethodController-offSendFunctionKey(callback?: Callback<FunctionKey>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FunctionKey&gt; | No | the callback called when the input method send function key. |

## offSendKeyboardStatus

```TypeScript
offSendKeyboardStatus(callback?: Callback<KeyboardStatus>): void
```

Unregister the callback of sendKeyboardStatus.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-offSendKeyboardStatus(callback?: Callback<KeyboardStatus>): void--><!--Device-InputMethodController-offSendKeyboardStatus(callback?: Callback<KeyboardStatus>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyboardStatus](arkts-ime-inputmethod-keyboardstatus-e.md)&gt; | No | the callback called when the inputmethod send keyboard's status. |

## offSetPreviewText

```TypeScript
offSetPreviewText(callback?:SetPreviewTextCallback): void
```

Unsubscribe 'setPreviewText' event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-InputMethodController-offSetPreviewText(callback?:SetPreviewTextCallback): void--><!--Device-InputMethodController-offSetPreviewText(callback?:SetPreviewTextCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | No | optional, the callback called when the input method sets preview text. |

## off_deleteLeft

```TypeScript
off(type: 'deleteLeft', callback?: (length: number) => void): void
```

Unregister the callback of deleteLeft.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-off(type: 'deleteLeft', callback?: (length: number) => void): void--><!--Device-InputMethodController-off(type: 'deleteLeft', callback?: (length: number) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deleteLeft' | Yes | event type, fixed as 'deleteLeft'. |
| callback | (length: number) =&gt; void | No | the callback of 'deleteLeft', when subscriber unsubscribes all callback functions of event 'deleteLeft', this parameter can be left blank. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onDeleteLeftCallback: Callback<number> = (length: number): void => {
  console.info(`Succeeded in subscribing deleteLeft, length: ${length}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('deleteLeft', onDeleteLeftCallback);
inputMethodController.off('deleteLeft');
```

## off_deleteRight

```TypeScript
off(type: 'deleteRight', callback?: (length: number) => void): void
```

Unregister the callback of deleteRight.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-off(type: 'deleteRight', callback?: (length: number) => void): void--><!--Device-InputMethodController-off(type: 'deleteRight', callback?: (length: number) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deleteRight' | Yes | event type, fixed as 'deleteRight'. |
| callback | (length: number) =&gt; void | No | the callback of 'deleteRight', when subscriber unsubscribes all callback functions of event 'deleteRight', this parameter can be left blank. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onDeleteRightCallback: Callback<number> = (length: number): void => {
  console.info(`Succeeded in subscribing deleteRight, length: ${length}`);
};
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('deleteRight', onDeleteRightCallback);
inputMethodController.off('deleteRight');
```

## off_finishTextPreview

```TypeScript
off(type: 'finishTextPreview', callback?: Callback<void>): void
```

Unsubscribe 'finishTextPreview' event.

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Deprecated since:** -1

<!--Device-InputMethodController-off(type: 'finishTextPreview', callback?: Callback<void>): void--><!--Device-InputMethodController-off(type: 'finishTextPreview', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'finishTextPreview' | Yes | the type of unsubscribe event. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | optional, the callback of off('finishTextPreview'). |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let finishTextPreviewCallback1: Callback<void> = (): void => {
  console.info(`FinishTextPreviewCallback1: finishTextPreview event triggered`);
};
let finishTextPreviewCallback2: Callback<void> = (): void => {
  console.info(`FinishTextPreviewCallback2: finishTextPreview event triggered`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('finishTextPreview', finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 subscribed to finishTextPreview`);
inputMethodController.on('finishTextPreview', finishTextPreviewCallback2);
console.info(`FinishTextPreviewCallback2 subscribed to finishTextPreview`);
// Cancel only the callback1 of finishTextPreview.
inputMethodController.off('finishTextPreview', finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 unsubscribed from finishTextPreview`);
// Cancel all callbacks of finishTextPreview.
inputMethodController.off('finishTextPreview');
console.info(`All callbacks unsubscribed from finishTextPreview`);
```

## off_getLeftTextOfCursor

```TypeScript
off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void
```

Unregister the callback of getLeftTextOfCursor event.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void--><!--Device-InputMethodController-off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'getLeftTextOfCursor' | Yes | event type, fixed as 'getLeftTextOfCursor'. |
| callback | (length: number) =&gt; string | No | the callback of 'getLeftTextOfCursor', when subscriber unsubscribes all callback functions of event 'getLeftTextOfCursor', this parameter can be left blank. |

## Examples

```TypeScript
let getLeftTextOfCursorCallback: (length: number) => string = (length: number): string => {
  console.info(`Succeeded in unsubscribing getLeftTextOfCursor, length: ${length}`);
  let text: string = "";
  return text;
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('getLeftTextOfCursor', getLeftTextOfCursorCallback);
inputMethodController.off('getLeftTextOfCursor');
```

## off_getRightTextOfCursor

```TypeScript
off(type: 'getRightTextOfCursor', callback?: (length: number) => string): void
```

Unregister the callback of getRightTextOfCursor event.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-off(type: 'getRightTextOfCursor', callback?: (length: number) => string): void--><!--Device-InputMethodController-off(type: 'getRightTextOfCursor', callback?: (length: number) => string): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'getRightTextOfCursor' | Yes | event type, fixed as 'getRightTextOfCursor'. |
| callback | (length: number) =&gt; string | No | the callback of 'getRightTextOfCursor', when subscriber unsubscribes all callback functions of event 'getRightTextOfCursor', this parameter can be left blank. |

## Examples

```TypeScript
let getRightTextOfCursorCallback: (length: number) => string = (length: number): string => {
  console.info(`Succeeded in unsubscribing getRightTextOfCursor, length: ${length}`);
  let text: string = "";
  return text;
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('getRightTextOfCursor', getRightTextOfCursorCallback);
inputMethodController.off('getRightTextOfCursor');
```

## off_getTextIndexAtCursor

```TypeScript
off(type: 'getTextIndexAtCursor', callback?: () => number): void
```

Unregister the callback of getTextIndexAtCursor.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-off(type: 'getTextIndexAtCursor', callback?: () => number): void--><!--Device-InputMethodController-off(type: 'getTextIndexAtCursor', callback?: () => number): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'getTextIndexAtCursor' | Yes | event type, fixed as 'getTextIndexAtCursor'. |
| callback | () =&gt; number | No | the callback of 'getTextIndexAtCursor', when subscriber unsubscribes all callback functions of event 'getTextIndexAtCursor', this parameter can be left blank. |

## Examples

```TypeScript
let getTextIndexAtCursorCallback: () => number = (): number => {
  console.info(`Succeeded in unsubscribing getTextIndexAtCursor.`);
  let index: number = 0;
  return index;
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('getTextIndexAtCursor', getTextIndexAtCursorCallback);
inputMethodController.off('getTextIndexAtCursor');
```

## off_handleExtendAction

```TypeScript
off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void
```

Unregister the callback of handleExtendAction.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void--><!--Device-InputMethodController-off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'handleExtendAction' | Yes | event type, fixed as 'handleExtendAction'. |
| callback | (action: ExtendAction) =&gt; void | No | the callback of 'handleExtendAction', when subscriber unsubscribes all callback functions of event 'handleExtendAction', this parameter can be left blank. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onHandleExtendActionCallback: Callback<inputMethod.ExtendAction> = (action: inputMethod.ExtendAction): void => {
  console.info(`Succeeded in subscribing handleExtendAction, action: ${action}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('handleExtendAction', onHandleExtendActionCallback);
inputMethodController.off('handleExtendAction');
```

## off_insertText

```TypeScript
off(type: 'insertText', callback?: (text: string) => void): void
```

Unregister the callback of insertText.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-off(type: 'insertText', callback?: (text: string) => void): void--><!--Device-InputMethodController-off(type: 'insertText', callback?: (text: string) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'insertText' | Yes | event type, fixed as 'insertText'. |
| callback | (text: string) =&gt; void | No | the callback of 'insertText', when subscriber unsubscribes all callback functions of event 'insertText', this parameter can be left blank. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onInsertTextCallback: Callback<string> = (text: string): void => {
  console.info(`Succeeded in subscribing insertText: ${text}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('insertText', onInsertTextCallback);
inputMethodController.off('insertText');
```

## off_moveCursor

```TypeScript
off(type: 'moveCursor', callback?: (direction: Direction) => void): void
```

Unregister the callback of moveCursor.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-off(type: 'moveCursor', callback?: (direction: Direction) => void): void--><!--Device-InputMethodController-off(type: 'moveCursor', callback?: (direction: Direction) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'moveCursor' | Yes | event type, fixed as 'moveCursor'. |
| callback | (direction: Direction) =&gt; void | No | the callback of 'moveCursor', when subscriber unsubscribes all callback functions of event 'moveCursor', this parameter can be left blank. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onMoveCursorCallback: Callback<inputMethod.Direction> = (direction: inputMethod.Direction): void => {
  console.info(`Succeeded in subscribing moveCursor, direction: ${direction}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('moveCursor', onMoveCursorCallback);
inputMethodController.off('moveCursor');
```

## off_selectByMovement

```TypeScript
off(type: 'selectByMovement', callback?: Callback<Movement>): void
```

Unregister the callback of selectedByMovement.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-off(type: 'selectByMovement', callback?: Callback<Movement>): void--><!--Device-InputMethodController-off(type: 'selectByMovement', callback?: Callback<Movement>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'selectByMovement' | Yes | event type, fixed as 'selectByMovement'. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | No | the callback of 'selectByMovement', when subscriber unsubscribes all callback functions of event 'selectByMovement', this parameter can be left blank. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onSelectByMovementCallback: Callback<inputMethod.Movement> = (movement: inputMethod.Movement): void => {
  console.info(`Succeeded in subscribing selectByMovement, movement.direction: ${movement.direction}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('selectByMovement', onSelectByMovementCallback);
inputMethodController.off('selectByMovement');
```

## off_selectByRange

```TypeScript
off(type: 'selectByRange', callback?: Callback<Range>): void
```

Unregister the callback of selectedByRange.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-off(type: 'selectByRange', callback?: Callback<Range>): void--><!--Device-InputMethodController-off(type: 'selectByRange', callback?: Callback<Range>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'selectByRange' | Yes | event type, fixed as 'selectByRange'. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | No | the callback of 'selectByRange', when subscriber unsubscribes all callback functions of event 'selectByRange', this parameter can be left blank. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onSelectByRangeCallback: Callback<inputMethod.Range> = (range: inputMethod.Range): void => {
  console.info(`Succeeded in subscribing selectByRange, start: ${range.start} , end: ${range.end}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('selectByRange', onSelectByRangeCallback);
inputMethodController.off('selectByRange');
```

## off_sendFunctionKey

```TypeScript
off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void
```

Unregister the callback of sendFunctionKey.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void--><!--Device-InputMethodController-off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sendFunctionKey' | Yes | event type, fixed as 'sendFunctionKey'. |
| callback | (functionKey: FunctionKey) =&gt; void | No | the callback of 'sendFunctionKey', when subscriber unsubscribes all callback functions of event 'sendFunctionKey', this parameter can be left blank. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onSendFunctionKey: Callback<inputMethod.FunctionKey> = (functionKey: inputMethod.FunctionKey): void => {
  console.info(`Succeeded in subscribing sendFunctionKey, functionKey: ${functionKey.enterKeyType}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('sendFunctionKey', onSendFunctionKey);
inputMethodController.off('sendFunctionKey');
```

## off_sendKeyboardStatus

```TypeScript
off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void
```

Unregister the callback of sendKeyboardStatus.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void--><!--Device-InputMethodController-off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sendKeyboardStatus' | Yes | event type, fixed as 'sendKeyboardStatus'. |
| callback | (keyboardStatus: KeyboardStatus) =&gt; void | No | the callback of 'sendKeyboardStatus', when subscriber unsubscribes all callback functions of event 'sendKeyboardStatus', this parameter can be left blank. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let onSendKeyboardStatus: Callback<inputMethod.KeyboardStatus> = (keyboardStatus: inputMethod.KeyboardStatus): void => {
  console.info(`Succeeded in subscribing sendKeyboardStatus, keyboardStatus: ${keyboardStatus}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.off('sendKeyboardStatus', onSendKeyboardStatus);
inputMethodController.off('sendKeyboardStatus');
```

## off_setPreviewText

```TypeScript
off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void
```

Unsubscribe 'setPreviewText' event.

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Deprecated since:** -1

<!--Device-InputMethodController-off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void--><!--Device-InputMethodController-off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'setPreviewText' | Yes | the type of unsubscribe event. |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | No | optional, the callback of off('setPreviewText'). |

## Examples

```TypeScript
let setPreviewTextCallback1: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(`SetPreviewTextCallback1: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

let setPreviewTextCallback2: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(`setPreviewTextCallback2: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('setPreviewText', setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 subscribed to setPreviewText`);
inputMethodController.on('setPreviewText', setPreviewTextCallback2);
console.info(`SetPreviewTextCallback2 subscribed to setPreviewText`);
// Cancel only the callback1 of setPreviewText.
inputMethodController.off('setPreviewText', setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 unsubscribed from setPreviewText`);
// Cancel all callbacks of setPreviewText.
inputMethodController.off('setPreviewText');
console.info(`All callbacks unsubscribed from setPreviewText`);
```

## onDeleteLeft

```TypeScript
onDeleteLeft(callback: Callback<int>): void
```

Register a callback and when IME sends delete left event with length, the callback will be invoked.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-onDeleteLeft(callback: Callback<int>): void--><!--Device-InputMethodController-onDeleteLeft(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | the callback called when the input method deletes text to the left of the cursor. The length of delete is provided for this callback. Subscribers are expected to delete specified length of text to the left of the cursor and update changes in editor by changeSelection and updateCursor as needed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## onDeleteRight

```TypeScript
onDeleteRight(callback: Callback<int>): void
```

Register a callback and when IME sends delete right event with length, the callback will beinvoked.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-onDeleteRight(callback: Callback<int>): void--><!--Device-InputMethodController-onDeleteRight(callback: Callback<int>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;int&gt; | Yes | the callback called whenthe input method deletes text to theright of the cursor. The length of delete is provided for this callback. Subscribers are expected to delete specified length of text to the right of the cursor and update changes in editor by changeSelection and updateCursor as needed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## onFinishTextPreview

```TypeScript
onFinishTextPreview(callback: Callback<void>): void
```

&lt;p&gt;Subscribe 'finishTextPreview' event.&lt;/p&gt; &lt;p&gt;To support the preview text feature, developers should subscribe to this event before calling attach.&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-onFinishTextPreview(callback: Callback<void>): void--><!--Device-InputMethodController-onFinishTextPreview(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | the callback called when the input method finishes text preview. |

## onGetLeftTextOfCursor

```TypeScript
onGetLeftTextOfCursor(callback: GetTextCallback): void
```

Register a callback and when input method ability gets left text of cursor, the callback will be invoked.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-onGetLeftTextOfCursor(callback: GetTextCallback): void--><!--Device-InputMethodController-onGetLeftTextOfCursor(callback: GetTextCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) | Yes | the callback called when the input method gets text to the left of the cursor. The callback must be a synchronization method and will block the input method application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## onGetRightTextOfCursor

```TypeScript
onGetRightTextOfCursor(callback: GetTextCallback): void
```

Register a callback and when input method ability gets right text of cursor, the callback will be invoked.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-onGetRightTextOfCursor(callback: GetTextCallback): void--><!--Device-InputMethodController-onGetRightTextOfCursor(callback: GetTextCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [GetTextCallback](arkts-ime-inputmethod-gettextcallback-t.md) | Yes | the callback called when the input method gets text to the right of the cursor. The callback must be a synchronization method and will block the input method application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## onGetTextIndexAtCursor

```TypeScript
onGetTextIndexAtCursor(callback: GetTextIndexAtCursorCallback): void
```

Register a callback and when input method ability gets the text index at cursor, the callback will be invoked.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-onGetTextIndexAtCursor(callback: GetTextIndexAtCursorCallback): void--><!--Device-InputMethodController-onGetTextIndexAtCursor(callback: GetTextIndexAtCursorCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [GetTextIndexAtCursorCallback](arkts-ime-inputmethod-gettextindexatcursorcallback-t.md) | Yes | the callback called when input method the gets cursor index. The callback must be a synchronization method, and should return the text index at the cursor. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## onHandleExtendAction

```TypeScript
onHandleExtendAction(callback: Callback<ExtendAction>): void
```

Register a callback and when IME sends extend action code, the callback will be invoked.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-onHandleExtendAction(callback: Callback<ExtendAction>): void--><!--Device-InputMethodController-onHandleExtendAction(callback: Callback<ExtendAction>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ExtendAction&gt; | Yes | the callback called when the input method sends extend action. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## onInsertText

```TypeScript
onInsertText(callback: Callback<string>): void
```

Register a callback and when IME sends insert text event, the callback will be invoked.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-onInsertText(callback: Callback<string>): void--><!--Device-InputMethodController-onInsertText(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes | the callback called when the input method inserts text. Subscribers are expected to process the inserted text and update changes in editor by changeSelection and updateCursor as needed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## onMoveCursor

```TypeScript
onMoveCursor(callback: Callback<Direction>): void
```

Register a callback and when IME sends move cursor, the callback will be invoked.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-onMoveCursor(callback: Callback<Direction>): void--><!--Device-InputMethodController-onMoveCursor(callback: Callback<Direction>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Direction&gt; | Yes | the callback called when the input method moves cursor. The direction of cursor is provided for this callback. Subscribers are expected to move the cursor and update changes in editor by changeSelection and updateCursor. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## onSelectByMovement

```TypeScript
onSelectByMovement(callback: Callback<Movement>): void
```

Register a callback and when IME sends select event witch movement of cursor, the callback will be invoked.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-onSelectByMovement(callback: Callback<Movement>): void--><!--Device-InputMethodController-onSelectByMovement(callback: Callback<Movement>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | Yes | the callback called when the input method selects text by movement. The movement of the cursor is provided for this callback, and subscribers are expected to select corresponding text in callback according to themovement. |

## onSelectByRange

```TypeScript
onSelectByRange(callback: Callback<Range>): void
```

Register a callback and when IME sends select event with range of selection, the callback will be invoked.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-onSelectByRange(callback: Callback<Range>): void--><!--Device-InputMethodController-onSelectByRange(callback: Callback<Range>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | Yes | the callback called when the input method selects text by range. The range of selection is provided for this callback, and subscribers are expected to select corresponding text in callback according to the range. |

## onSendFunctionKey

```TypeScript
onSendFunctionKey(callback: Callback<FunctionKey>): void
```

Register a callback and whenIME sends functionKey, the callback will be invoked.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-onSendFunctionKey(callback: Callback<FunctionKey>): void--><!--Device-InputMethodController-onSendFunctionKey(callback: Callback<FunctionKey>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;FunctionKey&gt; | Yes | the callback called when the input method send function key. The functionKey is provided for this callback. Subscribers are expected to complete the corresponding task based on the value of functionKey. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## onSendKeyboardStatus

```TypeScript
onSendKeyboardStatus(callback: Callback<KeyboardStatus>): void
```

Register a callback and when IME sends keyboard status, the callback will be invoked.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-onSendKeyboardStatus(callback: Callback<KeyboardStatus>): void--><!--Device-InputMethodController-onSendKeyboardStatus(callback: Callback<KeyboardStatus>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[KeyboardStatus](arkts-ime-inputmethod-keyboardstatus-e.md)&gt; | Yes | the callback called when the input method send keyboard's status. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## onSetPreviewText

```TypeScript
onSetPreviewText(callback: SetPreviewTextCallback): void
```

&lt;p&gt;Subscribe 'setPreviewText' event.&lt;/p&gt; &lt;p&gt;To support the preview text feature, developers should subscribe to this event before calling attach.&lt;/p&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-onSetPreviewText(callback: SetPreviewTextCallback): void--><!--Device-InputMethodController-onSetPreviewText(callback: SetPreviewTextCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | Yes | the callback called when the input method setspreview text. |

## on_deleteLeft

```TypeScript
on(type: 'deleteLeft', callback: (length: number) => void): void
```

Register a callback and when IME sends delete left event with length, the callback will be invoked.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-on(type: 'deleteLeft', callback: (length: number) => void): void--><!--Device-InputMethodController-on(type: 'deleteLeft', callback: (length: number) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deleteLeft' | Yes | event type, fixed as 'deleteLeft'. |
| callback | (length: number) =&gt; void | Yes | processes deleteLeft command. The length of delete is provided for this callback. Subscribers are expected to delete specified length of text to the left of the cursor and update changes in editor by changeSelection and updateCursor as needed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## Examples

```TypeScript
inputMethod.getController().on('deleteLeft', (length: number) => {
  console.info(`Succeeded in subscribing deleteLeft, length: ${length}`);
});
```

## on_deleteRight

```TypeScript
on(type: 'deleteRight', callback: (length: number) => void): void
```

Register a callback and when IME sends delete right event with length, the callback will be invoked.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-on(type: 'deleteRight', callback: (length: number) => void): void--><!--Device-InputMethodController-on(type: 'deleteRight', callback: (length: number) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'deleteRight' | Yes | event type, fixed as 'deleteRight'. |
| callback | (length: number) =&gt; void | Yes | processes deleteRight command. The length of delete is provided for this callback. Subscribers are expected to delete specified length of text to the right of the cursor and update changes in editor by changeSelection and updateCursor as needed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## Examples

```TypeScript
inputMethod.getController().on('deleteRight', (length: number) => {
  console.info(`Succeeded in subscribing deleteRight, length: ${length}`);
});
```

## on_finishTextPreview

```TypeScript
on(type: 'finishTextPreview', callback: Callback<void>): void
```

&lt;p&gt;Subscribe 'finishTextPreview' event.&lt;/p&gt; &lt;p&gt;To support the preview text feature, developers should subscribe to this event before calling attach.&lt;/p&gt;

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Deprecated since:** -1

<!--Device-InputMethodController-on(type: 'finishTextPreview', callback: Callback<void>): void--><!--Device-InputMethodController-on(type: 'finishTextPreview', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'finishTextPreview' | Yes | the type of subscribe event. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | the callback of on('finishTextPreview'). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

## Examples

```TypeScript
import { Callback } from '@kit.BasicServicesKit';

let finishTextPreviewCallback1: Callback<void> = (): void => {
  console.info(`FinishTextPreviewCallback1: finishTextPreview event triggered`);
};
let finishTextPreviewCallback2: Callback<void> = (): void => {
  console.info(`FinishTextPreviewCallback2: finishTextPreview event triggered`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('finishTextPreview', finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 subscribed to finishTextPreview`);
inputMethodController.on('finishTextPreview', finishTextPreviewCallback2);
console.info(`FinishTextPreviewCallback2 subscribed to finishTextPreview`);
// Cancel only the callback1 of finishTextPreview.
inputMethodController.off('finishTextPreview', finishTextPreviewCallback1);
console.info(`FinishTextPreviewCallback1 unsubscribed from finishTextPreview`);
// Cancel all callbacks of finishTextPreview.
inputMethodController.off('finishTextPreview');
console.info(`All callbacks unsubscribed from finishTextPreview`);
```

## on_getLeftTextOfCursor

```TypeScript
on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void
```

Register a callback and when input method ability gets left text of cursor, the callback will be invoked.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void--><!--Device-InputMethodController-on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'getLeftTextOfCursor' | Yes | event type, fixed as 'getLeftTextOfCursor'. |
| callback | (length: number) =&gt; string | Yes | processes getLeftTextOfCursor command. The callback must be a synchronization method and will block the input method application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## Examples

```TypeScript
inputMethod.getController().on('getLeftTextOfCursor', (length: number) => {
  console.info(`Succeeded in subscribing getLeftTextOfCursor, length: ${length}`);
  let text: string = "";
  return text;
});
```

## on_getRightTextOfCursor

```TypeScript
on(type: 'getRightTextOfCursor', callback: (length: number) => string): void
```

Register a callback and when input method ability gets right text of cursor, the callback will be invoked.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-on(type: 'getRightTextOfCursor', callback: (length: number) => string): void--><!--Device-InputMethodController-on(type: 'getRightTextOfCursor', callback: (length: number) => string): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'getRightTextOfCursor' | Yes | event type, fixed as 'getRightTextOfCursor'. |
| callback | (length: number) =&gt; string | Yes | processes getRightTextOfCursor command. The callback must be a synchronization method and will block the input method application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## Examples

```TypeScript
inputMethod.getController().on('getRightTextOfCursor', (length: number) => {
  console.info(`Succeeded in subscribing getRightTextOfCursor, length: ${length}`);
  let text: string = "";
  return text;
});
```

## on_getTextIndexAtCursor

```TypeScript
on(type: 'getTextIndexAtCursor', callback: () => number): void
```

Register a callback and when input method ability gets the text index at cursor, the callback will be invoked.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-on(type: 'getTextIndexAtCursor', callback: () => number): void--><!--Device-InputMethodController-on(type: 'getTextIndexAtCursor', callback: () => number): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'getTextIndexAtCursor' | Yes | event type, fixed as 'getTextIndexAtCursor'. |
| callback | () =&gt; number | Yes | processes getTextIndexAtCursor command. The callback must be a synchronization method, and should return the text index at the cursor. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## Examples

```TypeScript
inputMethod.getController().on('getTextIndexAtCursor', () => {
  console.info(`Succeeded in subscribing getTextIndexAtCursor.`);
  let index: number = 0;
  return index;
});
```

## on_handleExtendAction

```TypeScript
on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void
```

Register a callback and when IME sends extend action code, the callback will be invoked.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void--><!--Device-InputMethodController-on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'handleExtendAction' | Yes | event type, fixed as 'handleExtendAction'. |
| callback | (action: ExtendAction) =&gt; void | Yes | processes handleExtendAction command. The action code is provided for this callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## Examples

```TypeScript
inputMethod.getController().on('handleExtendAction', (action: inputMethod.ExtendAction) => {
  console.info(`Succeeded in subscribing handleExtendAction, action: ${action}`);
});
```

## on_insertText

```TypeScript
on(type: 'insertText', callback: (text: string) => void): void
```

Register a callback and when IME sends insert text event, the callback will be invoked.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-on(type: 'insertText', callback: (text: string) => void): void--><!--Device-InputMethodController-on(type: 'insertText', callback: (text: string) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'insertText' | Yes | event type, fixed as 'insertText'. |
| callback | (text: string) =&gt; void | Yes | processes insertText command. The text of insert is provided for this callback. Subscribers are expected to process the inserted text and update changes in editor by changeSelection and updateCursor as needed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## Examples

```TypeScript
function callback1(text: string): void {
  console.info(`Succeeded in getting callback1, data: ${text}`);
}

function callback2(text: string): void {
  console.info(`Succeeded in getting callback2, data: ${text}`);
}

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
// Register a callback.
inputMethodController.on('insertText', callback1);
inputMethodController.on('insertText', callback2);
// Cancel only callback1 of insertText.
inputMethodController.off('insertText', callback1);
// Cancel all callbacks of insertText.
inputMethodController.off('insertText');
```

## on_moveCursor

```TypeScript
on(type: 'moveCursor', callback: (direction: Direction) => void): void
```

Register a callback and when IME sends move cursor, the callback will be invoked.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-on(type: 'moveCursor', callback: (direction: Direction) => void): void--><!--Device-InputMethodController-on(type: 'moveCursor', callback: (direction: Direction) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'moveCursor' | Yes | event type, fixed as 'moveCursor'. |
| callback | (direction: Direction) =&gt; void | Yes | processes moveCursor command. The direction of cursor is provided for this callback. Subscribers are expected to move the cursor and update changes in editor by changeSelection and updateCursor. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## Examples

```TypeScript
inputMethod.getController().on('moveCursor', (direction: inputMethod.Direction) => {
  console.info(`Succeeded in subscribing moveCursor, direction: ${direction}`);
});
```

## on_selectByMovement

```TypeScript
on(type: 'selectByMovement', callback: Callback<Movement>): void
```

Register a callback and when IME sends select event witch movement of cursor, the callback will be invoked.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-on(type: 'selectByMovement', callback: Callback<Movement>): void--><!--Device-InputMethodController-on(type: 'selectByMovement', callback: Callback<Movement>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'selectByMovement' | Yes | event type, fixed as 'selectByMovement'. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | Yes | processes selectByMovement command. The movement of cursor is provided for this callback, and subscribers are expected to select corresponding text in callback according to the movement. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## Examples

```TypeScript
inputMethod.getController().on('selectByMovement', (movement: inputMethod.Movement) => {
  console.info('Succeeded in subscribing selectByMovement: direction: ' + movement.direction);
});
```

## on_selectByRange

```TypeScript
on(type: 'selectByRange', callback: Callback<Range>): void
```

Register a callback and when IME sends select event with range of selection, the callback will be invoked.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-on(type: 'selectByRange', callback: Callback<Range>): void--><!--Device-InputMethodController-on(type: 'selectByRange', callback: Callback<Range>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'selectByRange' | Yes | event type, fixed as 'selectByRange'. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | Yes | processes selectByRange command. The range of selection is provided for this callback, and subscribers are expected to select corresponding text in callback according to the range. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |

## Examples

```TypeScript
inputMethod.getController().on('selectByRange', (range: inputMethod.Range) => {
  console.info(`Succeeded in subscribing selectByRange: start: ${range.start} , end: ${range.end}`);
});
```

## on_sendFunctionKey

```TypeScript
on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void
```

Register a callback and when IME sends functionKey, the callback will be invoked.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void--><!--Device-InputMethodController-on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sendFunctionKey' | Yes | event type, fixed as 'sendFunctionKey'. |
| callback | (functionKey: FunctionKey) =&gt; void | Yes | processes sendFunctionKey command. The functionKey is provided for this callback.Subscribers are expected to complete the corresponding task based on the value of functionKey. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## Examples

```TypeScript
inputMethod.getController().on('sendFunctionKey', (functionKey: inputMethod.FunctionKey) => {
  console.info(`Succeeded in subscribing sendFunctionKey, functionKey.enterKeyType: ${functionKey.enterKeyType}`);
});
```

## on_sendKeyboardStatus

```TypeScript
on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void
```

Register a callback and when IME sends keyboard status, the callback will be invoked.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-InputMethodController-on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void--><!--Device-InputMethodController-on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'sendKeyboardStatus' | Yes | event type, fixed as 'sendKeyboardStatus'. |
| callback | (keyboardStatus: KeyboardStatus) =&gt; void | Yes | processes sendKeyboardStatus command. The keyboardStatus is provided for this callback. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |

## Examples

```TypeScript
inputMethod.getController().on('sendKeyboardStatus', (keyboardStatus: inputMethod.KeyboardStatus) => {
  console.info(`Succeeded in subscribing sendKeyboardStatus, keyboardStatus: ${keyboardStatus}`);
});
```

## on_setPreviewText

```TypeScript
on(type: 'setPreviewText', callback: SetPreviewTextCallback): void
```

&lt;p&gt;Subscribe 'setPreviewText' event.&lt;/p&gt; &lt;p&gt;To support the preview text feature, developers should subscribe to this event before calling attach.&lt;/p&gt;

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Deprecated since:** -1

<!--Device-InputMethodController-on(type: 'setPreviewText', callback: SetPreviewTextCallback): void--><!--Device-InputMethodController-on(type: 'setPreviewText', callback: SetPreviewTextCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'setPreviewText' | Yes | the type of subscribe event. |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | Yes | the callback of on('setPreviewText'). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3.Parameter verification failed. |

## Examples

```TypeScript
let setPreviewTextCallback1: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(`SetPreviewTextCallback1: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

let setPreviewTextCallback2: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
  console.info(`setPreviewTextCallback2: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
};

let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.on('setPreviewText', setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 subscribed to setPreviewText`);
inputMethodController.on('setPreviewText', setPreviewTextCallback2);
console.info(`SetPreviewTextCallback2 subscribed to setPreviewText`);
// Cancel only the callback1 of setPreviewText.
inputMethodController.off('setPreviewText', setPreviewTextCallback1);
console.info(`SetPreviewTextCallback1 unsubscribed from setPreviewText`);
// Cancel all callbacks of setPreviewText.
inputMethodController.off('setPreviewText');
console.info(`All callbacks unsubscribed from setPreviewText`);
```

## recvMessage

```TypeScript
recvMessage(msgHandler?: MessageHandler): void
```

Start receiving message from input method.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-recvMessage(msgHandler?: MessageHandler): void--><!--Device-InputMethodController-recvMessage(msgHandler?: MessageHandler): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msgHandler | MessageHandler | No | optional, the handler of the custom message. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Incorrect parameter types. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let messageHandler: inputMethod.MessageHandler = {
  onTerminated(): void {
    console.info('OnTerminated.');
  },
  onMessage(msgId: string, msgParam?: ArrayBuffer): void {
    console.info('recv message.');
  }
};
let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
inputMethodController.recvMessage(messageHandler);
// Unregister the MessageHandler.
inputMethodController.recvMessage();
```

## sendMessage

```TypeScript
sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>
```

Send message to input method.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>--><!--Device-InputMethodController-sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| msgId | string | Yes | the identifier of the message. Max size is 256B. |
| msgParam | ArrayBuffer | No | the param of the custom message. Max size is 128KB. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Incorrect parameter length. |
| [12800016](../errorcode-inputmethod-framework.md#12800016-input-method-client-not-in-edit-mode) | input method client is not editable. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800015](../errorcode-inputmethod-framework.md#12800015-message-receiver-unable-to-receive-custom-communication-data) | the other side does not accept the request. |
| [12800014](../errorcode-inputmethod-framework.md#12800014-nonfull-access-mode-of-the-input-method-application) | the input method is in basic mode. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let msgId: string = "testMsgId";
let msgParam: ArrayBuffer = new ArrayBuffer(128);
inputMethod.getController().sendMessage(msgId, msgParam).then(() => {
  console.info('Succeeded send message.');
}).catch((err: BusinessError) => {
  console.error(`Failed to send message, code: ${err.code}, message: ${err.message}`);
});
```

## setCallingWindow

```TypeScript
setCallingWindow(windowId: int, callback: AsyncCallback<void>): void
```

Inform the system of the window ID of the application currently bound to the input method. After the correct setting, the window where the client is located can avoid the input method window.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-setCallingWindow(windowId: int, callback: AsyncCallback<void>): void--><!--Device-InputMethodController-setCallingWindow(windowId: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| windowId | int | Yes | the window ID of the application currently bound to the input method. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of setCallingWindow. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let windowId: number = 2000;
inputMethod.getController().setCallingWindow(windowId, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to setCallingWindow, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting callingWindow.');
});
```

## setCallingWindow

```TypeScript
setCallingWindow(windowId: int): Promise<void>
```

Inform the system of the window ID of the application currently bound to the input method. After the correct setting, the window where the client is located can avoid the input method window.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-setCallingWindow(windowId: int): Promise<void>--><!--Device-InputMethodController-setCallingWindow(windowId: int): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| windowId | int | Yes | the window ID of the application currently bound to the input method. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let windowId: number = 2000;
inputMethod.getController().setCallingWindow(windowId).then(() => {
  console.info('Succeeded in setting callingWindow.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setCallingWindow, code: ${err.code}, message: ${err.message}`);
})
```

## showSoftKeyboard

```TypeScript
showSoftKeyboard(callback: AsyncCallback<void>): void
```

Show soft keyboard. This API can be called only by system applications.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

<!--Device-InputMethodController-showSoftKeyboard(callback: AsyncCallback<void>): void--><!--Device-InputMethodController-showSoftKeyboard(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of showSoftKeyboard. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [201](../../errorcode-universal.md#201-permission-denied) | permissions check fails. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showSoftKeyboard((err: BusinessError) => {
  if (!err) {
    console.info('Succeeded in showing softKeyboard.');
  } else {
    console.error(`Failed to show softKeyboard, ${err.code}, message: ${err.message}`);
  }
});
```

## showSoftKeyboard

```TypeScript
showSoftKeyboard(): Promise<void>
```

Show soft keyboard. This API can be called only by system applications.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

<!--Device-InputMethodController-showSoftKeyboard(): Promise<void>--><!--Device-InputMethodController-showSoftKeyboard(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [201](../../errorcode-universal.md#201-permission-denied) | permissions check fails. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showSoftKeyboard().then(() => {
  console.info('Succeeded in showing softKeyboard.');
}).catch((err: BusinessError) => {
  console.error(`Failed to show softKeyboard, code: ${err.code}, message: ${err.message}`);
});
```

## showTextInput

```TypeScript
showTextInput(callback: AsyncCallback<void>): void
```

Show the text input and start typing.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-showTextInput(callback: AsyncCallback<void>): void--><!--Device-InputMethodController-showTextInput(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of showTextInput. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showTextInput((err: BusinessError) => {
  if (err) {
    console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in showing the inputMethod.');
});
```

## showTextInput

```TypeScript
showTextInput(): Promise<void>
```

Show the text input and start typing.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-showTextInput(): Promise<void>--><!--Device-InputMethodController-showTextInput(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().showTextInput().then(() => {
  console.info('Succeeded in showing text input.');
}).catch((err: BusinessError) => {
  console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
});
```

## showTextInput

```TypeScript
showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>
```

Show the text input and start typing.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>--><!--Device-InputMethodController-showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| requestKeyboardReason | RequestKeyboardReason | Yes | requestKeyboardReason of show the keyboard . |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let requestKeyboardReason: inputMethod.RequestKeyboardReason = inputMethod.RequestKeyboardReason.MOUSE;

inputMethod.getController().showTextInput(requestKeyboardReason).then(() => {
  console.info('Succeeded in showing text input.');
}).catch((err: BusinessError) => {
  console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
});
```

## stopInput

```TypeScript
stopInput(callback: AsyncCallback<boolean>): void
```

Stop input

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [stopInputSession](#stopInputSession)

<!--Device-InputMethodController-stopInput(callback: AsyncCallback<boolean>): void--><!--Device-InputMethodController-stopInput(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | the callback of stopInput. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInput((err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to stopInput, code: ${err.code}, message: ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in stopping input.');
  } else {
    console.error('Failed to stopInput.');
  }
});
```

## stopInput

```TypeScript
stopInput(): Promise<boolean>
```

Stop input

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** [stopInputSession](#stopInputSession)

<!--Device-InputMethodController-stopInput(): Promise<boolean>--><!--Device-InputMethodController-stopInput(): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | the promise returned by the function. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInput().then((result: boolean) => {
  if (result) {
    console.info('Succeeded in stopping input.');
  } else {
    console.error('Failed to stopInput.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to stopInput, code: ${err.code}, message: ${err.message}`);
})
```

## stopInputSession

```TypeScript
stopInputSession(callback: AsyncCallback<boolean>): void
```

Stop input session

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-stopInputSession(callback: AsyncCallback<boolean>): void--><!--Device-InputMethodController-stopInputSession(callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes | the callback of stopInputSession. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInputSession((err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to stopInputSession, code: ${err.code}, message: ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in stopping inputSession.');
  } else {
    console.error('Failed to stopInputSession.');
  }
});
```

## stopInputSession

```TypeScript
stopInputSession(): Promise<boolean>
```

Stop input session

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-stopInputSession(): Promise<boolean>--><!--Device-InputMethodController-stopInputSession(): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethod.getController().stopInputSession().then((result: boolean) => {
  if (result) {
    console.info('Succeeded in stopping inputSession.');
  } else {
    console.error('Failed to stopInputSession.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to stopInputSession, code: ${err.code}, message: ${err.message}`);
});
```

## updateAttribute

```TypeScript
updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void
```

Update InputAttribute information of input text.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void--><!--Device-InputMethodController-updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| attribute | [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md) | Yes | the InputAttribute object. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of updateAttribute. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = { textInputType: 0, enterKeyType: 1 };
inputMethod.getController().updateAttribute(inputAttribute, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to updateAttribute, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in updating attribute.');
});
```

## updateAttribute

```TypeScript
updateAttribute(attribute: InputAttribute): Promise<void>
```

Update InputAttribute information of input text.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-updateAttribute(attribute: InputAttribute): Promise<void>--><!--Device-InputMethodController-updateAttribute(attribute: InputAttribute): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| attribute | [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md) | Yes | the InputAttribute object. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let inputAttribute: inputMethod.InputAttribute = { textInputType: 0, enterKeyType: 1 };
inputMethod.getController().updateAttribute(inputAttribute).then(() => {
  console.info('Succeeded in updating attribute.');
}).catch((err: BusinessError) => {
  console.error(`Failed to updateAttribute, code: ${err.code}, message: ${err.message}`);
});
```

## updateCursor

```TypeScript
updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void
```

Update Cursor and notify the input method that the current application cursor has changed.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void--><!--Device-InputMethodController-updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cursorInfo | [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) | Yes | the CursorInfo object. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of updateCursor. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let cursorInfo: inputMethod.CursorInfo = {
  left: 0,
  top: 0,
  width: 600,
  height: 800
};
inputMethod.getController().updateCursor(cursorInfo, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to updateCursor, code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in updating cursorInfo.');
});
```

## updateCursor

```TypeScript
updateCursor(cursorInfo: CursorInfo): Promise<void>
```

Update Cursor and notify the input method that the current application cursor has changed.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-InputMethodController-updateCursor(cursorInfo: CursorInfo): Promise<void>--><!--Device-InputMethodController-updateCursor(cursorInfo: CursorInfo): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cursorInfo | [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) | Yes | the CursorInfo object. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types; 3.Parameter verification failed. |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) | input method client detached. |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let cursorInfo: inputMethod.CursorInfo = {
  left: 0,
  top: 0,
  width: 600,
  height: 800
};
inputMethod.getController().updateCursor(cursorInfo).then(() => {
  console.info('Succeeded in updating cursorInfo.');
}).catch((err: BusinessError) => {
  console.error(`Failed to updateCursor, code: ${err.code}, message: ${err.message}`);
});
```

