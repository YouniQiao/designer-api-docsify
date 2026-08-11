# removeDisallowedUsbDevices

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.MDMKit';
```

## removeDisallowedUsbDevices

```TypeScript
function removeDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void
```

Removes the disallowed USB device types.

Use cases:

- Lifts the restriction on certain USB device types in enterprise security management scenarios.  
- Enable device administrators to dynamically adjust the list of disallowed USB device types.  
- Remove USB device types from the blocklist when they no longer pose a security risk.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_USB

**Model restriction:** This API can be used only in the stage model.

<!--Device-usbManager-function removeDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void--><!--Device-usbManager-function removeDisallowedUsbDevices(admin: Want, usbDevices: Array<UsbDeviceType>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of the EnterpriseAdminExtensionAbility and the bundle name of the application. |
| usbDevices | Array&lt;UsbDeviceType&gt; | Yes | Array of the USB devices to be removed, which can be obtained through [getDevices](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-usbmanager-getdevices-f.md/arkts-basicservices-usbmanager-getdevices-f.md#getdevices). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |

## Examples

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
  usbManager.removeDisallowedUsbDevices(wantTemp, usbDevices);
  console.info(`Succeeded in removing disallowed USB devices.`);
} catch (err) {
  console.error(`Failed to remove disallowed USB devices. Code: ${err.code}, message: ${err.message}`);
}
```

