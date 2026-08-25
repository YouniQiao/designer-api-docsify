# TextAreaSubmitCallback

```TypeScript
export type TextAreaSubmitCallback = (enterKeyType: EnterKeyType, event?: SubmitEvent) => void
```

Declare the event listener callback of the enter key.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enterKeyType | [EnterKeyType](arkts-arkui-textinput-enterkeytype-e.md) | 是 |
| event | [SubmitEvent](arkts-arkui-textinput-submitevent-i.md) | 否 |
