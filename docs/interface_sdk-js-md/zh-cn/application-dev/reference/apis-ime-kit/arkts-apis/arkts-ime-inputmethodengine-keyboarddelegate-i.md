# KeyboardDelegate

**起始版本：** 23

<!--Device-inputMethodEngine-interface KeyboardDelegate--><!--Device-inputMethodEngine-interface KeyboardDelegate-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethodEngine } from '@kit.IMEKit';
```

## offCursorContextChange

```TypeScript
offCursorContextChange(callback?: CursorContextChangeCallback): void
```

**起始版本：** 23

<!--Device-KeyboardDelegate-offCursorContextChange(callback?: CursorContextChangeCallback): void--><!--Device-KeyboardDelegate-offCursorContextChange(callback?: CursorContextChangeCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [CursorContextChangeCallback](arkts-ime-inputmethodengine-cursorcontextchangecallback-t.md) | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodEngineDelegate = inputMethodEngine.getKeyboardDelegate();
if (inputMethodEngineDelegate) {
  inputMethodEngineDelegate!.offCursorContextChange((x: double, y: double, height: double) => {
    console.info('delete cursorContextChange notification.');
  });
}
```

## offEditorAttributeChanged

```TypeScript
offEditorAttributeChanged(callback?: Callback<EditorAttribute>): void
```

**起始版本：** 23

<!--Device-KeyboardDelegate-offEditorAttributeChanged(callback?: Callback<EditorAttribute>): void--><!--Device-KeyboardDelegate-offEditorAttributeChanged(callback?: Callback<EditorAttribute>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md)&gt; | 否 | 所要取消订阅的回调处理函数。参数不填写时，默认取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodEngineDelegate = inputMethodEngine.getKeyboardDelegate();
if (inputMethodEngineDelegate) {
  inputMethodEngineDelegate!.offEditorAttributeChanged();
}
```

## offKeyDown

```TypeScript
offKeyDown(callback?: KeyEventCallback): void
```

**起始版本：** 23

<!--Device-KeyboardDelegate-offKeyDown(callback?: KeyEventCallback): void--><!--Device-KeyboardDelegate-offKeyDown(callback?: KeyEventCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodEngineDelegate = inputMethodEngine.getKeyboardDelegate();
if (inputMethodEngineDelegate) {
  inputMethodEngineDelegate!.offKeyUp((keyEvent: inputMethodEngine.KeyEvent) => {
    console.info('delete keyUp notification.');
    return true;
  });
  inputMethodEngineDelegate!.offKeyDown((keyEvent: inputMethodEngine.KeyEvent) => {
    console.info('delete keyDown notification.');
    return true;
  });
}
```

## offKeyEvent

```TypeScript
offKeyEvent(callback?: InputKeyEventCallback): void
```

**起始版本：** 23

