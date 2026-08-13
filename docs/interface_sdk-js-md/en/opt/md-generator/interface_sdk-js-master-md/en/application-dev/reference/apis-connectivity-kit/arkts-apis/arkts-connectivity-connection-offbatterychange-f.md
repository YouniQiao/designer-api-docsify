# offBatteryChange

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## offBatteryChange

```TypeScript
function offBatteryChange(callback?: Callback<BatteryInfo>): void
```

Unsubscribe the event of battery state changed from a remote device.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function offBatteryChange(callback?: Callback<BatteryInfo>): void--><!--Device-connection-function offBatteryChange(callback?: Callback<BatteryInfo>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BatteryInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 2900099 |
