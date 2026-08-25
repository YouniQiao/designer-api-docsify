# InputClient

You must first use on('inputStart') to obtain a **InputClient** instance, and then use this instance to call the following APIs.

**Since:** 9

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

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## deleteBackward

```TypeScript
deleteBackward(length: number): Promise<boolean>
```

Deletes the fixed-length text after the cursor. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## deleteBackwardSync

```TypeScript
deleteBackwardSync(length: number): void
```

Deletes the fixed-length text after the cursor.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## deleteForward

```TypeScript
deleteForward(length: number, callback: AsyncCallback<boolean>): void
```

Deletes the fixed-length text before the cursor. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## deleteForward

```TypeScript
deleteForward(length: number): Promise<boolean>
```

Deletes the fixed-length text before the cursor. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## deleteForwardSync

```TypeScript
deleteForwardSync(length: number): void
```

Deletes the fixed-length text before the cursor.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## finishTextPreview

```TypeScript
finishTextPreview(): Promise<void>
```

Finishes the text preview. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> If there is preview text in the current text box, calling this API will display the preview text on the screen.

**Since:** 12

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800011](../errorcode-inputmethod-framework.md#12800011-text-preview-not-supported) |

## finishTextPreviewSync

```TypeScript
finishTextPreviewSync(): void
```

Finishes the text preview.   
> **NOTE：**
   
> 
   
> If there is preview text in the current text box, calling this API will display the preview text on the screen.

**Since:** 12

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800011](../errorcode-inputmethod-framework.md#12800011-text-preview-not-supported) |

## getAttachOptions

```TypeScript
getAttachOptions(): AttachOptions
```

Obtains the additional options for binding an input method.

**Since:** 19

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AttachOptions](arkts-ime-inputmethod-attachoptions-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## getBackward

```TypeScript
getBackward(length: number, callback: AsyncCallback<string>): void
```

Obtains the specific-length text after the cursor. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## getBackward

```TypeScript
getBackward(length: number): Promise<string>
```

Obtains the specific-length text after the cursor. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## getBackwardSync

```TypeScript
getBackwardSync(length: number): string
```

Obtains the specific-length text after the cursor.

**Since:** 10

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## getCallingWindowInfo

```TypeScript
getCallingWindowInfo(): Promise<WindowInfo>
```

Obtains information about the application window, in which the input box that starts an input method is located. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> This API applies only to the input method applications that use [Panel](arkts-ime-inputmethodengine-panel-i.md) as the soft keyboard window.

**Since:** 12

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;WindowInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800012](../errorcode-inputmethod-framework.md#12800012-soft-keyboard-panel-not-created) |
| [12800013](../errorcode-inputmethod-framework.md#12800013-window-manager-service-error) |

## getEditorAttribute

```TypeScript
getEditorAttribute(callback: AsyncCallback<EditorAttribute>): void
```

Obtains the attribute of the edit box. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## getEditorAttribute

```TypeScript
getEditorAttribute(): Promise<EditorAttribute>
```

Obtains the attribute of the edit box. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## getEditorAttributeSync

```TypeScript
getEditorAttributeSync(): EditorAttribute
```

Obtains the attribute of the edit box.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## getForward

```TypeScript
getForward(length: number, callback: AsyncCallback<string>): void
```

Obtains the specific-length text before the cursor. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## getForward

```TypeScript
getForward(length: number): Promise<string>
```

Obtains the specific-length text before the cursor. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| length | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## getForwardSync

```TypeScript
getForwardSync(length: number): string
```

Obtains the specific-length text before the cursor.

**Since:** 10

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
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## getTextIndexAtCursor

```TypeScript
getTextIndexAtCursor(callback: AsyncCallback<number>): void
```

Obtains the index of the text where the cursor is located. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## getTextIndexAtCursor

```TypeScript
getTextIndexAtCursor(): Promise<number>
```

Obtains the index of the text where the cursor is located. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## getTextIndexAtCursorSync

```TypeScript
getTextIndexAtCursorSync(): number
```

Obtains the index of the text where the cursor is located.

**Since:** 10

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

## insertText

```TypeScript
insertText(text: string, callback: AsyncCallback<boolean>): void
```

Inserts text. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## insertText

```TypeScript
insertText(text: string): Promise<boolean>
```

Inserts text. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## insertTextSync

```TypeScript
insertTextSync(text: string): void
```

Inserts text.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800002](../errorcode-inputmethod-framework.md#12800002-input-method-engine-error) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## moveCursor

```TypeScript
moveCursor(direction: number, callback: AsyncCallback<void>): void
```

Moves the cursor. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| direction | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## moveCursor

```TypeScript
moveCursor(direction: number): Promise<void>
```

Moves the cursor. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| direction | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## moveCursorSync

```TypeScript
moveCursorSync(direction: number): void
```

Moves the cursor.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| direction | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## off('attachOptionsDidChange')

```TypeScript
off(type: 'attachOptionsDidChange', callback?: Callback<AttachOptions>): void
```

Unsubscribes from the event indicating that additional options for binding an input method are changed. This API uses an asynchronous callback to return the result.

**Since:** 19

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'attachOptionsDidChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachOptions&gt; | No |

## on('attachOptionsDidChange')

```TypeScript
on(type: 'attachOptionsDidChange', callback: Callback<AttachOptions>): void
```

Subscribes to the event indicating that the additional options for binding an input method are changed. This API uses an asynchronous callback to return the result.

**Since:** 19

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'attachOptionsDidChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AttachOptions&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |

## recvMessage

```TypeScript
recvMessage(msgHandler?: MessageHandler): void
```

Registers or unregisters MessageHandler.   
> **NOTE：**
   
> 
   
> The [MessageHandler](arkts-ime-inputmethodengine-messagehandler-i.md) object is globally unique. After multiple registrations, only the last registered object is valid and retained, and the [onTerminated](arkts-ime-inputmethodengine-messagehandler-i.md#onterminated) callback of the penultimate registered object is triggered.
   
> 
   
> If no parameter is set, unregister [MessageHandler](arkts-ime-inputmethodengine-messagehandler-i.md). Its [onTerminated](arkts-ime-inputmethodengine-messagehandler-i.md#onterminated) callback will be triggered.

**Since:** 15

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| msgHandler | [MessageHandler](arkts-ime-inputmethod-messagehandler-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## selectByMovement

```TypeScript
selectByMovement(movement: Movement, callback: AsyncCallback<void>): void
```

Selects text based on the cursor movement direction. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| movement | [Movement](arkts-ime-inputmethod-movement-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## selectByMovement

```TypeScript
selectByMovement(movement: Movement): Promise<void>
```

Selects text based on the cursor movement direction. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| movement | [Movement](arkts-ime-inputmethod-movement-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## selectByMovementSync

```TypeScript
selectByMovementSync(movement: Movement): void
```

Selects text based on the cursor movement direction.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| movement | [Movement](arkts-ime-inputmethod-movement-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## selectByRange

```TypeScript
selectByRange(range: Range, callback: AsyncCallback<void>): void
```

Selects text based on the specified range. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## selectByRange

```TypeScript
selectByRange(range: Range): Promise<void>
```

Selects text based on the specified range. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## selectByRangeSync

```TypeScript
selectByRangeSync(range: Range): void
```

Selects text based on the specified range.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## sendExtendAction

```TypeScript
sendExtendAction(action: ExtendAction, callback: AsyncCallback<void>): void
```

Sends an extended edit action. This API uses an asynchronous callback to return the result.   
> **NOTE：**
   
> 
   
> The input method applications call this API to send extended edit actions to the edit box. The edit box listens for the corresponding event using on('handleExtendAction') for further processing.
   
> 
   
> When the edit box responds to the **PASTE** command of [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md), the edit box application needs to apply for the [ohos.permission.READ_PASTEBOARD](../../../security/AccessToken/restricted-permissions.md#ohospermissionread_pasteboard) permission.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| action | [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## sendExtendAction

```TypeScript
sendExtendAction(action: ExtendAction): Promise<void>
```

Sends an extended edit action. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> The input method applications call this API to send extended edit actions to the edit box. The edit box listens for the corresponding event using [on('handleExtendAction')] on for further processing.
   
> 
   
> When the edit box responds to the **PASTE** command of [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md), the edit box application needs to apply for the [ohos.permission.READ_PASTEBOARD](../../../security/AccessToken/restricted-permissions.md#ohospermissionread_pasteboard) permission.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| action | [ExtendAction](arkts-ime-inputmethodengine-extendaction-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800006](../errorcode-inputmethod-framework.md#12800006-input-method-controller-error) |

## sendKeyFunction

```TypeScript
sendKeyFunction(action: number, callback: AsyncCallback<boolean>): void
```

Sends the function key. This API uses an asynchronous callback to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| action | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## sendKeyFunction

```TypeScript
sendKeyFunction(action: number): Promise<boolean>
```

Sends the function key. This API uses a promise to return the result.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| action | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |

## sendMessage

```TypeScript
sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>
```

Sends the custom communication to the edit box application attached to the input method application. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> This API can be called only when the edit box is attached to the input method and enter the edit mode, and the input method application is in full experience mode.
   
> 
   
> The maximum length of **msgId** is 256 B, and the maximum length of **msgParam** is 128 KB.

**Since:** 15

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [msgId](../../apis-network-kit/arkts-apis/arkts-network-eap-eapdata-i.md) | string | Yes |
| msgParam | ArrayBuffer | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |
| [12800014](../errorcode-inputmethod-framework.md#12800014-non-full-access-mode-of-the-input-method-application) |
| [12800015](../errorcode-inputmethod-framework.md#12800015-message-receiver-unable-to-receive-custom-communication-data) |
| [12800016](../errorcode-inputmethod-framework.md#12800016-input-method-client-not-in-edit-mode) |

## sendPrivateCommand

```TypeScript
sendPrivateCommand(commandData: Record<string, CommandDataType>): Promise<void>
```

Sends private data to the system component that needs to communicate with the input method application. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> - The private data channel allows communication between the system preset input method application and specific system components (such as a text box or a home screen application). It is usually used to implement custom input on a specific device.
   
> 
   
> - The total size of the private data is 32 KB, and the maximum number of private data records is 5.
   
> 
   
> - Private data is sent to the text box by default. To send it to a desktop application, add a data entry `{'sys_cmd':1}` to the private data.

**Since:** 12

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| commandData | Record & lt;string, CommandDataType & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800010](../errorcode-inputmethod-framework.md#12800010-not-preconfigured-default-input-method) |

## setPreviewText

```TypeScript
setPreviewText(text: string, range: Range): Promise<void>
```

Sets the preview text. This API uses a promise to return the result.

**Since:** 12

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800011](../errorcode-inputmethod-framework.md#12800011-text-preview-not-supported) |

## setPreviewTextSync

```TypeScript
setPreviewTextSync(text: string, range: Range): void
```

Sets the preview text.

**Since:** 12

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| range | [Range](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-scan-range-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800011](../errorcode-inputmethod-framework.md#12800011-text-preview-not-supported) |
