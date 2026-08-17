# @ohos.distributedMissionManager

The distributedMissionManager module implements mission management across devices. You can use the APIs provided by this module to register or unregister a mission status listener, start or stop synchronizing a remote mission list, and continue a mission on a remote device by mission ID or bundle name.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace distributedMissionManager--><!--Device-unnamed-declare namespace distributedMissionManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Mission

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { distributedMissionManager } from 'distributedMissionManager';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [continueMission](arkts-ability-distributedmissionmanager-continuemission-f-sys.md#continuemission) | Continues a mission on a remote device, with the mission ID specified. This API uses an asynchronous callback to return the result. |
| [continueMission](arkts-ability-distributedmissionmanager-continuemission-f-sys.md#continuemission-system-api) | Continues a mission on a remote device, with the mission ID specified. This API uses a promise to return the result. |
| [continueMission](arkts-ability-distributedmissionmanager-continuemission-f-sys.md#continuemission-system-api) | Continues a mission on a remote device, with the bundle name specified. This API uses an asynchronous callback to return the result. |
| [continueMission](arkts-ability-distributedmissionmanager-continuemission-f-sys.md#continuemission-system-api) | Continues a mission on a remote device, with the bundle name specified. This API uses a promise to return the result. |
| [offContinueStateChange](arkts-ability-distributedmissionmanager-offcontinuestatechange-f-sys.md#offcontinuestatechange) | Unregister continuable info listener to ams. |
| [off_continueStateChange](arkts-ability-distributedmissionmanager-offcontinuestatechange-f-sys.md#offcontinuestatechange) | Unsubscribes from continuation state change events of the current mission. |
| [onContinueStateChange](arkts-ability-distributedmissionmanager-oncontinuestatechange-f-sys.md#oncontinuestatechange) | Register continuable info listener to ams. |
| [on_continueStateChange](arkts-ability-distributedmissionmanager-oncontinuestatechange-f-sys.md#oncontinuestatechange) | Subscribes to continuation state change events of the current mission. |
| [registerMissionListener](arkts-ability-distributedmissionmanager-registermissionlistener-f-sys.md#registermissionlistener) | Registers a mission status listener. This API uses an asynchronous callback to return the result. |
| [registerMissionListener](arkts-ability-distributedmissionmanager-registermissionlistener-f-sys.md#registermissionlistener-system-api) | Registers a mission status listener. This API uses a promise to return the result. |
| [startSyncRemoteMissions](arkts-ability-distributedmissionmanager-startsyncremotemissions-f-sys.md#startsyncremotemissions) | Starts to synchronize the remote mission list. This API uses an asynchronous callback to return the result. |
| [startSyncRemoteMissions](arkts-ability-distributedmissionmanager-startsyncremotemissions-f-sys.md#startsyncremotemissions-system-api) | Starts to synchronize the remote mission list. This API uses a promise to return the result. |
| [stopSyncRemoteMissions](arkts-ability-distributedmissionmanager-stopsyncremotemissions-f-sys.md#stopsyncremotemissions) | Stops synchronizing the remote mission list. This API uses an asynchronous callback to return the result. |
| [stopSyncRemoteMissions](arkts-ability-distributedmissionmanager-stopsyncremotemissions-f-sys.md#stopsyncremotemissions-system-api) | Stops synchronizing the remote mission list. This API uses a promise to return the result. |
| [unRegisterMissionListener](arkts-ability-distributedmissionmanager-unregistermissionlistener-f-sys.md#unregistermissionlistener) | Unregisters a mission status listener. This API uses an asynchronous callback to return the result. |
| [unRegisterMissionListener](arkts-ability-distributedmissionmanager-unregistermissionlistener-f-sys.md#unregistermissionlistener-system-api) | Unregisters a mission status listener. This API uses a promise to return the result. |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [ContinueCallbackInfo](arkts-ability-distributedmissionmanager-continuecallbackinfo-i-sys.md) | Defines the information about the callback that is triggered for mission continuation state changes. |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [ContinueState](arkts-ability-distributedmissionmanager-continuestate-e-sys.md) | Enumerates the mission continuation states. |
<!--DelEnd-->

<!--Del-->
### Types（系统接口）

| Name | Description |
| --- | --- |
| [ContinuableInfo](arkts-ability-distributedmissionmanager-continuableinfo-t-sys.md) | Continuable information corresponding to ability. |
| [ContinueCallback](arkts-ability-distributedmissionmanager-continuecallback-t-sys.md) | ContinueCallback registered for notify continue result. |
| [ContinueDeviceInfo](arkts-ability-distributedmissionmanager-continuedeviceinfo-t-sys.md) | Parameters corresponding to continue mission. |
| [ContinueMissionInfo](arkts-ability-distributedmissionmanager-continuemissioninfo-t-sys.md) | Parameters corresponding to continue mission. |
| [MissionCallback](arkts-ability-distributedmissionmanager-missioncallback-t-sys.md) | Defines the callback invoked after synchronization starts. It is used as an input parameter in [registerMissionListener](arkts-ability-distributedmissionmanager-registermissionlistener-f-sys.md#registermissionlistener-system-api) . |
| [MissionDeviceInfo](arkts-ability-distributedmissionmanager-missiondeviceinfo-t-sys.md) | Defines the parameters required for registering a listener. It is used as an input parameter in [registerMissionListener](arkts-ability-distributedmissionmanager-registermissionlistener-f-sys.md#registermissionlistener-system-api) . |
| [MissionParameter](arkts-ability-distributedmissionmanager-missionparameter-t-sys.md) | Defines the parameters required for mission synchronization. It is used an input parameter in [startSyncRemoteMissions](arkts-ability-distributedmissionmanager-startsyncremotemissions-f-sys.md#startsyncremotemissions-system-api) . |
<!--DelEnd-->

