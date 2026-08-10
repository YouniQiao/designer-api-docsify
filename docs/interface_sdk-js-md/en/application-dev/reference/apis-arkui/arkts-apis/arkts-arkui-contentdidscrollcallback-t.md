# ContentDidScrollCallback

```TypeScript
export type ContentDidScrollCallback = (selectedIndex: int, index: int, position: double,
  mainAxisLength: double) => void
```

Swiper滑动时触发的回调，参数可参考[SwiperContentTransitionProxy](../arkts-components/arkts-arkui-swipercontenttransitionproxy-i.md/arkts-arkui-swipercontenttransitionproxy-i.md)中的说明。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export type ContentDidScrollCallback = (selectedIndex: int, index: int, position: double,  mainAxisLength: double) => void--><!--Device-unnamed-export type ContentDidScrollCallback = (selectedIndex: int, index: int, position: double,  mainAxisLength: double) => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| selectedIndex | int | Yes | 当前选中页面的索引。 取值范围为全体整数 取值限定为整数。 |
| index | int | Yes | 视窗内页面的索引。 取值范围为全体整数 取值限定为整数。 |
| position | double | Yes | index页面相对于Swiper主轴起始位置（selectedIndex对应页面的起始位置）的移动比例。 |
| mainAxisLength | double | Yes | index页面相对于Swiper主轴起始位置（selectedIndex对应页面的起始位置）的移动比例。 |

