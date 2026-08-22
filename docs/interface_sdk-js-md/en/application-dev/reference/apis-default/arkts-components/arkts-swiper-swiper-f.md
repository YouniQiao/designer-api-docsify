# Swiper

## Swiper

```TypeScript
@ComponentBuilder
export declare function Swiper(
  controller?: SwiperController,
  content_?: CustomBuilder
): SwiperAttribute
```

Defines Swiper Component

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Swiper(  controller?: SwiperController,  content_?: CustomBuilder): SwiperAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Swiper(  controller?: SwiperController,  content_?: CustomBuilder): SwiperAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [SwiperController](arkts-swiper-swipercontroller-c.md) | No | Swiper constructor options |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SwiperAttribute](arkts-swiper-attribute.md) |  |


## Swiper

```TypeScript
@Builder
export declare function Swiper(
 style_: CustomBuilderT<SwiperAttribute>,
 content_?: CustomBuilder,
): SwiperAttribute
```

Defines Swiper Component

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Swiper( style_: CustomBuilderT<SwiperAttribute>, content_?: CustomBuilder,): SwiperAttribute--><!--Device-unnamed-@Builderexport declare function Swiper( style_: CustomBuilderT<SwiperAttribute>, content_?: CustomBuilder,): SwiperAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[SwiperAttribute](arkts-swiper-attribute.md)&gt; | Yes | swiper attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SwiperAttribute](arkts-swiper-attribute.md) |  |

