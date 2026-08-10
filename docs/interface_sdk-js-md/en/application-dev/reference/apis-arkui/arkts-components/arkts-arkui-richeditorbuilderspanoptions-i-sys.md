# RichEditorBuilderSpanOptions

设置builder的偏移位置和样式。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-unnamed-declare interface RichEditorBuilderSpanOptions--><!--Device-unnamed-declare interface RichEditorBuilderSpanOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## dragBackgroundColor

```TypeScript
dragBackgroundColor? : ColorMetrics
```

设置BuilderSpan单独拖拽时的背板颜色。未配置或传入无效颜色值时，按默认值处理。

默认值：跟随系统主题拖拽背板色。

**Type:** [ColorMetrics](../arkts-apis/arkts-arkui-graphics-colormetrics-c-sys.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBuilderSpanOptions-dragBackgroundColor? : ColorMetrics--><!--Device-RichEditorBuilderSpanOptions-dragBackgroundColor? : ColorMetrics-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## isDragShadowNeeded

```TypeScript
isDragShadowNeeded?: boolean
```

设置BuilderSpan单独拖拽时是否需要投影。true表示需要投影，false表示不需要投影。未配置或传入无效值时，按默认值处理。

默认值：true。

**Type:** boolean

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RichEditorBuilderSpanOptions-isDragShadowNeeded?: boolean--><!--Device-RichEditorBuilderSpanOptions-isDragShadowNeeded?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

