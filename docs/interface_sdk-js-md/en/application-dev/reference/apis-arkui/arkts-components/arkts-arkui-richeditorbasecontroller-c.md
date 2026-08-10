# RichEditorBaseController

RichEditor组件控制器基类。

**Inheritance/Implementation:** RichEditorBaseController implements [TextEditControllerEx](../arkts-apis/arkts-arkui-textcommon-texteditcontrollerex-i.md/arkts-arkui-textcommon-texteditcontrollerex-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class RichEditorBaseController implements TextEditControllerEx--><!--Device-unnamed-declare class RichEditorBaseController implements TextEditControllerEx-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## closeSelectionMenu

```TypeScript
closeSelectionMenu(): void
```

关闭自定义选择菜单或系统默认选择菜单。

当controller未绑定组件或绑定controller的组件被释放时，该接口调用无效。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorBaseController-closeSelectionMenu(): void--><!--Device-RichEditorBaseController-closeSelectionMenu(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deleteBackward

```TypeScript
deleteBackward(): void
```

删除光标前字符或选中内容。没有内容被选中时，删除当前光标位置前的1个字符；有内容被选中时，删除选中内容。

该接口不支持预上屏场景使用。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-RichEditorBaseController-deleteBackward(): void--><!--Device-RichEditorBaseController-deleteBackward(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getCaretOffset

```TypeScript
getCaretOffset(): number
```

返回当前光标所在位置。

当无法获取光标位置时（例如controller未与组件绑定时），该接口返回-1。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorBaseController-getCaretOffset(): number--><!--Device-RichEditorBaseController-getCaretOffset(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | 当前光标所在位置。 |

## getCaretRect

```TypeScript
getCaretRect(): RectResult | undefined
```

返回当前光标与RichEditor组件的相对位置。如果光标不闪烁或controller未绑定组件，返回undefined。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-RichEditorBaseController-getCaretRect(): RectResult | undefined--><!--Device-RichEditorBaseController-getCaretRect(): RectResult | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RectResult](../arkts-apis/arkts-arkui-common-rectresult-i.md) | 当前光标与RichEditor的相对位置。 |

## getLayoutManager

```TypeScript
getLayoutManager(): LayoutManager
```

获取布局管理器对象。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorBaseController-getLayoutManager(): LayoutManager--><!--Device-RichEditorBaseController-getLayoutManager(): LayoutManager-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [LayoutManager](../arkts-apis/arkts-arkui-layoutmanager-i.md) | 布局管理器对象，可用于获取组件内容的布局位置等信息。 &lt;br&gt;当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

## getPreviewText

```TypeScript
getPreviewText(): PreviewText
```

获取预上屏信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorBaseController-getPreviewText(): PreviewText--><!--Device-RichEditorBaseController-getPreviewText(): PreviewText-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PreviewText](../arkts-apis/arkts-arkui-previewtext-i.md) | 预上屏文本信息，包含输入法预显示的候选文本内容及起始位置。 &lt;br&gt;当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

## getTypingStyle

```TypeScript
getTypingStyle(): RichEditorTextStyle
```

获取用户预设的文本样式。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorBaseController-getTypingStyle(): RichEditorTextStyle--><!--Device-RichEditorBaseController-getTypingStyle(): RichEditorTextStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RichEditorTextStyle](arkts-arkui-richeditortextstyle-i.md) | 用户预设的文本输入样式对象，包含字体颜色、大小、粗细等样式属性，可用于查询当前组件的输入文本样式配置。 &lt;br&gt;当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

## isEditing

```TypeScript
isEditing(): boolean
```

获取当前富文本的编辑状态。当controller未绑定组件或绑定controller的组件被释放时，返回false。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorBaseController-isEditing(): boolean--><!--Device-RichEditorBaseController-isEditing(): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示编辑态，false表示非编辑态。 |

## scrollToVisible

```TypeScript
scrollToVisible(range?: TextRange): void
```

将指定范围内的内容滚动到可视区域。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-RichEditorBaseController-scrollToVisible(range?: TextRange): void--><!--Device-RichEditorBaseController-scrollToVisible(range?: TextRange): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| range | [TextRange](../arkts-apis/arkts-arkui-textrange-i.md) | No | 滚动到可视区域的内容范围，包括内容起始位置和终止位置。 &lt;br&gt;起始位置应小于等于结束位置，否则接口调用无效。起始位置小于0视为0，结束位置大于全文长度视为全文长度。 &lt;br&gt;未指定范围时，默认为全部内容。未指定起始位置，默认起始位置为0；未指定结束位置，默认结束位置为全文长度。 |

## setCaretOffset

```TypeScript
setCaretOffset(offset: number): boolean
```

设置光标位置。

当controller未绑定组件或绑定controller的组件被释放时，该接口返回false，设置不成功。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RichEditorBaseController-setCaretOffset(offset: number): boolean--><!--Device-RichEditorBaseController-setCaretOffset(offset: number): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| offset | number | Yes | 光标偏移位置。超出所有内容范围时，设置失败。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 光标是否设置成功。&lt;br/&gt;true表示光标位置设置成功，false表示未成功。 |

## setSelection

```TypeScript
setSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void
```

设置组件内的内容选中，选中部分背板高亮。

selectionStart和selectionEnd均为-1时表示全选，均为0时可以清空选中区。

未获焦时调用该接口不产生选中效果。

从API version 12开始，在PC/2in1设备（可通过deviceInfo.deviceType获取设备类型进行判断）中，无论options取何值，调用setSelection接口都不会弹出菜单；如果组件中已经存在菜单，调用setSelection接口会关闭菜单。在非PC/2in1设备中，options取值为MenuPolicy.DEFAULT时，遵循以下规则：

1. 组件内有手柄菜单时，接口调用后不关闭菜单，并且调整菜单位置。2. 组件内有不带手柄的菜单时，接口调用后不关闭菜单，并且菜单位置不变。3. 组件内无菜单时，接口调用后也无菜单显示。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorBaseController-setSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void--><!--Device-RichEditorBaseController-setSelection(selectionStart: number, selectionEnd: number, options?: SelectionOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectionStart | number | Yes | 选中开始位置。 |
| selectionEnd | number | Yes | 选中结束位置。 |
| options | [SelectionOptions](../arkts-apis/arkts-arkui-common-selectionoptions-i.md) | No | 选择项配置，用于控制选中操作时的菜单弹出策略。 &lt;br&gt;当需要自定义菜单弹出行为（如强制显示或隐藏菜单）时传入此参数； &lt;br&gt;省略时默认使用MenuPolicy.DEFAULT，遵循系统默认菜单弹出策略。 &lt;br&gt;各MenuPolicy取值的适用场景请参考SelectionOptions对象说明。<br>**Since:** 12 |

## setStyledPlaceholder

```TypeScript
setStyledPlaceholder(styledString: StyledString): void
```

设置无输入时的属性字符串样式的提示文本。

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-RichEditorBaseController-setStyledPlaceholder(styledString: StyledString): void--><!--Device-RichEditorBaseController-setStyledPlaceholder(styledString: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | [StyledString](../arkts-apis/arkts-arkui-styledstring-c.md) | Yes | 设置属性字符串样式的提示文本，其优先级高于[placeholder](RichEditorAttribute#placeholder)属性设 置的提示文本。 &lt;br&gt;提示文本不支持触发属性字符串[GestureStyle](../arkts-apis/arkts-arkui-styledstring-gesturestyle-c.md/arkts-arkui-styledstring-gesturestyle-c.md)样式绑定的手势事件，以及[UrlStyle](../arkts-apis/arkts-arkui-styledstring-urlstyle-c.md/arkts-arkui-styledstring-urlstyle-c.md)样式的超链接跳转能力。 |

## setTypingParagraphStyle

```TypeScript
setTypingParagraphStyle(style: RichEditorParagraphStyle): void
```

设置用户预设的段落样式。仅在组件内容为空或组件末尾换行后，输入文本生效。当controller未绑定组件或绑定controller的组件被释放时，该接口调用无效。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-RichEditorBaseController-setTypingParagraphStyle(style: RichEditorParagraphStyle): void--><!--Device-RichEditorBaseController-setTypingParagraphStyle(style: RichEditorParagraphStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [RichEditorParagraphStyle](../arkts-apis/arkts-arkui-richeditor-richeditorparagraphstyle-i.md) | Yes | 预设段落样式。 |

## setTypingStyle

```TypeScript
setTypingStyle(value: RichEditorTextStyle): void
```

设置用户预设的文本样式。

当controller未绑定组件或绑定controller的组件被释放时，该接口调用无效。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorBaseController-setTypingStyle(value: RichEditorTextStyle): void--><!--Device-RichEditorBaseController-setTypingStyle(value: RichEditorTextStyle): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [RichEditorTextStyle](arkts-arkui-richeditortextstyle-i.md) | Yes | 预设的文本输入样式，包含字体颜色、大小、粗细等属性，用于设置后续输入文本的默认样式。 |

## stopEditing

```TypeScript
stopEditing(): void
```

退出编辑态。

当controller未绑定组件或绑定controller的组件被释放时，该接口调用无效。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorBaseController-stopEditing(): void--><!--Device-RichEditorBaseController-stopEditing(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

