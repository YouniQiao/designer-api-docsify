# RichEditorStyledStringController

使用属性字符串构建的RichEditor组件的控制器，继承自[RichEditorBaseController](arkts-arkui-richeditorbasecontroller-c.md)。

## 导入对象

```ts controller: RichEditorStyledStringController = new RichEditorStyledStringController();```

**Inheritance/Implementation:** RichEditorStyledStringController extends [RichEditorBaseController](arkts-arkui-richeditorbasecontroller-c.md) and implements [StyledStringController](../arkts-apis/arkts-arkui-textcommon-styledstringcontroller-i.md/arkts-arkui-textcommon-styledstringcontroller-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class RichEditorStyledStringController extends RichEditorBaseController implements StyledStringController--><!--Device-unnamed-declare class RichEditorStyledStringController extends RichEditorBaseController implements StyledStringController-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getSelection

```TypeScript
getSelection(): RichEditorRange
```

获取富文本当前的选中区域范围。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorStyledStringController-getSelection(): RichEditorRange--><!--Device-RichEditorStyledStringController-getSelection(): RichEditorRange-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [RichEditorRange](arkts-arkui-richeditorrange-i.md) | 选中区域范围。 &lt;br&gt;当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

## getStyledString

```TypeScript
getStyledString(): MutableStyledString
```

获取富文本组件显示的属性字符串。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorStyledStringController-getStyledString(): MutableStyledString--><!--Device-RichEditorStyledStringController-getStyledString(): MutableStyledString-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [MutableStyledString](../arkts-apis/arkts-arkui-mutablestyledstring-c.md) | 富文本组件显示的属性字符串。 &lt;br&gt;当controller未绑定组件或绑定controller的组件被释放时，返回undefined。 |

## onContentChanged

```TypeScript
onContentChanged(listener: StyledStringChangedListener): void
```

注册文本内容变化回调，该回调仅在后端程序导致文本内容变更时触发，调用[setStyledString](arkts-arkui-richeditorstyledstringcontroller-c.md#setstyledstring)时不会触发。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorStyledStringController-onContentChanged(listener: StyledStringChangedListener): void--><!--Device-RichEditorStyledStringController-onContentChanged(listener: StyledStringChangedListener): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| listener | [StyledStringChangedListener](../arkts-apis/arkts-arkui-textcommon-styledstringchangedlistener-i.md) | Yes | 文本内容变化回调监听器。 |

## setStyledString

```TypeScript
setStyledString(styledString: StyledString): void
```

设置富文本组件显示的属性字符串。

> **说明：**
> 
> - 调用该接口时，会全量替换富文本组件的StyledString，并重新渲染。
> 
> - 当内容超过组件本身区域时，组件会自动向上滚动内容直到末尾处可见。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorStyledStringController-setStyledString(styledString: StyledString): void--><!--Device-RichEditorStyledStringController-setStyledString(styledString: StyledString): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| styledString | [StyledString](../arkts-apis/arkts-arkui-styledstring-c.md) | Yes | 属性字符串。&lt;br/&gt;**说明：** &lt;br/&gt;StyledString的子类 [MutableStyledString](../arkts-apis/arkts-arkui-styledstring-mutablestyledstring-c.md/arkts-arkui-styledstring-mutablestyledstring-c.md)也可以作为入参值。 |

