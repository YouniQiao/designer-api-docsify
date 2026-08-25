# RunningLock

阻止系统睡眠或使能接近光控制亮灭屏的锁，不同的锁类型具有不同的功能，详见[RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md)。 需结合[create](arkts-basicservices-runninglock-create-f.md)创建锁、[hold](#hold)持锁、[unhold](#unhold)释放锁使用。具体使用方法见示例。

**起始版本：** 7

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

## 导入模块

```TypeScript
import { runningLock } from 'kits/@kit.BasicServicesKit';
```

## hold

```TypeScript
hold(timeout: number): void
```

锁定和持有RunningLock。适用于应用需要在后台持续运行（如后台下载、长时间定位追踪等）时阻止系统睡眠的场景或通话时需要接近光控制亮灭屏的场景等。调用此方法后， 必须在使用完毕时调用unhold()释放锁，或者在调用时设置超时释放时间由系统自动释放，与unhold()方法配对使用。未释放锁会导致阻止睡眠或者控制亮灭屏功能持续生效。

**起始版本：** 9

**需要权限：** ohos.permission.RUNNING_LOCK

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeout | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## isHolding

```TypeScript
isHolding(): boolean
```

查询当前RunningLock是持有状态还是释放状态。

**起始版本：** 9

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## isUsed

```TypeScript
isUsed(): boolean
```

查询当前RunningLock是持有状态还是释放状态。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [isHolding](#isholding)

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 |
| --- |
| boolean |

## lock

```TypeScript
lock(timeout: number): void
```

持有RunningLock锁。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [hold](#hold)

**需要权限：** ohos.permission.RUNNING_LOCK

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| timeout | number | 是 |

## unhold

```TypeScript
unhold(): void
```

释放RunningLock锁。此方法与hold()配对使用，在调用hold()锁定后调用此方法释放锁。

**起始版本：** 9

**需要权限：** ohos.permission.RUNNING_LOCK

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## unlock

```TypeScript
unlock(): void
```

释放RunningLock锁。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [unhold](#unhold)

**需要权限：** ohos.permission.RUNNING_LOCK

**系统能力：** SystemCapability.PowerManager.PowerManager.Core
