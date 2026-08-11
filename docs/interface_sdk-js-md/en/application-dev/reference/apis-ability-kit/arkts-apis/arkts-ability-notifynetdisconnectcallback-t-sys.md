# NotifyNetDisconnectCallback (System API)

```TypeScript
type NotifyNetDisconnectCallback = (deviceId: string, state: int) => void
```

Callback function on network disconnect.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type NotifyNetDisconnectCallback = (deviceId: string, state: int) => void--><!--Device-unnamed-type NotifyNetDisconnectCallback = (deviceId: string, state: int) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates the deviceId network disconnect. |
| state | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the state of network. |

