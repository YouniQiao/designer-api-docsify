# createWaterFlowNode

## createWaterFlowNode

```TypeScript
export function createWaterFlowNode(context: UIContext, options?: FrameNodeOptions): WaterFlow
```

Create a FrameNode of WaterFlow type.On API 26.0.0 and above, It can also create a FrameNode of WaterFlow type with options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createWaterFlowNode(context: UIContext, options?: FrameNodeOptions): WaterFlow--><!--Device-typeNode-export function createWaterFlowNode(context: UIContext, options?: FrameNodeOptions): WaterFlow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [FrameNodeOptions](arkts-arkui-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| [WaterFlow](arkts-arkui-typenode-waterflow-t.md) | Return WaterFlow type FrameNode. |

