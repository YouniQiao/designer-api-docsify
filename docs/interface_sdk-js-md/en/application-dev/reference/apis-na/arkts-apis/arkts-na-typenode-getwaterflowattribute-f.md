# getWaterFlowAttribute

## getWaterFlowAttribute

```TypeScript
export function getWaterFlowAttribute(node: FrameNode): WaterFlowAttribute | undefined
```

Get the attribute instance of FrameNode to set attributes.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getWaterFlowAttribute(node: FrameNode): WaterFlowAttribute | undefined--><!--Device-typeNode-export function getWaterFlowAttribute(node: FrameNode): WaterFlowAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-na-framenode-c.md) | Yes | the target FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| WaterFlowAttribute \| undefined | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

