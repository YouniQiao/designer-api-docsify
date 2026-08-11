# TextAreaController

TextArea组件的控制器继承自[TextContentControllerBase](arkts-arkui-textcontentcontrollerbase-c.md)，涉及的接口有  
[getTextContentRect](arkts-arkui-textcontentcontrollerbase-c.md#gettextcontentrect)、  
[getTextContentLineCount](arkts-arkui-textcontentcontrollerbase-c.md#gettextcontentlinecount)、  
[getCaretOffset](arkts-arkui-textcontentcontrollerbase-c.md#getcaretoffset)、[addText](arkts-arkui-textcontentcontrollerbase-c.md#addtext)、  
[deleteText](arkts-arkui-textcontentcontrollerbase-c.md#deletetext)、[getSelection](arkts-arkui-textcontentcontrollerbase-c.md#getselection)、[clearPreviewText](arkts-arkui-textcontentcontrollerbase-c.md#clearpreviewtext)、  
[setStyledPlaceholder](arkts-arkui-textcontentcontrollerbase-c.md#setstyledplaceholder)、  
[deleteBackward](arkts-arkui-textcontentcontrollerbase-c.md#deletebackward)、  
[scrollToVisible](arkts-arkui-textcontentcontrollerbase-c.md#scrolltovisible)&lt;!--Del--&gt;以及系统接口  
[getText](arkts-arkui-textcontentcontrollerbase-c-sys.md#gettext)&lt;!--DelEnd--&gt;。

## 导入对象

```ts controller: TextAreaController = new TextAreaController();```

**继承/实现关系：** TextAreaController extends [TextContentControllerBase](arkts-arkui-textcontentcontrollerbase-c.md)

**起始版本：** 8

<!--Device-unnamed-declare class TextAreaController extends TextContentControllerBase--><!--Device-unnamed-declare class TextAreaController extends TextContentControllerBase-End-->

**系统能力：** 
- API版本10+：SystemCapability.ArkUI.ArkUI.Full

## caretPosition

```TypeScript
caretPosition(value: number): void
```

设置输入光标的位置。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-TextAreaController-caretPosition(value: number): void--><!--Device-TextAreaController-caretPosition(value: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## constructor

```TypeScript
constructor()
```

TextAreaController的构造函数。

**起始版本：** 8

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-TextAreaController-constructor()--><!--Device-TextAreaController-constructor()-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void
```

组件在获焦状态下，调用该接口设置文本选择区域并高亮显示，且只有在selectionStart小于selectionEnd时，文字才会被选取、高亮显示。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-TextAreaController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void--><!--Device-TextAreaController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| selectionStart | number | 是 |
| selectionEnd | number | 是 |
| options | [SelectionOptions](arkts-arkui-selectionoptions-i.md) | 否 |

## stopEditing

```TypeScript
stopEditing(): void
```

退出编辑态。

**起始版本：** 10

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-TextAreaController-stopEditing(): void--><!--Device-TextAreaController-stopEditing(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
