# create

## 导入模块

```TypeScript
import { runningLock } from 'kits/@kit.BasicServicesKit';
```

## create

```TypeScript
function create(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void
```

创建RunningLock锁对象。使用callback异步回调。创建锁对象后，需调用hold()方法锁定和持有该锁，才能使锁功能生效。

**起始版本：** 9

**需要权限：** ohos.permission.RUNNING_LOCK

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| type | [RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[RunningLock](arkts-basicservices-runninglock-runninglock-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## create

```TypeScript
function create(name: string, type: RunningLockType): Promise<RunningLock>
```

创建RunningLock锁对象。使用Promise异步回调。创建锁对象后，需调用hold()方法锁定和持有该锁，才能使锁功能生效。

**起始版本：** 9

**需要权限：** ohos.permission.RUNNING_LOCK

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| type | [RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[RunningLock](arkts-basicservices-runninglock-runninglock-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
