# off_bondStateChange

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## off_bondStateChange

```TypeScript
function off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void
```

Unsubscribe the event reported when a remote Bluetooth device is bonded.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** bondStateChange

**Required permissions:** ohos.permission.USE_BLUETOOTH

<!--Device-bluetooth-function off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void--><!--Device-bluetooth-function off(type: 'bondStateChange', callback?: Callback<BondStateParam>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'bondStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BondStateParam&gt; | No |

## Examples

```TypeScript
function onReceiveEvent(data : bluetooth.BondStateParam) {
    console.info('bond state = '+ JSON.stringify(data));
}
bluetooth.on('bondStateChange', onReceiveEvent);
bluetooth.off('bondStateChange', onReceiveEvent);
```
