# NotifyNetDisconnectCallback (System API)

```TypeScript
type NotifyNetDisconnectCallback = (deviceId: string, state: number) => void
```

Callback function on network disconnect.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-type NotifyNetDisconnectCallback = (deviceId: string, state: int) => void--><!--Device-unnamed-type NotifyNetDisconnectCallback = (deviceId: string, state: int) => void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceId | string | Yes |
| state | number | Yes |
