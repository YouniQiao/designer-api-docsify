# @ohos.app.ability.missionManager

The missionManager module provides APIs to lock, unlock, and clear missions, and switch a mission to the foreground.

**Since:** 23

<!--Device-unnamed-declare namespace missionManager--><!--Device-unnamed-declare namespace missionManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { missionManager } from '@kit.AbilityKit';
import { missionManager } from '@kit.AbilityKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [clearAllMissions](arkts-ability-missionmanager-clearallmissions-f-sys.md#clearallmissions) | Clears all unlocked missions. This API uses an asynchronous callback to return the result. |
| [clearAllMissions](arkts-ability-missionmanager-clearallmissions-f-sys.md#clearallmissions-system-api) | Clears all unlocked missions. This API uses a promise to return the result. |
| [clearMission](arkts-ability-missionmanager-clearmission-f-sys.md#clearmission) | Clears a given mission, regardless of whether it is locked. This API uses an asynchronous callback to return the result. |
| [clearMission](arkts-ability-missionmanager-clearmission-f-sys.md#clearmission-system-api) | Clears a given mission, regardless of whether it is locked. This API uses a promise to return the result. |
| [getLowResolutionMissionSnapShot](arkts-ability-missionmanager-getlowresolutionmissionsnapshot-f-sys.md#getlowresolutionmissionsnapshot) | Obtains the low-resolution snapshot of a given mission. This API uses an asynchronous callback to return the result. |
| [getLowResolutionMissionSnapShot](arkts-ability-missionmanager-getlowresolutionmissionsnapshot-f-sys.md#getlowresolutionmissionsnapshot-system-api) | Obtains the low-resolution snapshot of a given mission. This API uses a promise to return the result. |
| [getMissionInfo](arkts-ability-missionmanager-getmissioninfo-f-sys.md#getmissioninfo) | Obtains the mission information. This API uses an asynchronous callback to return the result. |
| [getMissionInfo](arkts-ability-missionmanager-getmissioninfo-f-sys.md#getmissioninfo-system-api) | Obtains the mission information. This API uses a promise to return the result. |
| [getMissionInfos](arkts-ability-missionmanager-getmissioninfos-f-sys.md#getmissioninfos) | Obtains information about all missions. This API uses an asynchronous callback to return the result. |
| [getMissionInfos](arkts-ability-missionmanager-getmissioninfos-f-sys.md#getmissioninfos-system-api) | Obtains information about all missions. This API uses a promise to return the result. |
| [getMissionSnapShot](arkts-ability-missionmanager-getmissionsnapshot-f-sys.md#getmissionsnapshot) | Obtains the snapshot of a given mission. This API uses an asynchronous callback to return the result. |
| [getMissionSnapShot](arkts-ability-missionmanager-getmissionsnapshot-f-sys.md#getmissionsnapshot-system-api) | Obtains the snapshot of a given mission. This API uses a promise to return the result. |
| [lockMission](arkts-ability-missionmanager-lockmission-f-sys.md#lockmission) | Locks a given mission. This API uses an asynchronous callback to return the result. |
| [lockMission](arkts-ability-missionmanager-lockmission-f-sys.md#lockmission-system-api) | Locks a given mission. This API uses a promise to return the result. |
| [moveMissionToFront](arkts-ability-missionmanager-movemissiontofront-f-sys.md#movemissiontofront) | Switches a given mission to the foreground. This API uses an asynchronous callback to return the result. |
| [moveMissionToFront](arkts-ability-missionmanager-movemissiontofront-f-sys.md#movemissiontofront-system-api) | Switches a given mission to the foreground, with the startup parameters for the switching specified. This API uses an asynchronous callback to return the result. |
| [moveMissionToFront](arkts-ability-missionmanager-movemissiontofront-f-sys.md#movemissiontofront-system-api) | Switches a given mission to the foreground, with the startup parameters for the switching specified. This API uses a promise to return the result. |
| [moveMissionsToBackground](arkts-ability-missionmanager-movemissionstobackground-f-sys.md#movemissionstobackground) | Switches a batch of missions to the background. The mission IDs returned are sorted by mission level when the missions are switched. This API uses an asynchronous callback to return the result. |
| [moveMissionsToBackground](arkts-ability-missionmanager-movemissionstobackground-f-sys.md#movemissionstobackground-system-api) | Switches a batch of missions to the background. The mission IDs returned are sorted by mission level when the missions are switched. This API uses a promise to return the result. |
| [moveMissionsToForeground](arkts-ability-missionmanager-movemissionstoforeground-f-sys.md#movemissionstoforeground) | Switches a batch of missions to the foreground. This API uses an asynchronous callback to return the result. |
| [moveMissionsToForeground](arkts-ability-missionmanager-movemissionstoforeground-f-sys.md#movemissionstoforeground-system-api) | Switches a batch of missions to the foreground, and moves the mission with the specified ID to the top. This API uses an asynchronous callback to return the result. |
| [moveMissionsToForeground](arkts-ability-missionmanager-movemissionstoforeground-f-sys.md#movemissionstoforeground-system-api) | Switches a batch of missions to the foreground, and moves the mission with the specified ID to the top. This API uses a promise to return the result. |
| [offMission](arkts-ability-missionmanager-offmission-f-sys.md#offmission) | Unregister the missionListener to ams. |
| [offMission](arkts-ability-missionmanager-offmission-f-sys.md#offmission-system-api) | Unregister the missionListener to ams. |
| [off_mission](arkts-ability-missionmanager-offmission-f-sys.md#offmission) | Deregisters a mission status listener. This API uses an asynchronous callback to return the result. |
| [off_mission](arkts-ability-missionmanager-offmission-f-sys.md#offmission-system-api) | Unregisters a mission status listener. This API uses a promise to return the result. |
| [off_missionEvent](arkts-ability-missionmanager-offmissionevent-f-sys.md#offmissionevent) | Deregisters a mission status listener. This API uses an asynchronous callback to return the result. |
| [off_missionEvent](arkts-ability-missionmanager-offmissionevent-f-sys.md#offmissionevent-1) | Unregisters a mission status listener. This API uses a promise to return the result. |
| [onMission](arkts-ability-missionmanager-onmission-f-sys.md#onmission) | Register the missionListener to ams. |
| [on_mission](arkts-ability-missionmanager-onmission-f-sys.md#onmission) | Registers a listener to observe the mission status. |
| [on_missionEvent](arkts-ability-missionmanager-onmissionevent-f-sys.md#onmissionevent) | Registers a listener to observe the mission status. |
| [unlockMission](arkts-ability-missionmanager-unlockmission-f-sys.md#unlockmission) | Unlocks a given mission. This API uses an asynchronous callback to return the result. |
| [unlockMission](arkts-ability-missionmanager-unlockmission-f-sys.md#unlockmission-system-api) | Unlocks a given mission. This API uses a promise to return the result. |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [MissionInfo](arkts-ability-missionmanager-missioninfo-t-sys.md) | Mission information corresponding to ability. |
| [MissionListener](arkts-ability-missionmanager-missionlistener-t-sys.md) | MissionListener registered by app. |
| [MissionSnapshot](arkts-ability-missionmanager-missionsnapshot-t-sys.md) | Mission snapshot corresponding to mission. |
<!--DelEnd-->

