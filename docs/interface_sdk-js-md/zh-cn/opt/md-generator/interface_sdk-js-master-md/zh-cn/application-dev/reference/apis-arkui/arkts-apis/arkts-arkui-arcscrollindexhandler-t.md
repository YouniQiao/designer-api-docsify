# ArcScrollIndexHandler

```TypeScript
declare type ArcScrollIndexHandler = (start: number, end: number, center: number) => void
```

有子组件划入或划出ArcList显示区域时触发的回调。

**起始版本：** 18

**废弃版本：** -1

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type ArcScrollIndexHandler = (start: number, end: number, center: number) => void--><!--Device-unnamed-declare type ArcScrollIndexHandler = (start: number, end: number, center: number) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Circle

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| start | number | 是 |
| end | number | 是 |
| center | number | 是 |
