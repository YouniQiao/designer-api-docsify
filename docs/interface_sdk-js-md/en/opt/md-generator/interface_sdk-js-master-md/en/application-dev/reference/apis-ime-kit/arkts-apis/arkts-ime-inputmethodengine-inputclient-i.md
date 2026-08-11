# InputClient

You must first use [on('inputStart')](inputMethodEngine.InputMethodAbility. on(type: 'inputStart', callback:(kbController: KeyboardController, inputClient: InputClient) => void): void;) to obtain a   
**InputClient** instance, and then use this instance to call the following APIs.

**Since:** 9

<!--Device-inputMethodEngine-interface InputClient--><!--Device-inputMethodEngine-interface InputClient-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## deleteBackward

```TypeScript
deleteBackward(length: number, callback: AsyncCallback<boolean>): void
```

Deletes the fixed-length text after the cursor. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputClient-deleteBackward(length: int, callback: AsyncCallback<boolean>): void--><!--Device-InputClient-deleteBackward(length: int, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteBackward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error(`Failed to deleteBackward.`);
  }
});
```

## deleteBackward

```TypeScript
deleteBackward(length: number): Promise<boolean>
```

Deletes the fixed-length text after the cursor. This API uses a promise to return the result.

**Since:** 9

<!--Device-InputClient-deleteBackward(length: int): Promise<boolean>--><!--Device-InputClient-deleteBackward(length: int): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteBackward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
});
```

## deleteBackwardSync

```TypeScript
deleteBackwardSync(length: number): void
```

Deletes the fixed-length text after the cursor.

**Since:** 10

<!--Device-InputClient-deleteBackwardSync(length: int): void--><!--Device-InputClient-deleteBackwardSync(length: int): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |

## Examples

```TypeScript
let length: number = 1;
inputClient.deleteBackwardSync(length);
```

## deleteForward

```TypeScript
deleteForward(length: number, callback: AsyncCallback<boolean>): void
```

Deletes the fixed-length text before the cursor. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputClient-deleteForward(length: int, callback: AsyncCallback<boolean>): void--><!--Device-InputClient-deleteForward(length: int, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteForward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error(`Failed to deleteForward.`);
  }
});
```

## deleteForward

```TypeScript
deleteForward(length: number): Promise<boolean>
```

Deletes the fixed-length text before the cursor. This API uses a promise to return the result.

**Since:** 9

<!--Device-InputClient-deleteForward(length: int): Promise<boolean>--><!--Device-InputClient-deleteForward(length: int): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.deleteForward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to delete Forward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
});
```

## deleteForwardSync

```TypeScript
deleteForwardSync(length: number): void
```

Deletes the fixed-length text before the cursor.

**Since:** 10

<!--Device-InputClient-deleteForwardSync(length: int): void--><!--Device-InputClient-deleteForwardSync(length: int): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |

## Examples

```TypeScript
let length: number = 1;
inputClient.deleteForwardSync(length);
```

## finishTextPreview

```TypeScript
finishTextPreview(): Promise<void>
```

Finishes the text preview. This API uses a promise to return the result.

> **NOTE：**
> 
> If there is preview text in the current text box, calling this API will display the preview text on the screen.

**Since:** 12

<!--Device-InputClient-finishTextPreview(): Promise<void>--><!--Device-InputClient-finishTextPreview(): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800011](../errorcode-inputmethod-framework.md#12800011-text-preview-not-supported) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.finishTextPreview().then(() => {
  console.info('Succeeded in finishing text preview.');
}).catch((err: BusinessError) => {
  console.error(`Failed to finishTextPreview. Code is ${err.code}, message is ${err.message}`);
});
```

## finishTextPreviewSync

```TypeScript
finishTextPreviewSync(): void
```

Finishes the text preview.

> **NOTE：**
> 
> If there is preview text in the current text box, calling this API will display the preview text on the screen.

**Since:** 12

<!--Device-InputClient-finishTextPreviewSync(): void--><!--Device-InputClient-finishTextPreviewSync(): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800011](../errorcode-inputmethod-framework.md#12800011-text-preview-not-supported) |

## Examples

```TypeScript
inputClient.finishTextPreviewSync();
```

## getAttachOptions

```TypeScript
getAttachOptions(): AttachOptions
```

Obtains the additional options for binding an input method.

**Since:** 19

<!--Device-InputClient-getAttachOptions(): AttachOptions--><!--Device-InputClient-getAttachOptions(): AttachOptions-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AttachOptions](arkts-ime-inputmethod-attachoptions-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## Examples

```TypeScript
let attachOptions: inputMethodEngine.AttachOptions = inputClient.getAttachOptions();
console.info(`Succeeded in getting AttachOptions, AttachOptions is ${attachOptions}`);
```

## getBackward

```TypeScript
getBackward(length: number, callback: AsyncCallback<string>): void
```

Obtains the specific-length text after the cursor. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputClient-getBackward(length: int, callback: AsyncCallback<string>): void--><!--Device-InputClient-getBackward(length: int, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getBackward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting backward, text: ' + text);
});
```

