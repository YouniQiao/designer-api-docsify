# createListItemNode

## createListItemNode

```TypeScript
export function createListItemNode(context: UIContext, options?: FrameNodeOptions): ListItem
```

Create a FrameNode of ListItem type. On API 26.0.0 and above, It can also create a FrameNode of ListItem type with options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createListItemNode(context: UIContext, options?: FrameNodeOptions): ListItem--><!--Device-typeNode-export function createListItemNode(context: UIContext, options?: FrameNodeOptions): ListItem-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [FrameNodeOptions](arkts-na-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| ListItem | Return ListItem type FrameNode. |

