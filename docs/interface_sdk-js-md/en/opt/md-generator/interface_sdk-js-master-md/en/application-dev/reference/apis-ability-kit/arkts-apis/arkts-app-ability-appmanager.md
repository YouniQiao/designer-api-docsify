# @ohos.app.ability.appManager

The appManager module implements application management. You can use the APIs of this module to query whether the application is undergoing a stability test, whether the application is running on a RAM constrained device, the memory size of the application, and information about the running process.

**Since:** 23

**Deprecated since:** -1

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
| [getAppMemorySize](arkts-ability-appmanager-getappmemorysize-f.md#getAppMemorySize) |
| [getAppMemorySize](arkts-ability-appmanager-getappmemorysize-f.md#getAppMemorySize) |
| [getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md#getRunningProcessInformation) |
| [getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md#getRunningProcessInformation) |
| [isAppRunning](arkts-ability-appmanager-isapprunning-f.md#isAppRunning) |
| [isRamConstrainedDevice](arkts-ability-appmanager-isramconstraineddevice-f.md#isRamConstrainedDevice) |
| [isRamConstrainedDevice](arkts-ability-appmanager-isramconstraineddevice-f.md#isRamConstrainedDevice) |
| [isRunningInStabilityTest](arkts-ability-appmanager-isrunninginstabilitytest-f.md#isRunningInStabilityTest) |
| [isRunningInStabilityTest](arkts-ability-appmanager-isrunninginstabilitytest-f.md#isRunningInStabilityTest) |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f.md#killProcessesByBundleName) |
| [offApplicationStateChange](arkts-ability-appmanager-offapplicationstatechange-f.md#offApplicationStateChange) |
| [offApplicationStateChange](arkts-ability-appmanager-offapplicationstatechange-f.md#offApplicationStateChange) |
| [off_applicationState](arkts-ability-appmanager-offapplicationstate-f.md#off_applicationState) |
| [off_applicationState](arkts-ability-appmanager-offapplicationstate-f.md#off_applicationState) |
| [onApplicationStateChange](arkts-ability-appmanager-onapplicationstatechange-f.md#onApplicationStateChange) |
| [onApplicationStateChange](arkts-ability-appmanager-onapplicationstatechange-f.md#onApplicationStateChange) |
| [on_applicationState](arkts-ability-appmanager-onapplicationstate-f.md#on_applicationState) |
| [on_applicationState](arkts-ability-appmanager-onapplicationstate-f.md#on_applicationState) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [clearUpAppData](arkts-ability-appmanager-clearupappdata-f-sys.md#clearUpAppData-(System-API)) |
| [clearUpApplicationData](arkts-ability-appmanager-clearupapplicationdata-f-sys.md#clearUpApplicationData-(System-API)) |
| [clearUpApplicationData](arkts-ability-appmanager-clearupapplicationdata-f-sys.md#clearUpApplicationData-(System-API)) |
| [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-f-sys.md#getForegroundApplications-(System-API)) |
| [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-f-sys.md#getForegroundApplications-(System-API)) |
| [getKeepAliveAppServiceExtensions](arkts-ability-appmanager-getkeepaliveappserviceextensions-f-sys.md#getKeepAliveAppServiceExtensions-(System-API)) |
| [getKeepAliveBundles](arkts-ability-appmanager-getkeepalivebundles-f-sys.md#getKeepAliveBundles-(System-API)) |
| [getProcessMemoryByPid](arkts-ability-appmanager-getprocessmemorybypid-f-sys.md#getProcessMemoryByPid-(System-API)) |
| [getProcessMemoryByPid](arkts-ability-appmanager-getprocessmemorybypid-f-sys.md#getProcessMemoryByPid-(System-API)) |
| [getProcessRunningInfos](arkts-ability-appmanager-getprocessrunninginfos-f-sys.md#getProcessRunningInfos-(System-API)) |
| [getProcessRunningInfos](arkts-ability-appmanager-getprocessrunninginfos-f-sys.md#getProcessRunningInfos-(System-API)) |
| [getRunningMultiAppInfo](arkts-ability-appmanager-getrunningmultiappinfo-f-sys.md#getRunningMultiAppInfo-(System-API)) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getRunningProcessInfoByBundleName-(System-API)) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getRunningProcessInfoByBundleName-(System-API)) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getRunningProcessInfoByBundleName-(System-API)) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getRunningProcessInfoByBundleName-(System-API)) |
| [getRunningProcessInformationByBundleType](arkts-ability-appmanager-getrunningprocessinformationbybundletype-f-sys.md#getRunningProcessInformationByBundleType-(System-API)) |
| [getSupportedProcessCachePids](arkts-ability-appmanager-getsupportedprocesscachepids-f-sys.md#getSupportedProcessCachePids-(System-API)) |
| [isApplicationRunning](arkts-ability-appmanager-isapplicationrunning-f-sys.md#isApplicationRunning-(System-API)) |
| [isApplicationRunning](arkts-ability-appmanager-isapplicationrunning-f-sys.md#isApplicationRunning-(System-API)) |
| [isSharedBundleRunning](arkts-ability-appmanager-issharedbundlerunning-f-sys.md#isSharedBundleRunning-(System-API)) |
| [isSharedBundleRunning](arkts-ability-appmanager-issharedbundlerunning-f-sys.md#isSharedBundleRunning-(System-API)) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md#killProcessWithAccount-(System-API)) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md#killProcessWithAccount-(System-API)) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md#killProcessWithAccount-(System-API)) |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f-sys.md#killProcessesByBundleName-(System-API)) |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f-sys.md#killProcessesByBundleName-(System-API)) |
| [killProcessesInBatch](arkts-ability-appmanager-killprocessesinbatch-f-sys.md#killProcessesInBatch-(System-API)) |
| [offAbilityFirstFrameStateChange](arkts-ability-appmanager-offabilityfirstframestatechange-f-sys.md#offAbilityFirstFrameStateChange-(System-API)) |
| [offAppForegroundStateChange](arkts-ability-appmanager-offappforegroundstatechange-f-sys.md#offAppForegroundStateChange-(System-API)) |
| [off_abilityFirstFrameState](arkts-ability-appmanager-offabilityfirstframestate-f-sys.md#off_abilityFirstFrameState) |
| [off_appForegroundState](arkts-ability-appmanager-offappforegroundstate-f-sys.md#off_appForegroundState) |
| [onAbilityFirstFrameStateChange](arkts-ability-appmanager-onabilityfirstframestatechange-f-sys.md#onAbilityFirstFrameStateChange-(System-API)) |
| [onAppForegroundStateChange](arkts-ability-appmanager-onappforegroundstatechange-f-sys.md#onAppForegroundStateChange-(System-API)) |
| [onApplicationStateChange](arkts-ability-appmanager-onapplicationstatechange-f-sys.md#onApplicationStateChange-(System-API)) |
| [on_abilityFirstFrameState](arkts-ability-appmanager-onabilityfirstframestate-f-sys.md#on_abilityFirstFrameState) |
| [on_appForegroundState](arkts-ability-appmanager-onappforegroundstate-f-sys.md#on_appForegroundState) |
| [on_applicationState](arkts-ability-appmanager-onapplicationstate-f-sys.md#on_applicationState) |
| [preloadApplication](arkts-ability-appmanager-preloadapplication-f-sys.md#preloadApplication-(System-API)) |
| [setKeepAliveForAppServiceExtension](arkts-ability-appmanager-setkeepaliveforappserviceextension-f-sys.md#setKeepAliveForAppServiceExtension-(System-API)) |
| [setKeepAliveForBundle](arkts-ability-appmanager-setkeepaliveforbundle-f-sys.md#setKeepAliveForBundle-(System-API)) |
| [terminateMission](arkts-ability-appmanager-terminatemission-f-sys.md#terminateMission-(System-API)) |
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
