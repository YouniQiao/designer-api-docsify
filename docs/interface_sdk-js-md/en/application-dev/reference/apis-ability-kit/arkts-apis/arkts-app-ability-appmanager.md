# @ohos.app.ability.appManager

The appManager module implements application management. You can use the APIs of this module to query whether the application is undergoing a stability test, whether the application is running on a RAM constrained device, the memory size of the application, and information about the running process.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAppMemorySize](arkts-ability-appmanager-getappmemorysize-f.md) |
| [getAppMemorySize](arkts-ability-appmanager-getappmemorysize-f.md) |
| [getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md) |
| [getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md) |
| [isAppRunning](arkts-ability-appmanager-isapprunning-f.md) |
| [isRamConstrainedDevice](arkts-ability-appmanager-isramconstraineddevice-f.md) |
| [isRamConstrainedDevice](arkts-ability-appmanager-isramconstraineddevice-f.md) |
| [isRunningInStabilityTest](arkts-ability-appmanager-isrunninginstabilitytest-f.md) |
| [isRunningInStabilityTest](arkts-ability-appmanager-isrunninginstabilitytest-f.md) |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f.md) |
| [off](arkts-ability-appmanager-off-f.md#offapplicationstate) |
| [off](arkts-ability-appmanager-off-f.md#offapplicationstate) |
| [offApplicationStateChange](arkts-ability-appmanager-offapplicationstatechange-f.md) |
| [offApplicationStateChange](arkts-ability-appmanager-offapplicationstatechange-f.md) |
| [on](arkts-ability-appmanager-on-f.md#onapplicationstate) |
| [on](arkts-ability-appmanager-on-f.md#onapplicationstate) |
| [onApplicationStateChange](arkts-ability-appmanager-onapplicationstatechange-f.md) |
| [onApplicationStateChange](arkts-ability-appmanager-onapplicationstatechange-f.md) |

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [clearUpAppData](arkts-ability-appmanager-clearupappdata-f-sys.md) |
| [clearUpApplicationData](arkts-ability-appmanager-clearupapplicationdata-f-sys.md) |
| [clearUpApplicationData](arkts-ability-appmanager-clearupapplicationdata-f-sys.md) |
| [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-f-sys.md) |
| [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-f-sys.md) |
| [getKeepAliveAppServiceExtensions](arkts-ability-appmanager-getkeepaliveappserviceextensions-f-sys.md) |
| [getKeepAliveBundles](arkts-ability-appmanager-getkeepalivebundles-f-sys.md) |
| [getProcessMemoryByPid](arkts-ability-appmanager-getprocessmemorybypid-f-sys.md) |
| [getProcessMemoryByPid](arkts-ability-appmanager-getprocessmemorybypid-f-sys.md) |
| [getProcessRunningInfos](arkts-ability-appmanager-getprocessrunninginfos-f-sys.md) |
| [getProcessRunningInfos](arkts-ability-appmanager-getprocessrunninginfos-f-sys.md) |
| [getRunningMultiAppInfo](arkts-ability-appmanager-getrunningmultiappinfo-f-sys.md) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md) |
| [getRunningProcessInformationByBundleType](arkts-ability-appmanager-getrunningprocessinformationbybundletype-f-sys.md) |
| [getSupportedProcessCachePids](arkts-ability-appmanager-getsupportedprocesscachepids-f-sys.md) |
| [isApplicationRunning](arkts-ability-appmanager-isapplicationrunning-f-sys.md) |
| [isApplicationRunning](arkts-ability-appmanager-isapplicationrunning-f-sys.md) |
| [isSharedBundleRunning](arkts-ability-appmanager-issharedbundlerunning-f-sys.md) |
| [isSharedBundleRunning](arkts-ability-appmanager-issharedbundlerunning-f-sys.md) |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f-sys.md) |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f-sys.md) |
| [killProcessesInBatch](arkts-ability-appmanager-killprocessesinbatch-f-sys.md) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md) |
| [off](arkts-ability-appmanager-off-f-sys.md#offappforegroundstate) |
| [off](arkts-ability-appmanager-off-f-sys.md#offabilityfirstframestate) |
| [offAbilityFirstFrameStateChange](arkts-ability-appmanager-offabilityfirstframestatechange-f-sys.md) |
| [offAppForegroundStateChange](arkts-ability-appmanager-offappforegroundstatechange-f-sys.md) |
| [on](arkts-ability-appmanager-on-f-sys.md#onapplicationstate) |
| [on](arkts-ability-appmanager-on-f-sys.md#onappforegroundstate) |
| [on](arkts-ability-appmanager-on-f-sys.md#onabilityfirstframestate) |
| [onAbilityFirstFrameStateChange](arkts-ability-appmanager-onabilityfirstframestatechange-f-sys.md) |
| [onAppForegroundStateChange](arkts-ability-appmanager-onappforegroundstatechange-f-sys.md) |
| [onApplicationStateChange](arkts-ability-appmanager-onapplicationstatechange-f-sys.md) |
| [preloadApplication](arkts-ability-appmanager-preloadapplication-f-sys.md) |
| [setKeepAliveForAppServiceExtension](arkts-ability-appmanager-setkeepaliveforappserviceextension-f-sys.md) |
| [setKeepAliveForBundle](arkts-ability-appmanager-setkeepaliveforbundle-f-sys.md) |
| [terminateMission](arkts-ability-appmanager-terminatemission-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AppStateFilter](arkts-ability-appmanager-appstatefilter-i-sys.md) |
| [KeepAliveBundleInfo](arkts-ability-appmanager-keepalivebundleinfo-i-sys.md) |
<!--DelEnd-->

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ProcessState](arkts-ability-appmanager-processstate-e.md) |

<!--Del-->
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ApplicationState](arkts-ability-appmanager-applicationstate-e-sys.md) |
| [FilterAbilityStateType](arkts-ability-appmanager-filterabilitystatetype-e-sys.md) |
| [FilterAppStateType](arkts-ability-appmanager-filterappstatetype-e-sys.md) |
| [FilterBundleType](arkts-ability-appmanager-filterbundletype-e-sys.md) |
| [FilterCallback](arkts-ability-appmanager-filtercallback-e-sys.md) |
| [FilterProcessStateType](arkts-ability-appmanager-filterprocessstatetype-e-sys.md) |
| [KeepAliveAppType](arkts-ability-appmanager-keepaliveapptype-e-sys.md) |
| [KeepAliveSetter](arkts-ability-appmanager-keepalivesetter-e-sys.md) |
| [PreloadMode](arkts-ability-appmanager-preloadmode-e-sys.md) |
<!--DelEnd-->

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AbilityStateData](arkts-ability-appmanager-abilitystatedata-t.md) |
| [ApplicationStateObserver](arkts-ability-appmanager-applicationstateobserver-t.md) |
| [AppStateData](arkts-ability-appmanager-appstatedata-t.md) |
| [ProcessData](arkts-ability-appmanager-processdata-t.md) |
| [ProcessInformation](arkts-ability-appmanager-processinformation-t.md) |

<!--Del-->
### Types(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AbilityFirstFrameStateData](arkts-ability-appmanager-abilityfirstframestatedata-t-sys.md) |
| [AbilityFirstFrameStateObserver](arkts-ability-appmanager-abilityfirstframestateobserver-t-sys.md) |
| [AppForegroundStateObserver](arkts-ability-appmanager-appforegroundstateobserver-t-sys.md) |
| [RunningMultiAppInfo](arkts-ability-appmanager-runningmultiappinfo-t-sys.md) |
<!--DelEnd-->