<!--Device-KeyboardDelegate-offKeyEvent(callback?: InputKeyEventCallback): void--><!--Device-KeyboardDelegate-offKeyEvent(callback?: InputKeyEventCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [InputKeyEventCallback](arkts-ime-inputmethodengine-inputkeyeventcallback-t.md) | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
import type { KeyEvent } from '@kit.InputKit';

let inputMethodEngineDelegate = inputMethodEngine.getKeyboardDelegate();
if (inputMethodEngineDelegate) {
  inputMethodEngineDelegate!.offKeyEvent((keyEvent: KeyEvent) => {
    console.info('This is a callback function which will be deregistered.');
    return true;
  });
  inputMethodEngineDelegate!.offKeyEvent();
}
```

## offKeyUp

```TypeScript
offKeyUp(callback?: KeyEventCallback): void
```

**起始版本：** 23

<!--Device-KeyboardDelegate-offKeyUp(callback?: KeyEventCallback): void--><!--Device-KeyboardDelegate-offKeyUp(callback?: KeyEventCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodEngineDelegate = inputMethodEngine.getKeyboardDelegate();
if (inputMethodEngineDelegate) {
  inputMethodEngineDelegate!.offKeyUp((keyEvent: inputMethodEngine.KeyEvent) => {
    console.info('delete keyUp notification.');
    return true;
  });
  inputMethodEngineDelegate!.offKeyDown((keyEvent: inputMethodEngine.KeyEvent) => {
    console.info('delete keyDown notification.');
    return true;
  });
}
```

## offSelectionChange

```TypeScript
offSelectionChange(callback?: SelectionChangeCallback): void
```

**起始版本：** 23

<!--Device-KeyboardDelegate-offSelectionChange(callback?: SelectionChangeCallback): void--><!--Device-KeyboardDelegate-offSelectionChange(callback?: SelectionChangeCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [SelectionChangeCallback](arkts-ime-inputmethodengine-selectionchangecallback-t.md) | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodEngineDelegate = inputMethodEngine.getKeyboardDelegate();
if (inputMethodEngineDelegate) {
  inputMethodEngineDelegate!.offSelectionChange((oldBegin: int, oldEnd: int, newBegin: int, newEnd: int) => {
    console.info('delete selectionChange notification.');
  });
}
```

## offTextChange

```TypeScript
offTextChange(callback?: Callback<string>): void
```

**起始版本：** 23

<!--Device-KeyboardDelegate-offTextChange(callback?: Callback<string>): void--><!--Device-KeyboardDelegate-offTextChange(callback?: Callback<string>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
let inputMethodEngineDelegate = inputMethodEngine.getKeyboardDelegate();
if (inputMethodEngineDelegate) {
  inputMethodEngineDelegate!.offTextChange((text: string) => {
    console.info(`delete textChange notification. text: ${text}`);
  });
}
```

## off('cursorContextChange')

```TypeScript
off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void
```

**起始版本：** 8

<!--Device-KeyboardDelegate-off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void--><!--Device-KeyboardDelegate-off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'cursorContextChange' | 是 | 光标变化事件，固定取值为'cursorContextChange'。 |
| callback | (x: number, y: number, height: number) =&gt; void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
inputMethodEngine.getKeyboardDelegate().off('cursorContextChange');
```

## off('editorAttributeChanged')

```TypeScript
off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void
```

**起始版本：** 10

<!--Device-KeyboardDelegate-off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void--><!--Device-KeyboardDelegate-off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'editorAttributeChanged' | 是 | 编辑框属性变化事件，固定取值为'editorAttributeChanged'。 |
| callback | (attr: EditorAttribute) =&gt; void | 否 | 所要取消订阅的回调处理函数。参数不填写时，默认取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
inputMethodEngine.getKeyboardDelegate().off('editorAttributeChanged');
```

## off('keyDown' | 'keyUp')

```TypeScript
off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void
```

**起始版本：** 8

<!--Device-KeyboardDelegate-off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void--><!--Device-KeyboardDelegate-off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | 是 | 设置监听类型。<br/>- 'keyDown'表示键盘按下。<br/>- 'keyUp'表示键盘抬起。 |
| callback | (event: KeyEvent) =&gt; boolean | 否 | 取消订阅的回调函数，用于取消特定的键盘按键事件订阅。传入callback时取消指定回调的订阅，参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

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

## off('keyEvent')

```TypeScript
off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void
```

**起始版本：** 10

<!--Device-KeyboardDelegate-off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void--><!--Device-KeyboardDelegate-off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'keyEvent' | 是 | 设置监听类型，固定取值为'keyEvent'。 |
| callback | (event: InputKeyEvent) =&gt; boolean | 否 | 取消订阅的回调函数，用于取消特定的键盘事件订阅。传入callback时取消指定回调的订阅，参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
import type { KeyEvent } from '@kit.InputKit';

inputMethodEngine.getKeyboardDelegate().off('keyEvent', (keyEvent: KeyEvent) => {
  console.info('This is a callback function which will be deregistered.');
  return true;
});
inputMethodEngine.getKeyboardDelegate().off('keyEvent');
```

## off('keyDown' | 'keyUp')

```TypeScript
off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void
```

**起始版本：** 8

<!--Device-KeyboardDelegate-off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void--><!--Device-KeyboardDelegate-off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | 是 | 设置监听类型。<br/>- 'keyDown'表示键盘按下。<br/>- 'keyUp'表示键盘抬起。 |
| callback | (event: KeyEvent) =&gt; boolean | 否 | 取消订阅的回调函数，用于取消特定的键盘按键事件订阅。传入callback时取消指定回调的订阅，参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

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

## off('selectionChange')

```TypeScript
off(
      type: 'selectionChange',
      callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void
    ): void
```

**起始版本：** 8

<!--Device-KeyboardDelegate-off(      type: 'selectionChange',      callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void    ): void--><!--Device-KeyboardDelegate-off(      type: 'selectionChange',      callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void    ): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'selectionChange' | 是 | 文本选择变化事件，固定取值为'selectionChange'。 |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) =&gt; void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
inputMethodEngine.getKeyboardDelegate()
  .off('selectionChange', (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => {
    console.info('delete selectionChange notification.');
  });
```

## off('textChange')

```TypeScript
off(type: 'textChange', callback?: (text: string) => void): void
```

**起始版本：** 8

<!--Device-KeyboardDelegate-off(type: 'textChange', callback?: (text: string) => void): void--><!--Device-KeyboardDelegate-off(type: 'textChange', callback?: (text: string) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'textChange' | 是 | 文本变化事件，固定取值为'textChange'。 |
| callback | (text: string) =&gt; void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例**

```TypeScript
inputMethodEngine.getKeyboardDelegate().off('textChange', (text: string) => {
  console.info('delete textChange notification. text:' + text);
});
```

## onCursorContextChange

```TypeScript
onCursorContextChange(callback: CursorContextChangeCallback): void
```

**起始版本：** 23

<!--Device-KeyboardDelegate-onCursorContextChange(callback: CursorContextChangeCallback): void--><!--Device-KeyboardDelegate-onCursorContextChange(callback: CursorContextChangeCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [CursorContextChangeCallback](arkts-ime-inputmethodengine-cursorcontextchangecallback-t.md) | 是 | 回调函数，返回光标信息。<br/>-x为光标上端的的x坐标值，单位为px。y为光标上端的y坐标值，单位为px。height为光 标的高度值，单位为px。 |

**示例**

```TypeScript
let inputMethodEngineDelegate = inputMethodEngine.getKeyboardDelegate();
if (inputMethodEngineDelegate) {
  inputMethodEngineDelegate!.onCursorContextChange((x: double, y: double, height: double) => {
    console.info(`inputMethodEngine cursorContextChange x:${x}, y:${y}, height:${height}`);
  });
}
```

## onEditorAttributeChanged

```TypeScript
onEditorAttributeChanged(callback: Callback<EditorAttribute>): void
```

**起始版本：** 23

<!--Device-KeyboardDelegate-onEditorAttributeChanged(callback: Callback<EditorAttribute>): void--><!--Device-KeyboardDelegate-onEditorAttributeChanged(callback: Callback<EditorAttribute>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[EditorAttribute](arkts-ime-inputmethodengine-editorattribute-i.md)&gt; | 是 | 回调函数，返回变化的编辑框属性。 |

**示例**

```TypeScript
let inputMethodEngineDelegate = inputMethodEngine.getKeyboardDelegate();
if (inputMethodEngineDelegate) {
  inputMethodEngineDelegate!.onEditorAttributeChanged((attr: inputMethodEngine.EditorAttribute) => {
    console.info(`Succeeded in receiving attribute of editor, inputPattern = ${attr.inputPattern}, enterKeyType = ${attr.enterKeyType}`);
  });
}
```

## onKeyDown

```TypeScript
onKeyDown(callback: KeyEventCallback): void
```

**起始版本：** 23

<!--Device-KeyboardDelegate-onKeyDown(callback: KeyEventCallback): void--><!--Device-KeyboardDelegate-onKeyDown(callback: KeyEventCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) | 是 | 回调函数，返回按键信息。 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。 |

**示例**

```TypeScript
let KeyboardDelegate = inputMethodEngine.getKeyboardDelegate()
let inputMethodEngineDelegate = inputMethodEngine.getKeyboardDelegate();
if (inputMethodEngineDelegate) {

  inputMethodEngineDelegate!.onKeyUp((keyEvent: inputMethodEngine.KeyEvent) => {
    console.info(`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}`);
    console.info(`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}`);
    return true;
  });
  inputMethodEngineDelegate!.onKeyDown((keyEvent: inputMethodEngine.KeyEvent) => {
    console.info(`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}`);
    console.info(`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}`);
    return true;
  });
}
```

## onKeyEvent

```TypeScript
onKeyEvent(callback: InputKeyEventCallback): void
```

**起始版本：** 23

<!--Device-KeyboardDelegate-onKeyEvent(callback: InputKeyEventCallback): void--><!--Device-KeyboardDelegate-onKeyEvent(callback: InputKeyEventCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [InputKeyEventCallback](arkts-ime-inputmethodengine-inputkeyeventcallback-t.md) | 是 | the callback called when a key event event occurs. If the key is processed by event subscriber, callback should be return true, else return false. |

**示例**

```TypeScript
import type { KeyEvent } from '@kit.InputKit';

let inputMethodEngineDelegate = inputMethodEngine.getKeyboardDelegate();
if (inputMethodEngineDelegate) {
  inputMethodEngineDelegate!.onKeyEvent((keyEvent: KeyEvent) => {
    console.info(`inputMethodEngine keyEvent.action: ${keyEvent.action}`);
    console.info(`inputMethodEngine keyEvent.key.code: ${keyEvent.key.code}`);
    console.info(`inputMethodEngine keyEvent.ctrlKey: ${keyEvent.ctrlKey}`);
    console.info(`inputMethodEngine keyEvent.unicodeChar: ${keyEvent.unicodeChar}`);
    return true;
  });
}
```

## onKeyUp

```TypeScript
onKeyUp(callback: KeyEventCallback): void
```

**起始版本：** 23

<!--Device-KeyboardDelegate-onKeyUp(callback: KeyEventCallback): void--><!--Device-KeyboardDelegate-onKeyUp(callback: KeyEventCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) | 是 | 回调函数，返回按键信息。 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。 |

**示例**

```TypeScript
let inputMethodEngineDelegate = inputMethodEngine.getKeyboardDelegate();
if (inputMethodEngineDelegate) {
  inputMethodEngineDelegate!.onKeyUp((keyEvent: inputMethodEngine.KeyEvent) => {
    console.info(`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}`);
    console.info(`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}`);
    return true;
  });
  inputMethodEngineDelegate!.onKeyDown((keyEvent: inputMethodEngine.KeyEvent) => {
    console.info(`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}`);
    console.info(`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}`);
    return true;
  });
}
```

