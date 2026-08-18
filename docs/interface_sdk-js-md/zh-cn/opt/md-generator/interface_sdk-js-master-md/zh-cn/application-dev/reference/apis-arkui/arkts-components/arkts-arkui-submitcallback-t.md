# SubmitCallback

```TypeScript
declare type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void
```

软键盘按下回车键时的回调事件。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-unnamed-declare type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void--><!--Device-unnamed-declare type SubmitCallback = (enterKey: EnterKeyType, event: SubmitEvent) => void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enterKey | [EnterKeyType](arkts-arkui-enterkeytype-e.md) | 是 |
| event | [SubmitEvent](arkts-arkui-submitevent-i.md) | 是 |
