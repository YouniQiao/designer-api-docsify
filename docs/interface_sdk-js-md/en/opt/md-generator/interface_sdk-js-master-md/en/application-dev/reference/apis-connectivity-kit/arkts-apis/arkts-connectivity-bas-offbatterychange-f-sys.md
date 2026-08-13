# offBatteryChange (System API)

## Modules to Import

```TypeScript
import { bas } from '@kit.ConnectivityKit';
```

## offBatteryChange

```TypeScript
function offBatteryChange(callback?: Callback<BatteryInfo>): void
```

Unsubscribe the event of battery state changes from a remote device.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-bas-function offBatteryChange(callback?: Callback<BatteryInfo>): void--><!--Device-bas-function offBatteryChange(callback?: Callback<BatteryInfo>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BatteryInfo&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 2900099 |
