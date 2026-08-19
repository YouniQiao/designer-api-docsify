# on_missionEvent (System API)

## Modules to Import

```TypeScript
import { missionManager } from '@kit.AbilityKit';
```

## on('missionEvent')

```TypeScript
function on(type: 'missionEvent', listener: MissionListener): long
```

Registers a listener to observe the mission status.

**Since:** 9

**Deprecated since:** 10

**Substitutes:** [on](arkts-ability-missionmanager-onmission-f-sys.md)(type: 'mission', listener: MissionListener)

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function on(type: 'missionEvent', listener: MissionListener): long--><!--Device-missionManager-function on(type: 'missionEvent', listener: MissionListener): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'missionEvent' | Yes | Name of the target mission. The value is fixed at **'missionEvent'**, indicating the system mission status listener. |
| listener | MissionListener | Yes | Mission status listener to register. |

**Return value:**

| Type | Description |
| --- | --- |
| long | Index of the mission status listener, which is created by the system and allocated when the listener is registered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

