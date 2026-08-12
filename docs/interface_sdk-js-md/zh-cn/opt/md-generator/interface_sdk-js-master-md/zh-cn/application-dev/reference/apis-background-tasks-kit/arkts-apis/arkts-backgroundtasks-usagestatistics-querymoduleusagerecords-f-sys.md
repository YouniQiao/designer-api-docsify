# queryModuleUsageRecords（系统接口）

## queryModuleUsageRecords

```TypeScript
function queryModuleUsageRecords(maxNum: number, callback: AsyncCallback<Array<HapModuleInfo>>): void
```

根据设置的maxNum，查询FA模型下各应用不用Hap包的使用记录。若Hap包中存在FA卡片，使用信息中也包含卡片信息。使用Callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryModuleUsageRecords(maxNum: int, callback: AsyncCallback<Array<HapModuleInfo>>): void--><!--Device-usageStatistics-function queryModuleUsageRecords(maxNum: int, callback: AsyncCallback<Array<HapModuleInfo>>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| maxNum | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;HapModuleInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [10000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-内存操作失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [10000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failed) |
| [10000003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-系统服务操作失败) |
| [10000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-通信失败) |
| [10000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |
| [10000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-时间操作失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

usageStatistics.queryModuleUsageRecords(1000, (err: BusinessError, res: Array<usageStatistics.HapModuleInfo>) => {
  if(err) {
    console.error('BUNDLE_ACTIVE queryModuleUsageRecords callback failed. code is: ' + err.code + ',message is: ' + err.message);
  } else {
    console.info('BUNDLE_ACTIVE queryModuleUsageRecords callback succeeded.');
    for (let i = 0; i < res.length; i++) {
      console.info('BUNDLE_ACTIVE queryModuleUsageRecords callback number : ' + (i + 1));
      console.info('BUNDLE_ACTIVE queryModuleUsageRecords callback result ' + JSON.stringify(res[i]));
    }
  }
});
```


## queryModuleUsageRecords

```TypeScript
function queryModuleUsageRecords(maxNum: number): Promise<Array<HapModuleInfo>>
```

根据设置的maxNum，查询FA模型下各应用不用Hap包的使用记录。若Hap包中存在FA卡片，使用信息中也包含卡片信息。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryModuleUsageRecords(maxNum: int): Promise<Array<HapModuleInfo>>--><!--Device-usageStatistics-function queryModuleUsageRecords(maxNum: int): Promise<Array<HapModuleInfo>>-End-->

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| maxNum | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;HapModuleInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [10000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-内存操作失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [10000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failed) |
| [10000003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-系统服务操作失败) |
| [10000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-通信失败) |
| [10000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |
| [10000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-时间操作失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

usageStatistics.queryModuleUsageRecords(1000).then((res: Array<usageStatistics.HapModuleInfo>) => {
  console.info('BUNDLE_ACTIVE queryModuleUsageRecords promise succeeded');
  for (let i = 0; i < res.length; i++) {
    console.info('BUNDLE_ACTIVE queryModuleUsageRecords promise number : ' + (i + 1));
    console.info('BUNDLE_ACTIVE queryModuleUsageRecords promise result ' + JSON.stringify(res[i]));
  }
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE queryModuleUsageRecords promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```


## queryModuleUsageRecords

```TypeScript
function queryModuleUsageRecords(callback: AsyncCallback<Array<HapModuleInfo>>): void
```

查询FA模型下各应用不用Hap包的使用记录（不超过1000条）。若Hap包中存在FA卡片，使用信息中也包含卡片信息。使用CallBack异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryModuleUsageRecords(callback: AsyncCallback<Array<HapModuleInfo>>): void--><!--Device-usageStatistics-function queryModuleUsageRecords(callback: AsyncCallback<Array<HapModuleInfo>>): void-End-->

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;HapModuleInfo&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [10000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-内存操作失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [10000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failed) |
| [10000003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-系统服务操作失败) |
| [10000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-通信失败) |
| [10000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |
| [10000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-时间操作失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

usageStatistics.queryModuleUsageRecords((err: BusinessError, res: Array<usageStatistics.HapModuleInfo>) => {
  if(err) {
    console.error('BUNDLE_ACTIVE queryModuleUsageRecords callback failed. code is: ' + err.code + ',message is: ' + err.message);
  } else {
    console.info('BUNDLE_ACTIVE queryModuleUsageRecords callback succeeded.');
    for (let i = 0; i < res.length; i++) {
      console.info('BUNDLE_ACTIVE queryModuleUsageRecords callback number : ' + (i + 1));
      console.info('BUNDLE_ACTIVE queryModuleUsageRecords callback result ' + JSON.stringify(res[i]));
    }
  }
});
```


## queryModuleUsageRecords

```TypeScript
function queryModuleUsageRecords(): Promise<Array<HapModuleInfo>>
```

查询FA模型下各应用不用Hap包的使用记录（不超过1000条）。若Hap包中存在FA卡片，使用信息中也包含卡片信息。使用Promise异步回调。

使用Promise形式返回不超过1000条FA使用记录，FA使用记录由近及远排序。

**起始版本：** 9

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

<!--Device-usageStatistics-function queryModuleUsageRecords(): Promise<Array<HapModuleInfo>>--><!--Device-usageStatistics-function queryModuleUsageRecords(): Promise<Array<HapModuleInfo>>-End-->

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;HapModuleInfo & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [10000001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000001-内存操作失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
| [10000002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000002-ipc-parcel-write-failed) |
| [10000003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000003-系统服务操作失败) |
| [10000004](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000004-通信失败) |
| [10000006](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000006-获取应用信息失败) |
| [10000007](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-backgroundtasks-kit/errorcode-DeviceUsageStatistics.md#10000007-时间操作失败) |

## 示例

```TypeScript
// 无maxNum参数调用方式
import { BusinessError } from '@kit.BasicServicesKit';
import { usageStatistics } from '@kit.BackgroundTasksKit';

usageStatistics.queryModuleUsageRecords().then((res: Array<usageStatistics.HapModuleInfo>) => {
  console.info('BUNDLE_ACTIVE queryModuleUsageRecords promise succeeded');
  for (let i = 0; i < res.length; i++) {
    console.info('BUNDLE_ACTIVE queryModuleUsageRecords promise number : ' + (i + 1));
    console.info('BUNDLE_ACTIVE queryModuleUsageRecords promise result ' + JSON.stringify(res[i]));
  }
}).catch((err: BusinessError) => {
  console.error('BUNDLE_ACTIVE queryModuleUsageRecords promise failed. code is: ' + err.code + ',message is: ' + err.message);
});
```
