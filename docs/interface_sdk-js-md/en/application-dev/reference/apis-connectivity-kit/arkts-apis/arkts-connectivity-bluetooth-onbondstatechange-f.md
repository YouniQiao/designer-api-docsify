# on_bondStateChange

## Modules to Import

```TypeScript
import { bluetooth } from 'bluetooth';
```

## on_bondStateChange

```TypeScript
function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void
```

Subscribe the event reported when a remote Bluetooth device is bonded.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** bondStateChange

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void--><!--Device-bluetooth-function on(type: 'bondStateChange', callback: Callback<BondStateParam>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'bondStateChange' | Yes | Type of the bond state event to listen for. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BondStateParam&gt; | Yes | Callback used to listen for the bond state event, [BondStateParam](arkts-connectivity-bluetooth-bondstateparam-i.md#bondstateparam). |

**Examples**

```TypeScript
function onReceiveEvent(data : bluetooth.BondStateParam) { // data, as the input parameter of the callback, indicates the pairing state.
    console.info('pair state = '+ JSON.stringify(data));
}
bluetooth.on('bondStateChange', onReceiveEvent);
```

