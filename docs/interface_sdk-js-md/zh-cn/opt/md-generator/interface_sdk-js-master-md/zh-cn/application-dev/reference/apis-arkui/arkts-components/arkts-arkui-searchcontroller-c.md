# SearchController

Search组件的控制器继承自[TextContentControllerBase](arkts-arkui-textcontentcontrollerbase-c.md#TextContentControllerBase)，涉及的接口有 [getTextContentRect](arkts-arkui-textcontentcontrollerbase-c.md#getTextContentRect)、 [getTextContentLineCount](arkts-arkui-textcontentcontrollerbase-c.md#getTextContentLineCount)、 getCaretOffset、addText、 [deleteText](arkts-arkui-textcontentcontrollerbase-c.md#deleteText)、getSelection 、[clearPreviewText](arkts-arkui-textcontentcontrollerbase-c.md#clearPreviewText)、 setStyledPlaceholder、 deleteBackward、 scrollToVisible&lt;!--Del--&gt;以及系统接口 getText&lt;!--DelEnd--&gt;。

## 导入对象 ```ts controller: SearchController = new SearchController(); ```

**继承/实现关系：** SearchController extends [TextContentControllerBase](arkts-arkui-textcontentcontrollerbase-c.md#TextContentControllerBase)

**起始版本：** 8

**废弃版本：** -1

<!--Device-unnamed-declare class SearchController--><!--Device-unnamed-declare class SearchController-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## caretPosition

```TypeScript
caretPosition(value: number): void
```

设置输入光标的位置。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-SearchController-caretPosition(value: number): void--><!--Device-SearchController-caretPosition(value: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| value | number | 是 |

## constructor

```TypeScript
constructor()
```

SearchController的构造函数。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-SearchController-constructor()--><!--Device-SearchController-constructor()-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void
```

组件在获焦状态下，调用该接口设置文本选择区域并高亮显示，且只有在selectionStart小于selectionEnd时，文字才会被选取并高亮显示。 > **说明：** > > - 如果selectionStart或selectionEnd被赋值为undefined时，当作0处理。 > > - 如果selectionMenuHidden被赋值为true或设备为2in1时，即使options被赋值为MenuPolicy.SHOW，调用setTextSelection也不弹出菜单。 > > - 如果选中的文本含有emoji表情时，表情的起始位置包含在设置的文本选中区域内就会被选中。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-SearchController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void--><!--Device-SearchController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void-End-->

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

<!--Device-SearchController-stopEditing(): void--><!--Device-SearchController-stopEditing(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
