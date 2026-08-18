# KeyboardDelegate

In the following API examples, you must first use [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md) to obtain a **KeyboardDelegate** instance, and then call the APIs using the obtained instance.

**Since:** 23

<!--Device-inputMethodEngine-interface KeyboardDelegate--><!--Device-inputMethodEngine-interface KeyboardDelegate-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## offCursorContextChange

```TypeScript
offCursorContextChange(callback?: CursorContextChangeCallback): void
```

Unsubscribe cursor context change.

**Since:** 23

<!--Device-KeyboardDelegate-offCursorContextChange(callback?: CursorContextChangeCallback): void--><!--Device-KeyboardDelegate-offCursorContextChange(callback?: CursorContextChangeCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [CursorContextChangeCallback](arkts-ime-inputmethodengine-cursorcontextchangecallback-t.md) | No | optional, the callback called when cursor information changes. |

## offEditorAttributeChanged

```TypeScript
offEditorAttributeChanged(callback?: Callback<EditorAttribute>): void
```

Unsubscribe input text attribute change.

**Since:** 23

<!--Device-KeyboardDelegate-offEditorAttributeChanged(callback?: Callback<EditorAttribute>): void--><!--Device-KeyboardDelegate-offEditorAttributeChanged(callback?: Callback<EditorAttribute>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md)&gt; | No | optional, the callback called when editor's attribute changes. |

## offKeyDown

```TypeScript
offKeyDown(callback?: KeyEventCallback): void
```

Unsubscribe key down event

**Since:** 23

<!--Device-KeyboardDelegate-offKeyDown(callback?: KeyEventCallback): void--><!--Device-KeyboardDelegate-offKeyDown(callback?: KeyEventCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) | No | optional, the callback called when a key down event occurs. |

## offKeyEvent

```TypeScript
offKeyEvent(callback?: InputKeyEventCallback): void
```

Unsubscribe key event.

**Since:** 23

<!--Device-KeyboardDelegate-offKeyEvent(callback?: InputKeyEventCallback): void--><!--Device-KeyboardDelegate-offKeyEvent(callback?: InputKeyEventCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [InputKeyEventCallback](arkts-ime-inputmethodengine-inputkeyeventcallback-t.md) | No | optional, the callback called when a key event event occurs. |

## offKeyUp

```TypeScript
offKeyUp(callback?: KeyEventCallback): void
```

Unsubscribe key up event

**Since:** 23

<!--Device-KeyboardDelegate-offKeyUp(callback?: KeyEventCallback): void--><!--Device-KeyboardDelegate-offKeyUp(callback?: KeyEventCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) | No | optional, the callback called when a key up event occurs. |

## offSelectionChange

```TypeScript
offSelectionChange(callback?: SelectionChangeCallback): void
```

Unsubscribe selection change.

**Since:** 23

<!--Device-KeyboardDelegate-offSelectionChange(callback?: SelectionChangeCallback): void--><!--Device-KeyboardDelegate-offSelectionChange(callback?: SelectionChangeCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SelectionChangeCallback](arkts-ime-inputmethodengine-selectionchangecallback-t.md) | No | optional, the callback called when the text selection changes. |

## offTextChange

```TypeScript
offTextChange(callback?: Callback<string>): void
```

Unsubscribe text change.

**Since:** 23

<!--Device-KeyboardDelegate-offTextChange(callback?: Callback<string>): void--><!--Device-KeyboardDelegate-offTextChange(callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt; | No | optional, the callback called when the text changes. |

## off_cursorContextChange('cursorContextChange')

```TypeScript
off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void
```

Disables listening for cursor context changes. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-KeyboardDelegate-off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void--><!--Device-KeyboardDelegate-off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cursorContextChange' | Yes | Event type, which is **'cursorContextChange'**. |
| callback | (x: number, y: number, height: number) =&gt; void | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
inputMethodEngine.getKeyboardDelegate().off('cursorContextChange', (x: number, y: number, height: number) => {
  console.info('delete cursorContextChange notification.');
});
```

## off_editorAttributeChanged('editorAttributeChanged')

```TypeScript
off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void
```

Disables listening for the edit box attribute change event. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-KeyboardDelegate-off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void--><!--Device-KeyboardDelegate-off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'editorAttributeChanged' | Yes | Event type, which is **'editorAttributeChanged'**. |
| callback | (attr: EditorAttribute) =&gt; void | No | Callback used for unsubscription. If this parameter is not specified, this API unregisters all callbacks for the specified type by default. |

**Examples**

```TypeScript
inputMethodEngine.getKeyboardDelegate().off('editorAttributeChanged');
```

## off_keyDown('keyDown' | 'keyUp')

```TypeScript
off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void
```

Disables listening for a physical keyboard event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-KeyboardDelegate-off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void--><!--Device-KeyboardDelegate-off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | Yes | Event type. <br>- The value **'keyDown'** indicates the keydown event. <br>- The value **'keyUp'** indicates the keyup event. |
| callback | (event: KeyEvent) =&gt; boolean | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
inputMethodEngine.getKeyboardDelegate().off('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info('delete keyUp notification.');
  return true;
});
inputMethodEngine.getKeyboardDelegate().off('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info('delete keyDown notification.');
  return true;
});
```

## off_keyEvent('keyEvent')

```TypeScript
off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void
```

Disables listening for a keyboard event. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-KeyboardDelegate-off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void--><!--Device-KeyboardDelegate-off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyEvent' | Yes | Event type, which is **'keyEvent'**. |
| callback | (event: InputKeyEvent) =&gt; boolean | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
import type { KeyEvent } from '@kit.InputKit';

inputMethodEngine.getKeyboardDelegate().off('keyEvent', (keyEvent: KeyEvent) => {
  console.info('This is a callback function which will be deregistered.');
  return true;
});
inputMethodEngine.getKeyboardDelegate().off('keyEvent');
```

## off_keyUp('keyDown' | 'keyUp')

```TypeScript
off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void
```

Disables listening for a physical keyboard event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-KeyboardDelegate-off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void--><!--Device-KeyboardDelegate-off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | Yes | Event type. <br>- The value **'keyDown'** indicates the keydown event. <br>- The value **'keyUp'** indicates the keyup event. |
| callback | (event: KeyEvent) =&gt; boolean | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
inputMethodEngine.getKeyboardDelegate().off('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info('delete keyUp notification.');
  return true;
});
inputMethodEngine.getKeyboardDelegate().off('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info('delete keyDown notification.');
  return true;
});
```

## off_selectionChange('selectionChange')

```TypeScript
off(
      type: 'selectionChange',
      callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void
    ): void
```

Disables listening for the text selection change event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-KeyboardDelegate-off(      type: 'selectionChange',      callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void    ): void--><!--Device-KeyboardDelegate-off(      type: 'selectionChange',      callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void    ): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'selectionChange' | Yes | Event type, which is **'selectionChange'**. |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) =&gt; void | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
inputMethodEngine.getKeyboardDelegate()
  .off('selectionChange', (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => {
    console.info('delete selectionChange notification.');
  });
```

## off_textChange('textChange')

```TypeScript
off(type: 'textChange', callback?: (text: string) => void): void
```

Disables listening for the text change event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-KeyboardDelegate-off(type: 'textChange', callback?: (text: string) => void): void--><!--Device-KeyboardDelegate-off(type: 'textChange', callback?: (text: string) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'textChange' | Yes | Event type, which is **'textChange'**. |
| callback | (text: string) =&gt; void | No | Callback to unregister. If this parameter is not specified, this API unregisters all callbacks for the specified type. |

**Examples**

```TypeScript
inputMethodEngine.getKeyboardDelegate().off('textChange', (text: string) => {
  console.info('delete textChange notification. text:' + text);
});
```

## onCursorContextChange

```TypeScript
onCursorContextChange(callback: CursorContextChangeCallback): void
```

Subscribe cursor context change.

**Since:** 23

<!--Device-KeyboardDelegate-onCursorContextChange(callback: CursorContextChangeCallback): void--><!--Device-KeyboardDelegate-onCursorContextChange(callback: CursorContextChangeCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [CursorContextChangeCallback](arkts-ime-inputmethodengine-cursorcontextchangecallback-t.md) | Yes | the callback called when cursor information changes. |

## onEditorAttributeChanged

```TypeScript
onEditorAttributeChanged(callback: Callback<EditorAttribute>): void
```

Subscribe input text attribute change.

**Since:** 23

<!--Device-KeyboardDelegate-onEditorAttributeChanged(callback: Callback<EditorAttribute>): void--><!--Device-KeyboardDelegate-onEditorAttributeChanged(callback: Callback<EditorAttribute>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md)&gt; | Yes | the callback called when editor's attribute changes. |

## onKeyDown

```TypeScript
onKeyDown(callback: KeyEventCallback): void
```

Subscribe key down event

**Since:** 23

<!--Device-KeyboardDelegate-onKeyDown(callback: KeyEventCallback): void--><!--Device-KeyboardDelegate-onKeyDown(callback: KeyEventCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) | Yes | the callback called when a key down event occurs. If the key is processed by event subscriber, callback should be return true, else return false. |

## onKeyEvent

```TypeScript
onKeyEvent(callback: InputKeyEventCallback): void
```

Subscribe key event.

**Since:** 23

<!--Device-KeyboardDelegate-onKeyEvent(callback: InputKeyEventCallback): void--><!--Device-KeyboardDelegate-onKeyEvent(callback: InputKeyEventCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [InputKeyEventCallback](arkts-ime-inputmethodengine-inputkeyeventcallback-t.md) | Yes | the callback called when a key event event occurs. If the key is processed by event subscriber, callback should be return true, else return false. |

## onKeyUp

```TypeScript
onKeyUp(callback: KeyEventCallback): void
```

Subscribe key up event

**Since:** 23

<!--Device-KeyboardDelegate-onKeyUp(callback: KeyEventCallback): void--><!--Device-KeyboardDelegate-onKeyUp(callback: KeyEventCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) | Yes | the callback called when a key up event occurs. If the key is processed by event subscriber, callback should be return true, else return false. |

## onSelectionChange

```TypeScript
onSelectionChange(callback: SelectionChangeCallback): void
```

Subscribe selection change.

**Since:** 23

<!--Device-KeyboardDelegate-onSelectionChange(callback: SelectionChangeCallback): void--><!--Device-KeyboardDelegate-onSelectionChange(callback: SelectionChangeCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SelectionChangeCallback](arkts-ime-inputmethodengine-selectionchangecallback-t.md) | Yes | the callback called when the text selection changes. |

## onTextChange

```TypeScript
onTextChange(callback: Callback<string>): void
```

Subscribe text change.

**Since:** 23

<!--Device-KeyboardDelegate-onTextChange(callback: Callback<string>): void--><!--Device-KeyboardDelegate-onTextChange(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;string&gt; | Yes | the callback called when the text changes. |

## on_cursorContextChange('cursorContextChange')

```TypeScript
on(type: 'cursorContextChange', callback: (x: number, y: number, height: number) => void): void
```

Enables listening for the cursor change event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-KeyboardDelegate-on(type: 'cursorContextChange', callback: (x: number, y: number, height: number) => void): void--><!--Device-KeyboardDelegate-on(type: 'cursorContextChange', callback: (x: number, y: number, height: number) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cursorContextChange' | Yes | Event type, which is **'cursorContextChange'**. |
| callback | (x: number, y: number, height: number) =&gt; void | Yes | Callback used to return the cursor information. <br>- **x**: x coordinate of the top of the cursor. <br>- **y**: y coordinate of the bottom of the cursor. <br>- **height**: height of the cursor. |

**Examples**

```TypeScript
inputMethodEngine.getKeyboardDelegate().on('cursorContextChange', (x: number, y: number, height: number) => {
  console.info('inputMethodEngine cursorContextChange x:' + x);
  console.info('inputMethodEngine cursorContextChange y:' + y);
  console.info('inputMethodEngine cursorContextChange height:' + height);
});
```

## on_editorAttributeChanged('editorAttributeChanged')

```TypeScript
on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void
```

Enables listening for the edit box attribute change event. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-KeyboardDelegate-on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void--><!--Device-KeyboardDelegate-on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'editorAttributeChanged' | Yes | Event type, which is **'editorAttributeChanged'**. |
| callback | (attr: EditorAttribute) =&gt; void | Yes | Callback used to return the changed edit box attribute. |

**Examples**

```TypeScript
inputMethodEngine.getKeyboardDelegate()
  .on('editorAttributeChanged', (attr: inputMethodEngine.EditorAttribute) => {
    console.info(`Succeeded in receiving attribute of editor, inputPattern = ${attr.inputPattern}, enterKeyType = ${attr.enterKeyType}`);
  });
```

## on_keyDown('keyDown' | 'keyUp')

```TypeScript
on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void
```

Enables listening for a physical keyboard event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-KeyboardDelegate-on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void--><!--Device-KeyboardDelegate-on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | Yes | Event type. <br>- The value **'keyDown'** indicates the keydown event. <br>- The value **'keyUp'** indicates the keyup event. |
| callback | (event: KeyEvent) =&gt; boolean | Yes | Callback used to return the key information. If the event is consumed by the event subscriber, **true** is returned. Otherwise, **false** is returned. |

**Examples**

```TypeScript
inputMethodEngine.getKeyboardDelegate().on('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info(`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}`);
  console.info(`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}`);
  return true;
});
inputMethodEngine.getKeyboardDelegate().on('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info(`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}`);
  console.info(`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}`);
  return true;
});
```

## on_keyEvent('keyEvent')

```TypeScript
on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void
```

Enables listening for a keyboard event. This API uses an asynchronous callback to return the result.

**Since:** 10

<!--Device-KeyboardDelegate-on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void--><!--Device-KeyboardDelegate-on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyEvent' | Yes | Event type, which is **'keyEvent'**. |
| callback | (event: InputKeyEvent) =&gt; boolean | Yes | Callback used to return the result. The input parameter is the key event information and the return value is of the Boolean type. <br>- Input parameter: [InputKeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md). <br>- If the event is consumed by the event subscriber, **true** is returned. Otherwise, **false** is returned. |

**Examples**

```TypeScript
import type { KeyEvent } from '@kit.InputKit';

inputMethodEngine.getKeyboardDelegate().on('keyEvent', (keyEvent: KeyEvent) => {
  console.info(`inputMethodEngine keyEvent.action:${ keyEvent.action}`);
  console.info(`inputMethodEngine keyEvent.key.code: ${keyEvent.key.code}`);
  console.info(`inputMethodEngine keyEvent.ctrlKey: ${keyEvent.ctrlKey}`);
  console.info(`inputMethodEngine keyEvent.unicodeChar: ${keyEvent.unicodeChar}`);
  return true;
});
```

## on_keyUp('keyDown' | 'keyUp')

```TypeScript
on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void
```

Enables listening for a physical keyboard event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-KeyboardDelegate-on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void--><!--Device-KeyboardDelegate-on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | Yes | Event type. <br>- The value **'keyDown'** indicates the keydown event. <br>- The value **'keyUp'** indicates the keyup event. |
| callback | (event: KeyEvent) =&gt; boolean | Yes | Callback used to return the key information. If the event is consumed by the event subscriber, **true** is returned. Otherwise, **false** is returned. |

**Examples**

```TypeScript
inputMethodEngine.getKeyboardDelegate().on('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info(`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}`);
  console.info(`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}`);
  return true;
});
inputMethodEngine.getKeyboardDelegate().on('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info(`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}`);
  console.info(`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}`);
  return true;
});
```

## on_selectionChange('selectionChange')

```TypeScript
on(
      type: 'selectionChange',
      callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void
    ): void
