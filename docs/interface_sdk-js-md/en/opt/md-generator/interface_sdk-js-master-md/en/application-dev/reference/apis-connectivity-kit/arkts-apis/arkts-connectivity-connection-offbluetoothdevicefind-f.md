# offBluetoothDeviceFind

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## offBluetoothDeviceFind

```TypeScript
function offBluetoothDeviceFind(callback?: Callback<Array<string>>): void
```

Unsubscribe the event reported when a remote Bluetooth device is discovered.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

<!--Device-connection-function offBluetoothDeviceFind(callback?: Callback<Array<string>>): void--><!--Device-connection-function offBluetoothDeviceFind(callback?: Callback<Array<string>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;string&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900099 |
