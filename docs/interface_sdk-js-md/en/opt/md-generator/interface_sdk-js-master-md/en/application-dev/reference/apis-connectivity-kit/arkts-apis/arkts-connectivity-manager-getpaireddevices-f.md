# getPairedDevices

## Modules to Import

```TypeScript
import { manager } from '@kit.ConnectivityKit';
```

## getPairedDevices

```TypeScript
function getPairedDevices(): string[]
```

Gets the list of devices that have been paired with the current device.If the user has the ohos.permission.GET_NEARLINK_PEER_MAC permission, the real device address is returned.Otherwise, a random device address is returned.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

<!--Device-manager-function getPairedDevices(): string[]--><!--Device-manager-function getPairedDevices(): string[]-End-->

**System capability:** SystemCapability.Communication.NearLink.Base

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string[] |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| 36100003 |
| 36100099 |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
