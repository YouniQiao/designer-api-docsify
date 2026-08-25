# setUsbStorageDeviceAccessPolicy

## Modules to Import

```TypeScript
import { usbManager } from 'kits/@kit.MDMKit';
```

## setUsbStorageDeviceAccessPolicy

```TypeScript
function setUsbStorageDeviceAccessPolicy(admin: Want, usbPolicy: UsbPolicy): void
```

Sets the USB storage device (baseClass = 0x08) access policy.

> **NOTE：**&gt;
> Before calling the API, read and write operations on the USB storage device should be suspended to ensure
> operational stability and data integrity. Otherwise, unexpected exceptions may occur.
> A policy conflict occurs when you set the USB storage device access policy to read, write, or read-only in the
> following scenarios:
1. The USB capability of the device has been disabled via [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md).
2. The USB storage device has been disallowed to use through [addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md).
3. The USB storage write capability has been disabled for specific users via [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md).
A policy conflict is reported if the USB storage device access policy is disabled by calling this API in the following scenarios:
1. The USB capability of the device has been disabled via [setDisallowedPolicy](arkts-mdm-restrictions-setdisallowedpolicy-f.md).
2. The available USB devices have been added through [addAllowedUsbDevices](arkts-mdm-usbmanager-addallowedusbdevices-f.md).
3. The USB storage write capability has been disabled for specific users via [setDisallowedPolicyForAccount](arkts-mdm-restrictions-setdisallowedpolicyforaccount-f.md).
You can disable a USB storage device by calling this API or [addDisallowedUsbDevices](arkts-mdm-usbmanager-adddisallowedusbdevices-f.md). The latter is recommended.

**Since:** 12

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ENTERPRISE_MANAGE_USB or ohos.permission.PERSONAL_MANAGE_RESTRICTIONS
- API version 12 - 24: ohos.permission.ENTERPRISE_MANAGE_USB

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| usbPolicy | [UsbPolicy](arkts-mdm-usbmanager-usbpolicy-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) |
| [9200007](../errorcode-enterpriseDeviceManager.md#9200007-system-ability-error) |
| [9200010](../errorcode-enterpriseDeviceManager.md#9200010-policy-conflict) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
