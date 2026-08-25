# OnTabsAnimationStartCallback

```TypeScript
export type OnTabsAnimationStartCallback = (index: int, targetIndex: int, extraInfo: TabsAnimationEvent) => void
```

切换动画开始时触发的回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | int | 是 |
| targetIndex | int | 是 |
| extraInfo | [TabsAnimationEvent](arkts-arkui-tabs-tabsanimationevent-i.md) | 是 |
