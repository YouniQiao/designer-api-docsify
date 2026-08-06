# setSwitchStatus

## setSwitchStatus

```TypeScript
function setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void
```

Sets the state of a switch. This API can enable or disable NearLink, Bluetooth, Wi-Fi, and NFC. After the setting is applied, users can manually enable or disable them. Bluetooth and NFC can be forced on. Once set, they cannot be manually turned on or off by the user. If a switch has been disabled through the  
[setDisallowedPolicy]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ API, error code 203will be reported when you attempt to set the state of the switch through this API. In this case, you need to use the [setDisallowedPolicy]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API to enable the switch. When multiple MDM applications are present on the device, there are no conflicts among the switch states set by different MDM applications. The policy set last takes effect. The three states, on (user can manually enable/disable), off (user can manually enable/disable), and forced on (user cannot manually disable), can be switched arbitrarily, and no conflict occurs.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_SETTINGS or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS

**Model restriction:** This API can be used only in the stage model.

<!--Device-deviceSettings-function setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void--><!--Device-deviceSettings-function setSwitchStatus(admin: Want, key: SwitchKey, status: SwitchStatus): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| key | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Switch name. An application that has obtained the ohos.permission.PERSONAL\_\_\_ESCAPED\_UNDERSCORE\_\_\_MANAGE\_\_\_ESCAPED\_UNDERSCORE\_\_\_RESTRICTIONS permission and has been activated as the built-in device administrator application via [startAdminProvision]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ can use this API to set the following switches: NearLink, Bluetooth, and Wi-Fi. Attempting to set the NFC switch will result in error code 9200002. |
| status | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Switch state. An application that has obtained the ohos.permission.PERSONAL\_\_\_ESCAPED\_UNDERSCORE\_\_\_MANAGE\_\_\_ESCAPED\_UNDERSCORE\_\_\_RESTRICTIONS permission and has been activated as the built-in device administrator application via [startAdminProvision]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ can use this API to set the following states: ON and OFF. Attempting to set the FORCE\_\_\_ESCAPED\_UNDERSCORE\_\_\_ON state will result in error code 9200002. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| 9201042 | Failed to toggle the switch state. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [203](../../errorcode-universal.md#203-system-function-prohibited-by-enterprise-management-policies) | This function is prohibited by enterprise management policies. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call the API due to limited device capabilities. |

