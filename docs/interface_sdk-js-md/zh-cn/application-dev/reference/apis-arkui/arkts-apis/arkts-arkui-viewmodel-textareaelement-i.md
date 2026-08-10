# TextAreaElement

The &lt;textarea&gt; component provides an interactive interface to receive user input, which is displayed in multiple lines by default.

**继承/实现关系：** TextAreaElement extends [Element](arkts-arkui-viewmodel-element-i.md)

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

<!--Device-unnamed-export interface TextAreaElement extends Element--><!--Device-unnamed-export interface TextAreaElement extends Element-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## focus

```TypeScript
focus(param: { focus: boolean }): void
```

Obtains or loses the focus of a component, which can display or collapse the input method.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-TextAreaElement-focus(param: { focus: boolean }): void--><!--Device-TextAreaElement-focus(param: { focus: boolean }): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | { focus: boolean } | 是 | If focus is not passed, the default value true is used. |

