# queryBundleStateInfoByInterval（系统接口）

## 导入模块

```TypeScript
import { bundleState } from 'kits/@kit.BackgroundTasksKit';
```

## queryBundleStateInfoByInterval

```TypeScript
function queryBundleStateInfoByInterval(
    byInterval: IntervalType,
    begin: number,
    end: number,
    callback: AsyncCallback<Array<BundleStateInfo>>
  ): void
```

Queries usage information about each bundle within a specified period at a specified interval.

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| byInterval | [IntervalType](arkts-backgroundtasks-bundlestate-intervaltype-e.md) | 是 |
| begin | number | 是 |
| end | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[BundleStateInfo](arkts-backgroundtasks-bundlestate-bundlestateinfo-i.md)&gt;&gt; | 是 |


## queryBundleStateInfoByInterval

```TypeScript
function queryBundleStateInfoByInterval(
    byInterval: IntervalType,
    begin: number,
    end: number
  ): Promise<Array<BundleStateInfo>>
```

Queries usage information about each bundle within a specified period at a specified interval.

**起始版本：** 7

**废弃版本：** 9

**需要权限：** ohos.permission.BUNDLE_ACTIVE_INFO

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| byInterval | [IntervalType](arkts-backgroundtasks-bundlestate-intervaltype-e.md) | 是 |
| begin | number | 是 |
| end | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[BundleStateInfo](arkts-backgroundtasks-bundlestate-bundlestateinfo-i.md)&gt;&gt; |
