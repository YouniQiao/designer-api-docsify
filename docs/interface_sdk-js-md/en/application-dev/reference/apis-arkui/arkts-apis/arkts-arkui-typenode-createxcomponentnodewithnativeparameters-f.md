# createXComponentNodeWithNativeParameters

## createXComponentNodeWithNativeParameters

```TypeScript
export function createXComponentNodeWithNativeParameters(
    context: UIContext, parameters: NativeXComponentParameters, options?: FrameNodeOptions): XComponent
```

Create a FrameNode of XComponent type with options for native developing.On API 26.0.0 and above, It can also create a FrameNode of XComponent type with options for native developing and  FrameNode options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createXComponentNodeWithNativeParameters(    context: UIContext, parameters: NativeXComponentParameters, options?: FrameNodeOptions): XComponent--><!--Device-typeNode-export function createXComponentNodeWithNativeParameters(    context: UIContext, parameters: NativeXComponentParameters, options?: FrameNodeOptions): XComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| parameters | [NativeXComponentParameters](../arkts-components/arkts-arkui-nativexcomponentparameters-i.md) | Yes | initialization parameters. |
| options | [FrameNodeOptions](arkts-arkui-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| [XComponent](arkts-arkui-typenode-xcomponent-t.md) | Return XComponent type FrameNode. |

