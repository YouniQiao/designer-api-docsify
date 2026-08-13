# @ohos.application.missionManager

The missionManager module provides APIs to lock, unlock, and clear missions, and switch a mission to the foreground.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [missionManager/missionManager](arkts-app-ability-missionmanager.md#@ohos.app.ability.missionManager)

**Required permissions:** ohos.permission.MANAGE_MISSIONS

<!--Device-unnamed-declare namespace missionManager--><!--Device-unnamed-declare namespace missionManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [clearAllMissions](arkts-ability-missionmanager-clearallmissions-depr-f-sys.md#clearAllMissions) | Clears all unlocked missions. This API uses an asynchronous callback to return the result. |
| [clearAllMissions](arkts-ability-missionmanager-clearallmissions-depr-f-sys.md#clearAllMissions) | Clears all unlocked missions. This API uses a promise to return the result. |
| [clearMission](arkts-ability-missionmanager-clearmission-depr-f-sys.md#clearMission) | Clears a given mission, regardless of whether it is locked. This API uses an asynchronous callback to return the result. |
| [clearMission](arkts-ability-missionmanager-clearmission-depr-f-sys.md#clearMission) | Clears a given mission, regardless of whether it is locked. This API uses a promise to return the result. |
| [getMissionInfo](arkts-ability-missionmanager-getmissioninfo-depr-f-sys.md#getMissionInfo) | Obtains the information about a given mission. This API uses an asynchronous callback to return the result. |
| [getMissionInfo](arkts-ability-missionmanager-getmissioninfo-depr-f-sys.md#getMissionInfo) | Obtains the information about a given mission. This API uses a promise to return the result. |
| [getMissionInfos](arkts-ability-missionmanager-getmissioninfos-depr-f-sys.md#getMissionInfos) | Obtains information about all missions. This API uses an asynchronous callback to return the result. |
| [getMissionInfos](arkts-ability-missionmanager-getmissioninfos-depr-f-sys.md#getMissionInfos) | Obtains information about all missions. This API uses a promise to return the result. |
| [getMissionSnapShot](arkts-ability-missionmanager-getmissionsnapshot-depr-f-sys.md#getMissionSnapShot) | Obtains the snapshot of a given mission. This API uses an asynchronous callback to return the result. |
| [getMissionSnapShot](arkts-ability-missionmanager-getmissionsnapshot-depr-f-sys.md#getMissionSnapShot) | Obtains the snapshot of a given mission. This API uses a promise to return the result. |
| [lockMission](arkts-ability-missionmanager-lockmission-depr-f-sys.md#lockMission) | Locks a given mission. This API uses an asynchronous callback to return the result. |
| [lockMission](arkts-ability-missionmanager-lockmission-depr-f-sys.md#lockMission) | Locks a given mission. This API uses a promise to return the result. |
| [moveMissionToFront](arkts-ability-missionmanager-movemissiontofront-depr-f-sys.md#moveMissionToFront) | Switches a given mission to the foreground. This API uses an asynchronous callback to return the result. |
| [moveMissionToFront](arkts-ability-missionmanager-movemissiontofront-depr-f-sys.md#moveMissionToFront) | Switches a given mission to the foreground, with the startup parameters for the switching specified. This API uses an asynchronous callback to return the result. |
| [moveMissionToFront](arkts-ability-missionmanager-movemissiontofront-depr-f-sys.md#moveMissionToFront) | Switches a given mission to the foreground, with the startup parameters for the switching specified. This API uses a promise to return the result. |
| [registerMissionListener](arkts-ability-missionmanager-registermissionlistener-depr-f-sys.md#registerMissionListener) | Registers a listener to observe the mission status. |
| [unlockMission](arkts-ability-missionmanager-unlockmission-depr-f-sys.md#unlockMission) | Unlocks a given mission. This API uses an asynchronous callback to return the result. |
| [unlockMission](arkts-ability-missionmanager-unlockmission-depr-f-sys.md#unlockMission) | Unlocks a given mission. This API uses a promise to return the result. |
| [unregisterMissionListener](arkts-ability-missionmanager-unregistermissionlistener-depr-f-sys.md#unregisterMissionListener) | Unregisters a mission status listener. This API uses an asynchronous callback to return the result. |
| [unregisterMissionListener](arkts-ability-missionmanager-unregistermissionlistener-depr-f-sys.md#unregisterMissionListener) | Unregisters a mission status listener. This API uses a promise to return the result. |
<!--DelEnd-->

