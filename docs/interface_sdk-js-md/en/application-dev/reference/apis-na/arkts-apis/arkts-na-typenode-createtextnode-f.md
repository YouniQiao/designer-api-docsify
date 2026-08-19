# createTextNode

## createTextNode

```TypeScript
export function createTextNode(context: UIContext, options?: FrameNodeOptions): Text
```

Create a FrameNode of Text type. On API 26.0.0 and above, It can also create a FrameNode of Text type with options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createTextNode(context: UIContext, options?: FrameNodeOptions): Text--><!--Device-typeNode-export function createTextNode(context: UIContext, options?: FrameNodeOptions): Text-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-na-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [FrameNodeOptions](arkts-na-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| Text | Return Text type FrameNode. |

