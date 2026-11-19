# getProfileConnectionState

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## getProfileConnectionState

```TypeScript
function getProfileConnectionState(profileId?: ProfileId): ProfileConnectionState
```

Get the profile connection state of the current device.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function getProfileConnectionState(profileId?: ProfileId): ProfileConnectionState--><!--Device-connection-function getProfileConnectionState(profileId?: ProfileId): ProfileConnectionState-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| profileId | [ProfileId](arkts-connectivity-connection-profileid-t.md) | No | Indicate the profile id. This is an optional parameter. With profileId, returns the current connection state of this profile, [ProfileConnectionState](arkts-connectivity-connection-profileconnectionstate-t.md). Without profileId, if any profile is connected, STATE_CONNECTED is returned. Otherwise, STATE_DISCONNECTED is returned. |

**Return value:**

| Type | Description |
| --- | --- |
| [ProfileConnectionState](arkts-connectivity-connection-profileconnectionstate-t.md) | Returns the connection state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900004 | Profile not supported. |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { constant } from '@kit.ConnectivityKit';
try {
    let result: connection.ProfileConnectionState = connection.getProfileConnectionState(constant.ProfileId.PROFILE_A2DP_SOURCE);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
