# addDisallowedPermissiveUsbDevices

## addDisallowedPermissiveUsbDevices

```TypeScript
function addDisallowedPermissiveUsbDevices(admin: Want, usbDevices: Array<PermissiveUsbDeviceType>): void
```

Adds disallowed USB device types. Unlike the [addDisallowedUsbDevices]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API, this API does not require matching based on the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ standard. This API takes effect immediately on connected USB devices without requiring re-plugging. For example, if a USB wired headset is in normal use and this API is called to disable it, the headset will become unavailable immediately. A policy conflict is reported when this API is called in the following scenarios: 1. Disallowed USB device types have been added using the [addDisallowedUsbDevices]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ API. 2. The USB capability of the device has been disabled via [setDisallowedPolicy]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_. 3. The available USB devices have been added through [addAllowedUsbDevices]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_. 4. The USB storage write capability has been disabled for specific users via [setDisallowedPolicyForAccount]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_USB

**Model restriction:** This API can be used only in the stage model.

<!--Device-usbManager-function addDisallowedPermissiveUsbDevices(admin: Want, usbDevices: Array<PermissiveUsbDeviceType>): void--><!--Device-usbManager-function addDisallowedPermissiveUsbDevices(admin: Want, usbDevices: Array<PermissiveUsbDeviceType>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| usbDevices | Array&lt;PermissiveUsbDeviceType&gt; | Yes | Array of USB device types to be added. Partial field matching is supported. The array can have a maximum of 1000 elements. If there are already 500 USB device IDs in the array, only 500 more can be added. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) | A conflict policy has been configured. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed.The application does not have the permission required to call the API. |

