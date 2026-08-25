# OnHoverCallback

```TypeScript
declare type OnHoverCallback = (status: boolean, event: HoverEvent) => void
```

鼠标悬浮触发回调。

**起始版本：** 14

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本14开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| status | boolean | 是 |
| event | [HoverEvent](arkts-arkui-hoverevent-i.md) | 是 |
