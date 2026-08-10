# RichEditorChangeValue

图文变化信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface RichEditorChangeValue--><!--Device-unnamed-declare interface RichEditorChangeValue-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## changeReason

```TypeScript
changeReason?: TextChangeReason
```

组件内容变化的原因，用于标识触发内容变化的操作类型（如用户输入、粘贴、剪切等），需通过注册onWillChange回调获取。开发者可根据changeReason的值在onWillChange回调中针对不同变化原因做出相应处理决策。字段缺省值为undefined。

**Type:** [TextChangeReason](../arkts-apis/arkts-arkui-textcommon-textchangereason-e-sys.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorChangeValue-changeReason?: TextChangeReason--><!--Device-RichEditorChangeValue-changeReason?: TextChangeReason-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