## onSelectionChange

```TypeScript
onSelectionChange(callback: SelectionChangeCallback): void
```

**起始版本：** 23

<!--Device-KeyboardDelegate-onSelectionChange(callback: SelectionChangeCallback): void--><!--Device-KeyboardDelegate-onSelectionChange(callback: SelectionChangeCallback): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [SelectionChangeCallback](arkts-ime-inputmethodengine-selectionchangecallback-t.md) | 是 | 回调函数，返回文本选择信息。<br/>- oldBegin为变化前被选中文本的起始下标，oldEnd为变化前被选中文本的终止下标。&lt; br/&gt;- newBegin为变化后被选中文本的起始下标，newEnd为变化后被选中文本的终止下标。 |

**示例**

```TypeScript
let inputMethodEngineDelegate = inputMethodEngine.getKeyboardDelegate();
if (inputMethodEngineDelegate) {
  inputMethodEngineDelegate!
    .onSelectionChange((oldBegin: int, oldEnd: int, newBegin: int, newEnd: int) => {
      console.info(`inputMethodEngine beforeEach selectionChange oldBegin: ${oldBegin}`);
      console.info(`inputMethodEngine beforeEach selectionChange oldEnd: ${oldEnd}`);
      console.info(`inputMethodEngine beforeEach selectionChange newBegin: ${newBegin}`);
      console.info(`inputMethodEngine beforeEach selectionChange newEnd: ${newEnd}`);
    });

}
```

