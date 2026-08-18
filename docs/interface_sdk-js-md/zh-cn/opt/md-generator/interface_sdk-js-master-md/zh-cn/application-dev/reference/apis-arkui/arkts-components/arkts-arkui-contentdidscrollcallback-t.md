# ContentDidScrollCallback

```TypeScript
declare type ContentDidScrollCallback = (selectedIndex: number, index: number, position: number, mainAxisLength: number) => void
```

Swiper滑动时触发的回调，参数可参考[SwiperContentTransitionProxy](arkts-arkui-swipercontenttransitionproxy-i.md#swipercontenttransitionproxy)中的说明。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type ContentDidScrollCallback = (selectedIndex: number, index: number, position: number, mainAxisLength: number) => void--><!--Device-unnamed-declare type ContentDidScrollCallback = (selectedIndex: number, index: number, position: number, mainAxisLength: number) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| selectedIndex | number | 是 |
| index | number | 是 |
| position | number | 是 |
| mainAxisLength | number | 是 |
