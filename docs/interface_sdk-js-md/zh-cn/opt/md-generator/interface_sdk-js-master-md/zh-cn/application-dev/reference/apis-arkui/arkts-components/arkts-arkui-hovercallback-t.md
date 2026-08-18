# HoverCallback

```TypeScript
declare type HoverCallback = (isHover: boolean, event: HoverEvent) => void
```

hover事件的回调类型。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type HoverCallback = (isHover: boolean, event: HoverEvent) => void--><!--Device-unnamed-declare type HoverCallback = (isHover: boolean, event: HoverEvent) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| isHover | boolean | 是 |
| event | [HoverEvent](arkts-arkui-hoverevent-i.md) | 是 |
