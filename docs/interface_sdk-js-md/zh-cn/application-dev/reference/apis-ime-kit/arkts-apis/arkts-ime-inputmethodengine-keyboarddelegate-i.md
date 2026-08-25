# KeyboardDelegate

KeyboardDelegate是键盘事件监听代理对象，用于输入法应用监听物理键盘按键事件和编辑框文本/光标/选区变化事件。输入法应用通过 [getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md)获取该实例。 核心功能概述：   
- 物理键盘按键事件：通过on('keyDown'|'keyUp')订阅物理按键的按下/抬起事件，通过on('keyEvent')订阅更完整的按键事件（含组合键信息）。callback返回true表示按键事件被消费，返回false 表示不消费。   
- 光标与选区变化事件：通过on('cursorContextChange')订阅光标位置变化事件，通过on('selectionChange')订阅文本选区变化事件。输入法应用可根据这些事件调整候选词位置或输入策略。   
- 文本变化事件：通过on('textChange')订阅编辑框文本内容变化事件，输入法应用可据此更新候选词或输入建议。   
- 编辑框属性变化事件：通过on('editorAttributeChanged')订阅编辑框属性变化事件，输入法应用可根据编辑框属性变化动态调整键盘布局。   
 使用场景：   
- 开发物理键盘快捷键处理功能时，订阅on('keyDown'|'keyUp')或on('keyEvent')事件拦截特定按键。   
- 需要根据编辑框实时状态（光标、选区、文本、属性）调整输入法行为时，订阅对应的on事件。   
 下列API均需使用[getKeyboardDelegate](arkts-ime-inputmethodengine-getkeyboarddelegate-f.md)获取到KeyboardDelegate实例后，通过实例调用。

**起始版本：** 8

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

## 导入模块

```TypeScript
import { inputMethodEngine } from 'kits/@kit.IMEKit';
```

## off('keyDown' | 'keyUp')

```TypeScript
off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void
```

取消订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。

**起始版本：** 8

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | 是 |
| callback | (event: KeyEvent) = & gt; boolean | 否 |

## off('keyDown' | 'keyUp')

```TypeScript
off(type: 'keyDown' | 'keyUp', callback?: (event: KeyEvent) => boolean): void
```

取消订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。

**起始版本：** 8

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | 是 |
| callback | (event: KeyEvent) = & gt; boolean | 否 |

## off('keyEvent')

```TypeScript
off(type: 'keyEvent', callback?: (event: InputKeyEvent) => boolean): void
```

取消订阅硬键盘（即物理键盘）事件。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyEvent' | 是 |
| callback | (event: InputKeyEvent) = & gt; boolean | 否 |

## off('cursorContextChange')

```TypeScript
off(type: 'cursorContextChange', callback?: (x: number, y: number, height: number) => void): void
```

取消订阅光标变化事件。

**起始版本：** 8

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cursorContextChange' | 是 |
| callback | (x: number, y: number, height: number) = & gt; void | 否 |

## off('selectionChange')

```TypeScript
off(
      type: 'selectionChange',
      callback?: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void
    ): void
```

取消订阅文本选择范围变化事件。

**起始版本：** 8

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'selectionChange' | 是 |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) = & gt; void | 否 |

## off('textChange')

```TypeScript
off(type: 'textChange', callback?: (text: string) => void): void
```

取消订阅文本内容变化事件。使用callback异步回调。

**起始版本：** 8

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'textChange' | 是 |
| callback | (text: string) = & gt; void | 否 |

## off('editorAttributeChanged')

```TypeScript
off(type: 'editorAttributeChanged', callback?: (attr: EditorAttribute) => void): void
```

取消订阅编辑框属性变化事件。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'editorAttributeChanged' | 是 |
| callback | (attr: EditorAttribute) = & gt; void | 否 |

## on('keyDown' | 'keyUp')

```TypeScript
on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void
```

订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。 使用场景：实现快捷键功能、拦截特殊按键、处理功能键（如删除、回车等）等。 使用后效果：当物理按键按下/抬起时触发回调，回调函数返回按键信息。若按键事件被事件订阅者消费，则callback应返回true，否则返回false。返回true时按键事件不再向编辑框传递，返回false时按键事件继续向编辑框传 递。

