# startAdvertising

## Modules to Import

```TypeScript
import { advertising } from '@kit.ConnectivityKit';
```

## startAdvertising

```TypeScript
function startAdvertising(advertisingParams: AdvertisingParams): Promise<number>
```

Starts NearLink advertising. This API uses a promise to return the result. This API is applicable to scenarios where the local device capabilities or data needs to be advertised, such as device discovery and device information advertising. You can use [advertising.onAdvertisingStateChange](arkts-connectivity-advertising-onadvertisingstatechange-f.md) to monitor the advertising status.

**Since:** 26.0.0

**Required permissions:** ohos.permission.ACCESS_NEARLINK

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.NearLink.Base

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| advertisingParams | AdvertisingParams | Yes | Advertising parameters. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | Promise used to return the advertising ID. The advertising ID is a unique ID randomly allocated. The value range is [0, 255]. Similar to [advertising.stopAdvertising]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported because the chip does not support it. |
| 36100003 | NearLink disabled. |
| 36100040 | Integer out of range. |
| 36100043 | Invalid UUID. |
| 36100099 | Operation failed. |
