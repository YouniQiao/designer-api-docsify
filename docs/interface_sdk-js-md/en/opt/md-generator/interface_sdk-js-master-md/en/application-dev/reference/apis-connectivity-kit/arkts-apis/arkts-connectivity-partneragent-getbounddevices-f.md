# getBoundDevices

## Modules to Import

```TypeScript
import { partnerAgent } from '@kit.ConnectivityKit';
```

## getBoundDevices

```TypeScript
function getBoundDevices(): PartnerDeviceAddress[]
```

Gets the list of addresses of the bound partner device for this application.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-partnerAgent-function getBoundDevices(): PartnerDeviceAddress[]--><!--Device-partnerAgent-function getBoundDevices(): PartnerDeviceAddress[]-End-->

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [PartnerDeviceAddress[]](arkts-connectivity-partnerdeviceaddress-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [34900099](../errorcode-fusionConnectivity.md#34900099-operation-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
