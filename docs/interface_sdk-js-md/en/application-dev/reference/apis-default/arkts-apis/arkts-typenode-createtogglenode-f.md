# createToggleNode

## createToggleNode

```TypeScript
export function createToggleNode(
    context: UIContext, options?: ToggleOptions, frameNodeOptions?: FrameNodeOptions): Toggle
```

Create a FrameNode of Toggle type with Toggle options and FrameNode options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createToggleNode(    context: UIContext, options?: ToggleOptions, frameNodeOptions?: FrameNodeOptions): Toggle--><!--Device-typeNode-export function createToggleNode(    context: UIContext, options?: ToggleOptions, frameNodeOptions?: FrameNodeOptions): Toggle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | ToggleOptions | No | Toggle component options |
| frameNodeOptions | [FrameNodeOptions](arkts-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| Toggle | Return Toggle type FrameNode. |

