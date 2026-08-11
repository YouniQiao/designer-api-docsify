# ContentWillScrollCallback

```TypeScript
declare type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean
```

Defines the callback triggered when the **Swiper** component is about to scroll. The return value indicates whether the scroll action is allowed.

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**Widget capability:** This API can be used in ArkTS widgets since API version 15.

<!--Device-unnamed-declare type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean--><!--Device-unnamed-declare type ContentWillScrollCallback = (result: SwiperContentWillScrollResult) => boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | [SwiperContentWillScrollResult](arkts-arkui-swipercontentwillscrollresult-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
