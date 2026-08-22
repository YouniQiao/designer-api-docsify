# createXComponentNodeWithOptions

## createXComponentNodeWithOptions

```TypeScript
export function createXComponentNodeWithOptions(
    context: UIContext, value: XComponentOptions, options?: FrameNodeOptions): XComponent
```

Create a FrameNode of XComponent type with options. On API 26.0.0 and above, It can also create a FrameNode of XComponent type with options and FrameNode options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createXComponentNodeWithOptions(    context: UIContext, value: XComponentOptions, options?: FrameNodeOptions): XComponent--><!--Device-typeNode-export function createXComponentNodeWithOptions(    context: UIContext, value: XComponentOptions, options?: FrameNodeOptions): XComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| value | XComponentOptions | Yes | XComponent options. |
| options | [FrameNodeOptions](arkts-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| XComponent | Return XComponent type FrameNode. |

