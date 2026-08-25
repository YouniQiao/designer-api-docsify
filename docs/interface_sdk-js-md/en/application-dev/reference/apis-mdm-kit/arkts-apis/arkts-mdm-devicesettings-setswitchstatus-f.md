# setSwitchStatus

## Modules to Import

```TypeScript
import { deviceSettings } from 'kits/@kit.MDMKit';
```

## setSwitchStatus

```TypeScript
function setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void
```

Sets the state of a switch. This API can enable or disable NearLink, Bluetooth, Wi-Fi, and NFC. After the setting is applied, users can manually enable or disable them. Bluetooth and NFC can be forced on. Once set, they cannot be manually turned on or off by the user. If a switch has been disabled through the [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md) API, error code 203 will be reported when you attempt to set the state of the switch through this API. In this case, you need to use the [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md) API to enable the switch. When multiple MDM applications are present on the device, there are no conflicts among the switch states set by different MDM applications. The policy set last takes effect. The three states, on (user can manually enable /disable), off (user can manually enable/disable), and forced on (user cannot manually disable), can be switched arbitrarily, and no conflict occurs.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| key | [SwitchKey](arkts-mdm-devicesettings-switchkey-e.md) | Yes |
| status | [SwitchStatus](arkts-mdm-devicesettings-switchstatus-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) |
| 9201042 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
