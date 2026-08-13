# turnOnWifi

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.MDMKit';
```

## turnOnWifi

```TypeScript
function turnOnWifi(admin: Want, isForce: boolean): void
```

Enables Wi-Fi. This API is applicable to enterprise device remote management scenarios, such as administrators remotely enabling Wi-Fi on employee devices, or ensuring that Wi-Fi is turned on when specific policies are enforced. In the following scenario, attempting to enable Wi-Fi using this API will fail, and a message indicating that the system function is disabled will be returned: ​Wi-Fi has been disabled via [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setDisallowedPolicy). In this case, you must call [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setDisallowedPolicy) to enable Wi-Fi.

**Since:** 20

**Deprecated since:** -1

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_WIFI

**Model restriction:** This API can be used only in the stage model.

<!--Device-wifiManager-function turnOnWifi(admin: Want, isForce: boolean): void--><!--Device-wifiManager-function turnOnWifi(admin: Want, isForce: boolean): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| isForce | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { wifiManager } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  wifiManager.turnOnWifi(wantTemp, true);
  console.info(`Succeeded in turning on Wi-Fi.`);
} catch (err) {
  console.error(`Failed to turn on Wi-Fi. Code: ${err.code}, message: ${err.message}`);
}
```
