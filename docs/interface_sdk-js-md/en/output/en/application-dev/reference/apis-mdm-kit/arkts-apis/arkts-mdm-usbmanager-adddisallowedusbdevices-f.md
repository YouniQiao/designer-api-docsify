# addDisallowedUsbDevices

## addDisallowedUsbDevices

```TypeScript
function addDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void
```

Adds disallowed USB device types. Use cases: - Disable specific types of USB devices in enterprise security management scenarios. - Prevent data leaks by disabling USB storage device types. - Enable device administrators to prohibit the use of certain USB device types based on security policies. - Work with the [removeDisallowedUsbDevices]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_ API to implement dynamic management of USB device types. > **NOTE** > > The [addDisallowedPermissiveUsbDevices]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_ API is recommended. > A policy conflict is reported when this API is called in the following scenarios: 1. The USB capability of the device has been disabled via [setDisallowedPolicy]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_. 2. The available USB devices have been added through [addAllowedUsbDevices]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_. 3. The USB storage write capability has been disabled for specific users via [setDisallowedPolicyForAccount]\_\_\_JSDOC\_LINK\_DESC\_USD\_4\_\_\_. 4. Disallowed USB device types have been added via [addDisallowedPermissiveUsbDevices]\_\_\_JSDOC\_LINK\_DESC\_USD\_5\_\_\_.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_USB

**Model restriction:** This API can be used only in the stage model.

<!--Device-usbManager-function addDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void--><!--Device-usbManager-function addDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| usbDevices | Array&lt;UsbDeviceType&gt; | Yes | Array of the USB devices to be added, which can be obtained through [getDevices]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. The maximum number of USB devices is 200. If there are already 100 USB device IDs, only 100 more can be added. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) | A conflict policy has been configured. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

```TypeScript
import { usbManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // Replace with actual values.
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};
try {
  let usbDevices: Array<usbManager.UsbDeviceType> = [{
      baseClass: 8,
      subClass: 0,
      protocol: 0,
      descriptor: usbManager.Descriptor.INTERFACE
  }];
  usbManager.addDisallowedUsbDevices(wantTemp, usbDevices);
  console.info(`Succeeded in adding disallowed USB devices.`);
} catch (err) {
  console.error(`Failed to add disallowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

