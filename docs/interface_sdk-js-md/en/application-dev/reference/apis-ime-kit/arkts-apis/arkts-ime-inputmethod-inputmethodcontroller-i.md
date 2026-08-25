# InputMethodController

In the following API examples, you must first use [getController](arkts-ime-inputmethod-getcontroller-f.md) to obtain an **InputMethodController** instance, and then call the APIs using the obtained instance.

**Since:** 6

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethod } from 'kits/@kit.IMEKit';
```

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void
```

Attaches a self-drawing component to the input method. This API uses an asynchronous callback to return the result.   
> **NOTE：**
   
> 
   
> An input method can use the following features only when it has a self-drawing component attached to it: showing or hiding the keyboard, updating the cursor information, changing the selection range of the edit box, saving the configuration information, and listening for and processing the information or commands sent by the input method.
   
> 
   
> If the window where the self-drawing component is located is set to be non-focusable via [setWindowFocusable](../../apis-arkui/arkts-apis/arkts-arkui-window-window-i.md#setwindowfocusable), the system cannot guarantee proper interaction between the self-drawing input component and the input method. If you want to draw an input box in a non-focusable window, refer to [Input Box and Input Method Interaction in Non-Focusable Windows](../../../inputmethod/use-inputmethod-in-not-focusable-window.md).

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [showKeyboard](arkts-ime-inputmethod-attachoptions-i.md) | boolean | Yes |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>
```

Attaches a self-drawing component to the input method. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> An input method can use the following features only when it has a self-drawing component attached to it: showing or hiding the keyboard, updating the cursor information, changing the selection range of the edit box, saving the configuration information, and listening for and processing the information or commands sent by the input method.
   
> 
   
> If the window where the self-drawing component is located is set to be non-focusable via [setWindowFocusable](../../apis-arkui/arkts-apis/arkts-arkui-window-window-i.md#setwindowfocusable), the system cannot guarantee proper interaction between the self-drawing input component and the input method. If you want to draw an input box in a non-focusable window, refer to [Input Box and Input Method Interaction in Non-Focusable Windows](../../../inputmethod/use-inputmethod-in-not-focusable-window.md).

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [showKeyboard](arkts-ime-inputmethod-attachoptions-i.md) | boolean | Yes |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## attach

```TypeScript
attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>
```

Attaches a self-drawing component to the input method. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> An input method can use the following features only when it has a self-drawing component attached to it: showing or hiding the keyboard, updating the cursor information, changing the selection range of the edit box, saving the configuration information, and listening for and processing the information or commands sent by the input method.
   
> 
   
> If the window where the self-drawing component is located is set to be non-focusable via [setWindowFocusable](../../apis-arkui/arkts-apis/arkts-arkui-window-window-i.md#setwindowfocusable), the system cannot guarantee proper interaction between the self-drawing input component and the input method. If you want to draw an input box in a non-focusable window, refer to [Input Box and Input Method Interaction in Non-Focusable Windows](../../../inputmethod/use-inputmethod-in-not-focusable-window.md).

**Since:** 15

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [showKeyboard](arkts-ime-inputmethod-attachoptions-i.md) | boolean | Yes |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | Yes |
| requestKeyboardReason | [RequestKeyboardReason](arkts-ime-inputmethod-requestkeyboardreason-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## attachWithUIContext

```TypeScript
attachWithUIContext(uiContext: UIContext, textConfig: TextConfig, attachOptions?: AttachOptions): Promise<void>
```

Attaches a self-drawing component to the input method. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> An input method can use the following features only when it has a self-drawing component attached to it: showing or hiding the keyboard, updating the cursor information, changing the selection range of the edit box, saving the configuration information, and listening for and processing the information or commands sent by the input method.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uiContext | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes |
| textConfig | [TextConfig](arkts-ime-inputmethod-textconfig-i.md) | Yes |
| attachOptions | [AttachOptions](arkts-ime-inputmethod-attachoptions-i.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## changeSelection

```TypeScript
changeSelection(text: string, start: number, end: number, callback: AsyncCallback<void>): void
```

Updates the information about the selected text in this edit box, to notify the input method when the selected text content or text range changes. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| start | number | Yes |
| end | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## changeSelection

```TypeScript
changeSelection(text: string, start: number, end: number): Promise<void>
```

Updates the information about the selected text in this edit box, to notify the input method when the selected text content or text range changes. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| start | number | Yes |
| end | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## detach

```TypeScript
detach(callback: AsyncCallback<void>): void
```

Detaches the self-drawing component from the input method. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## detach

```TypeScript
detach(): Promise<void>
```

Detaches the self-drawing component from the input method. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## discardTypingText

```TypeScript
discardTypingText(): Promise<void>
```

Discards the text that is being typed. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> This API can be called after the edit box is attached to an input method.

**Since:** 20

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |
| [12800015](../errorcode-inputmethod-framework.md#12800015-message-receiver-unable-to-receive-custom-communication-data) |

## hideSoftKeyboard

```TypeScript
hideSoftKeyboard(callback: AsyncCallback<void>): void
```

Hides the soft keyboard. This API uses an asynchronous callback to return the result.   
> **NOTE：**
   
> 
   
> This API can be called only when the edit box is attached to the input method. That is, it can be called to hide the soft keyboard only when the edit box is focused.

**Since:** 9

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## hideSoftKeyboard

```TypeScript
hideSoftKeyboard(): Promise<void>
```

Hides the soft keyboard. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> This API can be called only when the edit box is attached to the input method. That is, it can be called to hide the soft keyboard only when the edit box is focused.

**Since:** 9

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## hideTextInput

```TypeScript
hideTextInput(callback: AsyncCallback<void>): void
```

Exits the text editing mode. This API uses an asynchronous callback to return the result.   
> **NOTE：**
   
> 
   
> If the soft keyboard is displayed when this API is called, it will be hidden.
   
> 
   
> Calling this API does not detach the edit box from the input method. The edit box can call [showTextInput](#showtextinput) again to reenter the text editing mode.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## hideTextInput

```TypeScript
hideTextInput(): Promise<void>
```

Exits the text editing mode. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> If the soft keyboard is displayed when this API is called, it will be hidden.
   
> 
   
> Calling this API does not detach the edit box from the input method. The edit box can call [showTextInput](#showtextinput) again to reenter the text editing mode.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## off('selectByRange')

```TypeScript
off(type: 'selectByRange', callback?: Callback<Range>): void
```

Disables listening for the select-by-range event. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'selectByRange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | No |

## off('selectByMovement')

```TypeScript
off(type: 'selectByMovement', callback?: Callback<Movement>): void
```

Disables listening for the select-by-cursor-movement event. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'selectByMovement' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | No |

## off('insertText')

```TypeScript
off(type: 'insertText', callback?: (text: string) => void): void
```

Disables listening for the text insertion event of the input method.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'insertText' | Yes |
| callback | (text: string) = & gt; void | No |

## off('deleteLeft')

```TypeScript
off(type: 'deleteLeft', callback?: (length: number) => void): void
```

Disables listening for the leftward delete event.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deleteLeft' | Yes |
| callback | (length: number) = & gt; void | No |

## off('deleteRight')

```TypeScript
off(type: 'deleteRight', callback?: (length: number) => void): void
```

Disables listening for the rightward delete event.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deleteRight' | Yes |
| callback | (length: number) = & gt; void | No |

## off('sendKeyboardStatus')

```TypeScript
off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void
```

Disables listening for the input method soft keyboard status event of the input method.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'sendKeyboardStatus' | Yes |
| callback | (keyboardStatus: KeyboardStatus) = & gt; void | No |

## off('sendFunctionKey')

```TypeScript
off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void
```

Disables listening for the function key sending event of the input method.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'sendFunctionKey' | Yes |
| callback | (functionKey: FunctionKey) = & gt; void | No |

## off('moveCursor')

```TypeScript
off(type: 'moveCursor', callback?: (direction: Direction) => void): void
```

Disables listening for the cursor movement event of the input method.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'moveCursor' | Yes |
| callback | (direction: Direction) = & gt; void | No |

## off('handleExtendAction')

```TypeScript
off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void
```

Disables listening for the extended action handling event of the input method. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'handleExtendAction' | Yes |
| callback | (action: ExtendAction) = & gt; void | No |

## off('getLeftTextOfCursor')

```TypeScript
off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void
```

Disables listening for the event of obtaining the length of text deleted leftward. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'getLeftTextOfCursor' | Yes |
| callback | (length: number) = & gt; string | No |

## off('getRightTextOfCursor')

```TypeScript
off(type: 'getRightTextOfCursor', callback?: (length: number) => string): void
```

Disables listening for the event of obtaining the length of text deleted rightward. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'getRightTextOfCursor' | Yes |
| callback | (length: number) = & gt; string | No |

## off('getTextIndexAtCursor')

```TypeScript
off(type: 'getTextIndexAtCursor', callback?: () => number): void
```

Disables listening for the event of obtaining the index of text at the cursor. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'getTextIndexAtCursor' | Yes |
| callback | () = & gt; number | No |

## off('setPreviewText')

```TypeScript
off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void
```

Unsubscribes from the event for text preview operations in an input method application. This API uses an asynchronous callback to return the result.

**Since:** 17

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'setPreviewText' | Yes |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | No |

## off('finishTextPreview')

```TypeScript
off(type: 'finishTextPreview', callback?: Callback<void>): void
```

Unsubscribes from the event of finishing text preview. This API uses an asynchronous callback to return the result.

**Since:** 17

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'finishTextPreview' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

## on('selectByRange')

```TypeScript
on(type: 'selectByRange', callback: Callback<Range>): void
```

Enables listening for the select-by-range event. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'selectByRange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Range&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on('selectByMovement')

```TypeScript
on(type: 'selectByMovement', callback: Callback<Movement>): void
```

Enables listening for the select-by-cursor-movement event. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'selectByMovement' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Movement&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on('insertText')

```TypeScript
on(type: 'insertText', callback: (text: string) => void): void
```

Enables listening for the text insertion event of the input method. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'insertText' | Yes |
| callback | (text: string) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## on('deleteLeft')

```TypeScript
on(type: 'deleteLeft', callback: (length: number) => void): void
```

Enables listening for the leftward delete event. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deleteLeft' | Yes |
| callback | (length: number) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## on('deleteRight')

```TypeScript
on(type: 'deleteRight', callback: (length: number) => void): void
```

Enables listening for the rightward delete event. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'deleteRight' | Yes |
| callback | (length: number) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## on('sendKeyboardStatus')

```TypeScript
on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void
```

Enables listening for the soft keyboard status event of the input method. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'sendKeyboardStatus' | Yes |
| callback | (keyboardStatus: KeyboardStatus) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## on('sendFunctionKey')

```TypeScript
on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void
```

Enables listening for the function key sending event of the input method. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'sendFunctionKey' | Yes |
| callback | (functionKey: FunctionKey) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## on('moveCursor')

```TypeScript
on(type: 'moveCursor', callback: (direction: Direction) => void): void
```

Enables listening for the cursor movement event of the input method. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'moveCursor' | Yes |
| callback | (direction: Direction) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## on('handleExtendAction')

```TypeScript
on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void
```

Enables listening for the extended action handling event of the input method. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'handleExtendAction' | Yes |
| callback | (action: ExtendAction) = & gt; void | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## on('getLeftTextOfCursor')

```TypeScript
on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void
```

Enables listening for the event of obtaining the length of text deleted leftward. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'getLeftTextOfCursor' | Yes |
| callback | (length: number) = & gt; string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## on('getRightTextOfCursor')

```TypeScript
on(type: 'getRightTextOfCursor', callback: (length: number) => string): void
```

Enables listening for the event of obtaining the length of text deleted rightward. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'getRightTextOfCursor' | Yes |
| callback | (length: number) = & gt; string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## on('getTextIndexAtCursor')

```TypeScript
on(type: 'getTextIndexAtCursor', callback: () => number): void
```

Enables listening for the event of obtaining the index of text at the cursor. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'getTextIndexAtCursor' | Yes |
| callback | () = & gt; number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## on('setPreviewText')

```TypeScript
on(type: 'setPreviewText', callback: SetPreviewTextCallback): void
```

Subscribes to the event for text preview operations in an input method application. This API uses an asynchronous callback to return the result.   
> **NOTE：**
   
> 
   
> To use the text preview function, you need to subscribe to this event before calling [attach](#attach) and subscribe to this event together with on('finishTextPreview').

**Since:** 17

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'setPreviewText' | Yes |
| callback | [SetPreviewTextCallback](arkts-ime-inputmethod-setpreviewtextcallback-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## on('finishTextPreview')

```TypeScript
on(type: 'finishTextPreview', callback: Callback<void>): void
```

Subscribes to the event of finishing text preview. This API uses an asynchronous callback to return the result.   
> **NOTE：**
   
> 
   
> To use the text preview function, you need to subscribe to this event before calling [attach](#attach) and subscribe to this event together with [on('setPreviewText')](#onsetpreviewtext).

**Since:** 17

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'finishTextPreview' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |

## recvMessage

```TypeScript
recvMessage(msgHandler?: MessageHandler): void
```

Registers or unregisters MessageHandler.   
> **NOTE：**
   
> 
   
> The [MessageHandler](arkts-ime-inputmethod-messagehandler-i.md) object is globally unique. After multiple registrations, only the last registered object is valid and retained, and the [onTerminated](arkts-ime-inputmethod-messagehandler-i.md#onterminated) callback of the penultimate registered object is triggered.
   
> 
   
> If no parameter is set, unregister [MessageHandler](arkts-ime-inputmethod-messagehandler-i.md). Its [onTerminated](arkts-ime-inputmethod-messagehandler-i.md#onterminated) callback will be triggered.

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

## sendMessage

```TypeScript
sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>
```

Sends the custom communication to the input method application. This API uses a promise to return the result.   
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

## setCallingWindow

```TypeScript
setCallingWindow(windowId: number, callback: AsyncCallback<void>): void
```

Sets the window to be avoided by the input method. This API uses an asynchronous callback to return the result.   
> **NOTE：**
   
> 
   
> After the window ID of the application bound to the input method is passed in the API, the input method window will not cover the window holding the application.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## setCallingWindow

```TypeScript
setCallingWindow(windowId: number): Promise<void>
```

Sets the window to be avoided by the input method. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> After the window ID of the application bound to the input method is passed in the API, the input method window will not cover the window holding the application.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| windowId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## showSoftKeyboard

```TypeScript
showSoftKeyboard(callback: AsyncCallback<void>): void
```

Shows the soft keyboard. This API uses an asynchronous callback to return the result.   
> **NOTE：**
   
> 
   
> This API can be called only when the edit box is attached to the input method. That is, it can be called to show the soft keyboard only when the edit box is focused.

**Since:** 9

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## showSoftKeyboard

```TypeScript
showSoftKeyboard(): Promise<void>
```

Shows the soft keyboard. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> This API can be called only when the edit box is attached to the input method. That is, it can be called to show the soft keyboard only when the edit box is focused.

**Since:** 9

**Required permissions:** ohos.permission.CONNECT_IME_ABILITY

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## showTextInput

```TypeScript
showTextInput(callback: AsyncCallback<void>): void
```

Enters the text editing mode. This API uses an asynchronous callback to return the result.   
> **NOTE：**
   
> 
   
> After the edit box is attached to an input method, this API can be called to start the soft keyboard and enter the text editing state.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## showTextInput

```TypeScript
showTextInput(): Promise<void>
```

Enters the text editing mode. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> After the edit box is attached to an input method, this API can be called to start the soft keyboard and enter the text editing state.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## showTextInput

```TypeScript
showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>
```

Enters the text editing mode. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> After the edit box is attached to an input method, this API can be called to start the soft keyboard and enter the text editing state.

**Since:** 15

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| requestKeyboardReason | [RequestKeyboardReason](arkts-ime-inputmethod-requestkeyboardreason-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## stopInput

```TypeScript
stopInput(callback: AsyncCallback<boolean>): void
```

Ends this input session. This API uses an asynchronous callback to return the result.   
> **NOTE：**
   
> 
   
> This API can be called only when the edit box is attached to the input method. That is, it can be called to end the input session only when the edit box is focused.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [stopInputSession](#stopinputsession)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## stopInput

```TypeScript
stopInput(): Promise<boolean>
```

Ends this input session. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> This API can be called only when the edit box is attached to the input method. That is, it can be called to end the input session only when the edit box is focused.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [stopInputSession](#stopinputsession)

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

## stopInputSession

```TypeScript
stopInputSession(callback: AsyncCallback<boolean>): void
```

Ends this input session. This API uses an asynchronous callback to return the result.   
> **NOTE：**
   
> 
   
> This API can be called only when the edit box is attached to the input method. That is, it can be called to end the input session only when the edit box is focused.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## stopInputSession

```TypeScript
stopInputSession(): Promise<boolean>
```

Ends this input session. This API uses a promise to return the result.   
> **NOTE：**
   
> 
   
> This API can be called only when the edit box is attached to the input method. That is, it can be called to end the input session only when the edit box is focused.

**Since:** 9

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |

## updateAttribute

```TypeScript
updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void
```

Updates the attribute information of this edit box. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| attribute | [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## updateAttribute

```TypeScript
updateAttribute(attribute: InputAttribute): Promise<void>
```

Updates the attribute information of this edit box. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| attribute | [InputAttribute](arkts-ime-inputmethod-inputattribute-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## updateCursor

```TypeScript
updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void
```

Updates the cursor information in this edit box. This API can be called to notify the input method of the cursor changes. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [cursorInfo](arkts-ime-inputmethod-textconfig-i.md) | [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |

## updateCursor

```TypeScript
updateCursor(cursorInfo: CursorInfo): Promise<void>
```

Updates the cursor information in this edit box. This API can be called to notify the input method of the cursor changes. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [cursorInfo](arkts-ime-inputmethod-textconfig-i.md) | [CursorInfo](arkts-ime-inputmethod-cursorinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [12800003](../errorcode-inputmethod-framework.md#12800003-input-method-client-error) |
| [12800008](../errorcode-inputmethod-framework.md#12800008-input-method-manager-service-error) |
| [12800009](../errorcode-inputmethod-framework.md#12800009-input-method-client-detached) |
