# createProgressNode

## createProgressNode

```TypeScript
export function createProgressNode(context: UIContext, options?: FrameNodeOptions): Progress
```

Create a FrameNode of Progress type.On API 26.0.0 and above, It can also create a FrameNode of Progress type with options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createProgressNode(context: UIContext, options?: FrameNodeOptions): Progress--><!--Device-typeNode-export function createProgressNode(context: UIContext, options?: FrameNodeOptions): Progress-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [FrameNodeOptions](arkts-arkui-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| [Progress](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-progress-i.md) | Return Progress type FrameNode. |

