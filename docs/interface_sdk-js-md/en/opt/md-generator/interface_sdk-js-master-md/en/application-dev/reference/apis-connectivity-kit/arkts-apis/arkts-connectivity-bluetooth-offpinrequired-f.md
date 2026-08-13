# off_pinRequired

## Modules to Import

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## off_pinRequired

```TypeScript
function off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void
```

Unsubscribe the event of a pairing request from a remote Bluetooth device.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** pinRequired

**Required permissions:** ohos.permission.DISCOVER_BLUETOOTH

<!--Device-bluetooth-function off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void--><!--Device-bluetooth-function off(type: 'pinRequired', callback?: Callback<PinRequiredParam>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'pinRequired' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;PinRequiredParam&gt; | No |

## Examples

```TypeScript
function onReceiveEvent(data : bluetooth.PinRequiredParam) {
    console.info('pin required = '+ JSON.stringify(data));
}
bluetooth.on('pinRequired', onReceiveEvent);
bluetooth.off('pinRequired', onReceiveEvent);
```
