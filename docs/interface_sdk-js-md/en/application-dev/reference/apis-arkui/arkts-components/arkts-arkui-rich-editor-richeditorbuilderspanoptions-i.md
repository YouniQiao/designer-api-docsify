# RichEditorBuilderSpanOptions

Sets the offset and style of the builder.

**Since:** 11

<!--Device-unnamed-declare interface RichEditorBuilderSpanOptions--><!--Device-unnamed-declare interface RichEditorBuilderSpanOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilitySpanOptions

```TypeScript
accessibilitySpanOptions?: AccessibilitySpanOptions
```

Accessibility settings. By default, the default value of [AccessibilitySpanOptions](../arkts-apis/arkts-arkui-text-common-accessibilityspanoptions-i.md) is used.

**Type:** AccessibilitySpanOptions

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-RichEditorBuilderSpanOptions-accessibilitySpanOptions?: AccessibilitySpanOptions--><!--Device-RichEditorBuilderSpanOptions-accessibilitySpanOptions?: AccessibilitySpanOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## offset

```TypeScript
offset?: number
```

Position of the builder span to be added. If this parameter is omitted or set to an invalid value, the span is added to the end of all content.

**Type:** number

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RichEditorBuilderSpanOptions-offset?: number--><!--Device-RichEditorBuilderSpanOptions-offset?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

