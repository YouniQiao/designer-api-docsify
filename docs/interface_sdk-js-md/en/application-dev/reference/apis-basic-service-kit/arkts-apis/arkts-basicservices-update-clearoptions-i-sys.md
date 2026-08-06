# ClearOptions (System API)

Defines the clearing options, which specify the errors to be cleared.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-update-export interface ClearOptions--><!--Device-update-export interface ClearOptions-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## status

```TypeScript
status: UpgradeStatus
```

Exception status, which is used to specify the status to be cleared. This parameter can be set to  
**UPGRADE\_FAIL** only when the **upgrade** method fails to be executed and its status is **UPGRADE\_FAIL**.

Use scenarios: If the upgrade fails (with the status of **UPGRADE\_FAIL**), the system retains the error state to prevent the upgrade from being performed again. In this case, you need to call **status** passed by  
**clearError** so that errors can be cleared, and the system can be restored to the initial state to restart the upgrade process.

A common value is **UPGRADE\_FAIL**, including upgrade failure. Note: Only the **UPGRADE\_FAIL** status can be cleared.

**Type:** UpgradeStatus

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-ClearOptions-status: UpgradeStatus--><!--Device-ClearOptions-status: UpgradeStatus-End-->

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

