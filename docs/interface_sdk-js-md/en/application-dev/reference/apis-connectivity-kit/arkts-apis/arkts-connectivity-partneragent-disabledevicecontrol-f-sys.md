# disableDeviceControl (System API)

## Modules to Import

```TypeScript
import { partnerAgent } from 'kits/@kit.ConnectivityKit';
```

## disableDeviceControl

```TypeScript
function disableDeviceControl(deviceAddress: PartnerDeviceAddress): Promise<void>
```

Disables device control for a bound device.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceAddress | [PartnerDeviceAddress](arkts-connectivity-partnerdeviceaddress-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [34900001](../errorcode-fusionConnectivity.md#34900001-device-not-registered) |
| [34900099](../errorcode-fusionConnectivity.md#34900099-operation-failed) |
