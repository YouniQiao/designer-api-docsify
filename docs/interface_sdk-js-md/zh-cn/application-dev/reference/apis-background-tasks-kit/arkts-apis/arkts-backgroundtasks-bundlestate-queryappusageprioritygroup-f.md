# queryAppUsagePriorityGroup

## 导入模块

```TypeScript
import { bundleState } from 'kits/@kit.BackgroundTasksKit';
```

## queryAppUsagePriorityGroup

```TypeScript
function queryAppUsagePriorityGroup(callback: AsyncCallback<number>): void
```

Queries the usage priority group of the calling application.The priority defined in a priority group restricts the resource usage of an application, for example, restricting the running of background tasks.

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |


## queryAppUsagePriorityGroup

```TypeScript
function queryAppUsagePriorityGroup(): Promise<number>
```

Queries the usage priority group of the calling application.The priority defined in a priority group restricts the resource usage of an application, for example, restricting the running of background tasks.

**起始版本：** 7

**废弃版本：** 9

**系统能力：** SystemCapability.ResourceSchedule.UsageStatistics.AppGroup

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |
