# createToggleNode

## createToggleNode

```TypeScript
export function createToggleNode(
    context: UIContext, options?: ToggleOptions, frameNodeOptions?: FrameNodeOptions): Toggle
```

创建 Toggle 类型的 FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createToggleNode(    context: UIContext, options?: ToggleOptions, frameNodeOptions?: FrameNodeOptions): Toggle--><!--Device-typeNode-export function createToggleNode(    context: UIContext, options?: ToggleOptions, frameNodeOptions?: FrameNodeOptions): Toggle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 用于创建 FrameNode 的 UI 上下文。 |
| options | [ToggleOptions](../arkts-components/arkts-arkui-toggleoptions-i.md) | No | Toggle 组件选项。 |
| frameNodeOptions | [FrameNodeOptions](arkts-arkui-framenode-framenodeoptions-i.md) | No | FrameNode创建配置选项。【since24】。 |

**Return value:**

| Type | Description |
| --- | --- |
| [Toggle](arkts-arkui-typenode-toggle-t.md) | Return Toggle type FrameNode. |

