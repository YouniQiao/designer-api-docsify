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

**Deprecated since:** 9

**Substitutes:** stateChange

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function off(type: 'stateChange', callback?: Callback<BluetoothState>): void--><!--Device-bluetooth-function off(type: 'stateChange', callback?: Callback<BluetoothState>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'stateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BluetoothState&gt; | No |

## Examples

```TypeScript
function onReceiveEvent(data : bluetooth.BluetoothState) {
    console.info('bluetooth state = '+ JSON.stringify(data));
}
bluetooth.on('stateChange', onReceiveEvent);
bluetooth.off('stateChange', onReceiveEvent);
```
