# ScrollOnScrollCallback

```TypeScript
declare type ScrollOnScrollCallback = (xOffset: number, yOffset: number, scrollState: ScrollState) => void
```

Scroll滚动时触发的回调。

**起始版本：** 12

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type ScrollOnScrollCallback = (xOffset: number, yOffset: number, scrollState: ScrollState) => void--><!--Device-unnamed-declare type ScrollOnScrollCallback = (xOffset: number, yOffset: number, scrollState: ScrollState) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| xOffset | number | 是 |
| yOffset | number | 是 |
| scrollState | [ScrollState](arkts-arkui-scrollstate-e.md) | 是 |
