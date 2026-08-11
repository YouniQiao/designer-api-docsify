# NotifySnapshotCallback (System API)

```TypeScript
type NotifySnapshotCallback = (deviceId: string, mission: int) => void
```

Callback function on snapshot changed.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type NotifySnapshotCallback = (deviceId: string, mission: int) => void--><!--Device-unnamed-type NotifySnapshotCallback = (deviceId: string, mission: int) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates the deviceId snapshot changed. |
| mission | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the id of mission. |

