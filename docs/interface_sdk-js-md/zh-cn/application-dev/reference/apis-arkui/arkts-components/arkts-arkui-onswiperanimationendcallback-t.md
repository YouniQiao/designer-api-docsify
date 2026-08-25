# OnSwiperAnimationEndCallback

```TypeScript
declare type OnSwiperAnimationEndCallback = (index: number, extraInfo: SwiperAnimationEvent) => void
```

切换动画结束时触发的回调。

**起始版本：** 18

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本18开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| extraInfo | [SwiperAnimationEvent](arkts-arkui-swiperanimationevent-i.md) | 是 |
