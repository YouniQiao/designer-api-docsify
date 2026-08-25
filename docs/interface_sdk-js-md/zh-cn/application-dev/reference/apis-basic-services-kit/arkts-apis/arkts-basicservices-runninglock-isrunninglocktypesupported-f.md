# isRunningLockTypeSupported

## 导入模块

```TypeScript
import { runningLock } from 'kits/@kit.BasicServicesKit';
```

## isRunningLockTypeSupported

```TypeScript
function isRunningLockTypeSupported(type: RunningLockType, callback: AsyncCallback<boolean>): void
```

查询系统是否支持该类型的锁。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isSupported](arkts-basicservices-runninglock-issupported-f.md)

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## isRunningLockTypeSupported

```TypeScript
function isRunningLockTypeSupported(type: RunningLockType): Promise<boolean>
```

查询系统是否支持该类型的锁。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isSupported](arkts-basicservices-runninglock-issupported-f.md)

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |
