# queryBundleStateInfos（系统接口）

## 导入模块

```TypeScript
import { bundleState } from 'kits/@kit.BackgroundTasksKit';
```

## queryBundleStateInfos

```TypeScript
function queryBundleStateInfos(begin: number, end: number, callback: AsyncCallback<BundleActiveInfoResponse>): void
```

Queries usage information about each bundle within a specified period.This method queries usage information at the BY_OPTIMIZED interval by default.

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | number | 是 |
| end | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[BundleActiveInfoResponse](arkts-backgroundtasks-bundlestate-bundleactiveinforesponse-i.md)&gt; | 是 |


## queryBundleStateInfos

```TypeScript
function queryBundleStateInfos(begin: number, end: number): Promise<BundleActiveInfoResponse>
```

Queries usage information about each bundle within a specified period.This method queries usage information at the BY_OPTIMIZED interval by default.

**起始版本：** 7

**废弃版本：** 9

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
| Promise&lt;[BundleActiveInfoResponse](arkts-backgroundtasks-bundlestate-bundleactiveinforesponse-i.md)&gt; |
