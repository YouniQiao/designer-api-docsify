# setNetworkInterfaceDisabledSync

## Modules to Import

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## setNetworkInterfaceDisabledSync

```TypeScript
function setNetworkInterfaceDisabledSync(admin: Want, networkInterface: string, isDisabled: boolean): void
```

禁止设备使用指定网络接口。适用于企业网络安全管控场景，例如禁用高风险网络接口、限制设备使用特定网络连接、防止通过网络接口进行数据泄露，帮助企业降低网络安全风险，防止通过特定网络接口进行的攻击或数据外泄。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_NETWORK

**Model restriction:** This API can be used only in the stage model.

<!--Device-networkManager-function setNetworkInterfaceDisabledSync(admin: Want, networkInterface: string, isDisabled: boolean): void--><!--Device-networkManager-function setNetworkInterfaceDisabledSync(admin: Want, networkInterface: string, isDisabled: boolean): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| networkInterface | string | Yes | 指定网络接口。 |
| isDisabled | boolean | Yes | true表示禁用该网络接口，false表示开启该网络接口。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { networkManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  networkManager.setNetworkInterfaceDisabledSync(wantTemp, 'eth0', true);
  console.info(`Succeeded in setting network interface disabled`);
} catch (err) {
  console.error(`Failed to set network interface disabled. Code: ${err.code}, message: ${err.message}`);
}
```

