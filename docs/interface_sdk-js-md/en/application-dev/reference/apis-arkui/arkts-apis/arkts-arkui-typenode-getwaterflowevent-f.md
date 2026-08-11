# getWaterFlowEvent

## getWaterFlowEvent

```TypeScript
export function getWaterFlowEvent(node: FrameNode): UIWaterFlowEvent | undefined
```

Get the event instance of WaterFlow node.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getWaterFlowEvent(node: FrameNode): UIWaterFlowEvent | undefined--><!--Device-typeNode-export function getWaterFlowEvent(node: FrameNode): UIWaterFlowEvent | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | the target FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| [UIWaterFlowEvent](../arkts-components/arkts-arkui-uiwaterflowevent-i.md) | Return the event instance of FrameNode, and return undefined if it does not exist. |

