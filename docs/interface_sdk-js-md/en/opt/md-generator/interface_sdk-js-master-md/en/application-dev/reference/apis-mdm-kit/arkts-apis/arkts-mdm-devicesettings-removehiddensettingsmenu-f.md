# removeHiddenSettingsMenu

## Modules to Import

```TypeScript
import { deviceSettings } from 'kits/@kit.MDMKit';
```

## removeHiddenSettingsMenu

```TypeScript
function removeHiddenSettingsMenu(admin: Want, menusToHidden: Array<SettingsMenu>): void
```

Removes a setting item from the hidden setting item list of the current user. Setting items in the hidden setting item list are hidden in the current user's settings menu and cannot be found in settings search. Even if a setting item is located through some means, it cannot be opened when tapped. If the remaining hidden setting item list is empty after the removal, all setting items are displayed. The settings take effect immediately after the API is called. The Settings application does not need to be restarted.

Since API version 26.0.0, if you call  
[setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setdisallowedpolicyforaccount) to disable [SUPER_HUB](arkts-mdm-restrictions-featureforaccount-e.md) and then call this API to remove SuperHub from the hidden setting item list, a policy conflict occurs and error code 9200010 is reported.

**Since:** 24

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function removeHiddenSettingsMenu(admin: Want, menusToHidden: Array<SettingsMenu>): void--><!--Device-deviceSettings-function removeHiddenSettingsMenu(admin: Want, menusToHidden: Array<SettingsMenu>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| menusToHidden | Array&lt;SettingsMenu&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |

## Examples

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

let menusToHidden: Array<deviceSettings.SettingsMenu> = [
  // Replace or add items as needed.
  deviceSettings.SettingsMenu.ACCOUNT_ID,
  deviceSettings.SettingsMenu.WIFI,
]

try {
  deviceSettings.removeHiddenSettingsMenu(wantTemp, menusToHidden);
  console.info('Succeeded in removing hidden settings menu.');
} catch (err) {
  console.error(`Failed to remove hidden settings menu. Code: ${err.code}, message: ${err.message}`);
}
```