```

Enables listening for the text selection change event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-KeyboardDelegate-on(      type: 'selectionChange',      callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void    ): void--><!--Device-KeyboardDelegate-on(      type: 'selectionChange',      callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void    ): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'selectionChange' | Yes | Event type, which is **'selectionChange'**. |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) =&gt; void | Yes | Callback used to return the text selection information. <br>- **oldBegin**: start of the selected text before the change. <br>- **oldEnd**: end of the selected text before the change. <br>- **newBegin**: start of the selected text after the change. <br>- **newEnd**: end of the selected text after the change. |

**Examples**

```TypeScript
inputMethodEngine.getKeyboardDelegate()
  .on('selectionChange', (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => {
    console.info('selectionChange oldBegin:' + oldBegin);
    console.info('selectionChange oldEnd:' + oldEnd);
    console.info('selectionChange newBegin:' + newBegin);
    console.info('selectionChange newEnd:' + newEnd);
  });
```

## on_textChange('textChange')

```TypeScript
on(type: 'textChange', callback: (text: string) => void): void
```

Enables listening for the text change event. This API uses an asynchronous callback to return the result.

**Since:** 8

<!--Device-KeyboardDelegate-on(type: 'textChange', callback: (text: string) => void): void--><!--Device-KeyboardDelegate-on(type: 'textChange', callback: (text: string) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'textChange' | Yes | Event type, which is **'textChange'**. |
| callback | (text: string) =&gt; void | Yes | Callback used to return the text content. |

**Examples**

```TypeScript
inputMethodEngine.getKeyboardDelegate().on('textChange', (text: string) => {
  console.info('inputMethodEngine textChange. text:' + text);
});
```

