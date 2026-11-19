# ResultCallback

```TypeScript
type ResultCallback = (result: ControlComponentClickResult) => void
```

Callback function type used to receive the result of each simulated click operation.

**Since:** 26.1.0

**Model restriction:** This API can be used in both the stage model and FA model.

<!--Device-abilityToolAccessCtrl-type ResultCallback = (result: ControlComponentClickResult) => void--><!--Device-abilityToolAccessCtrl-type ResultCallback = (result: ControlComponentClickResult) => void-End-->

**System capability:** SystemCapability.Security.Asset

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | [ControlComponentClickResult](arkts-ability-abilitytoolaccessctrl-controlcomponentclickresult-i.md) | Yes | This interface is used to call back the service party to simulate the click result. |
