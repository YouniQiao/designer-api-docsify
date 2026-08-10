# getInstallLocalEnterpriseAppEnabled

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## getInstallLocalEnterpriseAppEnabled

```TypeScript
function getInstallLocalEnterpriseAppEnabled(admin: Want | null): boolean
```

查询是否支持本地安装企业应用。适用于需要验证设备本地安装企业应用功能是否开启的场景，帮助企业管理员确认策略配置状态，确保设备能够正常安装企业应用。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function getInstallLocalEnterpriseAppEnabled(admin: Want | null): boolean--><!--Device-systemManager-function getInstallLocalEnterpriseAppEnabled(admin: Want | null): boolean-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。&lt;br/&gt;API version 24之前，调用本接口查询系统当 前是否支持本地安装企业应用。当设备存在多个MDM应用时，传入admin查询对应admin设置的策略。从API version 24开始，admin新增支持传入null，传入null时查询整机实际生效的策 略。<br>**Since:** 20 - 23 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否支持本地安装企业应用，true为支持，false为不支持。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { systemManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let isEnable: boolean = systemManager.getInstallLocalEnterpriseAppEnabled(wantTemp);
  console.info('Succeeded in getting installLocalEnterpriseAppEnabled.');
} catch (err) {
  console.error(`Failed to get installLocalEnterpriseAppEnabled. Code is ${err.code}, message is ${err.message}`);
}
```

