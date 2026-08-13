# TextAreaController

TextArea组件的控制器继承自[TextContentControllerBase](arkts-arkui-textcontentcontrollerbase-c.md#TextContentControllerBase)，涉及的接口有 [getTextContentRect](arkts-arkui-textcontentcontrollerbase-c.md#getTextContentRect)、 [getTextContentLineCount](arkts-arkui-textcontentcontrollerbase-c.md#getTextContentLineCount)、 getCaretOffset、addText、 [deleteText](arkts-arkui-textcontentcontrollerbase-c.md#deleteText)、getSelection 、[clearPreviewText](arkts-arkui-textcontentcontrollerbase-c.md#clearPreviewText)、 setStyledPlaceholder、 deleteBackward、 scrollToVisible&lt;!--Del--&gt;以及系统接口 getText&lt;!--DelEnd--&gt;。

## 导入对象 ```ts controller: TextAreaController = new TextAreaController(); ```

**继承/实现关系：** TextAreaController extends [TextContentControllerBase](arkts-arkui-textcontentcontrollerbase-c.md#TextContentControllerBase)

**起始版本：** 8

**废弃版本：** -1

<!--Device-unnamed-declare class TextAreaController--><!--Device-unnamed-declare class TextAreaController-End-->

**系统能力：** 
- API版本10+：SystemCapability.ArkUI.ArkUI.Full

## caretPosition

```TypeScript
caretPosition(value: number): void
```

设置输入光标的位置。

**起始版本：** 8

**废弃版本：** -1

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

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-TextAreaController-constructor()--><!--Device-TextAreaController-constructor()-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void
```

组件在获焦状态下，调用该接口设置文本选择区域并高亮显示，且只有在selectionStart小于selectionEnd时，文字才会被选取、高亮显示。

**起始版本：** 10

**废弃版本：** -1

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

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-TextAreaController-stopEditing(): void--><!--Device-TextAreaController-stopEditing(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
