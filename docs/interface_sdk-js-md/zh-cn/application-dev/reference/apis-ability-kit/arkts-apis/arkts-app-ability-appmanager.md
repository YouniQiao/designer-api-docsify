# @ohos.app.ability.appManager

appManager模块提供App管理的能力，包括查询当前是否处于稳定性测试场景、查询是否为ram受限设备、获取应用程序的内存大小、获取有关运行进程的信息等。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
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
### 接口（系统接口）

| 名称 |
| --- |
| [AppStateFilter](arkts-ability-appmanager-appstatefilter-i-sys.md) |
| [KeepAliveBundleInfo](arkts-ability-appmanager-keepalivebundleinfo-i-sys.md) |
<!--DelEnd-->

### 枚举

| 名称 |
| --- |
| [ProcessState](arkts-ability-appmanager-processstate-e.md) |

<!--Del-->
### 枚举（系统接口）

| 名称 |
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

### 类型

| 名称 |
| --- |
| [AbilityStateData](arkts-ability-appmanager-abilitystatedata-t.md) |
| [ApplicationStateObserver](arkts-ability-appmanager-applicationstateobserver-t.md) |
| [AppStateData](arkts-ability-appmanager-appstatedata-t.md) |
| [ProcessData](arkts-ability-appmanager-processdata-t.md) |
| [ProcessInformation](arkts-ability-appmanager-processinformation-t.md) |

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [AbilityFirstFrameStateData](arkts-ability-appmanager-abilityfirstframestatedata-t-sys.md) |
| [AbilityFirstFrameStateObserver](arkts-ability-appmanager-abilityfirstframestateobserver-t-sys.md) |
| [AppForegroundStateObserver](arkts-ability-appmanager-appforegroundstateobserver-t-sys.md) |
| [RunningMultiAppInfo](arkts-ability-appmanager-runningmultiappinfo-t-sys.md) |
<!--DelEnd-->
