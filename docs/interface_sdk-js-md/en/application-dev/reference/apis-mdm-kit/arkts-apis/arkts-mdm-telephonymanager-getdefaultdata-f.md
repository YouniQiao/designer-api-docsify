# getDefaultData

## Modules to Import

```TypeScript
import { telephonyManager } from 'kits/@kit.MDMKit';
```

## getDefaultData

```TypeScript
function getDefaultData(admin: Want): number
```

获取设备当前默认使用的数据流量卡卡槽ID。例如，企业设备管理员可在设备管理过程中查询当前配置的默认数据流量卡，以便进行流量管理或切换数据卡配置。未插卡或者飞行模式下会获取上一次使用的数据流量卡卡槽ID、设备从未设置过默认数据流量卡场景下，该接口返回默认卡槽1，值为0。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_TELEPHONY

**Model restriction:** This API can be used only in the stage model.

<!--Device-telephonyManager-function getDefaultData(admin: Want): number--><!--Device-telephonyManager-function getDefaultData(admin: Want): number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**Return value:**

| Type | Description |
| --- | --- |
| number | 卡槽ID，目前仅支持单卡槽设备和双卡槽设备，取值范围为0或1，其中0表示卡槽1，1表示卡槽2。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
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

try {
  // Obtain the slot ID of the SIM card currently used as the default data SIM card.
  let slotId: number = telephonyManager.getDefaultData(wantTemp);
  console.info(`success to get default data SIM ID, current is ${slotId}`);
} catch (err) {
  console.error(`Failed to get default data. Code: ${err.code}, message: ${err.message}`);
}
```

