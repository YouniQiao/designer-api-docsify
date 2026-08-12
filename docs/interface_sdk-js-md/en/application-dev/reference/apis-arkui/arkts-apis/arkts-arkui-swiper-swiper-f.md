# Swiper

## Swiper

```TypeScript
export declare function Swiper(
  controller?: SwiperController,
  content_?: CustomBuilder
): SwiperAttribute
```

Defines Swiper Component

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Swiper(  controller?: SwiperController,  content_?: CustomBuilder): SwiperAttribute--><!--Device-unnamed-export declare function Swiper(  controller?: SwiperController,  content_?: CustomBuilder): SwiperAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [SwiperController](arkts-arkui-swiper-swipercontroller-c.md) | No | Swiper constructor options |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |  |


## Swiper

```TypeScript
export declare function Swiper(
 style_: CustomBuilderT<SwiperAttribute>,
 content_?: CustomBuilder,
): SwiperAttribute
```

Defines Swiper Component

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Swiper( style_: CustomBuilderT<SwiperAttribute>, content_?: CustomBuilder,): SwiperAttribute--><!--Device-unnamed-export declare function Swiper( style_: CustomBuilderT<SwiperAttribute>, content_?: CustomBuilder,): SwiperAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md)&gt; | Yes | swiper attribute instance |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |  |

