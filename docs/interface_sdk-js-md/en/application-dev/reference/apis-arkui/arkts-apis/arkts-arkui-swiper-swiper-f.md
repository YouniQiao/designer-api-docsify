# Swiper

## Swiper

```TypeScript
export declare function Swiper(
  controller?: SwiperController,
  content_?: CustomBuilder
): SwiperAttribute
```

创建滑块视图容器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Swiper(  controller?: SwiperController,  content_?: CustomBuilder): SwiperAttribute--><!--Device-unnamed-export declare function Swiper(  controller?: SwiperController,  content_?: CustomBuilder): SwiperAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [SwiperController](arkts-arkui-swiper-swipercontroller-c.md) | No | 给组件绑定一个控制器，用来控制组件翻页或者预加载指定子节点。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 子组件。 |

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

定义Swiper组件

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Swiper( style_: CustomBuilderT<SwiperAttribute>, content_?: CustomBuilder,): SwiperAttribute--><!--Device-unnamed-export declare function Swiper( style_: CustomBuilderT<SwiperAttribute>, content_?: CustomBuilder,): SwiperAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;SwiperAttribute&gt; | Yes | swiper属性实例 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 内容区。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SwiperAttribute](arkts-arkui-swiper-swiperattribute-i.md) |  |

