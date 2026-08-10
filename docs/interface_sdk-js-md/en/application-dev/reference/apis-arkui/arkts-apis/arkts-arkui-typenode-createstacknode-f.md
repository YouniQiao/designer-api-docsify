# createStackNode

## createStackNode

```TypeScript
export function createStackNode(context: UIContext, options?: FrameNodeOptions): Stack
```

创建Stack 类型的FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createStackNode(context: UIContext, options?: FrameNodeOptions): Stack--><!--Device-typeNode-export function createStackNode(context: UIContext, options?: FrameNodeOptions): Stack-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 用于创建 FrameNode 的 UI 上下文。 |
| options | [FrameNodeOptions](arkts-arkui-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 24 |

**Return value:**

| Type | Description |
| --- | --- |
| [Stack](arkts-arkui-typenode-stack-t.md) | 返回 Stack 类型的 FrameNode。 |