## onTextChange

```TypeScript
onTextChange(callback: Callback<string>): void
```

**起始版本：** 23

<!--Device-KeyboardDelegate-onTextChange(callback: Callback<string>): void--><!--Device-KeyboardDelegate-onTextChange(callback: Callback<string>): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 是 | 回调函数，返回订阅的文本内容。 |

**示例**

```TypeScript
let inputMethodEngineDelegate = inputMethodEngine.getKeyboardDelegate();
if (inputMethodEngineDelegate) {
  inputMethodEngineDelegate!.onTextChange((text: string) => {
    console.info(`inputMethodEngine textChange. text: ' ${text}`);
  });
}
```

## on('cursorContextChange')

```TypeScript
on(type: 'cursorContextChange', callback: (x: number, y: number, height: number) => void): void
```

**起始版本：** 8

<!--Device-KeyboardDelegate-on(type: 'cursorContextChange', callback: (x: number, y: number, height: number) => void): void--><!--Device-KeyboardDelegate-on(type: 'cursorContextChange', callback: (x: number, y: number, height: number) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'cursorContextChange' | 是 | 光标变化事件，固定取值为'cursorContextChange'。 |
| callback | (x: number, y: number, height: number) =&gt; void | 是 | 回调函数，返回光标信息。<br/>- x为光标上端的x坐标值，单位：px，y为光标上端的y坐标值，单位：px，height为光标的高度值，单位：px。 |

**示例**

```TypeScript
inputMethodEngine.getKeyboardDelegate().on('cursorContextChange', (x: number, y: number, height: number) => {
  console.info('inputMethodEngine cursorContextChange x:' + x);
  console.info('inputMethodEngine cursorContextChange y:' + y);
  console.info('inputMethodEngine cursorContextChange height:' + height);
});
```

## on('editorAttributeChanged')

```TypeScript
on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void
```

**起始版本：** 10

<!--Device-KeyboardDelegate-on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void--><!--Device-KeyboardDelegate-on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'editorAttributeChanged' | 是 | 编辑框属性变化事件，固定取值为'editorAttributeChanged'。 |
| callback | (attr: EditorAttribute) =&gt; void | 是 | 回调函数，返回变化的编辑框属性。 |

**示例**

```TypeScript
inputMethodEngine.getKeyboardDelegate()
  .on('editorAttributeChanged', (editorAttribute: inputMethodEngine.EditorAttribute) => {
    console.info(`Succeeded in receiving attribute of editor, inputPattern = ${editorAttribute.inputPattern}, enterKeyType = ${editorAttribute.enterKeyType}`);
  });
