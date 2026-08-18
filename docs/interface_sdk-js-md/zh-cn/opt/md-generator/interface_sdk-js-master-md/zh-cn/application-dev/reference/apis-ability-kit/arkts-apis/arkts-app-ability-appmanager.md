# @ohos.app.ability.appManager

appManager模块提供App管理的能力，包括查询当前是否处于稳定性测试场景、查询是否为ram受限设备、获取应用程序的内存大小、获取有关运行进程的信息等。

**起始版本：** 23

<!--Device-unnamed-declare namespace appManager--><!--Device-unnamed-declare namespace appManager-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## 导入模块

```TypeScript
```

## 汇总

### 函数

| 名称 |
| --- |
| [getAppMemorySize](arkts-ability-appmanager-getappmemorysize-f.md#getappmemorysize) |
| [getAppMemorySize](arkts-ability-appmanager-getappmemorysize-f.md#getappmemorysize) |
| [getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md#getrunningprocessinformation) |
| [getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md#getrunningprocessinformation) |
| [isAppRunning](arkts-ability-appmanager-isapprunning-f.md#isapprunning) |
| [isRamConstrainedDevice](arkts-ability-appmanager-isramconstraineddevice-f.md#isramconstraineddevice) |
| [isRamConstrainedDevice](arkts-ability-appmanager-isramconstraineddevice-f.md#isramconstraineddevice) |
| [isRunningInStabilityTest](arkts-ability-appmanager-isrunninginstabilitytest-f.md#isrunninginstabilitytest) |
| [isRunningInStabilityTest](arkts-ability-appmanager-isrunninginstabilitytest-f.md#isrunninginstabilitytest) |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f.md#killprocessesbybundlename) |
| [offApplicationStateChange](arkts-ability-appmanager-offapplicationstatechange-f.md#offapplicationstatechange) |
| [offApplicationStateChange](arkts-ability-appmanager-offapplicationstatechange-f.md#offapplicationstatechange) |
| [off_applicationState](arkts-ability-appmanager-offapplicationstate-f.md#offapplicationstate) |
| [off_applicationState](arkts-ability-appmanager-offapplicationstate-f.md#offapplicationstate) |
| [onApplicationStateChange](arkts-ability-appmanager-onapplicationstatechange-f.md#onapplicationstatechange) |
| [onApplicationStateChange](arkts-ability-appmanager-onapplicationstatechange-f.md#onapplicationstatechange) |
| [on_applicationState](arkts-ability-appmanager-onapplicationstate-f.md#onapplicationstate) |
| [on_applicationState](arkts-ability-appmanager-onapplicationstate-f.md#onapplicationstate) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [clearUpAppData](arkts-ability-appmanager-clearupappdata-f-sys.md#clearupappdata系统接口) |
| [clearUpApplicationData](arkts-ability-appmanager-clearupapplicationdata-f-sys.md#clearupapplicationdata系统接口) |
| [clearUpApplicationData](arkts-ability-appmanager-clearupapplicationdata-f-sys.md#clearupapplicationdata系统接口) |
| [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-f-sys.md#getforegroundapplications系统接口) |
| [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-f-sys.md#getforegroundapplications系统接口) |
| [getKeepAliveAppServiceExtensions](arkts-ability-appmanager-getkeepaliveappserviceextensions-f-sys.md#getkeepaliveappserviceextensions系统接口) |
| [getKeepAliveBundles](arkts-ability-appmanager-getkeepalivebundles-f-sys.md#getkeepalivebundles系统接口) |
| [getProcessMemoryByPid](arkts-ability-appmanager-getprocessmemorybypid-f-sys.md#getprocessmemorybypid系统接口) |
| [getProcessMemoryByPid](arkts-ability-appmanager-getprocessmemorybypid-f-sys.md#getprocessmemorybypid系统接口) |
| [getRunningMultiAppInfo](arkts-ability-appmanager-getrunningmultiappinfo-f-sys.md#getrunningmultiappinfo系统接口) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getrunningprocessinfobybundlename系统接口) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getrunningprocessinfobybundlename系统接口) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getrunningprocessinfobybundlename系统接口) |
| [getRunningProcessInfoByBundleName](arkts-ability-appmanager-getrunningprocessinfobybundlename-f-sys.md#getrunningprocessinfobybundlename系统接口) |
| [getRunningProcessInformationByBundleType](arkts-ability-appmanager-getrunningprocessinformationbybundletype-f-sys.md#getrunningprocessinformationbybundletype系统接口) |
| [getSupportedProcessCachePids](arkts-ability-appmanager-getsupportedprocesscachepids-f-sys.md#getsupportedprocesscachepids系统接口) |
| [isApplicationRunning](arkts-ability-appmanager-isapplicationrunning-f-sys.md#isapplicationrunning系统接口) |
| [isApplicationRunning](arkts-ability-appmanager-isapplicationrunning-f-sys.md#isapplicationrunning系统接口) |
| [isSharedBundleRunning](arkts-ability-appmanager-issharedbundlerunning-f-sys.md#issharedbundlerunning系统接口) |
| [isSharedBundleRunning](arkts-ability-appmanager-issharedbundlerunning-f-sys.md#issharedbundlerunning系统接口) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md#killprocesswithaccount系统接口) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md#killprocesswithaccount系统接口) |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-f-sys.md#killprocesswithaccount系统接口) |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f-sys.md#killprocessesbybundlename系统接口) |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-f-sys.md#killprocessesbybundlename系统接口) |
| [killProcessesInBatch](arkts-ability-appmanager-killprocessesinbatch-f-sys.md#killprocessesinbatch系统接口) |
| [offAbilityFirstFrameStateChange](arkts-ability-appmanager-offabilityfirstframestatechange-f-sys.md#offabilityfirstframestatechange系统接口) |
| [offAppForegroundStateChange](arkts-ability-appmanager-offappforegroundstatechange-f-sys.md#offappforegroundstatechange系统接口) |
| [off_abilityFirstFrameState](arkts-ability-appmanager-offabilityfirstframestate-f-sys.md#offabilityfirstframestate) |
| [off_appForegroundState](arkts-ability-appmanager-offappforegroundstate-f-sys.md#offappforegroundstate) |
| [onAbilityFirstFrameStateChange](arkts-ability-appmanager-onabilityfirstframestatechange-f-sys.md#onabilityfirstframestatechange系统接口) |
| [onAppForegroundStateChange](arkts-ability-appmanager-onappforegroundstatechange-f-sys.md#onappforegroundstatechange系统接口) |
| [onApplicationStateChange](arkts-ability-appmanager-onapplicationstatechange-f-sys.md#onapplicationstatechange系统接口) |
| [on_abilityFirstFrameState](arkts-ability-appmanager-onabilityfirstframestate-f-sys.md#onabilityfirstframestate) |
| [on_appForegroundState](arkts-ability-appmanager-onappforegroundstate-f-sys.md#onappforegroundstate) |
| [on_applicationState](arkts-ability-appmanager-onapplicationstate-f-sys.md#onapplicationstate) |
| [preloadApplication](arkts-ability-appmanager-preloadapplication-f-sys.md#preloadapplication系统接口) |
| [setKeepAliveForAppServiceExtension](arkts-ability-appmanager-setkeepaliveforappserviceextension-f-sys.md#setkeepaliveforappserviceextension系统接口) |
| [setKeepAliveForBundle](arkts-ability-appmanager-setkeepaliveforbundle-f-sys.md#setkeepaliveforbundle系统接口) |
| [terminateMission](arkts-ability-appmanager-terminatemission-f-sys.md#terminatemission系统接口) |
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
