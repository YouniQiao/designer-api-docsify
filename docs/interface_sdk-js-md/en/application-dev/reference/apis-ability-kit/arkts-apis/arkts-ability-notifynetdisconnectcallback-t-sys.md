# NotifyNetDisconnectCallback (System API)

```TypeScript
type NotifyNetDisconnectCallback = (deviceId: string, state: int) => void
```

Callback function on network disconnect.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| state | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |
