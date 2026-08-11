# createToggleNode

## createToggleNode

```TypeScript
export function createToggleNode(
    context: UIContext, options?: ToggleOptions, frameNodeOptions?: FrameNodeOptions): Toggle
```

Create a FrameNode of Toggle type with Toggle options and FrameNode options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createToggleNode(    context: UIContext, options?: ToggleOptions, frameNodeOptions?: FrameNodeOptions): Toggle--><!--Device-typeNode-export function createToggleNode(    context: UIContext, options?: ToggleOptions, frameNodeOptions?: FrameNodeOptions): Toggle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [ToggleOptions](../arkts-components/arkts-arkui-toggleoptions-i.md) | No | Toggle component options |
| frameNodeOptions | [FrameNodeOptions](arkts-arkui-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| [Toggle](arkts-arkui-typenode-toggle-t.md) | Return Toggle type FrameNode. |

