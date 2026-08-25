# queryAppGroupSync（系统接口）

## 导入模块

```TypeScript
import { usageStatistics } from 'kits/@kit.BackgroundTasksKit';
```

## queryAppGroupSync

```TypeScript
function queryAppGroupSync(): number
```

查询当前应用的优先级分组，使用同步方式返回。

**起始版本：** 10

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [10000001](../errorcode-DeviceUsageStatistics.md#10000001-内存操作失败) |
| [10000002](../errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failed) |
| [10000003](../errorcode-DeviceUsageStatistics.md#10000003-系统服务操作失败) |
| [10000004](../errorcode-DeviceUsageStatistics.md#10000004-通信失败) |
| [10000005](../errorcode-DeviceUsageStatistics.md#10000005-应用未安装) |
| [10000006](../errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |
| [10100002](../errorcode-DeviceUsageStatistics.md#10100002-获取应用分组信息失败) |


## queryAppGroupSync

```TypeScript
function queryAppGroupSync(bundleName: string): number
```

查询指定bundleName应用的优先级分组，使用同步方式返回。

**起始版本：** 10

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

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
| [10000005](../errorcode-DeviceUsageStatistics.md#10000005-应用未安装) |
| [10000006](../errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |
| [10100002](../errorcode-DeviceUsageStatistics.md#10100002-获取应用分组信息失败) |
