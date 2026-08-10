# getDisallowedNearLinkProtocols

## Modules to Import

```TypeScript
import { systemManager } from 'kits/@kit.MDMKit';
```

## getDisallowedNearLinkProtocols

```TypeScript
function getDisallowedNearLinkProtocols(admin: Want, accountId: number): Array<NearLinkProtocol>
```

获取指定用户下禁用的星闪协议名单。适用于需要查询用户当前星闪协议访问限制的场景，帮助企业管理员验证策略是否正确下发，或在进行策略调整前获取当前配置。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SYSTEM

**Model restriction:** This API can be used only in the stage model.

<!--Device-systemManager-function getDisallowedNearLinkProtocols(admin: Want, accountId: number): Array<NearLinkProtocol>--><!--Device-systemManager-function getDisallowedNearLinkProtocols(admin: Want, accountId: number): Array<NearLinkProtocol>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| accountId | number | Yes | 用户ID，取值范围：大于等于0。&lt;br/&gt;accountId可以通过 [getOsAccountLocalId](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid)等接口来获取。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;NearLinkProtocol&gt; | 指定用户下禁用的星闪协议名单。 |

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

// Replace with actual values.
let accountId: number = 100;

try {
  let result: systemManager.NearLinkProtocol[] = systemManager.getDisallowedNearLinkProtocols(wantTemp, accountId);
  console.info(`Succeeded in querying the disabled Starlink protocol list for the specified user: ${result}`);
} catch (err) {
  console.error(`Failed to query the disabled Starlink protocol list for the specified user. Code is ${err.code}, message is ${err.message}`);
}
```

