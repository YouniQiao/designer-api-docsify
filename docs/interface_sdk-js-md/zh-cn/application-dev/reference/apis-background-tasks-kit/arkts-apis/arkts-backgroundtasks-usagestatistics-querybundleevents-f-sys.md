# queryBundleEvents（系统接口）

## 导入模块

```TypeScript
import { usageStatistics } from 'kits/@kit.BackgroundTasksKit';
```

## queryBundleEvents

```TypeScript
function queryBundleEvents(begin: number, end: number, callback: AsyncCallback<Array<BundleEvents>>): void
```

通过指定起始和结束时间，查询所有应用的事件集合，使用Callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | number | 是 |
| end | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[BundleEvents](arkts-backgroundtasks-usagestatistics-bundleevents-i-sys.md)&gt;&gt; | 是 |

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


## queryBundleEvents

```TypeScript
function queryBundleEvents(begin: number, end: number): Promise<Array<BundleEvents>>
```

通过指定起始和结束时间，查询所有应用的事件集合，使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

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
| Promise&lt;Array&lt;[BundleEvents](arkts-backgroundtasks-usagestatistics-bundleevents-i-sys.md)&gt;&gt; |

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


## queryBundleEvents

```TypeScript
function queryBundleEvents(begin: number, end: number, maxNum: number): Promise<Array<BundleEvents>>
```

通过指定起始时间、结束时间及最大返回条数，查询指定时间段内所有应用的事件集合。若条数大于maxNum，则按事件发生时间降序排列，返回前maxNum条，否则返回所有数据。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | number | 是 |
| end | number | 是 |
| maxNum | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[BundleEvents](arkts-backgroundtasks-usagestatistics-bundleevents-i-sys.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [10000001](../errorcode-DeviceUsageStatistics.md#10000001-内存操作失败) |
| [10000002](../errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failed) |
| [10000003](../errorcode-DeviceUsageStatistics.md#10000003-系统服务操作失败) |
| [10000004](../errorcode-DeviceUsageStatistics.md#10000004-通信失败) |
| [10000006](../errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |
| [10000007](../errorcode-DeviceUsageStatistics.md#10000007-时间操作失败) |
| [10000008](../errorcode-DeviceUsageStatistics.md#10000008-参数检查失败) |
