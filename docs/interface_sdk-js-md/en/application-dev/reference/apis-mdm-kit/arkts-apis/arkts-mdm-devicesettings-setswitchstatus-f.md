# setSwitchStatus

## Modules to Import

```TypeScript
import { deviceSettings } from 'kits/@kit.MDMKit';
```

## setSwitchStatus

```TypeScript
function setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void
```

设置开关的状态。支持设置星闪、蓝牙、Wi-Fi、NFC的状态为开启或关闭，设置完毕后，用户可以手动开关。支持设置蓝牙、NFC的状态为强制开启，设置完毕后，用户不可以手动开关。若已经通过  
[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy) 接口禁用了某个开关，则通过本接口设置这个开关的状态会抛出错误码203，需通过[setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy) 接口解除该开关禁用策略。当设备有多个MDM应用时，各MDM应用设置开关状态不存在冲突，最后设置的策略生效。开启(用户可手动开启、关闭)、关闭(用户可手动开启、关闭)、强制开启(用户不可手动关闭)三个状态可以随意切换，也不存在冲突。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void--><!--Device-deviceSettings-function setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| key | [SwitchKey](arkts-mdm-devicesettings-switchkey-e.md) | Yes | 开关的名称，应用申请权限 ohos.permission.PERSONAL_MANAGE_RESTRICTIONS 并通过接口 [startAdminProvision](arkts-mdm-adminmanager-startadminprovision-f.md#startadminprovision)激活为自带设备管理应用，可以使用此接口设 置以下开关：星闪、蓝牙、Wi-Fi。设置NFC开关时会报错误码9200002。 |
| status | [SwitchStatus](arkts-mdm-devicesettings-switchstatus-e.md) | Yes | 开关的状态，应用申请权限 ohos.permission.PERSONAL_MANAGE_RESTRICTIONS 并通过接口 [startAdminProvision](arkts-mdm-adminmanager-startadminprovision-f.md#startadminprovision)激活为自带设备管理应用，可以使用此接口设 置以下状态：ON、OFF。设置为FORCE_ON状态时会报错误码9200002。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9200012 | Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 203 | This function is prohibited by enterprise management policies. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |
| 9201042 | Failed to toggle the switch state. |

## Examples

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace with actual values.
  let key: deviceSettings.SwitchKey = deviceSettings.SwitchKey.BLUETOOTH;
  let status: deviceSettings.SwitchStatus  = deviceSettings.SwitchStatus.ON;
  deviceSettings.setSwitchStatus(wantTemp, key, status);
  console.info(`Succeeded in setting switch status.`);
} catch (err) {
  console.error(`Failed to set switch status. Code: ${err.code}, message: ${err.message}`);
}
```

