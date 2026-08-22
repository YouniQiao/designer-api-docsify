# createFlowItemNode

## createFlowItemNode

```TypeScript
export function createFlowItemNode(context: UIContext, options?: FrameNodeOptions): FlowItem
```

Create a FrameNode of FlowItem type. On API 26.0.0 and above, It can also create a FrameNode of FlowItem type with options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createFlowItemNode(context: UIContext, options?: FrameNodeOptions): FlowItem--><!--Device-typeNode-export function createFlowItemNode(context: UIContext, options?: FrameNodeOptions): FlowItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [FrameNodeOptions](arkts-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| FlowItem | Return FlowItem type FrameNode. |

