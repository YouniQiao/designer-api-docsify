# createRowNode

## createRowNode

```TypeScript
export function createRowNode(context: UIContext, options?: FrameNodeOptions): Row
```

Create a FrameNode of Row type. On API 26.0.0 and above, It can also create a FrameNode of Row type with options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createRowNode(context: UIContext, options?: FrameNodeOptions): Row--><!--Device-typeNode-export function createRowNode(context: UIContext, options?: FrameNodeOptions): Row-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [FrameNodeOptions](arkts-na-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| Row | Return Row type FrameNode. |

