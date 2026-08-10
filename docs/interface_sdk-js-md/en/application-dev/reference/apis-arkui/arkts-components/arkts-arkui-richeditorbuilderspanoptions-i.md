# RichEditorBuilderSpanOptions

设置builder的偏移位置和样式。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface RichEditorBuilderSpanOptions--><!--Device-unnamed-declare interface RichEditorBuilderSpanOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilitySpanOptions

```TypeScript
accessibilitySpanOptions?: AccessibilitySpanOptions
```

无障碍朗读功能属性。缺省时，取[AccessibilitySpanOptions](../arkts-apis/arkts-arkui-textcommon-accessibilityspanoptions-i.md/arkts-arkui-textcommon-accessibilityspanoptions-i.md)的默认值。

**Type:** [AccessibilitySpanOptions](../arkts-apis/arkts-arkui-accessibilityspanoptions-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-RichEditorBuilderSpanOptions-accessibilitySpanOptions?: AccessibilitySpanOptions--><!--Device-RichEditorBuilderSpanOptions-accessibilitySpanOptions?: AccessibilitySpanOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: number
```

添加builder的位置。取值范围：[0, 所有内容长度]。省略或当值小于0或大于所有内容长度时，添加到所有内容最后面。

**Type:** number

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorBuilderSpanOptions-offset?: number--><!--Device-RichEditorBuilderSpanOptions-offset?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

