# KeyboardDelegate

KeyboardDelegate是键盘事件监听代理对象，用于输入法应用监听物理键盘按键事件和编辑框文本/光标/选区变化事件。输入法应用通过  
[getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getkeyboarddelegate)获取该实例。  
**核心功能概述：**

- **物理键盘按键事件**：通过on('keyDown'|'keyUp')订阅物理按键的按下/抬起事件，通过on('keyEvent')订阅更完整的按键事件（含组合键信息）。callback返回true表示按键事件被消费，返回  
false表示不消费。  
- **光标与选区变化事件**：通过on('cursorContextChange')订阅光标位置变化事件，通过on('selectionChange')订阅文本选区变化事件。输入法应用可根据这些事件调整候选词位置或输入策略。  
- **文本变化事件**：通过on('textChange')订阅编辑框文本内容变化事件，输入法应用可据此更新候选词或输入建议。  
- **编辑框属性变化事件**：通过on('editorAttributeChanged')订阅编辑框属性变化事件，输入法应用可根据编辑框属性变化动态调整键盘布局。  
**使用场景：**  
- 开发物理键盘快捷键处理功能时，订阅on('keyDown'|'keyUp')或on('keyEvent')事件拦截特定按键。  
- 需要根据编辑框实时状态（光标、选区、文本、属性）调整输入法行为时，订阅对应的on事件。

下列API均需使用[getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md#getkeyboarddelegate)获取到KeyboardDelegate实例后，通过实例调用。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-inputMethodEngine-interface KeyboardDelegate--><!--Device-inputMethodEngine-interface KeyboardDelegate-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## off('keyDown' | 'keyUp')

```TypeScript
off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void
```

取消订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-KeyboardDelegate-off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void--><!--Device-KeyboardDelegate-off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | Yes | 设置监听类型。&lt;br/&gt;- 'keyDown'表示键盘按下。&lt;br/&gt;- 'keyUp'表示键盘抬起。 |
| callback | (event: KeyEvent) =&gt; boolean | No | 取消订阅的回调函数，用于取消特定的键盘按键事件订阅。传入callback时取消指定回调的订阅，参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

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

## off('keyDown' | 'keyUp')

```TypeScript
off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void
```

取消订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-KeyboardDelegate-off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void--><!--Device-KeyboardDelegate-off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | Yes | 设置监听类型。&lt;br/&gt;- 'keyDown'表示键盘按下。&lt;br/&gt;- 'keyUp'表示键盘抬起。 |
| callback | (event: KeyEvent) =&gt; boolean | No | 取消订阅的回调函数，用于取消特定的键盘按键事件订阅。传入callback时取消指定回调的订阅，参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

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

取消订阅硬键盘（即物理键盘）事件。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-KeyboardDelegate-off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void--><!--Device-KeyboardDelegate-off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyEvent' | Yes | 设置监听类型，固定取值为'keyEvent'。 |
| callback | (event: InputKeyEvent) =&gt; boolean | No | 取消订阅的回调函数，用于取消特定的键盘事件订阅。传入callback时取消指定回调的订阅，参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
import type { KeyEvent } from '@kit.InputKit';

inputMethodEngine.getKeyboardDelegate().off('keyEvent', (keyEvent: KeyEvent) => {
  console.info('This is a callback function which will be deregistered.');
  return true;
});
inputMethodEngine.getKeyboardDelegate().off('keyEvent');
```

## off('cursorContextChange')

```TypeScript
off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void
```

取消订阅光标变化事件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-KeyboardDelegate-off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void--><!--Device-KeyboardDelegate-off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cursorContextChange' | Yes | 光标变化事件，固定取值为'cursorContextChange'。 |
| callback | (x: number, y: number, height: number) =&gt; void | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethodEngine.getKeyboardDelegate().off('cursorContextChange', (x: number, y: number, height: number) => {
  console.info('delete cursorContextChange notification.');
});
```

## off('selectionChange')

```TypeScript
off(
      type: 'selectionChange',
      callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void
    ): void
```

取消订阅文本选择范围变化事件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-KeyboardDelegate-off(      type: 'selectionChange',      callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void    ): void--><!--Device-KeyboardDelegate-off(      type: 'selectionChange',      callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void    ): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'selectionChange' | Yes | 文本选择变化事件，固定取值为'selectionChange'。 |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) =&gt; void | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

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

