# ContentWillScrollCallback

```TypeScript
export type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean
```

Swiper即将滑动前触发的回调，返回值表示是否允许此次滑动。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean--><!--Device-unnamed-export type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | [SwiperContentWillScrollResult](arkts-arkui-swiper-swipercontentwillscrollresult-i.md) | Yes | 即将滑动的相关信息，主要包括：当前页面对应的index、滑动方向上即将显示的页面index和此次滑动的位移。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Swiper是否响应本次滑动，true表示响应，false表示不响应。 |

