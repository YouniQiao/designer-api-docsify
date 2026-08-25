# queryBundleActiveStates（系统接口）

## 导入模块

```TypeScript
import { bundleState } from 'kits/@kit.BackgroundTasksKit';
```

## queryBundleActiveStates

```TypeScript
function queryBundleActiveStates(begin: number, end: number, callback: AsyncCallback<Array<BundleActiveState>>): void
```

Queries state data of all bundles within a specified period identified by the start and end time.

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
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[BundleActiveState](arkts-backgroundtasks-bundlestate-bundleactivestate-i.md)&gt;&gt; | 是 |


## queryBundleActiveStates

```TypeScript
function queryBundleActiveStates(begin: number, end: number): Promise<Array<BundleActiveState>>
```

Queries state data of all bundles within a specified period identified by the start and end time.

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
| Promise&lt;Array&lt;[BundleActiveState](arkts-backgroundtasks-bundlestate-bundleactivestate-i.md)&gt;&gt; |
