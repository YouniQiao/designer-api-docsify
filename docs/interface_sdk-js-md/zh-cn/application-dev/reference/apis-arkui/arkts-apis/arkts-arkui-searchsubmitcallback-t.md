# SearchSubmitCallback

```TypeScript
export type SearchSubmitCallback = (searchContent: string, event?: SubmitEvent) => void
```

点击搜索图标、搜索按钮或者按下软键盘搜索按钮时的回调事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| searchContent | string | 是 |
| event | [SubmitEvent](arkts-arkui-textinput-submitevent-i.md) | 否 |
