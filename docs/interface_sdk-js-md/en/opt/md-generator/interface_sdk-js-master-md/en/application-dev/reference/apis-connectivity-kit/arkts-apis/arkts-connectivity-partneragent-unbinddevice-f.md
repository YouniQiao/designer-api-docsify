# unbindDevice

## Modules to Import

```TypeScript
import { partnerAgent } from '@kit.ConnectivityKit';
```

## unbindDevice

```TypeScript
function unbindDevice(deviceAddress: PartnerDeviceAddress): Promise<void>
```

Unbinds a partner device.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-partnerAgent-function unbindDevice(deviceAddress: PartnerDeviceAddress): Promise<void>--><!--Device-partnerAgent-function unbindDevice(deviceAddress: PartnerDeviceAddress): Promise<void>-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

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
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [34900001](../errorcode-fusionConnectivity.md#34900001-device-not-registered) |
| [34900099](../errorcode-fusionConnectivity.md#34900099-operation-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
