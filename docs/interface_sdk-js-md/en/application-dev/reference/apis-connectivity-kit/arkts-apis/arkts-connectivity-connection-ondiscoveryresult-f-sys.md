# on_discoveryResult (System API)

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## on_discoveryResult('discoveryResult')

```TypeScript
function on(type: 'discoveryResult', callback: Callback<Array<DiscoveryResult>>): void
```

Subscribe the event reported when a remote Bluetooth device is discovered. On API 26.0.0 and above, if the application has ohos.permission.GET_BLUETOOTH_PEERS_MAC, the type of the peer device address is real. Otherwise, the type of the peer device address is virtual.

**Since:** 12

**Required permissions:** 
- API version 26.0.0+: ohos.permission.ACCESS_BLUETOOTH or (ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC)
- API version 18 - 24: ohos.permission.ACCESS_BLUETOOTH
- API version 12 - 17: ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function on(type: 'discoveryResult', callback: Callback<Array<DiscoveryResult>>): void--><!--Device-connection-function on(type: 'discoveryResult', callback: Callback<Array<DiscoveryResult>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'discoveryResult' | Yes | Type of the discovering event to listen for. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[DiscoveryResult](arkts-connectivity-connection-discoveryresult-i-sys.md)&gt;&gt; | Yes | Callback used to listen for the discovering event. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed.<br>**Applicable version:** 12 - 24 |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900099 | Operation failed. |

**Examples**

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

