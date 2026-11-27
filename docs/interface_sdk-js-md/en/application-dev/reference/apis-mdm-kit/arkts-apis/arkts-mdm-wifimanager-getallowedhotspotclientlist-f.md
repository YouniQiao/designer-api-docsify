# getAllowedHotspotClientList

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.MDMKit';
```

## getAllowedHotspotClientList

```TypeScript
function getAllowedHotspotClientList(queryPolicy?: common.QueryPolicy): Array<string>
```

Obtain the list of available network share MAC addresses.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ENTERPRISE_MANAGE_WIFI

**Model restriction:** This API can be used only in the stage model.

<!--Device-wifiManager-function getAllowedHotspotClientList(queryPolicy?: common.QueryPolicy): Array<string>--><!--Device-wifiManager-function getAllowedHotspotClientList(queryPolicy?: common.QueryPolicy): Array<string>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| queryPolicy | [common.QueryPolicy](arkts-mdm-common-querypolicy-e.md) | No | Specifies the query policy, The default value is [SELF](arkts-mdm-common-querypolicy-e.md#self), indicating that the policies set by the current device management application are queried. When [ALL](arkts-mdm-common-querypolicy-e.md#all) is transferred, the policy set on the current device can be queried. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | Indicates the list of available network share MAC addresses. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-permission-denied) | The administrator application does not have permission to manage the device. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-service-timeout) | Service timeout. |
