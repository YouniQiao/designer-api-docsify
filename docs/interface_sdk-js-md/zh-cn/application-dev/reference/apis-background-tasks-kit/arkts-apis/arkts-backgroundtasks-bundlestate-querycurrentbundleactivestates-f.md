# queryCurrentBundleActiveStates

## 导入模块

```TypeScript
import { bundleState } from 'kits/@kit.BackgroundTasksKit';
```

## queryCurrentBundleActiveStates

```TypeScript
function queryCurrentBundleActiveStates(
    begin: number,
    end: number,
    callback: AsyncCallback<Array<BundleActiveState>>
  ): void
```

Queries state data of the current bundle within a specified period.

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | number | 是 |
| end | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[BundleActiveState](arkts-backgroundtasks-bundlestate-bundleactivestate-i.md)&gt;&gt; | 是 |


## queryCurrentBundleActiveStates

```TypeScript
function queryCurrentBundleActiveStates(begin: number, end: number): Promise<Array<BundleActiveState>>
```

Queries state data of the current bundle within a specified period.

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.App

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| begin | number | 是 |
| end | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[BundleActiveState](arkts-backgroundtasks-bundlestate-bundleactivestate-i.md)&gt;&gt; |
