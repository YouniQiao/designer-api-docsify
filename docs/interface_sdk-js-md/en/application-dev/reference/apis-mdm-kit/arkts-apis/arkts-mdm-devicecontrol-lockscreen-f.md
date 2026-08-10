# lockScreen

## Modules to Import

```TypeScript
import { deviceControl } from 'kits/@kit.MDMKit';
```

## lockScreen

```TypeScript
function lockScreen(admin: Want): void
```

使设备屏幕锁定。设置之后设备立即锁屏。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** 26.0.0

**Substitutes:** [deviceControl.operateDevice](arkts-mdm-devicecontrol-operatedevice-f.md#operatedevice)(admin:

**Required permissions:** ohos.permission.ENTERPRISE_LOCK_DEVICE

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceControl-function lockScreen(admin: Want): void--><!--Device-deviceControl-function lockScreen(admin: Want): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { deviceControl } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  deviceControl.lockScreen(wantTemp);
} catch (err) {
  console.error(`Failed to lock screen. Code is ${err.code}, message is ${err.message}`);
}
```

