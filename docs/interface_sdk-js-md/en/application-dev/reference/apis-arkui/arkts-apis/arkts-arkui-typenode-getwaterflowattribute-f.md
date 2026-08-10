# getWaterFlowAttribute

## getWaterFlowAttribute

```TypeScript
export function getWaterFlowAttribute(node: FrameNode): WaterFlowAttribute | undefined
```

从FrameNode中获取属性实例用于属性设置。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function getWaterFlowAttribute(node: FrameNode): WaterFlowAttribute | undefined--><!--Device-typeNode-export function getWaterFlowAttribute(node: FrameNode): WaterFlowAttribute | undefined-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| node | [FrameNode](arkts-arkui-framenode-c.md) | Yes | 目标FrameNode. |

**Return value:**

| Type | Description |
| --- | --- |
| [WaterFlowAttribute](../arkts-components/arkts-arkui-waterflow-attribute.md) | Return the attribute instance of FrameNode, and return undefined if it does not exist. |

