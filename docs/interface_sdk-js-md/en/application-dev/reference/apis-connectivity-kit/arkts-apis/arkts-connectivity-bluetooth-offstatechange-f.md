# off_stateChange

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## off_stateChange

```TypeScript
function off(type: 'stateChange', callback?: Callback<BluetoothState>): void
```

Unsubscribe the event reported when the Bluetooth state changes.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** stateChange

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function off(type: 'stateChange', callback?: Callback<BluetoothState>): void--><!--Device-bluetooth-function off(type: 'stateChange', callback?: Callback<BluetoothState>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'stateChange' | Yes | Type of the Bluetooth state changes event to listen for. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BluetoothState&gt; | No | Callback used to listen for the Bluetooth state event. |

## Examples

```TypeScript
function onReceiveEvent(data : bluetooth.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
bluetooth.on('stateChange', onReceiveEvent);
bluetooth.off('stateChange', onReceiveEvent);
```

