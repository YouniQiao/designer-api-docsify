# getAllowedOpticalDiscDriveBurnUsbDevicesForAccount

## Modules to Import

```TypeScript
import { usbManager } from '@kit.MDMKit';
```

## getAllowedOpticalDiscDriveBurnUsbDevicesForAccount

```TypeScript
function getAllowedOpticalDiscDriveBurnUsbDevicesForAccount(accountId: number, policyType?: common.QueryPolicy): Array<UsbDevice>
```

Obtains USB devices in the burn whitelist for the specified account.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_USB

**Model restriction:** This API can be used only in the stage model.

<!--Device-usbManager-function getAllowedOpticalDiscDriveBurnUsbDevicesForAccount(accountId: number, policyType?: common.QueryPolicy): Array<UsbDevice>--><!--Device-usbManager-function getAllowedOpticalDiscDriveBurnUsbDevicesForAccount(accountId: number, policyType?: common.QueryPolicy): Array<UsbDevice>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| accountId | number | Yes | User ID, which must be greater than or equal to 0. |
| policyType | [common.QueryPolicy](arkts-mdm-common-querypolicy-e.md) | No | Query policy type. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[UsbDevice](arkts-mdm-usbmanager-usbdevice-i.md)&gt; | Returns the list of USB devices. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200006](../errorcode-enterpriseDeviceManager.md#9200006-invalid-user-id) | The specified account ID is invalid. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |
