# createRelativeContainerNode

## createRelativeContainerNode

```TypeScript
export function createRelativeContainerNode(context: UIContext, options?: FrameNodeOptions): RelativeContainer
```

Create a FrameNode of RelativeContainer type. On API 26.0.0 and above, It can also create a FrameNode of RelativeContainer type with options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createRelativeContainerNode(context: UIContext, options?: FrameNodeOptions): RelativeContainer--><!--Device-typeNode-export function createRelativeContainerNode(context: UIContext, options?: FrameNodeOptions): RelativeContainer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [FrameNodeOptions](arkts-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| RelativeContainer | Return RelativeContainer type FrameNode. |

