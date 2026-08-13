# onBatteryChange

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## onBatteryChange

```TypeScript
function onBatteryChange(callback: Callback<BatteryInfo>): void
```

Subscribe the event of battery state changed from a remote device.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function onBatteryChange(callback: Callback<BatteryInfo>): void--><!--Device-connection-function onBatteryChange(callback: Callback<BatteryInfo>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BatteryInfo&gt; | Yes | Callback used to listen. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| 2900099 | Operation failed. |

