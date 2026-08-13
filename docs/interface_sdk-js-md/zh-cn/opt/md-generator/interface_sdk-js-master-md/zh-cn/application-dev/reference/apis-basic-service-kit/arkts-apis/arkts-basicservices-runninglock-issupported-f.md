# isSupported

## isSupported

```TypeScript
function isSupported(type: RunningLockType): boolean
```

查询系统是否支持该类型的锁。

**起始版本：** 23

**废弃版本：** -1

<!--Device-runningLock-function isSupported(type: RunningLockType): boolean--><!--Device-runningLock-function isSupported(type: RunningLockType): boolean-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## 示例

```TypeScript
try {
    let isSupported = runningLock.isSupported(runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL);
    console.info('PROXIMITY_SCREEN_CONTROL type supported: ' + isSupported);
} catch (err) {
    console.error(`Failed to check supported. Code: ${err.code}, message: ${err.message}`);
}
```
