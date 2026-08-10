# MaxLinesOptions

配置TextArea组件，文本超长时的显示效果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface MaxLinesOptions--><!--Device-unnamed-export declare interface MaxLinesOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## overflowMode

```TypeScript
overflowMode?: MaxLinesMode
```

`overflowMode`可配置[TextArea](../../../reference/apis-arkui/arkui-ts/ts-basic-components-textarea.md)组件的非内联模式。当超出设置的`maxLines`最大行数时，会启用滚动效果。需同时配置  
[textOverflow](../../../reference/apis-arkui/arkui-ts/ts-basic-components-textarea.md#textoverflow12)，且仅当`textOverflow`为None或Clip时，`MaxLinesMode`才能生效。默认情况下，`MaxLinesMode`的值为Clip，超出`maxLines`后文本会被截断。

**Type:** [MaxLinesMode](arkts-arkui-maxlinesmode-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-MaxLinesOptions-overflowMode?: MaxLinesMode--><!--Device-MaxLinesOptions-overflowMode?: MaxLinesMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