**起始版本：** 8

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | 是 |
| callback | (event: KeyEvent) = & gt; boolean | 是 |

## on('keyDown' | 'keyUp')

```TypeScript
on(type: 'keyDown' | 'keyUp', callback: (event: KeyEvent) => boolean): void
```

订阅硬键盘（即物理键盘）上物理按键的按下或抬起事件。使用callback异步回调。 使用场景：实现快捷键功能、拦截特殊按键、处理功能键（如删除、回车等）等。 使用后效果：当物理按键按下/抬起时触发回调，回调函数返回按键信息。若按键事件被事件订阅者消费，则callback应返回true，否则返回false。返回true时按键事件不再向编辑框传递，返回false时按键事件继续向编辑框传 递。

**起始版本：** 8

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyDown' \| 'keyUp' | 是 |
| callback | (event: KeyEvent) = & gt; boolean | 是 |

## on('keyEvent')

```TypeScript
on(type: 'keyEvent', callback: (event: InputKeyEvent) => boolean): void
```

订阅硬键盘（即物理键盘）事件。使用callback异步回调。与on('keyDown'|'keyUp')相比，on('keyEvent')提供更完整的按键事件信息（包含组合键Ctrl/Shift/Alt状态、 unicodeChar等），适用于需要处理组合键或获取更丰富按键信息的场景。 使用场景：需要处理组合键（如Ctrl+C、Shift+Enter等）或获取更完整按键信息（如unicodeChar、ctrlKey等）的场景。 使用后效果：当物理按键事件触发时回调被调用。若按键事件被事件订阅者消费，则callback应返回true，否则返回false。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'keyEvent' | 是 |
| callback | (event: InputKeyEvent) = & gt; boolean | 是 |

## on('cursorContextChange')

```TypeScript
on(type: 'cursorContextChange', callback: (x: number, y: number, height: number) => void): void
```

订阅光标变化事件。使用callback异步回调。 使用场景：实时更新候选词显示位置、根据光标位置调整输入法界面、实现跟随光标的浮动菜单等。 使用后效果：当编辑框光标位置发生变化时触发回调，返回光标的x坐标、y坐标和高度信息，输入法应用可据此调整候选词窗口或面板的定位。

**起始版本：** 8

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cursorContextChange' | 是 |
| callback | (x: number, y: number, height: number) = & gt; void | 是 |

## on('selectionChange')

```TypeScript
on(
      type: 'selectionChange',
      callback: (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void
    ): void
```

订阅文本选择范围变化事件。使用callback异步回调。 使用场景：监听用户选中文本以提供剪切、复制、粘贴等快捷操作、根据选择文本显示相关建议、实现文本编辑辅助功能等。 使用后效果：当编辑框中文本选择范围发生变化时触发回调，返回变化前后的选区起始和终止下标。

**起始版本：** 8

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'selectionChange' | 是 |
| callback | (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) = & gt; void | 是 |

## on('textChange')

```TypeScript
on(type: 'textChange', callback: (text: string) => void): void
```

订阅文本内容变化事件。使用callback异步回调。 使用场景：输入法应用需要根据编辑框文本内容变化更新候选词、提供智能输入建议、实现联想输入等。 使用后效果：当编辑框文本内容发生变化时触发回调，返回当前编辑框的完整文本内容。

**起始版本：** 8

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'textChange' | 是 |
| callback | (text: string) = & gt; void | 是 |

## on('editorAttributeChanged')

```TypeScript
on(type: 'editorAttributeChanged', callback: (attr: EditorAttribute) => void): void
```

订阅编辑框属性变化事件。使用callback异步回调。 使用场景：输入法应用需要根据编辑框属性变化（如输入类型从文本切换到数字、回车键类型从"搜索"切换到"发送"等）动态调整键盘布局。 使用后效果：当编辑框属性发生变化时触发回调，返回变化后的编辑框属性信息（包括inputPattern和enterKeyType），输入法应用可据此重新调整键盘布局。

**起始版本：** 10

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'editorAttributeChanged' | 是 |
| callback | (attr: EditorAttribute) = & gt; void | 是 |
