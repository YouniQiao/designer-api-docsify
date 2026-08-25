# queryDeviceEventStats（系统接口）

## 导入模块

```TypeScript
import { usageStatistics } from '@kit.BackgroundTasksKit';
```

## queryDeviceEventStats

```TypeScript
function queryDeviceEventStats(begin: long, end: long, callback: AsyncCallback<Array<DeviceEventStats>>): void
```

通过指定起始和结束时间，查询系统事件（休眠、唤醒、解锁、锁屏）的统计信息，使用Callback异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| end | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[DeviceEventStats](arkts-backgroundtasks-usagestatistics-deviceeventstats-i-sys.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [10000001](../errorcode-DeviceUsageStatistics.md#10000001-内存操作失败) |
| [10000002](../errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failed) |
| [10000003](../errorcode-DeviceUsageStatistics.md#10000003-系统服务操作失败) |
| [10000004](../errorcode-DeviceUsageStatistics.md#10000004-通信失败) |
| [10000006](../errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |
| [10000007](../errorcode-DeviceUsageStatistics.md#10000007-时间操作失败) |

**示例**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

usageStatistics.queryDeviceEventStats(0, 20000000000000).then((res: Array<usageStatistics.DeviceEventStats>) => {
  console.info('BUNDLE_ACTIVE queryDeviceEventStats promise success.');
  console.info('BUNDLE_ACTIVE queryDeviceEventStats promise result ' + JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE queryDeviceEventStats promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

usageStatistics.queryDeviceEventStats(0, 20000000000000, (err: BusinessError, res: Array<usageStatistics.DeviceEventStats>) => {
  if(err) {
    console.error('BUNDLE_ACTIVE queryDeviceEventStats callback failed. code is: ' + err.code + ',message is: ' + err.message);
  } else {
    console.info('BUNDLE_ACTIVE queryDeviceEventStats callback success.');
    console.info('BUNDLE_ACTIVE queryDeviceEventStats callback result ' + JSON.stringify(res));
  }
});
```


## queryDeviceEventStats

```TypeScript
function queryDeviceEventStats(begin: long, end: long): Promise<Array<DeviceEventStats>>
```

通过指定起始和结束时间，查询系统事件（休眠、唤醒、解锁、锁屏）的统计信息，使用Promise异步回调。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |
| end | ArkTS-Dyn: number<br>ArkTS-Sta：long | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[DeviceEventStats](arkts-backgroundtasks-usagestatistics-deviceeventstats-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [10000001](../errorcode-DeviceUsageStatistics.md#10000001-内存操作失败) |
| [10000002](../errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failed) |
| [10000003](../errorcode-DeviceUsageStatistics.md#10000003-系统服务操作失败) |
| [10000004](../errorcode-DeviceUsageStatistics.md#10000004-通信失败) |
| [10000006](../errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |
| [10000007](../errorcode-DeviceUsageStatistics.md#10000007-时间操作失败) |

**示例**

参见 [queryDeviceEventStats](#querydeviceeventstats)
