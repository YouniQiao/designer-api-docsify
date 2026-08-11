# onBatteryChange (System API)

## Modules to Import

```TypeScript
import { bas } from 'kits/@kit.ConnectivityKit';
```

## onBatteryChange

```TypeScript
function onBatteryChange(callback: Callback<BatteryInfo>): void
```

Subscribe the event of battery state changed from a remote device.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-bas-function onBatteryChange(callback: Callback<BatteryInfo>): void--><!--Device-bas-function onBatteryChange(callback: Callback<BatteryInfo>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BatteryInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 2900099 |
