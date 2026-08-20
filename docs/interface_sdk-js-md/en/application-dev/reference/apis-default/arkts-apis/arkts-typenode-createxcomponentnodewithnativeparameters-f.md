# createXComponentNodeWithNativeParameters

## createXComponentNodeWithNativeParameters

```TypeScript
export function createXComponentNodeWithNativeParameters(
    context: UIContext, parameters: NativeXComponentParameters, options?: FrameNodeOptions): XComponent
```

Create a FrameNode of XComponent type with options for native developing. On API 26.0.0 and above, It can also create a FrameNode of XComponent type with options for native developing and FrameNode options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createXComponentNodeWithNativeParameters(    context: UIContext, parameters: NativeXComponentParameters, options?: FrameNodeOptions): XComponent--><!--Device-typeNode-export function createXComponentNodeWithNativeParameters(    context: UIContext, parameters: NativeXComponentParameters, options?: FrameNodeOptions): XComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| parameters | NativeXComponentParameters | Yes | initialization parameters. |
| options | [FrameNodeOptions](arkts-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| XComponent | Return XComponent type FrameNode. |

