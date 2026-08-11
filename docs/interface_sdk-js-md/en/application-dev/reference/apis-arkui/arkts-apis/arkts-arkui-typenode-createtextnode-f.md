# createTextNode

## createTextNode

```TypeScript
export function createTextNode(context: UIContext, options?: FrameNodeOptions): Text
```

Create a FrameNode of Text type.On API 26.0.0 and above, It can also create a FrameNode of Text type with options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createTextNode(context: UIContext, options?: FrameNodeOptions): Text--><!--Device-typeNode-export function createTextNode(context: UIContext, options?: FrameNodeOptions): Text-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [FrameNodeOptions](arkts-arkui-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| [Text](../../apis-arkdata/arkts-apis/arkts-arkdata-unifieddatachannel-text-c.md) | Return Text type FrameNode. |

