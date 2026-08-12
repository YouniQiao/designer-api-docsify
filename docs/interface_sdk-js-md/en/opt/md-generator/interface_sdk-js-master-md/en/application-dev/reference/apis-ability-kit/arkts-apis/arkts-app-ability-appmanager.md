# @ohos.app.ability.appManager

The appManager module implements application management. You can use the APIs of this module to query whether the application is undergoing a stability test, whether the application is running on a RAM constrained device, the memory size of the application, and information about the running process.

**Since:** 9

<!--Device-unnamed-declare namespace appManager--><!--Device-unnamed-declare namespace appManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getAppMemorySize](arkts-ability-appmanager-getappmemorysize-f.md#getappmemorysize) |
| [getAppMemorySize](arkts-ability-appmanager-getappmemorysize-f.md#getappmemorysize-1) |
| [getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md#getrunningprocessinformation) |
| [getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md#getrunningprocessinformation-1) |
| [isAppRunning](arkts-ability-appmanager-isapprunning-f.md#isapprunning) |
| [isRamConstrainedDevice](arkts-ability-appmanager-isramconstraineddevice-f.md#isramconstraineddevice) |
| [isRamConstrainedDevice](arkts-ability-appmanager-isramconstraineddevice-f.md#isramconstraineddevice-1) |
| [isRunningInStabilityTest](arkts-ability-appmanager-isrunninginstabilitytest-f.md#isrunninginstabilitytest) |
| [isRunningInStabilityTest](arkts-ability-appmanager-isrunninginstabilitytest-f.md#isrunninginstabilitytest-1) |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f.md#killprocessesbybundlename-1) |
| [off](arkts-ability-appmanager-off-f.md#off) |
| [off](arkts-ability-appmanager-off-f.md#off-1) |
| [on](arkts-ability-appmanager-on-f.md#on) |
| [on](arkts-ability-appmanager-on-f.md#on-1) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [clearUpAppData](arkts-ability-appmanager-clearupappdata-f-sys.md#clearupappdata) |
| [clearUpApplicationData](arkts-ability-appmanager-clearupapplicationdata-f-sys.md#clearupapplicationdata) |
| [clearUpApplicationData](arkts-ability-appmanager-clearupapplicationdata-f-sys.md#clearupapplicationdata-1) |
| [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-f-sys.md#getforegroundapplications) |
| [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-f-sys.md#getforegroundapplications-1) |
| [getKeepAliveAppServiceExtensions](arkts-ability-appmanager-getkeepaliveappserviceextensions-f-sys.md#getkeepaliveappserviceextensions) |
| [getKeepAliveBundles](arkts-ability-appmanager-getkeepalivebundles-f-sys.md#getkeepalivebundles) |
| [getProcessMemoryByPid](arkts-ability-appmanager-getprocessmemorybypid-f-sys.md#getprocessmemorybypid) |
| [getProcessMemoryByPid](arkts-ability-appmanager-getprocessmemorybypid-f-sys.md#getprocessmemorybypid-1) |
| [getProcessRunningInfos](arkts-ability-appmanager-getprocessrunninginfos-f-sys.md#getprocessrunninginfos) |
| [getProcessRunningInfos](arkts-ability-appmanager-getprocessrunninginfos-f-sys.md#getprocessrunninginfos-1) |
| [getRunningMultiAppInfo](arkts-ability-appmanager-getrunningmultiappinfo-f-sys.md#getrunningmultiappinfo) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getrunningprocessinfobybundlename) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getrunningprocessinfobybundlename-1) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getrunningprocessinfobybundlename-2) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getrunningprocessinfobybundlename-3) |
| [getRunningProcessInformationByBundleType](arkts-ability-appmanager-getrunningprocessinformationbybundletype-f-sys.md#getrunningprocessinformationbybundletype) |
| [getSupportedProcessCachePids](arkts-ability-appmanager-getsupportedprocesscachepids-f-sys.md#getsupportedprocesscachepids) |
| [isApplicationRunning](arkts-ability-appmanager-isapplicationrunning-f-sys.md#isapplicationrunning) |
| [isApplicationRunning](arkts-ability-appmanager-isapplicationrunning-f-sys.md#isapplicationrunning-1) |
| [isSharedBundleRunning](arkts-ability-appmanager-issharedbundlerunning-f-sys.md#issharedbundlerunning) |
| [isSharedBundleRunning](arkts-ability-appmanager-issharedbundlerunning-f-sys.md#issharedbundlerunning-1) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md#killprocesswithaccount) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md#killprocesswithaccount-1) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md#killprocesswithaccount-2) |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f-sys.md#killprocessesbybundlename) |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f-sys.md#killprocessesbybundlename-2) |
| [killProcessesInBatch](arkts-ability-appmanager-killprocessesinbatch-f-sys.md#killprocessesinbatch) |
| [off](arkts-ability-appmanager-off-f-sys.md#off-2) |
| [off](arkts-ability-appmanager-off-f-sys.md#off-3) |
| [on](arkts-ability-appmanager-on-f-sys.md#on-2) |
| [on](arkts-ability-appmanager-on-f-sys.md#on-3) |
| [on](arkts-ability-appmanager-on-f-sys.md#on-4) |
| [preloadApplication](arkts-ability-appmanager-preloadapplication-f-sys.md#preloadapplication) |
| [setKeepAliveForAppServiceExtension](arkts-ability-appmanager-setkeepaliveforappserviceextension-f-sys.md#setkeepaliveforappserviceextension) |
| [setKeepAliveForBundle](arkts-ability-appmanager-setkeepaliveforbundle-f-sys.md#setkeepaliveforbundle) |
| [terminateMission](arkts-ability-appmanager-terminatemission-f-sys.md#terminatemission) |
<!--DelEnd-->

<!--Del-->
### Interfaces（系统接口）

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
### Enums（系统接口）

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
| [AppStateData](arkts-ability-appmanager-appstatedata-t.md) |
| [ApplicationStateObserver](arkts-ability-appmanager-applicationstateobserver-t.md) |
| [ProcessData](arkts-ability-appmanager-processdata-t.md) |
| [ProcessInformation](arkts-ability-appmanager-processinformation-t.md) |

<!--Del-->
### Types（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AbilityFirstFrameStateData](arkts-ability-appmanager-abilityfirstframestatedata-t-sys.md) |
| [AbilityFirstFrameStateObserver](arkts-ability-appmanager-abilityfirstframestateobserver-t-sys.md) |
| [AppForegroundStateObserver](arkts-ability-appmanager-appforegroundstateobserver-t-sys.md) |
| [RunningMultiAppInfo](arkts-ability-appmanager-runningmultiappinfo-t-sys.md) |
<!--DelEnd-->
