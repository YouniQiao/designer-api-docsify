# createFlexNode

## createFlexNode

```TypeScript
export function createFlexNode(context: UIContext, options?: FrameNodeOptions): Flex
```

Create a FrameNode of Flex type. On API 26.0.0 and above, It can also create a FrameNode of Flex type with options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createFlexNode(context: UIContext, options?: FrameNodeOptions): Flex--><!--Device-typeNode-export function createFlexNode(context: UIContext, options?: FrameNodeOptions): Flex-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [FrameNodeOptions](arkts-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| Flex | Return Flex type FrameNode. |

