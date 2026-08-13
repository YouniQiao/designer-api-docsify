# @ohos.app.ability.appManager

appManager模块提供App管理的能力，包括查询当前是否处于稳定性测试场景、查询是否为ram受限设备、获取应用程序的内存大小、获取有关运行进程的信息等。

**起始版本：** 23

**废弃版本：** -1

<!--Device-unnamed-declare namespace appManager--><!--Device-unnamed-declare namespace appManager-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 汇总

### 函数

| 名称 |
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
### 函数（系统接口）

| 名称 |
| --- |
| [clearUpAppData](arkts-ability-appmanager-clearupappdata-f-sys.md#clearUpAppData（系统接口）) |
| [clearUpApplicationData](arkts-ability-appmanager-clearupapplicationdata-f-sys.md#clearUpApplicationData（系统接口）) |
| [clearUpApplicationData](arkts-ability-appmanager-clearupapplicationdata-f-sys.md#clearUpApplicationData（系统接口）) |
| [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-f-sys.md#getForegroundApplications（系统接口）) |
| [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-f-sys.md#getForegroundApplications（系统接口）) |
| [getKeepAliveAppServiceExtensions](arkts-ability-appmanager-getkeepaliveappserviceextensions-f-sys.md#getKeepAliveAppServiceExtensions（系统接口）) |
| [getKeepAliveBundles](arkts-ability-appmanager-getkeepalivebundles-f-sys.md#getKeepAliveBundles（系统接口）) |
| [getProcessMemoryByPid](arkts-ability-appmanager-getprocessmemorybypid-f-sys.md#getProcessMemoryByPid（系统接口）) |
| [getProcessMemoryByPid](arkts-ability-appmanager-getprocessmemorybypid-f-sys.md#getProcessMemoryByPid（系统接口）) |
| [getRunningMultiAppInfo](arkts-ability-appmanager-getrunningmultiappinfo-f-sys.md#getRunningMultiAppInfo（系统接口）) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getRunningProcessInfoByBundleName（系统接口）) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getRunningProcessInfoByBundleName（系统接口）) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getRunningProcessInfoByBundleName（系统接口）) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getRunningProcessInfoByBundleName（系统接口）) |
| [getRunningProcessInformationByBundleType](arkts-ability-appmanager-getrunningprocessinformationbybundletype-f-sys.md#getRunningProcessInformationByBundleType（系统接口）) |
| [getSupportedProcessCachePids](arkts-ability-appmanager-getsupportedprocesscachepids-f-sys.md#getSupportedProcessCachePids（系统接口）) |
| [isApplicationRunning](arkts-ability-appmanager-isapplicationrunning-f-sys.md#isApplicationRunning（系统接口）) |
| [isApplicationRunning](arkts-ability-appmanager-isapplicationrunning-f-sys.md#isApplicationRunning（系统接口）) |
| [isSharedBundleRunning](arkts-ability-appmanager-issharedbundlerunning-f-sys.md#isSharedBundleRunning（系统接口）) |
| [isSharedBundleRunning](arkts-ability-appmanager-issharedbundlerunning-f-sys.md#isSharedBundleRunning（系统接口）) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md#killProcessWithAccount（系统接口）) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md#killProcessWithAccount（系统接口）) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md#killProcessWithAccount（系统接口）) |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f-sys.md#killProcessesByBundleName（系统接口）) |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f-sys.md#killProcessesByBundleName（系统接口）) |
| [killProcessesInBatch](arkts-ability-appmanager-killprocessesinbatch-f-sys.md#killProcessesInBatch（系统接口）) |
| [offAbilityFirstFrameStateChange](arkts-ability-appmanager-offabilityfirstframestatechange-f-sys.md#offAbilityFirstFrameStateChange（系统接口）) |
| [offAppForegroundStateChange](arkts-ability-appmanager-offappforegroundstatechange-f-sys.md#offAppForegroundStateChange（系统接口）) |
| [off_abilityFirstFrameState](arkts-ability-appmanager-offabilityfirstframestate-f-sys.md#off_abilityFirstFrameState) |
| [off_appForegroundState](arkts-ability-appmanager-offappforegroundstate-f-sys.md#off_appForegroundState) |
| [onAbilityFirstFrameStateChange](arkts-ability-appmanager-onabilityfirstframestatechange-f-sys.md#onAbilityFirstFrameStateChange（系统接口）) |
| [onAppForegroundStateChange](arkts-ability-appmanager-onappforegroundstatechange-f-sys.md#onAppForegroundStateChange（系统接口）) |
| [onApplicationStateChange](arkts-ability-appmanager-onapplicationstatechange-f-sys.md#onApplicationStateChange（系统接口）) |
| [on_abilityFirstFrameState](arkts-ability-appmanager-onabilityfirstframestate-f-sys.md#on_abilityFirstFrameState) |
| [on_appForegroundState](arkts-ability-appmanager-onappforegroundstate-f-sys.md#on_appForegroundState) |
| [on_applicationState](arkts-ability-appmanager-onapplicationstate-f-sys.md#on_applicationState) |
| [preloadApplication](arkts-ability-appmanager-preloadapplication-f-sys.md#preloadApplication（系统接口）) |
| [setKeepAliveForAppServiceExtension](arkts-ability-appmanager-setkeepaliveforappserviceextension-f-sys.md#setKeepAliveForAppServiceExtension（系统接口）) |
| [setKeepAliveForBundle](arkts-ability-appmanager-setkeepaliveforbundle-f-sys.md#setKeepAliveForBundle（系统接口）) |
| [terminateMission](arkts-ability-appmanager-terminatemission-f-sys.md#terminateMission（系统接口）) |
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
| [AppStateData](arkts-ability-appmanager-appstatedata-t.md) |
| [ApplicationStateObserver](arkts-ability-appmanager-applicationstateobserver-t.md) |
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
