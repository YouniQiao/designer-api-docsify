# TextArea

多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示，适用于评论输入、反馈表单、内容编辑等需要多行文本输入的场景。

高度未设置时，组件无默认高度，自适应内容高度。宽度未设置时，默认撑满最大宽度。

## 子组件

无

## TextArea

```TypeScript
TextArea(value?: TextAreaOptions)
```

定义TextArea组件构造函数。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-TextAreaInterface-(value?: TextAreaOptions): TextAreaAttribute--><!--Device-TextAreaInterface-(value?: TextAreaOptions): TextAreaAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [TextAreaOptions](arkts-arkui-textareaoptions-i.md) | No | TextArea组件参数。默认值：详见TextAreaOptions。 |

## Summary

- [TextAreaOptions](arkts-arkui-textarea-textareaoptions-i.md)
- [TextAreaSubmitCallback](arkts-arkui-textarea-textareasubmitcallback-t.md)
- [TextAreaType](arkts-arkui-textarea-textareatype-e.md)
