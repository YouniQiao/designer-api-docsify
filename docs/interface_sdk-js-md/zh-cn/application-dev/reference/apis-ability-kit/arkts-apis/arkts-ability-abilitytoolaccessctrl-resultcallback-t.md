# ResultCallback

```TypeScript
type ResultCallback = (result: ControlComponentClickResult) => void
```

用于接收每次模拟点击操作结果的回调函数类型。

**起始版本：** 26.1.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-abilityToolAccessCtrl-type ResultCallback = (result: ControlComponentClickResult) => void--><!--Device-abilityToolAccessCtrl-type ResultCallback = (result: ControlComponentClickResult) => void-End-->

**系统能力：** SystemCapability.Security.Asset

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | [ControlComponentClickResult](arkts-ability-abilitytoolaccessctrl-controlcomponentclickresult-i.md) | 是 | 用于回调业务方模拟点击结果。 |
