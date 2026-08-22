# ArcSwiper

## Modules to Import

```TypeScript
```

## ArcSwiper

```TypeScript
@ComponentBuilder
export declare function ArcSwiper(
    controller?: ArcSwiperController, 
    content_?: CustomBuilder
): ArcSwiperAttribute
```

Defines ArcSwiper Component

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function ArcSwiper(    controller?: ArcSwiperController,     content_?: CustomBuilder): ArcSwiperAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ArcSwiper(    controller?: ArcSwiperController,     content_?: CustomBuilder): ArcSwiperAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [ArcSwiperController](arkts-arkui-arcswiper-arcswipercontroller-c.md) | No | ArcSwiper constructor options |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcSwiperAttribute](arkts-arkui-arcswiper-arcswiperattribute-i.md) |  |


## ArcSwiper

```TypeScript
@Builder
export declare function ArcSwiper(
 style_: CustomBuilderT<ArcSwiperAttribute>,
 content_?: CustomBuilder,
): ArcSwiperAttribute
```

Defines ArcSwiper Component

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ArcSwiper( style_: CustomBuilderT<ArcSwiperAttribute>, content_?: CustomBuilder,): ArcSwiperAttribute--><!--Device-unnamed-@Builderexport declare function ArcSwiper( style_: CustomBuilderT<ArcSwiperAttribute>, content_?: CustomBuilder,): ArcSwiperAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;[ArcSwiperAttribute](arkts-arkui-arcswiper-arcswiperattribute-i.md)&gt; | Yes | arcSwiper attribute instance |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcSwiperAttribute](arkts-arkui-arcswiper-arcswiperattribute-i.md) |  |

