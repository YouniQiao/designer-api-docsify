# setFingerprintAuthDisabled

## Modules to Import

```TypeScript
import { restrictions } from 'kits/@kit.MDMKit';
```

## setFingerprintAuthDisabled

```TypeScript
function setFingerprintAuthDisabled(admin: Want, disabled: boolean): void
```

禁用或启用指纹认证。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** 26.0.0

**Substitutes:** [restrictions.setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setdisallowedpolicy)(admin:

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_RESTRICTIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-restrictions-function setFingerprintAuthDisabled(admin: Want, disabled: boolean): void--><!--Device-restrictions-function setFingerprintAuthDisabled(admin: Want, disabled: boolean): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| disabled | boolean | Yes | true表示禁止指纹认证，false表示允许指纹认证。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 202 | Permission verification failed. A non-system application calls a system API. |
| 9200001 | The application is not an administrator application of the device. |
| 9200002 | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { restrictions } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  restrictions.setFingerprintAuthDisabled(wantTemp, true);
  console.info('Succeeded in disabling the fingerprint auth');
} catch (err) {
  console.error(`Failed to disable fingerprint auth. Code: ${err.code}, message: ${err.message}`);
};
```

