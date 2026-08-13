# on_discoveryResult (System API)

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## on_discoveryResult

```TypeScript
function on(type: 'discoveryResult', callback: Callback<Array<DiscoveryResult>>): void
```

Subscribe the event reported when a remote Bluetooth device is discovered. On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual.

**Since:** 12

**Deprecated since:** -1

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)
- API version 18 - 24: ohos.permission.ACCESS_BLUETOOTH
- API version 12 - 17: ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function on(type: 'discoveryResult', callback: Callback<Array<DiscoveryResult>>): void--><!--Device-connection-function on(type: 'discoveryResult', callback: Callback<Array<DiscoveryResult>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'discoveryResult' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[DiscoveryResult](arkts-connectivity-connection-discoveryresult-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900099 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let onReceiveEvent: (data: Array<connection.DiscoveryResult>) => void = (data: Array<connection.DiscoveryResult>) => { // data is an array of Bluetooth devices discovered.
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    connection.on('discoveryResult', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
