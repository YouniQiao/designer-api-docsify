# Marquee

跑马灯组件，用于滚动展示一段单行文本，支持自定义滚动速度、方向、循环次数等。仅当文本内容宽度大于等于跑马灯组件宽度时滚动，否则不滚动。适用于需要在有限空间内展示较长文本的场景，如新闻标题滚动、通知公告、广告轮播等，可以有效节省界面空间
并吸引用户注意。

> **说明：**
>
> 为了不影响滚动帧率，建议在滚动类组件中Marquee的个数不超过4个，或者使用
>
> 对于Marquee组件动态帧率的场景，可以使用[MarqueeDynamicSyncScene]{@link @ohos.arkui.UIContext}接口实现。
>
> 在文本宽度小于跑马灯组件宽度时，使用[属性动画]{@link ./common}实现滚动。

## 子组件

无

## Marquee

```TypeScript
Marquee(options: MarqueeOptions)
```

创建跑马灯组件。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-MarqueeInterface-(options: MarqueeOptions): MarqueeAttribute--><!--Device-MarqueeInterface-(options: MarqueeOptions): MarqueeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [MarqueeOptions](../arkts-apis/arkts-arkui-marquee-marqueeoptions-i.md) | Yes | 配置跑马灯组件的参数。 |

## Summary

- [MarqueeOptions](arkts-arkui-marquee-marqueeoptions-i.md)
