# @ohos.application.appManager

The appManager module provides APIs for application management. For example, you can query whether the system is undergoing a stability test, determine whether the device is RAM-constrained, obtain the maximum memory available to the current application, and retrieve information about running processes.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [appManager/appManager](arkts-app-ability-appmanager.md#@ohos.app.ability.appManager)

<!--Device-unnamed-declare namespace appManager--><!--Device-unnamed-declare namespace appManager-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getAppMemorySize](arkts-ability-appmanager-getappmemorysize-depr-f.md#getAppMemorySize) | Obtains the maximum memory (RAM allocation) available to the current application. This API uses a promise to return the result. |
| [getAppMemorySize](arkts-ability-appmanager-getappmemorysize-depr-f.md#getAppMemorySize) | Obtains the maximum memory (RAM allocation) available to the current application. This API uses an asynchronous callback to return the result. |
| [getProcessRunningInfos](arkts-ability-appmanager-getprocessrunninginfos-depr-f.md#getProcessRunningInfos) | Obtains information about the running processes. This API uses a promise to return the result. > This API is deprecated since API version 9. You are advised to use > [appManager.getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md#getRunningProcessInformation) > instead. |
| [getProcessRunningInfos](arkts-ability-appmanager-getprocessrunninginfos-depr-f.md#getProcessRunningInfos) | Obtains information about the running processes. This API uses an asynchronous callback to return the result. > This API is deprecated since API version 9. You are advised to use > [appManager.getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md#getRunningProcessInformation) > instead. |
| [isRamConstrainedDevice](arkts-ability-appmanager-isramconstraineddevice-depr-f.md#isRamConstrainedDevice) | Checks whether the current device is a RAM-constrained device (a device with severely limited memory resources). This API uses a promise to return the result. |
| [isRamConstrainedDevice](arkts-ability-appmanager-isramconstraineddevice-depr-f.md#isRamConstrainedDevice) | Checks whether the current device is a RAM-constrained device (a device with severely limited memory resources). This API uses an asynchronous callback to return the result. |
| [isRunningInStabilityTest](arkts-ability-appmanager-isrunninginstabilitytest-depr-f.md#isRunningInStabilityTest) | Checks whether the system is undergoing a stability test. This API uses an asynchronous callback to return the result. > **NOTE：**> > A stability test scenario refers to a specific testing environment designed to verify application reliability > under complex, extreme, or long-term operating conditions. |
| [isRunningInStabilityTest](arkts-ability-appmanager-isrunninginstabilitytest-depr-f.md#isRunningInStabilityTest) | Checks whether the system is undergoing a stability test. This API uses a promise to return the result. > **NOTE：**> > A stability test scenario refers to a specific testing environment designed to verify application reliability > under complex, extreme, or long-term operating conditions. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [clearUpApplicationData](arkts-ability-appmanager-clearupapplicationdata-depr-f-sys.md#clearUpApplicationData) | Clear up application data by bundle name |
| [clearUpApplicationData](arkts-ability-appmanager-clearupapplicationdata-depr-f-sys.md#clearUpApplicationData) | Clear up application data by bundle name |
| [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-depr-f-sys.md#getForegroundApplications) | getForegroundApplications. |
| [getForegroundApplications](arkts-ability-appmanager-getforegroundapplications-depr-f-sys.md#getForegroundApplications) | getForegroundApplications. |
| [getProcessRunningInformation](arkts-ability-appmanager-getprocessrunninginformation-depr-f-sys.md#getProcessRunningInformation) | Obtains information about the running processes. This API uses a promise to return the result. > This API is deprecated since API version 9. You are advised to use > [appManager.getRunningProcessInformation](arkts-ability-appmanager-getrunningprocessinformation-f.md#getRunningProcessInformation) > instead. |
| [getProcessRunningInformation](arkts-ability-appmanager-getprocessrunninginformation-depr-f-sys.md#getProcessRunningInformation) | Obtains information about the running processes. This API uses an asynchronous callback to return the result. > This API is deprecated since API version 9. You are advised to use > [appManager.getRunningProcessInformation]{ > @link @ohos.app.ability.appManager:appManager.getRunningProcessInformation()} instead. |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-depr-f-sys.md#killProcessWithAccount) | Kill process with account. |
| [killProcessWithAccount](arkts-ability-appmanager-killprocesswithaccount-depr-f-sys.md#killProcessWithAccount) | Kill process with account. |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-depr-f-sys.md#killProcessesByBundleName) | Kill processes by bundle name |
| [killProcessesByBundleName](arkts-ability-appmanager-killprocessesbybundlename-depr-f-sys.md#killProcessesByBundleName) | Kill processes by bundle name |
| [registerApplicationStateObserver](arkts-ability-appmanager-registerapplicationstateobserver-depr-f-sys.md#registerApplicationStateObserver) | Register application state observer. |
| [unregisterApplicationStateObserver](arkts-ability-appmanager-unregisterapplicationstateobserver-depr-f-sys.md#unregisterApplicationStateObserver) | Unregister application state observer. |
| [unregisterApplicationStateObserver](arkts-ability-appmanager-unregisterapplicationstateobserver-depr-f-sys.md#unregisterApplicationStateObserver) | Unregister application state observer. |
<!--DelEnd-->