## getBackward

```TypeScript
getBackward(length: number): Promise<string>
```

Obtains the specific-length text after the cursor. This API uses a promise to return the result.

**Since:** 9

<!--Device-InputClient-getBackward(length: int): Promise<string>--><!--Device-InputClient-getBackward(length: int): Promise<string>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getBackward(length).then((text: string) => {
  console.info('Succeeded in getting backward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
});
```

## getBackwardSync

```TypeScript
getBackwardSync(length: number): string
```

Obtains the specific-length text after the cursor.

**Since:** 10

<!--Device-InputClient-getBackwardSync(length: int): string--><!--Device-InputClient-getBackwardSync(length: int): string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## Examples

```TypeScript
let length: number = 1;
let text: string = inputClient.getBackwardSync(length);
console.info(`Succeeded in getting backward, text: ${text}`);
```

## getCallingWindowInfo

```TypeScript
getCallingWindowInfo(): Promise<WindowInfo>
```

Obtains information about the application window, in which the input box that starts an input method is located. This API uses a promise to return the result.

> **NOTE：**
> 
> This API applies only to the input method applications that use [Panel](arkts-ime-inputmethodengine-panel-i.md) as the
> soft keyboard window.

**Since:** 12

<!--Device-InputClient-getCallingWindowInfo(): Promise<WindowInfo>--><!--Device-InputClient-getCallingWindowInfo(): Promise<WindowInfo>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;WindowInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |
| [12800012](../errorcode-inputmethod-framework.md#12800012-soft-keyboard-panel-not-created) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getCallingWindowInfo().then((windowInfo: inputMethodEngine.WindowInfo) => {
  console.info(`windowInfo.rect: ${windowInfo.rect.left}, ${windowInfo.rect.top}, ${windowInfo.rect.width}, ${windowInfo.rect.height}`);
  console.info(`windowInfo.status: ${windowInfo.status}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getCallingWindowInfo. Code is ${err.code}, message is ${err.message}`);
});
```

## getEditorAttribute

```TypeScript
getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void
```

Obtains the attribute of the edit box. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputClient-getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void--><!--Device-InputClient-getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;EditorAttribute&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getEditorAttribute((err: BusinessError, editorAttribute: inputMethodEngine.EditorAttribute) => {
  if (err) {
    console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
});
```

## getEditorAttribute

```TypeScript
getEditorAttribute(): Promise<EditorAttribute>
```

Obtains the attribute of the edit box. This API uses a promise to return the result.

**Since:** 9

<!--Device-InputClient-getEditorAttribute(): Promise<EditorAttribute>--><!--Device-InputClient-getEditorAttribute(): Promise<EditorAttribute>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;EditorAttribute&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getEditorAttribute().then((editorAttribute: inputMethodEngine.EditorAttribute) => {
  console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
});
```

## getEditorAttributeSync

```TypeScript
getEditorAttributeSync(): EditorAttribute
```

Obtains the attribute of the edit box.

**Since:** 10

<!--Device-InputClient-getEditorAttributeSync(): EditorAttribute--><!--Device-InputClient-getEditorAttributeSync(): EditorAttribute-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## Examples

```TypeScript
let editorAttribute: inputMethodEngine.EditorAttribute = inputClient.getEditorAttributeSync();
console.info(`editorAttribute.inputPattern:  ${editorAttribute.inputPattern}`);
console.info(`editorAttribute.enterKeyType:  ${editorAttribute.enterKeyType}`);
```

## getForward

```TypeScript
getForward(length: number, callback: AsyncCallback<string>): void
```

Obtains the specific-length text before the cursor. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputClient-getForward(length: int, callback: AsyncCallback<string>): void--><!--Device-InputClient-getForward(length: int, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getForward(length, (err: BusinessError, text: string) => {
  if (err) {
    console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getting forward, text: ' + text);
});
```

## getForward

```TypeScript
getForward(length: number): Promise<string>
```

Obtains the specific-length text before the cursor. This API uses a promise to return the result.

**Since:** 9

<!--Device-InputClient-getForward(length: int): Promise<string>--><!--Device-InputClient-getForward(length: int): Promise<string>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
inputClient.getForward(length).then((text: string) => {
  console.info('Succeeded in getting forward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
});
```

## getForwardSync

```TypeScript
getForwardSync(length: number): string
```

Obtains the specific-length text before the cursor.

**Since:** 10

<!--Device-InputClient-getForwardSync(length: int): string--><!--Device-InputClient-getForwardSync(length: int): string-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## Examples

```TypeScript
let length: number = 1;
let text: string = inputClient.getForwardSync(length);
console.info(`Succeeded in getting forward, text: ${text}`);
```

## getTextIndexAtCursor

```TypeScript
getTextIndexAtCursor(callback: AsyncCallback<number>): void
```

Obtains the index of the text where the cursor is located. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-InputClient-getTextIndexAtCursor(callback: AsyncCallback<int>): void--><!--Device-InputClient-getTextIndexAtCursor(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getTextIndexAtCursor((err: BusinessError, index: number) => {
  if (err) {
    console.error(`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in getTextIndexAtCursor: ' + index);
});
```

## getTextIndexAtCursor

```TypeScript
getTextIndexAtCursor(): Promise<number>
```

Obtains the index of the text where the cursor is located. This API uses a promise to return the result.

**Since:** 10

<!--Device-InputClient-getTextIndexAtCursor(): Promise<int>--><!--Device-InputClient-getTextIndexAtCursor(): Promise<int>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.getTextIndexAtCursor().then((index: number) => {
  console.info('Succeeded in getTextIndexAtCursor: ' + index);
}).catch((err: BusinessError) => {
  console.error(`Failed to getTextIndexAtCursor. Code is ${err.code}, message is ${err.message}`);
});
```

## getTextIndexAtCursorSync

```TypeScript
getTextIndexAtCursorSync(): number
```

Obtains the index of the text where the cursor is located.

**Since:** 10

<!--Device-InputClient-getTextIndexAtCursorSync(): int--><!--Device-InputClient-getTextIndexAtCursorSync(): int-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## Examples

```TypeScript
let index: number = inputClient.getTextIndexAtCursorSync();
console.info(`Succeeded in getTextIndexAtCursorSync, index: ${index}`);
```

## insertText

```TypeScript
insertText(text: string, callback: AsyncCallback<boolean>): void
```

Inserts text. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputClient-insertText(text: string, callback: AsyncCallback<boolean>): void--><!--Device-InputClient-insertText(text: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';


inputClient.insertText('test', (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
});
```

## insertText

```TypeScript
insertText(text: string): Promise<boolean>
```

Inserts text. This API uses a promise to return the result.

**Since:** 9

<!--Device-InputClient-insertText(text: string): Promise<boolean>--><!--Device-InputClient-insertText(text: string): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.insertText('test').then((result: boolean) => {
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
});
```

## insertTextSync

```TypeScript
insertTextSync(text: string): void
```

Inserts text.

**Since:** 10

<!--Device-InputClient-insertTextSync(text: string): void--><!--Device-InputClient-insertTextSync(text: string): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |

## Examples

```TypeScript
inputClient.insertTextSync('test');
```

## moveCursor

```TypeScript
moveCursor(direction: number, callback: AsyncCallback<void>): void
```

Moves the cursor. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputClient-moveCursor(direction: int, callback: AsyncCallback<void>): void--><!--Device-InputClient-moveCursor(direction: int, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| direction | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.moveCursor(inputMethodEngine.Direction.CURSOR_UP, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to moveCursor. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in moving cursor.');
});
```

## moveCursor

```TypeScript
moveCursor(direction: number): Promise<void>
```

Moves the cursor. This API uses a promise to return the result.

**Since:** 9

<!--Device-InputClient-moveCursor(direction: int): Promise<void>--><!--Device-InputClient-moveCursor(direction: int): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| direction | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.moveCursor(inputMethodEngine.Direction.CURSOR_UP).then(() => {
  console.info('Succeeded in moving cursor.');
}).catch((err: BusinessError) => {
  console.error(`Failed to moveCursor. Code is ${err.code}, message is ${err.message}`);
});
```

## moveCursorSync

```TypeScript
moveCursorSync(direction: number): void
```

Moves the cursor.

**Since:** 10

<!--Device-InputClient-moveCursorSync(direction: int): void--><!--Device-InputClient-moveCursorSync(direction: int): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| direction | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
inputClient.moveCursorSync(inputMethodEngine.Direction.CURSOR_UP);
```

## off('attachOptionsDidChange')

```TypeScript
off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void
```

Unsubscribes from the event indicating that additional options for binding an input method are changed. This API uses an asynchronous callback to return the result.

**Since:** 19

<!--Device-InputClient-off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void--><!--Device-InputClient-off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'attachOptionsDidChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachOptions&gt; | No |

## Examples

```TypeScript
let attachOptionsDidChangeCallback: (attachOptions: inputMethodEngine.AttachOptions) => void =
  (attachOptions: inputMethodEngine.AttachOptions) => {
    console.info(`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered`);
  };

inputClient.on('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange`);
inputClient.off('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChange unsubscribed from attachOptionsDidChange`);
```

## on('attachOptionsDidChange')

```TypeScript
on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void
```

Subscribes to the event indicating that the additional options for binding an input method are changed. This API uses an asynchronous callback to return the result.

**Since:** 19

<!--Device-InputClient-on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void--><!--Device-InputClient-on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'attachOptionsDidChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachOptions&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## Examples

```TypeScript
let attachOptionsDidChangeCallback: (attachOptions: inputMethodEngine.AttachOptions) => void =
  (attachOptions: inputMethodEngine.AttachOptions) => {
    console.info(`AttachOptionsDidChangeCallback1: attachOptionsDidChange event triggered`);
  };

inputClient.on('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChangeCallback subscribed to attachOptionsDidChange`);
inputClient.off('attachOptionsDidChange', attachOptionsDidChangeCallback);
console.info(`attachOptionsDidChange unsubscribed from attachOptionsDidChange`);
```

## recvMessage

```TypeScript
recvMessage(msgHandler?: MessageHandler): void
```

Registers or unregisters MessageHandler.

> **NOTE：**
> 
> The [MessageHandler](arkts-ime-inputmethodengine-messagehandler-i.md) object is globally unique. After multiple
> registrations, only the last registered object is valid and retained, and the
> [onTerminated](arkts-ime-inputmethodengine-messagehandler-i.md#onterminated) callback of the penultimate registered
> object is triggered.
> 
> If no parameter is set, unregister [MessageHandler](arkts-ime-inputmethodengine-messagehandler-i.md). Its
> [onTerminated](arkts-ime-inputmethodengine-messagehandler-i.md#onterminated) callback will be triggered.

**Since:** 15

<!--Device-InputClient-recvMessage(msgHandler?: MessageHandler): void--><!--Device-InputClient-recvMessage(msgHandler?: MessageHandler): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| msgHandler | [MessageHandler](arkts-ime-inputmethod-messagehandler-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
inputMethodEngine.getInputMethodAbility()
  .on('inputStart',
    (kbController: inputMethodEngine.KeyboardController, client: inputMethodEngine.InputClient) => {
      let keyboardController: inputMethodEngine.KeyboardController = kbController;
      let inputClient: inputMethodEngine.InputClient = client;
      let messageHandler: inputMethodEngine.MessageHandler = {
        onTerminated(): void {
          console.info('OnTerminated.');
        },
        onMessage(msgId: string, msgParam?: ArrayBuffer): void {
          console.info('recv message.');
        }
      }
      inputClient.recvMessage(messageHandler);
    });
```

## selectByMovement

```TypeScript
selectByMovement(movement: Movement, callback: AsyncCallback<void>): void
```

Selects text based on the cursor movement direction. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-InputClient-selectByMovement(movement: Movement, callback: AsyncCallback<void>): void--><!--Device-InputClient-selectByMovement(movement: Movement, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| movement | [Movement](arkts-ime-inputmethod-movement-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovement(movement, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to selectByMovement. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in selecting by movement.');
});
```

## selectByMovement

```TypeScript
selectByMovement(movement: Movement): Promise<void>
```

Selects text based on the cursor movement direction. This API uses a promise to return the result.

**Since:** 10

<!--Device-InputClient-selectByMovement(movement: Movement): Promise<void>--><!--Device-InputClient-selectByMovement(movement: Movement): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| movement | [Movement](arkts-ime-inputmethod-movement-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovement(movement).then(() => {
  console.info('Succeeded in selecting by movement.');
}).catch((err: BusinessError) => {
  console.error(`Failed to selectByMovement. Code is ${err.code}, message is ${err.message}`);
});
```

## selectByMovementSync

```TypeScript
selectByMovementSync(movement: Movement): void
```

Selects text based on the cursor movement direction.

**Since:** 10

<!--Device-InputClient-selectByMovementSync(movement: Movement): void--><!--Device-InputClient-selectByMovementSync(movement: Movement): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| movement | [Movement](arkts-ime-inputmethod-movement-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
let movement: inputMethodEngine.Movement = { direction: 1 };
inputClient.selectByMovementSync(movement);
```

## selectByRange

```TypeScript
selectByRange(range: Range, callback: AsyncCallback<void>): void
```

Selects text based on the specified range. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-InputClient-selectByRange(range: Range, callback: AsyncCallback<void>): void--><!--Device-InputClient-selectByRange(range: Range, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRange(range, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to selectByRange. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in selecting by range.');
});
```

## selectByRange

```TypeScript
selectByRange(range: Range): Promise<void>
```

Selects text based on the specified range. This API uses a promise to return the result.

**Since:** 10

<!--Device-InputClient-selectByRange(range: Range): Promise<void>--><!--Device-InputClient-selectByRange(range: Range): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRange(range).then(() => {
  console.info('Succeeded in selecting by range.');
}).catch((err: BusinessError) => {
  console.error(`Failed to selectByRange. Code is ${err.code}, message is ${err.message}`);
});
```

## selectByRangeSync

```TypeScript
selectByRangeSync(range: Range): void
```

Selects text based on the specified range.

**Since:** 10

<!--Device-InputClient-selectByRangeSync(range: Range): void--><!--Device-InputClient-selectByRangeSync(range: Range): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.selectByRangeSync(range);
```

## sendExtendAction

```TypeScript
sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void
```

Sends an extended edit action. This API uses an asynchronous callback to return the result.

> **NOTE：**
> 
> The input method applications call this API to send extended edit actions to the edit box. The edit box listens
> for the corresponding event using
> [on('handleExtendAction')](@ohos.inputMethod:inputMethod.InputMethodController.on(type: 'handleExtendAction',callback: (action: ExtendAction) => void): void) for further processing.
> 
> When the edit box responds to the **PASTE** command of [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md),
> the edit box application needs to apply for the
> [ohos.permission.READ_PASTEBOARD](../../../security/AccessToken/restricted-permissions.md#ohospermissionread_pasteboard)
> permission.

**Since:** 10

<!--Device-InputClient-sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void--><!--Device-InputClient-sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| action | [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.sendExtendAction(inputMethodEngine.ExtendAction.COPY, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to sendExtendAction. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info('Succeeded in sending extend action.');
});
```

## sendExtendAction

```TypeScript
sendExtendAction(action: ExtendAction): Promise<void>
```

Sends an extended edit action. This API uses a promise to return the result.

> **NOTE：**
> 
> The input method applications call this API to send extended edit actions to the edit box. The edit box listens
> for the corresponding event using
> [on('handleExtendAction')](@ohos.inputMethod:inputMethod.InputMethodController.on(type: 'handleExtendAction',callback: (action: ExtendAction) => void): void;) for
> further processing.
> 
> When the edit box responds to the **PASTE** command of [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md),
> the edit box application needs to apply for the
> [ohos.permission.READ_PASTEBOARD](../../../security/AccessToken/restricted-permissions.md#ohospermissionread_pasteboard)
> permission.

**Since:** 10

<!--Device-InputClient-sendExtendAction(action: ExtendAction): Promise<void>--><!--Device-InputClient-sendExtendAction(action: ExtendAction): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| action | [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputClient.sendExtendAction(inputMethodEngine.ExtendAction.COPY).then(() => {
  console.info('Succeeded in sending extend action.');
}).catch((err: BusinessError) => {
  console.error(`Failed to sendExtendAction. Code is ${err.code}, message is ${err.message}`);
});
```

## sendKeyFunction

```TypeScript
sendKeyFunction(action: number, callback: AsyncCallback<boolean>): void
```

Sends the function key. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-InputClient-sendKeyFunction(action: int, callback: AsyncCallback<boolean>): void--><!--Device-InputClient-sendKeyFunction(action: int, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| action | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;

inputClient.sendKeyFunction(action, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
});
```

## sendKeyFunction

```TypeScript
sendKeyFunction(action: number): Promise<boolean>
```

Sends the function key. This API uses a promise to return the result.

**Since:** 9

<!--Device-InputClient-sendKeyFunction(action: int): Promise<boolean>--><!--Device-InputClient-sendKeyFunction(action: int): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| action | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
inputClient.sendKeyFunction(action).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to sendKeyFunction. Code is ${err.code}, message is ${err.message}`);
});
```

## sendMessage

```TypeScript
sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>
```

Sends the custom communication to the edit box application attached to the input method application. This API uses a promise to return the result.

> **NOTE：**
> 
> This API can be called only when the edit box is attached to the input method and enter the edit mode, and the
> input method application is in full experience mode.
> 
> The maximum length of **msgId** is 256 B, and the maximum length of **msgParam** is 128 KB.

**Since:** 15

<!--Device-InputClient-sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>--><!--Device-InputClient-sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| msgId | string | Yes |
| msgParam | ArrayBuffer | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800016](../errorcode-inputmethod-framework.md#12800016-input-method-client-not-in-edit-mode) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |
| [12800015](../errorcode-inputmethod-framework.md#12800015-message-receiver-unable-to-receive-custom-communication-data) |
| [12800014](../errorcode-inputmethod-framework.md#12800014-nonfull-access-mode-of-the-input-method-application) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let msgId: string = "testMsgId";
let msgParam: ArrayBuffer = new ArrayBuffer(128);
inputClient.sendMessage(msgId, msgParam).then(() => {
  console.info('Succeeded send message.');
}).catch((err: BusinessError) => {
  console.error(`Failed to send message. Code is ${err.code}, message is ${err.message}`);
});
```

## sendPrivateCommand

```TypeScript
sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>
```

Sends private data to the system component that needs to communicate with the input method application. This API uses a promise to return the result.

> **NOTE：**
> 
> - The private data channel allows communication between the system preset input method application and specific
> system components (such as a text box or a home screen application). It is usually used to implement custom
> input on a specific device.
> 
> - The total size of the private data is 32 KB, and the maximum number of private data records is 5.

**Since:** 12

<!--Device-InputClient-sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>--><!--Device-InputClient-sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| commandData | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, CommandDataType&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800010](../errorcode-inputmethod-framework.md#12800010-not-preconfigured-default-input-method) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

inputMethodEngine.getInputMethodAbility().on('inputStart', (kbController, textInputClient) => {
  let record: Record<string, inputMethodEngine.CommandDataType> = {
    "valueString1": "abcdefg",
    "valueString2": true,
    "valueString3": 500,
  }
  textInputClient.sendPrivateCommand(record).then(() => {
  }).catch((err: BusinessError) => {
    if (err !== undefined) {
      console.error(`sendPrivateCommand catch error: ${err.code} ${err.message}`);
    }
  });
})
```

## setPreviewText

```TypeScript
setPreviewText(text: string, range: Range): Promise<void>
```

Sets the preview text. This API uses a promise to return the result.

**Since:** 12

<!--Device-InputClient-setPreviewText(text: string, range: Range): Promise<void>--><!--Device-InputClient-setPreviewText(text: string, range: Range): Promise<void>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800011](../errorcode-inputmethod-framework.md#12800011-text-preview-not-supported) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.setPreviewText('test', range).then(() => {
  console.info('Succeeded in setting preview text.');
}).catch((err: BusinessError) => {
  console.error(`Failed to setPreviewText. Code is ${err.code}, message is ${err.message}`);
});
```

## setPreviewTextSync

```TypeScript
setPreviewTextSync(text: string, range: Range): void
```

Sets the preview text.

**Since:** 12

<!--Device-InputClient-setPreviewTextSync(text: string, range: Range): void--><!--Device-InputClient-setPreviewTextSync(text: string, range: Range): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| range | [Range](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [12800011](../errorcode-inputmethod-framework.md#12800011-text-preview-not-supported) |

## Examples

```TypeScript
let range: inputMethodEngine.Range = { start: 0, end: 1 };
inputClient.setPreviewTextSync('test', range);
```
