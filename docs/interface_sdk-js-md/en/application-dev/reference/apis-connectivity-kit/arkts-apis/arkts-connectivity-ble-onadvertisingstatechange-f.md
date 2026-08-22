# on_advertisingStateChange

## Modules to Import

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## on('advertisingStateChange')

```TypeScript
function on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void
```

Subscribing to advertising state change event.

**Since:** 11

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-ble-function on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void--><!--Device-ble-function on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'advertisingStateChange' | Yes | Type of the advertising state to listen for. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AdvertisingStateChangeInfo&gt; | Yes | Callback used to listen for the advertising state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: ble.AdvertisingStateChangeInfo) {
    console.info('bluetooth advertising state = ' + JSON.stringify(data));
}
try {
    ble.on('advertisingStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

