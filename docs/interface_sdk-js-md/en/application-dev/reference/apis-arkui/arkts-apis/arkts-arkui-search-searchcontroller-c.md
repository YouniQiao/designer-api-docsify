# SearchController

Search组件的控制器继承自  
[TextContentControllerBase](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#textcontentcontrollerbase)，涉及的接口有  
[getTextContentRect](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#gettextcontentrect)、  
[getTextContentLineCount](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#gettextcontentlinecount)、[getCaretOffset](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#getcaretoffset11)、  
[addText](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#addtext15)、  
[deleteText](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#deletetext15)、  
[getSelection](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#getselection15)、  
[clearPreviewText](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#clearpreviewtext17)、  
[setStyledPlaceholder](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#setstyledplaceholder22)、[deleteBackward](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#deletebackward23)、  
[scrollToVisible](../../../reference/apis-arkui/arkui-ts/ts-universal-attributes-text-style.md#scrolltovisible23)&lt;!-  
-Del--&gt;以及系统接口[getText](../../../reference/apis-arkui/arkui-ts/ts-text-common-sys.md#gettext19)&lt;!--DelEnd--&gt;。

**Inheritance/Implementation:** SearchController extends [TextContentControllerBase](arkts-arkui-common-textcontentcontrollerbase-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class SearchController extends TextContentControllerBase--><!--Device-unnamed-export declare class SearchController extends TextContentControllerBase-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## caretPosition

```TypeScript
caretPosition(value: int): void
```

设置输入光标的位置。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchController-caretPosition(value: int): void--><!--Device-SearchController-caretPosition(value: int): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int | Yes | 从字符串开始到光标所在位置的长度。 &lt;br/&gt;取值范围：大于等于0。 |

## constructor

```TypeScript
constructor()
```

SearchController的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchController-constructor()--><!--Device-SearchController-constructor()-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## setTextSelection

```TypeScript
setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void
```

组件在获焦状态下，调用该接口设置文本选择区域并高亮显示，且只有在selectionStart小于selectionEnd时，文字才会被选取并高亮显示。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchController-setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void--><!--Device-SearchController-setTextSelection(selectionStart: int, selectionEnd: int, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | int | Yes | 文本选择区域起始位置，文本框中文字的起始位置为0。&lt;br/&gt;当selectionStart小于0时、按照0处理；当selectionStart大于文字最大长度时、 按照文字最大长度处理。&lt;br/&gt; |
| selectionEnd | int | Yes | 文本选择区域结束位置。&lt;br/&gt;当selectionEnd小于0时、按照0处理；当selectionEnd大于文字最大长度时、按照文字最大长度处理。&lt;br/&gt; |
| options | [SelectionOptions](../arkts-components/arkts-arkui-selectionoptions-i.md) | No | 选中文字时的配置。&lt;br /&gt;默认值：MenuPolicy.DEFAULT。 |

## stopEditing

```TypeScript
stopEditing(): void
```

退出编辑态。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchController-stopEditing(): void--><!--Device-SearchController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

