# isScreenLockDisabledForAccount

## Modules to Import

```TypeScript
import { securityManager } from 'kits/@kit.MDMKit';
```

## isScreenLockDisabledForAccount

```TypeScript
function isScreenLockDisabledForAccount(admin: Want): boolean
```

查询当前用户的滑动解锁能力是否被禁用。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SECURITY

**Model restriction:** This API can be used only in the stage model.

<!--Device-securityManager-function isScreenLockDisabledForAccount(admin: Want): boolean--><!--Device-securityManager-function isScreenLockDisabledForAccount(admin: Want): boolean-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回true表示当前用户的滑动解锁能力已禁用，false表示未禁用。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { securityManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let result: boolean = securityManager.isScreenLockDisabledForAccount(wantTemp);
  console.info(`Succeeded in checking screen lock disabled for account, result : ${result}`);
} catch(err) {
  console.error(`Failed to check screen lock disabled for account. Code: ${err.code}, message: ${err.message}`);
}
```

