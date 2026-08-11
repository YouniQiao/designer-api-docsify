# ArcSwiper

## Modules to Import

```TypeScript
import { ArcSwiperAttribute, ArcSwiper, ArcDirection, ArcSwiperController, ArcDotIndicator } from 'kits/@kit.ArkUI';
```

## ArcSwiper

```TypeScript
export declare function ArcSwiper(
    controller?: ArcSwiperController, 
    content_?: CustomBuilder
): ArcSwiperAttribute
```

Defines ArcSwiper Component

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ArcSwiper(    controller?: ArcSwiperController,     content_?: CustomBuilder): ArcSwiperAttribute--><!--Device-unnamed-export declare function ArcSwiper(    controller?: ArcSwiperController,     content_?: CustomBuilder): ArcSwiperAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [ArcSwiperController](arkts-arkui-arkui-arcswiper-arcswipercontroller-c.md) | No | ArcSwiper constructor options |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcSwiperAttribute](arkts-arkui-arkui-arcswiper-arcswiperattribute-i.md) |  |


## ArcSwiper

```TypeScript
export declare function ArcSwiper(
 style_: CustomBuilderT<ArcSwiperAttribute>,
 content_?: CustomBuilder,
): ArcSwiperAttribute
```

Defines ArcSwiper Component

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ArcSwiper( style_: CustomBuilderT<ArcSwiperAttribute>, content_?: CustomBuilder,): ArcSwiperAttribute--><!--Device-unnamed-export declare function ArcSwiper( style_: CustomBuilderT<ArcSwiperAttribute>, content_?: CustomBuilder,): ArcSwiperAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ArcSwiperAttribute&gt; | Yes | arcSwiper attribute instance |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcSwiperAttribute](arkts-arkui-arkui-arcswiper-arcswiperattribute-i.md) |  |