```

## on('keyDown' | 'keyUp')

```TypeScript
on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void
```

**起始版本：** 8

<!--Device-KeyboardDelegate-on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void--><!--Device-KeyboardDelegate-on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | 是 | 设置监听类型。<br/>- 'keyDown'表示键盘按下。<br/>- 'keyUp'表示键盘抬起。 |
| callback | (event: KeyEvent) =&gt; boolean | 是 | 回调函数，返回按键信息。 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。 |

**示例**

```TypeScript
inputMethodEngine.getKeyboardDelegate().on('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info(`inputMethodEngine keyCode.(keyUp): ${keyEvent.keyCode}`);
  console.info(`inputMethodEngine keyAction.(keyUp): ${keyEvent.keyAction}`);
  return true;
});
inputMethodEngine.getKeyboardDelegate().on('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info(`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}`);
  console.info(`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}`);
  return true;
});
```

## on('keyEvent')

```TypeScript
on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void
```

**起始版本：** 10

<!--Device-KeyboardDelegate-on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void--><!--Device-KeyboardDelegate-on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'keyEvent' | 是 | 设置监听类型，固定取值为'keyEvent'。 |
| callback | (event: InputKeyEvent) =&gt; boolean | 是 | 回调函数，入参为按键事件信息，返回值类型为布尔类型。<br/>- 入参按键事件信息的数据类型为 [InputKeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md)。<br/>- 若按键事件被事件订阅者消费，则callback应返回true，否则返回 false。 |

**示例**

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

## on('keyDown' | 'keyUp')

```TypeScript
on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void
```

**起始版本：** 8

<!--Device-KeyboardDelegate-on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void--><!--Device-KeyboardDelegate-on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | 是 | 设置监听类型。<br/>- 'keyDown'表示键盘按下。<br/>- 'keyUp'表示键盘抬起。 |
| callback | (event: KeyEvent) =&gt; boolean | 是 | 回调函数，返回按键信息。 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。 |

**示例**

```TypeScript
inputMethodEngine.getKeyboardDelegate().on('keyUp', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info(`inputMethodEngine keyCode.(keyUp): ${keyEvent.keyCode}`);
  console.info(`inputMethodEngine keyAction.(keyUp): ${keyEvent.keyAction}`);
  return true;
});
inputMethodEngine.getKeyboardDelegate().on('keyDown', (keyEvent: inputMethodEngine.KeyEvent) => {
  console.info(`inputMethodEngine keyCode.(keyDown): ${keyEvent.keyCode}`);
  console.info(`inputMethodEngine keyAction.(keyDown): ${keyEvent.keyAction}`);
  return true;
});
```

## on('selectionChange')

```TypeScript
on(
      type: 'selectionChange',
      callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void
    ): void
