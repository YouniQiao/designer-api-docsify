# setDisallowedPolicy

## 导入模块

```TypeScript
import { restrictions } from 'kits/@kit.MDMKit';
```

## setDisallowedPolicy

```TypeScript
function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void
```

设置禁用/启用某特性。

> **说明：**
> 
> 本接口为设备级禁用策略，影响设备所有用户。如需针对特定用户设置禁用策略，请使用
> [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount)接口。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为12。

**废弃版本：** 26.0.0

**替代接口：** [restrictions.setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy)(admin:

**需要权限：** 
- API版本20+：ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS or ohos.permission.ENTERPRISE_MANAGE_NETWORK
- API版本15 - 19：ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS
- API版本12 - 14：ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-restrictions-function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void--><!--Device-restrictions-function setDisallowedPolicy(admin: Want, feature: string, disallow: boolean): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| feature | string | 是 | 支持设置的特性清单参考表1。&lt;br/&gt; **说明：** 从API version 15开始，应用申请权限 ohos.permission.PERSONAL_MANAGE_RESTRICTIONS并通过 [startAdminProvision](arkts-mdm-adminmanager-startadminprovision-f.md#startadminprovision)激活为 [BDA](../../../mdm/mdm-kit-term.md#byod-device-admin-bdabyod设备管理员)，可以使用此接口设置以下特性：bluetooth、hdc、microphone、usb、 wifi、tethering、camera，从API版本26.0.0开始，新增支持使用此接口设置mtpServer特性。 |
| disallow | boolean | 是 | true表示禁止使用，false表示允许使用。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 9200013 | The enterprise management policy has been successfully set, but the function has not taken effect in real time.<br>**适用版本：** 21+ |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## 示例

```TypeScript
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 参数需根据实际情况进行替换
  restrictions.setDisallowedPolicy(wantTemp, 'printer', true);
  console.info('Succeeded in setting printer disabled');
} catch (err) {
  console.error(`Failed to set printer disabled. Code is ${err.code}, message is ${err.message}`);
}
```


## setDisallowedPolicy

```TypeScript
function setDisallowedPolicy(admin: Want, feature: FeatureForDevice, disallow: boolean): void
```

设置禁用/启用指定设备特性，禁用后相关设备特性无法被使用。

**起始版本：** 24

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为24。

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-restrictions-function setDisallowedPolicy(admin: Want, feature: FeatureForDevice, disallow: boolean): void--><!--Device-restrictions-function setDisallowedPolicy(admin: Want, feature: FeatureForDevice, disallow: boolean): void-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| feature | [FeatureForDevice](arkts-mdm-restrictions-featurefordevice-e.md) | 是 | 指定要禁用或允许的设备特性。&lt;br/&gt; **说明：** 应用申请权限 ohos.permission.PERSONAL_MANAGE_RESTRICTIONS并通过 [startAdminProvision](arkts-mdm-adminmanager-startadminprovision-f.md#startadminprovision)激活为 [BDA](../../../mdm/mdm-kit-term.md#byod-device-admin-bdabyod设备管理员)，可以使用此接口设置以下特性： [FeatureForDevice.WIFI_P2P](arkts-mdm-restrictions-featurefordevice-e.md)。 |
| disallow | boolean | 是 | true表示禁止使用，false表示允许使用。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 9200013 | The enterprise management policy has been successfully set, but the function has not taken effect in real time. |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 9200010 | A conflict policy has been configured. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## 示例

```TypeScript
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  restrictions.setDisallowedPolicy(wantTemp, restrictions.FeatureForDevice.WIFI_P2P, true);
  console.info('Succeeded in setting Wi-Fi P2P disabled');
} catch (err) {
  console.error(`Failed to set Wi-Fi P2P disabled. Code is ${err.code}, message is ${err.message}`);
}
```

