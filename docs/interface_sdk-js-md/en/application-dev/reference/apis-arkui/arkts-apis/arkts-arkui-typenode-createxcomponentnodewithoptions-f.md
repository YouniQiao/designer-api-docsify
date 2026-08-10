# createXComponentNodeWithOptions

## createXComponentNodeWithOptions

```TypeScript
export function createXComponentNodeWithOptions(
    context: UIContext, value: XComponentOptions, options?: FrameNodeOptions): XComponent
```

创建 XComponent 类型的 FrameNode（支持 XComponent 组件选项）

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createXComponentNodeWithOptions(    context: UIContext, value: XComponentOptions, options?: FrameNodeOptions): XComponent--><!--Device-typeNode-export function createXComponentNodeWithOptions(    context: UIContext, value: XComponentOptions, options?: FrameNodeOptions): XComponent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 用于创建 FrameNode 的 UI 上下文 |
| value | [XComponentOptions](../arkts-components/arkts-arkui-xcomponentoptions-i.md) | Yes | XComponent 组件选项 |
| options | [FrameNodeOptions](arkts-arkui-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 24 |

**Return value:**

| Type | Description |
| --- | --- |
| [XComponent](arkts-arkui-typenode-xcomponent-t.md) | Return XComponent type FrameNode. |

