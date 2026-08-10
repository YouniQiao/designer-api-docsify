# SwiperFrameNode

定义Swiper类型的FrameNode。

**Inheritance/Implementation:** SwiperFrameNode extends [TypedFrameNode<SwiperAttribute>](TypedFrameNode<SwiperAttribute>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-typeNode-abstract class SwiperFrameNode extends TypedFrameNode<SwiperAttribute>--><!--Device-typeNode-abstract class SwiperFrameNode extends TypedFrameNode<SwiperAttribute>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## initialize

```TypeScript
abstract initialize(controller?: SwiperController): SwiperAttribute
```

初始化Swiper类型的FrameNode。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SwiperFrameNode-abstract initialize(controller?: SwiperController): SwiperAttribute--><!--Device-SwiperFrameNode-abstract initialize(controller?: SwiperController): SwiperAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| controller | [SwiperController](../arkts-components/arkts-arkui-swipercontroller-c.md) | No | swiper的控制器。 |

**Return value:**

| Type | Description |
| --- | --- |
| [SwiperAttribute](../arkts-components/arkts-arkui-swiper-attribute.md) |  |

