# setWifiDisabled (System API)

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.MDMKit';
```

## setWifiDisabled

```TypeScript
function setWifiDisabled(admin: Want, disabled: boolean): void
```

Sets the Wi-Fi disabling policy.

**Since:** 11

**Deprecated since:** 26.0.0

**Substitutes:** [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md#setDisallowedPolicy)(admin: Want, feature: FeatureForDevice, disallow: boolean)

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_WIFI

**Model restriction:** This API can be used only in the stage model.

<!--Device-wifiManager-function setWifiDisabled(admin: Want, disabled: boolean): void--><!--Device-wifiManager-function setWifiDisabled(admin: Want, disabled: boolean): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| disabled | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { wifiManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  wifiManager.setWifiDisabled(wantTemp, true);
  console.info('Succeeded in setting the wifi disabled');
} catch (err) {
  console.error(`Failed to set the wifi disabled. Code: ${err.code}, message: ${err.message}`);
};
```
