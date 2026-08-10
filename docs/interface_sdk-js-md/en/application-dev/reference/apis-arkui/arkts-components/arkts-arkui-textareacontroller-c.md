# TextAreaController

TextArea组件的控制器继承自[TextContentControllerBase](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md)，涉及的接口有  
[getTextContentRect](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#gettextcontentrect)、  
[getTextContentLineCount](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#gettextcontentlinecount)、  
[getCaretOffset](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#getcaretoffset)、[addText](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#addtext)、  
[deleteText](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#deletetext)、[getSelection](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#getselection)、[clearPreviewText](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#clearpreviewtext)、  
[setStyledPlaceholder](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#setstyledplaceholder)、  
[deleteBackward](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#deletebackward)、  
[scrollToVisible](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md#scrolltovisible)&lt;!--Del--&gt;以及系统接口  
[getText](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c-sys.md/arkts-arkui-common-textcontentcontrollerbase-c-sys.md#gettext)&lt;!--DelEnd--&gt;。

## 导入对象

```ts controller: TextAreaController = new TextAreaController();```

**Inheritance/Implementation:** TextAreaController extends [TextContentControllerBase](../arkts-apis/arkts-arkui-common-textcontentcontrollerbase-c.md/arkts-arkui-common-textcontentcontrollerbase-c.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare class TextAreaController extends TextContentControllerBase--><!--Device-unnamed-declare class TextAreaController extends TextContentControllerBase-End-->

**System capability:** 
- API version 10 and later: SystemCapability.ArkUI.ArkUI.Full

## caretPosition

```TypeScript
caretPosition(value: number): void
```

设置输入光标的位置。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAreaController-caretPosition(value: number): void--><!--Device-TextAreaController-caretPosition(value: number): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number | Yes | 从字符串开始到光标所在位置的字符长度。 &lt;br&gt;当value&lt;0时，按照0处理。当value&gt;字符串长度时，按照字符串长度处理。 |

## constructor

```TypeScript
constructor()
```

TextAreaController的构造函数。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAreaController-constructor()--><!--Device-TextAreaController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void
```

组件在获焦状态下，调用该接口设置文本选择区域并高亮显示，且只有在selectionStart小于selectionEnd时，文字才会被选取、高亮显示。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAreaController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void--><!--Device-TextAreaController-setTextSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | number | Yes | 文本选择区域起始位置，文本框中文字的起始位置为0。 &lt;br&gt;当selectionStart小于0时，按0处理；当selectionStart大于文字最大长度时，按照文字最大长度处理。 |
| selectionEnd | number | Yes | 文本选择区域结束位置。 &lt;br&gt;当selectionEnd小于0时，按0处理；当selectionEnd大于文字最大长度时，按照文字最大长度处理。 |
| options | [SelectionOptions](../arkts-apis/arkts-arkui-common-selectionoptions-i.md) | No | 选中文字时的配置。 &lt;br&gt;默认值：MenuPolicy.DEFAULT<br>**Since:** 12 |

## stopEditing

```TypeScript
stopEditing(): void
```

退出编辑态。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAreaController-stopEditing(): void--><!--Device-TextAreaController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

