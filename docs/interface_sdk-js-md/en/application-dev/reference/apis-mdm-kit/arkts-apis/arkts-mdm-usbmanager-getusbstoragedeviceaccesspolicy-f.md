# getUsbStorageDeviceAccessPolicy

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.MDMKit';
```

## getUsbStorageDeviceAccessPolicy

```TypeScript
function getUsbStorageDeviceAccessPolicy(admin: Want): UsbPolicy
```

获取USB存储设备（baseClass = 0x08）访问策略。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ENTERPRISE_MANAGE_USB or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS
- API version 12 - 24: ohos.permission.ENTERPRISE_MANAGE_USB

**Model restriction:** This API can be used only in the stage model.

<!--Device-usbManager-function getUsbStorageDeviceAccessPolicy(admin: Want): UsbPolicy--><!--Device-usbManager-function getUsbStorageDeviceAccessPolicy(admin: Want): UsbPolicy-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**Return value:**

| Type | Description |
| --- | --- |
| [UsbPolicy](arkts-mdm-usbmanager-usbpolicy-e.md) | USB存储设备访问策略。设置为READ_WRITE表示允许读写USB存储设备；设置为READ_ONLY表示仅允许读取USB存储设备，禁止写入；设置为DISABLED表示完全禁止访问USB存储设备。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |


## getUsbStorageDeviceAccessPolicy

```TypeScript
function getUsbStorageDeviceAccessPolicy(admin: Want | null): UsbPolicy
```

获取USB存储设备（baseClass = 0x08）访问策略。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_USB or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-usbManager-function getUsbStorageDeviceAccessPolicy(admin: Want | null): UsbPolicy--><!--Device-usbManager-function getUsbStorageDeviceAccessPolicy(admin: Want | null): UsbPolicy-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 当设备存在多个MDM应用时，传入Want时查询对应企业设备管理应用设置的策略，传入null时查询实际生效的策略。 |

**Return value:**

| Type | Description |
| --- | --- |
| [UsbPolicy](arkts-mdm-usbmanager-usbpolicy-e.md) | USB存储设备访问策略。设置为READ_WRITE表示允许读写USB存储设备；设置为READ_ONLY表示仅允许读取USB存储设备，禁止写入；设置为DISABLED表示完全禁止访问 USB存储设备。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: usbManager.UsbPolicy = usbManager.getUsbStorageDeviceAccessPolicy(wantTemp);
  console.info(`Succeeded in getting USB storage device access policy. Result: ${JSON.stringify(result)}`);
} catch (err) {
  console.error(`Failed to get USB storage device access policy. Code: ${err.code}, message: ${err.message}`);
}
```

