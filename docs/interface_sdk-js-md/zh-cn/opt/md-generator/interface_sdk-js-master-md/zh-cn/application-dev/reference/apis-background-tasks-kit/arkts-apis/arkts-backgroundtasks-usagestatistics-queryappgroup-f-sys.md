# queryAppGroup（系统接口）

## queryAppGroup

```TypeScript
function queryAppGroup(callback: AsyncCallback<number>): void
```

查询当前应用的优先级分组，使用Callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryAppGroup(callback: AsyncCallback<int>): void--><!--Device-usageStatistics-function queryAppGroup(callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [10100002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10100002-获取应用分组信息失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-内存操作失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failed) |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-系统服务操作失败) |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-通信失败) |
| [10000005](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000005-应用未安装) |
| [10000006](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

usageStatistics.queryAppGroup((err: BusinessError, res: number) => {
  if(err) {
    console.error('BUNDLE_ACTIVE queryAppGroup callback failed. code is: ' + err.code + ',message is: ' + err.message);
  } else {
    console.info('BUNDLE_ACTIVE queryAppGroup callback succeeded. result: ' + JSON.stringify(res));
  }
});
```


## queryAppGroup

```TypeScript
function queryAppGroup(): Promise<number>
```

查询当前应用的优先级分组，使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryAppGroup(): Promise<int>--><!--Device-usageStatistics-function queryAppGroup(): Promise<int>-End-->

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [10100002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10100002-获取应用分组信息失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-内存操作失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failed) |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-系统服务操作失败) |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-通信失败) |
| [10000005](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000005-应用未安装) |
| [10000006](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

usageStatistics.queryAppGroup().then((res: number) => {
  console.info('BUNDLE_ACTIVE queryAppGroup promise succeeded. result: ' + JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE queryAppGroup promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```


## queryAppGroup

```TypeScript
function queryAppGroup(bundleName: string, callback: AsyncCallback<number>): void
```

查询指定bundleName应用的优先级分组，使用Callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryAppGroup(bundleName: string, callback: AsyncCallback<int>): void--><!--Device-usageStatistics-function queryAppGroup(bundleName: string, callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [10100002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10100002-获取应用分组信息失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-内存操作失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failed) |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-系统服务操作失败) |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-通信失败) |
| [10000005](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000005-应用未安装) |
| [10000006](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

let bundleName: string = 'com.ohos.camera';
usageStatistics.queryAppGroup(bundleName, (err: BusinessError, res: number) => {
  if(err) {
    console.error('BUNDLE_ACTIVE queryAppGroup callback failed. code is: ' + err.code + ',message is: ' + err.message);
  } else {
    console.info('BUNDLE_ACTIVE queryAppGroup callback succeeded. result: ' + JSON.stringify(res));
  }
});
```


## queryAppGroup

```TypeScript
function queryAppGroup(bundleName: string): Promise<number>
```

查询指定bundleName应用的优先级分组，使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryAppGroup(bundleName: string): Promise<int>--><!--Device-usageStatistics-function queryAppGroup(bundleName: string): Promise<int>-End-->

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleName | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [10100002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10100002-获取应用分组信息失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [10000001](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-内存操作失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [10000002](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failed) |
| [10000003](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-系统服务操作失败) |
| [10000004](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-通信失败) |
| [10000005](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000005-应用未安装) |
| [10000006](../../apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |

## 示例

```TypeScript
// 有bundleName的promise
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

let bundleName: string = 'com.ohos.camera';
usageStatistics.queryAppGroup(bundleName).then((res: number) => {
  console.info('BUNDLE_ACTIVE queryAppGroup promise succeeded. result: ' + JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE queryAppGroup promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```
