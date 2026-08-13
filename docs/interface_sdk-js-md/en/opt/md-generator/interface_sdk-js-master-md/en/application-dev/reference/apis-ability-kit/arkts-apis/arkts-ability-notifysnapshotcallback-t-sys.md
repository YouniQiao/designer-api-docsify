# NotifySnapshotCallback (System API)

```TypeScript
type NotifySnapshotCallback = (deviceId: string, mission: number) => void
```

Callback function on snapshot changed.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type NotifySnapshotCallback = (deviceId: string, mission: int) => void--><!--Device-unnamed-type NotifySnapshotCallback = (deviceId: string, mission: int) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| mission | number | Yes |
