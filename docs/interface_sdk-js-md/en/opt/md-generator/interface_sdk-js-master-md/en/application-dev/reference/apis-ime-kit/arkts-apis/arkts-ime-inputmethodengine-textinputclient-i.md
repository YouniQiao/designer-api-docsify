# TextInputClient

In the following API examples, you must first use   
[on('inputStart')](inputMethodEngine.InputMethodEngine.on(type: 'inputStart',callback: (kbController: KeyboardController, textInputClient: TextInputClient) => void): void;)to obtain a **TextInputClient** instance, and then call the APIs using the obtained instance.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient](arkts-ime-inputmethodengine-inputclient-i.md)

<!--Device-inputMethodEngine-interface TextInputClient--><!--Device-inputMethodEngine-interface TextInputClient-End-->

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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient.deleteBackward](arkts-ime-inputmethodengine-inputclient-i.md#deletebackward)(length:

<!--Device-TextInputClient-deleteBackward(length: number, callback: AsyncCallback<boolean>): void--><!--Device-TextInputClient-deleteBackward(length: number, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteBackward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
});
```

## deleteBackward

```TypeScript
deleteBackward(length: number): Promise<boolean>
```

Deletes the fixed-length text after the cursor. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient.deleteBackward](arkts-ime-inputmethodengine-inputclient-i.md#deletebackward)(length:

<!--Device-TextInputClient-deleteBackward(length: number): Promise<boolean>--><!--Device-TextInputClient-deleteBackward(length: number): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteBackward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting backward.');
  } else {
    console.error('Failed to deleteBackward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteBackward. Code is ${err.code}, message is ${err.message}`);
});
```

## deleteForward

```TypeScript
deleteForward(length: number, callback: AsyncCallback<boolean>): void
```

Deletes the fixed-length text before the cursor. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient.deleteForward](arkts-ime-inputmethodengine-inputclient-i.md#deleteforward)(length:

<!--Device-TextInputClient-deleteForward(length: number, callback: AsyncCallback<boolean>): void--><!--Device-TextInputClient-deleteForward(length: number, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteForward(length, (err: BusinessError, result: boolean) => {
  if (err) {
    console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to deleteForward.');
  }
});
```

## deleteForward

```TypeScript
deleteForward(length: number): Promise<boolean>
```

Deletes the fixed-length text before the cursor. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient.deleteForward](arkts-ime-inputmethodengine-inputclient-i.md#deleteforward)(length:

<!--Device-TextInputClient-deleteForward(length: number): Promise<boolean>--><!--Device-TextInputClient-deleteForward(length: number): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.deleteForward(length).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in deleting forward.');
  } else {
    console.error('Failed to delete forward.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to deleteForward. Code is ${err.code}, message is ${err.message}`);
});
```

## getBackward

```TypeScript
getBackward(length: number, callback: AsyncCallback<string>): void
```

Obtains the specific-length text after the cursor. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient.getBackward](arkts-ime-inputmethodengine-inputclient-i.md#getbackward)(length:

<!--Device-TextInputClient-getBackward(length: number, callback: AsyncCallback<string>): void--><!--Device-TextInputClient-getBackward(length: number, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getBackward(length, (err: BusinessError, text: string) => {
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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient.getBackward](arkts-ime-inputmethodengine-inputclient-i.md#getbackward)(length:

<!--Device-TextInputClient-getBackward(length: number): Promise<string>--><!--Device-TextInputClient-getBackward(length: number): Promise<string>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getBackward(length).then((text: string) => {
  console.info(`'Succeeded in getting backward: ${text}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getBackward. Code is ${err.code}, message is ${err.message}`);
});
```

## getEditorAttribute

```TypeScript
getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void
```

Obtains the attribute of the edit box. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient.getEditorAttribute](arkts-ime-inputmethodengine-inputclient-i.md#geteditorattribute)(callback:

<!--Device-TextInputClient-getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void--><!--Device-TextInputClient-getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;EditorAttribute&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';


textInputClient.getEditorAttribute((err: BusinessError,
  editorAttribute: inputMethodEngine.EditorAttribute) => {
  if (err) {
    console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`editorAttribute.inputPattern: ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType: ${editorAttribute.enterKeyType}`);
});
```

