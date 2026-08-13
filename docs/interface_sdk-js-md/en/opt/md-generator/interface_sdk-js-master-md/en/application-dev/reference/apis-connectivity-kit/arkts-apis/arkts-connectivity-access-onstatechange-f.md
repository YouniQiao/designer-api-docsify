# onStateChange

## Modules to Import

```TypeScript
import { access } from '@kit.ConnectivityKit';
```

## onStateChange

```TypeScript
function onStateChange(callback: Callback<BluetoothState>): void
```

Subscribe the event reported when the Bluetooth state changes.

**Since:** 23

**Deprecated since:** -1

<!--Device-access-function onStateChange(callback: Callback<BluetoothState>): void--><!--Device-access-function onStateChange(callback: Callback<BluetoothState>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BluetoothState&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| 2900099 |
