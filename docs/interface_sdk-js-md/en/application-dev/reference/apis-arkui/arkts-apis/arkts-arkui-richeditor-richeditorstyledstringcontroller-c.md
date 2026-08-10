# RichEditorStyledStringController

使用属性字符串构建的RichEditor组件的控制器，继承自[RichEditorBaseController](arkts-arkui-richeditor-richeditorbasecontroller-c.md)。

**Inheritance/Implementation:** RichEditorStyledStringController extends [RichEditorBaseController](arkts-arkui-richeditor-richeditorbasecontroller-c.md) and implements [StyledStringController](arkts-arkui-textcommon-styledstringcontroller-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class RichEditorStyledStringController extends RichEditorBaseController    implements StyledStringController--><!--Device-unnamed-export declare class RichEditorStyledStringController extends RichEditorBaseController    implements StyledStringController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getSelection

```TypeScript
getSelection(): RichEditorRange | undefined
```

获取富文本当前的选中区域范围。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorStyledStringController-getSelection(): RichEditorRange | undefined--><!--Device-RichEditorStyledStringController-getSelection(): RichEditorRange | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RichEditorRange](../arkts-components/arkts-arkui-richeditorrange-i.md) | 选中区域范围。&lt;br/&gt;返回undefined时表示controller未与组件绑定。 |

## getStyledString

```TypeScript
getStyledString(): MutableStyledString | undefined
```

获取富文本组件显示的属性字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorStyledStringController-getStyledString(): MutableStyledString | undefined--><!--Device-RichEditorStyledStringController-getStyledString(): MutableStyledString | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [MutableStyledString](arkts-arkui-mutablestyledstring-c.md) | 富文本组件显示的属性字符串。&lt;br/&gt;返回undefined时表示controller未与组件绑定。 |

## onContentChanged

```TypeScript
onContentChanged(listener: StyledStringChangedListener): void
```

注册文本内容变化回调，该回调会在后端程序导致文本内容变更时触发。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorStyledStringController-onContentChanged(listener: StyledStringChangedListener): void--><!--Device-RichEditorStyledStringController-onContentChanged(listener: StyledStringChangedListener): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| listener | [StyledStringChangedListener](arkts-arkui-styledstringchangedlistener-i.md) | Yes | 文本内容变化回调监听器。 |

## setStyledString

```TypeScript
setStyledString(styledString: StyledString): void
```

设置富文本组件显示的属性字符串。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorStyledStringController-setStyledString(styledString: StyledString): void--><!--Device-RichEditorStyledStringController-setStyledString(styledString: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | [StyledString](arkts-arkui-styledstring-c.md) | Yes | 属性字符串。&lt;br/&gt;**说明：** &lt;br/&gt;StyledString的子类 [MutableStyledString](arkts-arkui-styledstring-mutablestyledstring-c.md)也可以作为入参值。 |

