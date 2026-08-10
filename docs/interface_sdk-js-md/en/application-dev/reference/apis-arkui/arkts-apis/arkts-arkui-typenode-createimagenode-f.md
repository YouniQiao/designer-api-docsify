# createImageNode

## createImageNode

```TypeScript
export function createImageNode(context: UIContext, options?: FrameNodeOptions): Image
```

创建 Image 类型的 FrameNode

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createImageNode(context: UIContext, options?: FrameNodeOptions): Image--><!--Device-typeNode-export function createImageNode(context: UIContext, options?: FrameNodeOptions): Image-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | 用于创建 FrameNode 的 UI 上下文 |
| options | [FrameNodeOptions](arkts-arkui-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 24 |

**Return value:**

| Type | Description |
| --- | --- |
| [Image](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-sceneresources-image-i.md) | 返回 Image 类型的 FrameNode |

