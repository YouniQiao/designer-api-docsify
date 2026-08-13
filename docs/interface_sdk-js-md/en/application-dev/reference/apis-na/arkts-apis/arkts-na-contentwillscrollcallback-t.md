# ContentWillScrollCallback

```TypeScript
export type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean
```

The callback of onContentWillScroll.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean--><!--Device-unnamed-export type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | [SwiperContentWillScrollResult](arkts-na-swiper-swipercontentwillscrollresult-i.md) | Yes | the result of swiper ContentWillScrollCallback. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | whether to allow scroll, true indicating can scroll and false indicating can not scroll. |

