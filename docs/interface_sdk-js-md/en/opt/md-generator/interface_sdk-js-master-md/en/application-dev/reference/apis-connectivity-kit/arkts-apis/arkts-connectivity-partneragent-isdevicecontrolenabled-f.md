# isDeviceControlEnabled

## Modules to Import

```TypeScript
import { partnerAgent } from '@kit.ConnectivityKit';
```

## isDeviceControlEnabled

```TypeScript
function isDeviceControlEnabled(deviceAddress: PartnerDeviceAddress): boolean
```

Checks whether device control is enabled.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-partnerAgent-function isDeviceControlEnabled(deviceAddress: PartnerDeviceAddress): boolean--><!--Device-partnerAgent-function isDeviceControlEnabled(deviceAddress: PartnerDeviceAddress): boolean-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceAddress | [PartnerDeviceAddress](arkts-connectivity-partnerdeviceaddress-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [34900099](../errorcode-fusionConnectivity.md#34900099-operation-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
