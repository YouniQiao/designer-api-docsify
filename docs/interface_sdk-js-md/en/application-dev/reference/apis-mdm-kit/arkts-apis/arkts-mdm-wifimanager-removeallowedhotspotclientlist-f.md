# removeAllowedHotspotClientList

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.MDMKit';
```

## removeAllowedHotspotClientList

```TypeScript
function removeAllowedHotspotClientList(macAddresses: Array<string>): void
```

Remove the network share MAC address.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_WIFI

**Model restriction:** This API can be used only in the stage model.

<!--Device-wifiManager-function removeAllowedHotspotClientList(macAddresses: Array<string>): void--><!--Device-wifiManager-function removeAllowedHotspotClientList(macAddresses: Array<string>): void-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| macAddresses | Array&lt;string&gt; | Yes | Indicates the list of available network share MAC addresses to be removed. <br>The maximum length is 1000 characters. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-parameter-verification-failed) | Parameter verification failed. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |
| [9200019](../errorcode-enterpriseDeviceManager.md#9200019-policy-list-exceeds-the-limit) | The policy list has exceeded the limit. |
