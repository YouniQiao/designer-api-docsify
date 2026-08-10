# setAutoUnlockAfterReboot

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## setAutoUnlockAfterReboot

```TypeScript
function setAutoUnlockAfterReboot(admin: Want, isAllowed: boolean): void
```

设置设备重启自动解锁，仅针对无锁屏密码设备生效。适用于企业无人值守设备或需要快速重启恢复服务的场景，避免因手动解锁导致的设备停机时间，提升设备运维效率和业务连续性。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function setAutoUnlockAfterReboot(admin: Want, isAllowed: boolean): void--><!--Device-systemManager-function setAutoUnlockAfterReboot(admin: Want, isAllowed: boolean): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| isAllowed | boolean | Yes | true表示设备重启后自动解锁，false表示设备重启后不自动解锁。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { systemManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
let isAllowed: boolean = true;
try {
  systemManager.setAutoUnlockAfterReboot(wantTemp, isAllowed);
  console.info('Succeeded in setting setAutoUnlockAfterReboot.');
} catch (err) {
  console.error(`Failed to set auto unlock after reboot. Code is ${err.code}, message is ${err.message}`);
}
```

