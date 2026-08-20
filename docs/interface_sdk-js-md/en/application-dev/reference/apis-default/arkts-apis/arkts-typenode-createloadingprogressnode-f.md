# createLoadingProgressNode

## createLoadingProgressNode

```TypeScript
export function createLoadingProgressNode(context: UIContext, options?: FrameNodeOptions): LoadingProgress
```

Create a FrameNode of LoadingProgress type. On API 26.0.0 and above, It can also create a FrameNode of LoadingProgress type with options.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createLoadingProgressNode(context: UIContext, options?: FrameNodeOptions): LoadingProgress--><!--Device-typeNode-export function createLoadingProgressNode(context: UIContext, options?: FrameNodeOptions): LoadingProgress-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [FrameNodeOptions](arkts-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| LoadingProgress | Return LoadingProgress type FrameNode. |

