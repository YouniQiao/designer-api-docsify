# configEventPolicy

## 导入模块

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## configEventPolicy

```TypeScript
function configEventPolicy(policy: EventPolicy): Promise<void>
```

系统事件相关的配置策略设置方法，使用Promise方式作为异步回调。在同一生命周期中，可以通过配置策略设置系统事件相关的策略参数。

**起始版本：** 22

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| policy | [EventPolicy](arkts-performanceanalysis-hiappevent-eventpolicy-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
