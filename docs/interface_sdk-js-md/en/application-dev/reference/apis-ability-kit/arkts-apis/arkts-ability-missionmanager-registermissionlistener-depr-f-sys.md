# registerMissionListener (System API)

## Modules to Import

```TypeScript
```

## registerMissionListener

```TypeScript
function registerMissionListener(listener: MissionListener): number
```

Registers a listener to observe the mission status.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [on](arkts-ability-missionmanager-on-f-sys.md)

**Required permissions:** ohos.permission.MANAGE_MISSIONS

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| listener | [MissionListener](arkts-ability-missionlistener-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