```

**起始版本：** 8

<!--Device-KeyboardDelegate-on(      type: 'selectionChange',      callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void    ): void--><!--Device-KeyboardDelegate-on(      type: 'selectionChange',      callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void    ): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'selectionChange' | 是 | 文本选择变化事件，固定取值为'selectionChange'。 |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) =&gt; void | 是 | 回调函数，返回文本选择信息。<br/>- oldBegin为变化前被选中文本的起始下标，oldEnd为变化前被选中文本的终止下标。<br/>- newBegin为变 化后被选中文本的起始下标，newEnd为变化后被选中文本的终止下标。 |

**示例**

```TypeScript
inputMethodEngine.getKeyboardDelegate()
  .on('selectionChange', (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => {
    console.info('selectionChange oldBegin:' + oldBegin);
    console.info('selectionChange oldEnd:' + oldEnd);
    console.info('selectionChange newBegin:' + newBegin);
    console.info('selectionChange newEnd:' + newEnd);
  });
```

## on('textChange')

```TypeScript
on(type: 'textChange', callback: (text: string) => void): void
```

**起始版本：** 8

<!--Device-KeyboardDelegate-on(type: 'textChange', callback: (text: string) => void): void--><!--Device-KeyboardDelegate-on(type: 'textChange', callback: (text: string) => void): void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'textChange' | 是 | 文本变化事件，固定取值为'textChange'。 |
| callback | (text: string) =&gt; void | 是 | 回调函数，返回订阅的文本内容。 |

**示例**

```TypeScript
inputMethodEngine.getKeyboardDelegate().on('textChange', (text: string) => {
  console.info('inputMethodEngine textChange. text:' + text);
});
```

