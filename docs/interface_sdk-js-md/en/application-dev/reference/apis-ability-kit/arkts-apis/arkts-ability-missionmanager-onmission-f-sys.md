# onMission (System API)

## Modules to Import

```TypeScript
import { missionManager } from 'missionManager';
```

## onMission

```TypeScript
function onMission(listener: MissionListener): long
```

Register the missionListener to ams.

**Since:** 23

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function onMission(listener: MissionListener): long--><!--Device-missionManager-function onMission(listener: MissionListener): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| listener | MissionListener | Yes | Indicates the MissionListener to be registered. |

**Return value:**

| Type | Description |
| --- | --- |
| long | Returns the index number of the MissionListener. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. |

