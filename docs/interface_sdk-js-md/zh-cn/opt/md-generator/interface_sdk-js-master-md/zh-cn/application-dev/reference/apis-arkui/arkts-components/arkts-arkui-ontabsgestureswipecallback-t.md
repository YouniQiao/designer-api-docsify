# OnTabsGestureSwipeCallback

```TypeScript
declare type OnTabsGestureSwipeCallback = (index: number, extraInfo: TabsAnimationEvent) => void
```

在页面跟手滑动过程中，逐帧触发的回调。

**起始版本：** 18

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type OnTabsGestureSwipeCallback = (index: number, extraInfo: TabsAnimationEvent) => void--><!--Device-unnamed-declare type OnTabsGestureSwipeCallback = (index: number, extraInfo: TabsAnimationEvent) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |
| extraInfo | [TabsAnimationEvent](arkts-arkui-tabsanimationevent-i.md) | 是 |
