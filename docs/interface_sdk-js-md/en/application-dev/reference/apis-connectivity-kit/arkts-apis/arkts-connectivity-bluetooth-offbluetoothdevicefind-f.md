# off_bluetoothDeviceFind

## Modules to Import

```TypeScript
import { bluetooth } from 'bluetooth';
```

## off_bluetoothDeviceFind

```TypeScript
function off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void
```

Unsubscribe the event reported when a remote Bluetooth device is discovered.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** bluetoothDeviceFind

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void--><!--Device-bluetooth-function off(type: 'bluetoothDeviceFind', callback?: Callback<Array<string>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'bluetoothDeviceFind' | Yes | Type of the discovering event to listen for. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | No | Callback used to listen for the discovering event. |

**Examples**

```TypeScript
function onReceiveEvent(data : Array<string>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.on('bluetoothDeviceFind', onReceiveEvent);
bluetooth.off('bluetoothDeviceFind', onReceiveEvent);
```

