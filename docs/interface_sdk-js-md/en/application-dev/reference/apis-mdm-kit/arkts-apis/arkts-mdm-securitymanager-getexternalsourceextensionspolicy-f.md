# getExternalSourceExtensionsPolicy

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## getExternalSourceExtensionsPolicy

```TypeScript
function getExternalSourceExtensionsPolicy(admin: Want): common.ManagedPolicy
```

获取外部来源扩展程序的管控策略。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function getExternalSourceExtensionsPolicy(admin: Want): common.ManagedPolicy--><!--Device-securityManager-function getExternalSourceExtensionsPolicy(admin: Want): common.ManagedPolicy-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**Return value:**

| Type | Description |
| --- | --- |
| common.ManagedPolicy | 返回ManagedPolicy枚举类型的管控策略。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |


## getExternalSourceExtensionsPolicy

```TypeScript
function getExternalSourceExtensionsPolicy(admin: Want | null): common.ManagedPolicy
```

获取外部来源扩展程序的管控策略。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function getExternalSourceExtensionsPolicy(admin: Want | null): common.ManagedPolicy--><!--Device-securityManager-function getExternalSourceExtensionsPolicy(admin: Want | null): common.ManagedPolicy-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 当设备存在多个MDM应用时，传入Want时查询对应企业设备管理应用设置的策略，传入null时查询实际生效的策略。 |

**Return value:**

| Type | Description |
| --- | --- |
| common.ManagedPolicy | 返回ManagedPolicy枚举类型的管控策略。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { common, securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  let result: common.ManagedPolicy = securityManager.getExternalSourceExtensionsPolicy(wantTemp);
  console.info(`Succeeded in getting managed policy, result : ${result}`);
} catch(err) {
  console.error(`Failed to get managed policy. Code: ${err.code}, message: ${err.message}`);
}
```

