# on_bluetoothDeviceFind

## Modules to Import

```TypeScript
import { bluetooth } from 'bluetooth';
```

## on_bluetoothDeviceFind

```TypeScript
function on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void
```

Subscribe the event reported when a remote Bluetooth device is discovered.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** bluetoothDeviceFind

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void--><!--Device-bluetooth-function on(type: 'bluetoothDeviceFind', callback: Callback<Array<string>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'bluetoothDeviceFind' | Yes | Type of the discovering event to listen for. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | Yes | Callback used to listen for the discovering event. |

## Examples

```TypeScript
function onReceiveEvent(data : Array<string>) { // data is an array of Bluetooth device addresses.
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.on('bluetoothDeviceFind', onReceiveEvent);
```

