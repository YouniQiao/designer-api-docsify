# ContentDidScrollCallback

```TypeScript
export type ContentDidScrollCallback = (selectedIndex: int, index: int, position: double,
  mainAxisLength: double) => void
```

Swiper滑动时触发的回调，参数可参考[SwiperContentTransitionProxy](arkts-arkui-swiper-swipercontenttransitionproxy-i.md)中的说明。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| selectedIndex | int | 是 |
| index | int | 是 |
| position | double | 是 |
| mainAxisLength | double | 是 |