## getEditorAttribute

```TypeScript
getEditorAttribute(): Promise<EditorAttribute>
```

Obtains the attribute of the edit box. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient.getEditorAttribute](arkts-ime-inputmethodengine-inputclient-i.md#geteditorattribute)(callback:

<!--Device-TextInputClient-getEditorAttribute(): Promise<EditorAttribute>--><!--Device-TextInputClient-getEditorAttribute(): Promise<EditorAttribute>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;EditorAttribute&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.getEditorAttribute().then((editorAttribute: inputMethodEngine.EditorAttribute) => {
  console.info(`editorAttribute.inputPattern: ${editorAttribute.inputPattern}`);
  console.info(`editorAttribute.enterKeyType: ${editorAttribute.enterKeyType}}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to getEditorAttribute. Code is ${err.code}, message is ${err.message}`);
});
```

## getForward

```TypeScript
getForward(length: number, callback: AsyncCallback<string>): void
```

Obtains the specific-length text before the cursor. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient.getForward](arkts-ime-inputmethodengine-inputclient-i.md#getforward)(length:

<!--Device-TextInputClient-getForward(length: number, callback: AsyncCallback<string>): void--><!--Device-TextInputClient-getForward(length: number, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getForward(length, (err: BusinessError, text: string) => {
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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient.getForward](arkts-ime-inputmethodengine-inputclient-i.md#getforward)(length:

<!--Device-TextInputClient-getForward(length: number): Promise<string>--><!--Device-TextInputClient-getForward(length: number): Promise<string>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;string&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let length: number = 1;
textInputClient.getForward(length).then((text: string) => {
  console.info('Succeeded in getting forward, text: ' + text);
}).catch((err: BusinessError) => {
  console.error(`Failed to getForward. Code is ${err.code}, message is ${err.message}`);
});
```

## insertText

```TypeScript
insertText(text: string, callback: AsyncCallback<boolean>): void
```

Inserts text. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient.insertText](arkts-ime-inputmethodengine-inputclient-i.md#inserttext)(text:

<!--Device-TextInputClient-insertText(text: string, callback: AsyncCallback<boolean>): void--><!--Device-TextInputClient-insertText(text: string, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.insertText('test', (err: BusinessError, result: boolean) => {
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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient.insertText](arkts-ime-inputmethodengine-inputclient-i.md#inserttext)(text:

<!--Device-TextInputClient-insertText(text: string): Promise<boolean>--><!--Device-TextInputClient-insertText(text: string): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

textInputClient.insertText('test').then((result: boolean) => {
  if (result) {
    console.info('Succeeded in inserting text.');
  } else {
    console.error('Failed to insertText.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to insertText. Code is ${err.code}, message is ${err.message}`);
});
```

## sendKeyFunction

```TypeScript
sendKeyFunction(action: number, callback: AsyncCallback<boolean>): void
```

Sends the function key. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient.sendKeyFunction](arkts-ime-inputmethodengine-inputclient-i.md#sendkeyfunction)(action:

<!--Device-TextInputClient-sendKeyFunction(action: number, callback: AsyncCallback<boolean>): void--><!--Device-TextInputClient-sendKeyFunction(action: number, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| action | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
textInputClient.sendKeyFunction(action, (err: BusinessError, result: boolean) => {
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

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [inputMethodEngine.InputClient.sendKeyFunction](arkts-ime-inputmethodengine-inputclient-i.md#sendkeyfunction)(action:

<!--Device-TextInputClient-sendKeyFunction(action: number): Promise<boolean>--><!--Device-TextInputClient-sendKeyFunction(action: number): Promise<boolean>-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| action | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let action: number = 1;
textInputClient.sendKeyFunction(action).then((result: boolean) => {
  if (result) {
    console.info('Succeeded in sending key function.');
  } else {
    console.error('Failed to sendKeyFunction.');
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to sendKeyFunction:. Code is ${err.code}, message is ${err.message}`);
});
```
