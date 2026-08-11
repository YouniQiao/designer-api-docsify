# OnContentScrollCallback

```TypeScript
declare type OnContentScrollCallback = (totalOffsetX: number, totalOffsetY: number) => void
```

文本内容滚动时，触发该回调。

**起始版本：** 18

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type OnContentScrollCallback = (totalOffsetX: number, totalOffsetY: number) => void--><!--Device-unnamed-declare type OnContentScrollCallback = (totalOffsetX: number, totalOffsetY: number) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| totalOffsetX | number | 是 |
| totalOffsetY | number | 是 |
