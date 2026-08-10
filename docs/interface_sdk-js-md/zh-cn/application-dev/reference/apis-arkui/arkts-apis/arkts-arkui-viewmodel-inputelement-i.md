# InputElement

The &lt;input&gt; component provides an interactive interface to receive user input, which is displayed in a single line by default.

**继承/实现关系：** InputElement extends [Element](arkts-arkui-viewmodel-element-i.md)

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

<!--Device-unnamed-export interface InputElement extends Element--><!--Device-unnamed-export interface InputElement extends Element-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## delete

```TypeScript
delete(): void
```

Deletes the previous character at the cursor position.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-InputElement-delete(): void--><!--Device-InputElement-delete(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## focus

```TypeScript
focus(param: { focus: boolean }): void
```

Obtains or loses the focus of a component.When the component type is set to text, email, date, time, number, or password, the input method can be displayed or collapsed.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-InputElement-focus(param: { focus: boolean }): void--><!--Device-InputElement-focus(param: { focus: boolean }): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | { focus: boolean } | 是 | If focus is not passed, the default value true is used. |

## showError

```TypeScript
showError(param: { error: string }): void
```

Displays the error message.This attribute is available when the component type is set to text, email, date, time, number, or password.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-InputElement-showError(param: { error: string }): void--><!--Device-InputElement-showError(param: { error: string }): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | { error: string } | 是 |  |

