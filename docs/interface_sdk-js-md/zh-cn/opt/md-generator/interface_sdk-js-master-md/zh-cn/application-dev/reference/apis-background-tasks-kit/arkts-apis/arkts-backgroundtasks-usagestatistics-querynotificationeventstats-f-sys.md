# queryNotificationEventStats（系统接口）

## queryNotificationEventStats

```TypeScript
function queryNotificationEventStats(
    begin: number,
    end: number,
    callback: AsyncCallback<Array<DeviceEventStats>>
  ): void
```

通过指定起始和结束时间，查询所有应用的通知次数，使用Callback异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryNotificationEventStats(    begin: long,    end: long,    callback: AsyncCallback<Array<DeviceEventStats>>  ): void--><!--Device-usageStatistics-function queryNotificationEventStats(    begin: long,    end: long,    callback: AsyncCallback<Array<DeviceEventStats>>  ): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | number | 是 |
| end | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[DeviceEventStats](arkts-backgroundtasks-usagestatistics-deviceeventstats-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-内存操作失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failed) |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-系统服务操作失败) |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-通信失败) |
| [10000006](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |
| [10000007](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-时间操作失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

usageStatistics.queryNotificationEventStats(0, 20000000000000, (err: BusinessError, res: Array<usageStatistics.DeviceEventStats>) => {
  if(err) {
    console.error('BUNDLE_ACTIVE queryNotificationEventStats callback failed. code is: ' + err.code + ',message is: ' + err.message);
  } else {
    console.info('BUNDLE_ACTIVE queryNotificationEventStats callback success.');
    console.info('BUNDLE_ACTIVE queryNotificationEventStats callback result ' + JSON.stringify(res));
  }
});
```


## queryNotificationEventStats

```TypeScript
function queryNotificationEventStats(begin: number, end: number): Promise<Array<DeviceEventStats>>
```

通过指定起始和结束时间，查询所有应用的通知次数，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryNotificationEventStats(begin: long, end: long): Promise<Array<DeviceEventStats>>--><!--Device-usageStatistics-function queryNotificationEventStats(begin: long, end: long): Promise<Array<DeviceEventStats>>-End-->

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | number | 是 |
| end | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[DeviceEventStats](arkts-backgroundtasks-usagestatistics-deviceeventstats-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-内存操作失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failed) |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-系统服务操作失败) |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-通信失败) |
| [10000006](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |
| [10000007](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-时间操作失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

usageStatistics.queryNotificationEventStats(0, 20000000000000).then((res: Array<usageStatistics.DeviceEventStats>) => {
  console.info('BUNDLE_ACTIVE queryNotificationEventStats promise success.');
  console.info('BUNDLE_ACTIVE queryNotificationEventStats promise result ' + JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE queryNotificationEventStats promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```
