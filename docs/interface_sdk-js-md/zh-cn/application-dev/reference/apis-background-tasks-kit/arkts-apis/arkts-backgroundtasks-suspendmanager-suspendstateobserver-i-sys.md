# SuspendStateObserver（系统接口）

```TypeScript
export interface SuspendStateObserver
```

定义冻结状态变化的观察者。

**起始版本：** 26.1.0

<!--Device-suspendManager-export interface SuspendStateObserver--><!--Device-suspendManager-export interface SuspendStateObserver-End-->

**系统能力：** SystemCapability.Resourceschedule.BackgroundProcessManager

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { suspendManager } from '@kit.BackgroundTasksKit';
```

## onActive

```TypeScript
onActive(pidList: Array<number>, uid: number): void
```

当应用状态转换到活动状态时回调。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SuspendStateObserver-onActive(pidList: Array<int>, uid: int): void--><!--Device-SuspendStateObserver-onActive(pidList: Array<int>, uid: int): void-End-->

**系统能力：** SystemCapability.Resourceschedule.BackgroundProcessManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pidList | Array&lt;number&gt; | 是 | 转换为激活状态的uid对应的pid列表。 |
| uid | number | 是 | 应用转为激活状态的uid。 |

## onDoze

```TypeScript
onDoze(pidList: Array<number>, uid: number): void
```

当应用程序进入doze状态时回调。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SuspendStateObserver-onDoze(pidList: Array<int>, uid: int): void--><!--Device-SuspendStateObserver-onDoze(pidList: Array<int>, uid: int): void-End-->

**系统能力：** SystemCapability.Resourceschedule.BackgroundProcessManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pidList | Array&lt;number&gt; | 是 | 被doze的uid对应的pid列表。 |
| uid | number | 是 | 被doze的应用的uid。 |

## onFrozen

```TypeScript
onFrozen(pidList: Array<number>, uid: number): void
```

当应用程序完全冻结时回调。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SuspendStateObserver-onFrozen(pidList: Array<int>, uid: int): void--><!--Device-SuspendStateObserver-onFrozen(pidList: Array<int>, uid: int): void-End-->

**系统能力：** SystemCapability.Resourceschedule.BackgroundProcessManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pidList | Array&lt;number&gt; | 是 | 冻结的uid对应的pid列表。 |
| uid | number | 是 | 被冻结的应用uid |
