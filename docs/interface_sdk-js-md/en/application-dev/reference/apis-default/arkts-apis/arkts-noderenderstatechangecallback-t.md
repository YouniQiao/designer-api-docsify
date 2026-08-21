# NodeRenderStateChangeCallback

```TypeScript
export declare type NodeRenderStateChangeCallback = (state: NodeRenderState, node?: FrameNode) => void
```

Defines the callback type used in UIObserver to monitor one specific node's render state.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare type NodeRenderStateChangeCallback = (state: NodeRenderState, node?: FrameNode) => void--><!--Device-unnamed-export declare type NodeRenderStateChangeCallback = (state: NodeRenderState, node?: FrameNode) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| state | [NodeRenderState](../../apis-arkui/arkts-apis/arkts-arkui-arkuiuicontext-noderenderstate-e.md) | Yes | the node's render state |
| node | FrameNode | No | the information of frameNode |

