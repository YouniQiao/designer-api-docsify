# AnimationEndHandler

```TypeScript
declare type AnimationEndHandler = (index: number, event: SwiperAnimationEvent) => void
```

切换动画结束时的回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type AnimationEndHandler = (index: number, event: SwiperAnimationEvent) => void--><!--Device-unnamed-declare type AnimationEndHandler = (index: number, event: SwiperAnimationEvent) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| event | [SwiperAnimationEvent](../arkts-components/arkts-arkui-swiperanimationevent-i.md) | 是 |
