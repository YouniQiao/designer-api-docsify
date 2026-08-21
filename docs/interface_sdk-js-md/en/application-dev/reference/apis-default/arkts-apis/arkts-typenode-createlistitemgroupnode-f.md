# createListItemGroupNode

## createListItemGroupNode

```TypeScript
export function createListItemGroupNode(context: UIContext, options?: FrameNodeOptions): ListItemGroup
```

Create a FrameNode of ListItemGroup type. On API 26.0.0 and above, It can also create a FrameNode of ListItemGroup type.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createListItemGroupNode(context: UIContext, options?: FrameNodeOptions): ListItemGroup--><!--Device-typeNode-export function createListItemGroupNode(context: UIContext, options?: FrameNodeOptions): ListItemGroup-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [FrameNodeOptions](arkts-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| ListItemGroup | Return ListItemGroup type FrameNode. |

