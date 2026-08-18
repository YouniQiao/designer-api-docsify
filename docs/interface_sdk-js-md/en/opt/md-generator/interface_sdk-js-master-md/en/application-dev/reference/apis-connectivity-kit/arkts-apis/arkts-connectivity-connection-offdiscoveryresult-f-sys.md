# off_discoveryResult (System API)

## Modules to Import

```TypeScript
```

## off_discoveryResult

```TypeScript
function off(type: 'discoveryResult', callback?: Callback<Array<DiscoveryResult>>): void
```

Unsubscribe the event reported when a remote Bluetooth device is discovered.

**Since:** 12

**Required permissions:** 
- API version 18+: ohos.permission.ACCESS_BLUETOOTH
- API version 12 - 17: ohos.permission.ACCESS_BLUETOOTH and ohos.permission.GET_BLUETOOTH_PEERS_MAC

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function off(type: 'discoveryResult', callback?: Callback<Array<DiscoveryResult>>): void--><!--Device-connection-function off(type: 'discoveryResult', callback?: Callback<Array<DiscoveryResult>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'discoveryResult' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[DiscoveryResult](arkts-connectivity-connection-discoveryresult-i-sys.md)&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900099 |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
let onReceiveEvent: (data: Array<connection.DiscoveryResult>) => void = (data: Array<connection.DiscoveryResult>) => { // data is an array of Bluetooth devices discovered.
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    connection.on('discoveryResult', onReceiveEvent);
    connection.off('discoveryResult', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
