# SwiperElement

The &lt;swiper&gt; component provides a swiper container.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

<!--Device-unnamed-export interface SwiperElement--><!--Device-unnamed-export interface SwiperElement-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## rotation

```TypeScript
rotation(obj?: FocusParamObj): void
```

Requests or cancels the crown rotation focus for a component.If focus is set to true, the crown event focus is requested.If focus is set to false, the crown event focus is canceled.This attribute can be defaulted to true.

**起始版本：** 4

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为4。

**模型约束：** 此接口仅可在FA模型下使用。

<!--Device-SwiperElement-rotation(obj?: FocusParamObj): void--><!--Device-SwiperElement-rotation(obj?: FocusParamObj): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| obj | [FocusParamObj](arkts-arkui-viewmodel-focusparamobj-i.md) | 否 | { focus: true \| false } |

