# setUserRestriction

## Modules to Import

```TypeScript
import { restrictions } from '@kit.MDMKit';
```

## setUserRestriction

```TypeScript
function setUserRestriction(admin: Want, settingsItem: string, restricted: boolean): void
```

Sets restrictions on user behaviors.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** 26.0.0

**Substitutes:** [setUserRestriction](restrictions.setUserRestriction(admin:)

**Required permissions:** ohos.permission.ENTERPRISE_SET_USER_RESTRICTION

**Model restriction:** This API can be used only in the stage model.

<!--Device-restrictions-function setUserRestriction(admin: Want, settingsItem: string, restricted: boolean): void--><!--Device-restrictions-function setUserRestriction(admin: Want, settingsItem: string, restricted: boolean): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| settingsItem | string | Yes | Behavior name. Only the following values are supported. If other values are passed, an error will be reported. &lt;br&gt;- **setApn**: APN configuration, currently supported only on smartphones and tablets. &lt;br&gt;- **powerLongPress**: capability to open the power menu by long-pressing the power button. Currently, only smartphones and tablets are supported. &lt;br&gt;- **setEthernetIp**: Ethernet IP address configuration, currently supported only on PCs/2-in-1 devices. &lt;br&gt;- **setDeviceName**: device name configuration, currently supported only on PCs/2-in-1 devices, smartphones, and tablets. When it is disabled, the device name cannot be modified in the following settings: **About**, **Bluetooth**, and **More connectivity options** > **NearLink** on PCs/2-in-1 devices, and **About**, **Bluetooth**, and **Personal hotspot** on smartphones and tablets. &lt;br&gt;- **setBiometricsAndScreenLock**: screen lock password configuration, currently supported only on PCs/2-in- 1 devices, smartphones, and tablets. |
| restricted | boolean | Yes | Whether to disable the action. The value **true** means to disable the action, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

## Examples

```TypeScript
import { Want } from '@kit.AbilityKit';
import { restrictions } from '@kit.MDMKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // Replace parameters with actual values.
  restrictions.setUserRestriction(wantTemp, 'setApn', true);
  console.info('Succeeded in restricting from setting apn');
} catch (err) {
  console.error(`Failed to restrict from setting apn. Code is ${err.code}, message is ${err.message}`);
}
```


## setUserRestriction

```TypeScript
function setUserRestriction(admin: Want, settingsItem: SettingsForDevice, restricted: boolean): void
```

Restricts users from modifying specified device setting items.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_SET_USER_RESTRICTION

**Model restriction:** This API can be used only in the stage model.

<!--Device-restrictions-function setUserRestriction(admin: Want, settingsItem: SettingsForDevice, restricted: boolean): void--><!--Device-restrictions-function setUserRestriction(admin: Want, settingsItem: SettingsForDevice, restricted: boolean): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| settingsItem | [SettingsForDevice](arkts-mdm-restrictions-settingsfordevice-e.md) | Yes | Device setting items to be restricted from modification. |
| restricted | boolean | Yes | The value **true** means to disable the action, and **false** means the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

