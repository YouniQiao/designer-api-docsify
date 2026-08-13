# getBatteryStats (System API)

## Modules to Import

```TypeScript
import { batteryStats } from '@kit.BasicServicesKit';
```

## getBatteryStats

```TypeScript
function getBatteryStats(): Promise<Array<BatteryStatsInfo>>
```

Obtains the power consumption information list. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-batteryStats-function getBatteryStats(): Promise<Array<BatteryStatsInfo>>--><!--Device-batteryStats-function getBatteryStats(): Promise<Array<BatteryStatsInfo>>-End-->

**System capability:** SystemCapability.PowerManager.BatteryStatistics

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[BatteryStatsInfo](arkts-basicservices-batterystats-batterystatsinfo-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [4600101](../../apis-basic-services-kit/errorcode-batteryStatistics.md#4600101-service-connection-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
batteryStats.getBatteryStats()
.then((data: batteryStats.BatteryStatsInfo[]) => {
    console.info('battery statistics info: ' + data);
})
.catch((err: Error) => {
    console.error('get battery statistics failed, err: ' + err);
});
```


## getBatteryStats

```TypeScript
function getBatteryStats(callback: AsyncCallback<Array<BatteryStatsInfo>>): void
```

Obtains the power consumption information list. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

<!--Device-batteryStats-function getBatteryStats(callback: AsyncCallback<Array<BatteryStatsInfo>>): void--><!--Device-batteryStats-function getBatteryStats(callback: AsyncCallback<Array<BatteryStatsInfo>>): void-End-->

**System capability:** SystemCapability.PowerManager.BatteryStatistics

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[BatteryStatsInfo](arkts-basicservices-batterystats-batterystatsinfo-i-sys.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [4600101](../../apis-basic-services-kit/errorcode-batteryStatistics.md#4600101-service-connection-failure) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
batteryStats.getBatteryStats((err: Error, data : batteryStats.BatteryStatsInfo[]) => {
    if (typeof err === 'undefined') {
        console.info('battery statistics info: ' + data);
    } else {
        console.error('get battery statistics failed, err: ' + err);
    }
});
```
