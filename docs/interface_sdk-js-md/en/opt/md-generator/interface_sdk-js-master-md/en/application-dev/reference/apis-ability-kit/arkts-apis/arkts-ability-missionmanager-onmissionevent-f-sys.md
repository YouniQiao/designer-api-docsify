# on_missionEvent (System API)

## Modules to Import

```TypeScript
```

## on_missionEvent

```TypeScript
function on(type: 'missionEvent', listener: MissionListener): number
```

Registers a listener to observe the mission status.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [on](arkts-ability-missionmanager-onmission-f-sys.md#onmission)(type: 'mission', listener: MissionListener)

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function on(type: 'missionEvent', listener: MissionListener): long--><!--Device-missionManager-function on(type: 'missionEvent', listener: MissionListener): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'missionEvent' | Yes |
| listener | [MissionListener](arkts-ability-missionmanager-missionlistener-t-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
