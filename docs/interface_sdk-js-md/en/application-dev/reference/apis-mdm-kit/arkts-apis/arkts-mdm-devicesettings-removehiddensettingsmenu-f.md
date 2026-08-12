# removeHiddenSettingsMenu

## Modules to Import

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## removeHiddenSettingsMenu

```TypeScript
function removeHiddenSettingsMenu(admin: Want, menusToHidden: Array<SettingsMenu>): void
```

Removes a setting item from the hidden setting item list of the current user. Setting items in the hidden setting item list are hidden in the current user's settings menu and cannot be found in settings search. Even if a setting item is located through some means, it cannot be opened when tapped. If the remaining hidden setting item list is empty after the removal, all setting items are displayed. The settings take effect immediately after the API is called. The Settings application does not need to be restarted.

Since API version 26.0.0, if you call  
[setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md#setDisallowedPolicyForAccount) to disable [SUPER_HUB](arkts-mdm-restrictions-featureforaccount-e.md#FeatureForAccount) and then call this API to remove SuperHub from the hidden setting item list, a policy conflict occurs and error code 9200010 is reported.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function removeHiddenSettingsMenu(admin: Want, menusToHidden: Array<SettingsMenu>): void--><!--Device-deviceSettings-function removeHiddenSettingsMenu(admin: Want, menusToHidden: Array<SettingsMenu>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| menusToHidden | Array&lt;[SettingsMenu](arkts-mdm-devicesettings-settingsmenu-e.md)&gt; | Yes | Hidden setting item list. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200012](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [9200010](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) | A conflict policy has been configured.<br>**Applicable version:** 26.0.0 and later |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200016](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |
| [9200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