取消订阅文本内容变化事件。使用callback异步回调。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-KeyboardDelegate-off(type: 'textChange', callback?: (text: string) => void): void--><!--Device-KeyboardDelegate-off(type: 'textChange', callback?: (text: string) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'textChange' | Yes | 文本变化事件，固定取值为'textChange'。 |
| callback | (text: string) =&gt; void | No | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethodEngine.getKeyboardDelegate().off('textChange', (text: string) => {
  console.info('delete textChange notification. text:' + text);
});
```

## off('editorAttributeChanged')

```TypeScript
off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void
```

取消订阅编辑框属性变化事件。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-KeyboardDelegate-off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void--><!--Device-KeyboardDelegate-off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'editorAttributeChanged' | Yes | 编辑框属性变化事件，固定取值为'editorAttributeChanged'。 |
| callback | (attr: EditorAttribute) =&gt; void | No | 所要取消订阅的回调处理函数。参数不填写时，默认取消订阅type对应的所有回调事件。 |

## Examples

```TypeScript
inputMethodEngine.getKeyboardDelegate().off('editorAttributeChanged');
```

## offCursorContextChange

```TypeScript
offCursorContextChange(callback?: CursorContextChangeCallback): void
```

取消订阅光标上下文变更cursorcontextchange事件，停止监听编辑框中光标位置及上下文文本的变更动作。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-KeyboardDelegate-offCursorContextChange(callback?: CursorContextChangeCallback): void--><!--Device-KeyboardDelegate-offCursorContextChange(callback?: CursorContextChangeCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [CursorContextChangeCallback](arkts-ime-inputmethodengine-cursorcontextchangecallback-t.md) | No | 取消订阅的回调函数。 参数不填写时，取消订阅type对应的所有回调事件。 changes. |

## offEditorAttributeChanged

```TypeScript
offEditorAttributeChanged(callback?: Callback<EditorAttribute>): void
```

取消订阅编辑框属性变化事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-KeyboardDelegate-offEditorAttributeChanged(callback?: Callback<EditorAttribute>): void--><!--Device-KeyboardDelegate-offEditorAttributeChanged(callback?: Callback<EditorAttribute>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;EditorAttribute&gt; | No | 所要取消订阅的回调处理函数。 参数不填写时，取消订阅type对应的所有回调事件。 |

## offKeyDown

```TypeScript
offKeyDown(callback?: KeyEventCallback): void
```

取消订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-KeyboardDelegate-offKeyDown(callback?: KeyEventCallback): void--><!--Device-KeyboardDelegate-offKeyDown(callback?: KeyEventCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) | No | 取消订阅的回调函数。 参数不填写时，取消订阅type对应的所有回调事件。 |

## offKeyEvent

```TypeScript
offKeyEvent(callback?: InputKeyEventCallback): void
```

取消订阅硬键盘（即物理键盘）事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-KeyboardDelegate-offKeyEvent(callback?: InputKeyEventCallback): void--><!--Device-KeyboardDelegate-offKeyEvent(callback?: InputKeyEventCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [InputKeyEventCallback](arkts-ime-inputmethodengine-inputkeyeventcallback-t.md) | No | 取消订阅的回调函数。 参数不填写时，取消订阅type对应的所有回调事件。 |

## offKeyUp

```TypeScript
offKeyUp(callback?: KeyEventCallback): void
```

取消订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-KeyboardDelegate-offKeyUp(callback?: KeyEventCallback): void--><!--Device-KeyboardDelegate-offKeyUp(callback?: KeyEventCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) | No | 取消订阅的回调函数。 参数不填写时，取消订阅type对应的所有回调事件。 |

## offSelectionChange

```TypeScript
offSelectionChange(callback?: SelectionChangeCallback): void
```

取消订阅文本选择范围变化事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-KeyboardDelegate-offSelectionChange(callback?: SelectionChangeCallback): void--><!--Device-KeyboardDelegate-offSelectionChange(callback?: SelectionChangeCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SelectionChangeCallback](arkts-ime-inputmethodengine-selectionchangecallback-t.md) | No | 取消订阅的回调函数。 参数不填写时，取消订阅type对应的所有回调事件。 |

## offTextChange

```TypeScript
offTextChange(callback?: Callback<string>): void
```

取消订阅文本内容变化事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-KeyboardDelegate-offTextChange(callback?: Callback<string>): void--><!--Device-KeyboardDelegate-offTextChange(callback?: Callback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | No | 取消订阅的回调函数。 参数不填写时，取消订阅type对应的所有回调事件。 |

## on('keyDown' | 'keyUp')

```TypeScript
on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void
```

订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。

**使用场景：** 实现快捷键功能、拦截特殊按键、处理功能键（如删除、回车等）等。

**使用后效果：** 当物理按键按下/抬起时触发回调，回调函数返回按键信息。若按键事件被事件订阅者消费，则callback应返回true，否则返回false。返回true时按键事件不再向编辑框传递，返回false时按键事件继续向编辑框传递。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-KeyboardDelegate-on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void--><!--Device-KeyboardDelegate-on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | Yes | 设置监听类型。&lt;br/&gt;- 'keyDown'表示键盘按下。&lt;br/&gt;- 'keyUp'表示键盘抬起。 |
| callback | (event: KeyEvent) =&gt; boolean | Yes | 回调函数，返回按键信息。 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。 |

## Examples

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

## on('keyDown' | 'keyUp')

```TypeScript
on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void
```

订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。

**使用场景：** 实现快捷键功能、拦截特殊按键、处理功能键（如删除、回车等）等。

**使用后效果：** 当物理按键按下/抬起时触发回调，回调函数返回按键信息。若按键事件被事件订阅者消费，则callback应返回true，否则返回false。返回true时按键事件不再向编辑框传递，返回false时按键事件继续向编辑框传递。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-KeyboardDelegate-on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void--><!--Device-KeyboardDelegate-on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | Yes | 设置监听类型。&lt;br/&gt;- 'keyDown'表示键盘按下。&lt;br/&gt;- 'keyUp'表示键盘抬起。 |
| callback | (event: KeyEvent) =&gt; boolean | Yes | 回调函数，返回按键信息。 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。 |

## Examples

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

订阅硬键盘（即物理键盘）事件。使用callback异步回调。与on('keyDown'|'keyUp')相比，on('keyEvent')提供更完整的按键事件信息（包含组合键Ctrl/Shift/Alt状态、unicodeChar等），适用于需要处理组合键或获取更丰富按键信息的场景。

**使用场景：** 需要处理组合键（如Ctrl+C、Shift+Enter等）或获取更完整按键信息（如unicodeChar、ctrlKey等）的场景。

**使用后效果：** 当物理按键事件触发时回调被调用。若按键事件被事件订阅者消费，则callback应返回true，否则返回false。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-KeyboardDelegate-on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void--><!--Device-KeyboardDelegate-on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'keyEvent' | Yes | 设置监听类型，固定取值为'keyEvent'。 |
| callback | (event: InputKeyEvent) =&gt; boolean | Yes | 回调函数，入参为按键事件信息，返回值类型为布尔类型。&lt;br/&gt;- 入参按键事件信息的数据类型为 [InputKeyEvent](arkts-ime-inputmethodengine-keyevent-i.md)。&lt;br/&gt;- 若按键事件被事件订阅者消费，则callback应返回true，否则返回 false。 |

## Examples

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

## on('cursorContextChange')

```TypeScript
on(type: 'cursorContextChange', callback: (x: number, y: number, height: number) => void): void
```

订阅光标变化事件。使用callback异步回调。

**使用场景：** 实时更新候选词显示位置、根据光标位置调整输入法界面、实现跟随光标的浮动菜单等。

**使用后效果：** 当编辑框光标位置发生变化时触发回调，返回光标的x坐标、y坐标和高度信息，输入法应用可据此调整候选词窗口或面板的定位。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-KeyboardDelegate-on(type: 'cursorContextChange', callback: (x: number, y: number, height: number) => void): void--><!--Device-KeyboardDelegate-on(type: 'cursorContextChange', callback: (x: number, y: number, height: number) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cursorContextChange' | Yes | 光标变化事件，固定取值为'cursorContextChange'。 |
| callback | (x: number, y: number, height: number) =&gt; void | Yes | 回调函数，返回光标信息。&lt;br/&gt;- x为光标上端的x坐标值，单位：px，y为光标上端的y坐标值，单位：px，height为光标的高度值，单位：px。 |

## Examples

```TypeScript
inputMethodEngine.getKeyboardDelegate().on('cursorContextChange', (x: number, y: number, height: number) => {
  console.info('inputMethodEngine cursorContextChange x:' + x);
  console.info('inputMethodEngine cursorContextChange y:' + y);
  console.info('inputMethodEngine cursorContextChange height:' + height);
});
```

## on('selectionChange')

```TypeScript
on(
      type: 'selectionChange',
      callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void
    ): void
```

订阅文本选择范围变化事件。使用callback异步回调。

**使用场景：** 监听用户选中文本以提供剪切、复制、粘贴等快捷操作、根据选择文本显示相关建议、实现文本编辑辅助功能等。

**使用后效果：** 当编辑框中文本选择范围发生变化时触发回调，返回变化前后的选区起始和终止下标。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-KeyboardDelegate-on(      type: 'selectionChange',      callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void    ): void--><!--Device-KeyboardDelegate-on(      type: 'selectionChange',      callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void    ): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'selectionChange' | Yes | 文本选择变化事件，固定取值为'selectionChange'。 |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) =&gt; void | Yes | 回调函数，返回文本选择信息。&lt;br/&gt;- oldBegin为变化前被选中文本的起始下标，oldEnd为变化前被选中文本的终止下标。&lt;br/&gt;- newBegin为变 化后被选中文本的起始下标，newEnd为变化后被选中文本的终止下标。 |

## Examples

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

订阅文本内容变化事件。使用callback异步回调。

**使用场景：** 输入法应用需要根据编辑框文本内容变化更新候选词、提供智能输入建议、实现联想输入等。

**使用后效果：** 当编辑框文本内容发生变化时触发回调，返回当前编辑框的完整文本内容。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-KeyboardDelegate-on(type: 'textChange', callback: (text: string) => void): void--><!--Device-KeyboardDelegate-on(type: 'textChange', callback: (text: string) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'textChange' | Yes | 文本变化事件，固定取值为'textChange'。 |
| callback | (text: string) =&gt; void | Yes | 回调函数，返回订阅的文本内容。 |

## Examples

```TypeScript
inputMethodEngine.getKeyboardDelegate().on('textChange', (text: string) => {
  console.info('inputMethodEngine textChange. text:' + text);
});
```

## on('editorAttributeChanged')

```TypeScript
on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void
```

订阅编辑框属性变化事件。使用callback异步回调。

**使用场景：** 输入法应用需要根据编辑框属性变化（如输入类型从文本切换到数字、回车键类型从"搜索"切换到"发送"等）动态调整键盘布局。

**使用后效果：** 当编辑框属性发生变化时触发回调，返回变化后的编辑框属性信息（包括inputPattern和enterKeyType），输入法应用可据此重新调整键盘布局。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-KeyboardDelegate-on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void--><!--Device-KeyboardDelegate-on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'editorAttributeChanged' | Yes | 编辑框属性变化事件，固定取值为'editorAttributeChanged'。 |
| callback | (attr: EditorAttribute) =&gt; void | Yes | 回调函数，返回变化的编辑框属性。 |

## Examples

```TypeScript
inputMethodEngine.getKeyboardDelegate()
  .on('editorAttributeChanged', (attr: inputMethodEngine.EditorAttribute) => {
    console.info(`Succeeded in receiving attribute of editor, inputPattern = ${attr.inputPattern}, enterKeyType = ${attr.enterKeyType}`);
  });
```

## onCursorContextChange

```TypeScript
onCursorContextChange(callback: CursorContextChangeCallback): void
```

订阅光标变化事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-KeyboardDelegate-onCursorContextChange(callback: CursorContextChangeCallback): void--><!--Device-KeyboardDelegate-onCursorContextChange(callback: CursorContextChangeCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [CursorContextChangeCallback](arkts-ime-inputmethodengine-cursorcontextchangecallback-t.md) | Yes | 回调函数，返回光标信息。 x为光标上端的的x坐标值，单位为px。y为光标上端的y坐标值，单位为px。height为光标的高度值，单位为px。 |

## onEditorAttributeChanged

```TypeScript
onEditorAttributeChanged(callback: Callback<EditorAttribute>): void
```

订阅编辑框属性变化事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-KeyboardDelegate-onEditorAttributeChanged(callback: Callback<EditorAttribute>): void--><!--Device-KeyboardDelegate-onEditorAttributeChanged(callback: Callback<EditorAttribute>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;EditorAttribute&gt; | Yes | 回调函数，返回变化的编辑框属性。 |

## onKeyDown

```TypeScript
onKeyDown(callback: KeyEventCallback): void
```

订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-KeyboardDelegate-onKeyDown(callback: KeyEventCallback): void--><!--Device-KeyboardDelegate-onKeyDown(callback: KeyEventCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) | Yes | 回调函数，返回按键信息。 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。 |

## onKeyEvent

```TypeScript
onKeyEvent(callback: InputKeyEventCallback): void
```

订阅硬键盘（即物理键盘）事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-KeyboardDelegate-onKeyEvent(callback: InputKeyEventCallback): void--><!--Device-KeyboardDelegate-onKeyEvent(callback: InputKeyEventCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [InputKeyEventCallback](arkts-ime-inputmethodengine-inputkeyeventcallback-t.md) | Yes | 回调函数，入参为按键事件信息，返回值类型为布尔类型。 入参按键事件信息的数据类型为InputKeyEvent。 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。 |

## onKeyUp

```TypeScript
onKeyUp(callback: KeyEventCallback): void
```

订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-KeyboardDelegate-onKeyUp(callback: KeyEventCallback): void--><!--Device-KeyboardDelegate-onKeyUp(callback: KeyEventCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [KeyEventCallback](arkts-ime-inputmethodengine-keyeventcallback-t.md) | Yes | 回调函数，返回按键信息。 若按键事件被事件订阅者消费，则callback应返回true，否则返回false。 |

## onSelectionChange

```TypeScript
onSelectionChange(callback: SelectionChangeCallback): void
```

订阅文本选择范围变化事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-KeyboardDelegate-onSelectionChange(callback: SelectionChangeCallback): void--><!--Device-KeyboardDelegate-onSelectionChange(callback: SelectionChangeCallback): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [SelectionChangeCallback](arkts-ime-inputmethodengine-selectionchangecallback-t.md) | Yes | 回调函数，返回文本选择信息。 oldBegin为变化前被选中文本的起始下标，oldEnd为变化前被选中文本的终止下标。 newBegin为变化后被选中文本的起始下标，newEnd为变化后被选中文本的终止下标。 |

## onTextChange

```TypeScript
onTextChange(callback: Callback<string>): void
```

订阅文本内容变化事件。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-KeyboardDelegate-onTextChange(callback: Callback<string>): void--><!--Device-KeyboardDelegate-onTextChange(callback: Callback<string>): void-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | Yes | 回调函数，返回订阅的文本内容。 |

