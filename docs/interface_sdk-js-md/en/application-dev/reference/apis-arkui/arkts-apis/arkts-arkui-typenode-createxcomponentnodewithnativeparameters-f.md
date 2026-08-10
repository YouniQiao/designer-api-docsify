# createXComponentNodeWithNativeParameters

## createXComponentNodeWithNativeParameters

```TypeScript
export function createXComponentNodeWithNativeParameters(
    context: UIContext, parameters: NativeXComponentParameters, options?: FrameNodeOptions): XComponent
```

创建 XComponent 类型的 FrameNode（支持原生开发参数）

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createXComponentNodeWithNativeParameters(    context: UIContext, parameters: NativeXComponentParameters, options?: FrameNodeOptions): XComponent--><!--Device-typeNode-export function createXComponentNodeWithNativeParameters(    context: UIContext, parameters: NativeXComponentParameters, options?: FrameNodeOptions): XComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 用于创建 FrameNode 的 UI 上下文 |
| parameters | [NativeXComponentParameters](../arkts-components/arkts-arkui-nativexcomponentparameters-i.md) | Yes | 原生开发初始化参数 |
| options | [FrameNodeOptions](arkts-arkui-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| [XComponent](arkts-arkui-typenode-xcomponent-t.md) | 返回 XComponent 类型的 FrameNode |

