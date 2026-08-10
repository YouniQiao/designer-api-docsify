# deactiveSim

## Modules to Import

```TypeScript
import { telephonyManager } from 'kits/@kit.MDMKit';
```

## deactiveSim

```TypeScript
function deactiveSim(admin: Want, slotId: number): void
```

停用指定卡槽SIM卡。停用该SIM卡，无法使用该卡槽的SIM卡接打电话，收发短信，上网。例如，企业可在员工休假或设备维护期间，临时停用SIM卡。该接口需要插入SIM卡并关闭飞行模式才能成功调用。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**Model restriction:** This API can be used only in the stage model.

<!--Device-telephonyManager-function deactiveSim(admin: Want, slotId: number): void--><!--Device-telephonyManager-function deactiveSim(admin: Want, slotId: number): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| slotId | number | Yes | 卡槽ID，目前仅支持单卡槽设备和双卡槽设备，取值范围为0或1，其中0表示卡槽1，1表示卡槽2。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9200012 | Parameter verification failed. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 9201017 | SIM card activation or deactivation failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 203 | This function is prohibited by enterprise management policies. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { telephonyManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace the values as required.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
// Set the ID of the slot to be deactivated.
let slotId: number = 0;
try {
  // Deactivate the SIM card in the specified slot.
  telephonyManager.deactiveSim(wantTemp, slotId);
  console.info(`success to deactive SIM`);
} catch (err) {
  console.error(`Failed to deactive SIM. Code: ${err.code}, message: ${err.message}`);
}
```

