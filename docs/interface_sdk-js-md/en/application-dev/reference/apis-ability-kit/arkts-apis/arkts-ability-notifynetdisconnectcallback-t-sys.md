# NotifyNetDisconnectCallback (System API)

```TypeScript
type NotifyNetDisconnectCallback = (deviceId: string, state: int) => void
```

Callback function on network disconnect.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type NotifyNetDisconnectCallback = (deviceId: string, state: int) => void--><!--Device-unnamed-type NotifyNetDisconnectCallback = (deviceId: string, state: int) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates the deviceId network disconnect. |
| state | int | Yes | Indicates the state of network. |

