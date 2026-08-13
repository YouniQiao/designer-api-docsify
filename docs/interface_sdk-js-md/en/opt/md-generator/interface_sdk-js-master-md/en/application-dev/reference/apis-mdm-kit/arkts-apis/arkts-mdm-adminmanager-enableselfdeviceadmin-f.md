# enableSelfDeviceAdmin

## Modules to Import

```TypeScript
import { adminManager } from '@kit.MDMKit';
```

## enableSelfDeviceAdmin

```TypeScript
function enableSelfDeviceAdmin(admin: Want, credential: string): void
```

Allows an MDM application to enable itself in scenarios where it is not pre-enabled on the enterprise device. This API supports enablement of the MDM application itself only, and cannot be used to enable other MDM applications. The supported enablement types include super device administrator application and normal device administrator application.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_ACTIVATE_DEVICE_ADMIN

**Model restriction:** This API can be used only in the stage model.

<!--Device-adminManager-function enableSelfDeviceAdmin(admin: Want, credential: string): void--><!--Device-adminManager-function enableSelfDeviceAdmin(admin: Want, credential: string): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| credential | string | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [9200004](../errorcode-enterpriseDeviceManager.md#9200004-failed-to-enable-the-device-administrator-application) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200017](../errorcode-enterpriseDeviceManager.md#9200017-invalid-selfactivation-credential-of-the-enterprise-device-administrator) |
| [9200018](../errorcode-enterpriseDeviceManager.md#9200018-the-device-is-not-an-enterprise-device) |
| [9200003](../errorcode-enterpriseDeviceManager.md#9200003-invalid-administrator-ability-component) |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { adminManager } from '@kit.MDMKit';
import { BusinessError } from '@kit.BasicServicesKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

// Replace with actual values.
let credential: string = '{"enterpriseId": "123456", "appIdentifier": "123456", "type": "SDA", "sign": "", "certs": []}';

try {
  adminManager.enableSelfDeviceAdmin(wantTemp, credential);
  console.info(`succeed in enable self device admin.`);
} catch (err) {
  console.error(`Failed to enable self device admin. Code: ${err.code}, message: ${err.message}`);
}
```
