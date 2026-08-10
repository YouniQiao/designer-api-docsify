# FrameNodeOptions

FrameNode选项，可设置FrameNode是否支持多线程操作。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare interface FrameNodeOptions--><!--Device-unnamed-export declare interface FrameNodeOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## supportMultiThread

```TypeScript
supportMultiThread?: boolean
```

FrameNode是否支持多线程操作。

true表示支持多线程操作，该节点可以在多线程场景中使用。

false或不设置表示不支持多线程操作。

默认为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FrameNodeOptions-supportMultiThread?: boolean--><!--Device-FrameNodeOptions-supportMultiThread?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

