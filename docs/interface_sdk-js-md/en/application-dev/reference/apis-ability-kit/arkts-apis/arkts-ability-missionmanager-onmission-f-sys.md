# onMission (System API)

## Modules to Import

```TypeScript
import { missionManager } from 'kits/@kit.AbilityKit';
```

## onMission

```TypeScript
function onMission(listener: MissionListener): long
```

注册系统任务状态监听器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-missionManager-function onMission(listener: MissionListener): long--><!--Device-missionManager-function onMission(listener: MissionListener): long-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| listener | [MissionListener](arkts-ability-missionmanager-missionlistener-t-sys.md) | Yes | 系统任务监听器。 |

**Return value:**

| Type | Description |
| --- | --- |
| long | 监听器的index值，由系统创建，在注册系统任务状态监听时分配，和监听器一一对应 。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Not system application. |

