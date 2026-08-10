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

创建弧形滑块视图容器。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ArcSwiper(    controller?: ArcSwiperController,     content_?: CustomBuilder): ArcSwiperAttribute--><!--Device-unnamed-export declare function ArcSwiper(    controller?: ArcSwiperController,     content_?: CustomBuilder): ArcSwiperAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [ArcSwiperController](arkts-arkui-arkui-arcswiper-arcswipercontroller-c.md) | No | 给组件绑定一个控制器，用来控制组件翻页。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 可以包含子组件。&lt;br/&gt;**说明：** &lt;br/&gt;1. 子组件类型：系统组件和自定义组件，支持渲染控制类型（ [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md)、 [ForEach](../../../ui/rendering-control/arkts-rendering-control-foreach.md)和 [LazyForEach](../../../ui/rendering-control/arkts-rendering-control-lazyforeach.md)）。&lt;br/&gt;2. 不建议在执行翻页动画过程中增加或减少子 组件，会导致未进行动画的子组件提前进入视窗，引起显示异常。 |

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

定义ArcSwiper组件

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ArcSwiper( style_: CustomBuilderT<ArcSwiperAttribute>, content_?: CustomBuilder,): ArcSwiperAttribute--><!--Device-unnamed-export declare function ArcSwiper( style_: CustomBuilderT<ArcSwiperAttribute>, content_?: CustomBuilder,): ArcSwiperAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Circle

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ArcSwiperAttribute&gt; | Yes | arcSwiper属性实例 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 内容区 |

**Return value:**

| Type | Description |
| --- | --- |
| [ArcSwiperAttribute](arkts-arkui-arkui-arcswiper-arcswiperattribute-i.md) |  |

