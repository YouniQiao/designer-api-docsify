# createColumnNode

## createColumnNode

```TypeScript
export function createColumnNode(context: UIContext, options?: FrameNodeOptions): Column
```

Create a FrameNode of Column type. On API 26.0.0 and above, It can also create a FrameNode of Column type with options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createColumnNode(context: UIContext, options?: FrameNodeOptions): Column--><!--Device-typeNode-export function createColumnNode(context: UIContext, options?: FrameNodeOptions): Column-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](../../apis-arkui/arkts-apis/arkts-arkui-arkuiuicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [FrameNodeOptions](arkts-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| Column | Return Column type FrameNode. |

