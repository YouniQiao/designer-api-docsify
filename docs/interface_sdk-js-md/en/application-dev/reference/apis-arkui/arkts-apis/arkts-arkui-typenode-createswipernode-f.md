# createSwiperNode

## createSwiperNode

```TypeScript
export function createSwiperNode(context: UIContext, options?: FrameNodeOptions): Swiper
```

Create a FrameNode of Swiper type.On API 26.0.0 and above, It can also create a FrameNode of Swiper type with options.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-typeNode-export function createSwiperNode(context: UIContext, options?: FrameNodeOptions): Swiper--><!--Device-typeNode-export function createSwiperNode(context: UIContext, options?: FrameNodeOptions): Swiper-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c.md) | Yes | uiContext used to create the FrameNode. |
| options | [FrameNodeOptions](arkts-arkui-framenode-framenodeoptions-i.md) | No | Options for configuring FrameNode creation.<br>**Since:** 26.0.0 |

**Return value:**

| Type | Description |
| --- | --- |
| [Swiper](arkts-arkui-typenode-swiper-t.md) | Return Swiper type FrameNode. |

