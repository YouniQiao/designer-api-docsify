# create

## create

```TypeScript
function create(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void
```

创建RunningLock锁。使用callback异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.RUNNING_LOCK

<!--Device-runningLock-function create(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void--><!--Device-runningLock-function create(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| type | [RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md) | 是 |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;RunningLock&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: BusinessError, lock: runningLock.RunningLock) => {
    if (err) {
        console.error(`Failed to create running lock. Code: ${err.code}, message: ${err.message}`);
    } else {
        console.info('created running lock: ' + lock); // 创建并保存锁对象后，需要结合hold、unhold方法使用
    }
});
```


## create

```TypeScript
function create(name: string, type: RunningLockType): Promise<RunningLock>
```

创建RunningLock锁。使用Promise异步回调。

**起始版本：** 9

**需要权限：** ohos.permission.RUNNING_LOCK

<!--Device-runningLock-function create(name: string, type: RunningLockType): Promise<RunningLock>--><!--Device-runningLock-function create(name: string, type: RunningLockType): Promise<RunningLock>-End-->

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |
| type | [RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;RunningLock&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

```TypeScript
runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL)
.then((lock: runningLock.RunningLock) => {
    console.info('created running lock: ' + lock); // 创建并保存锁对象后，需要结合hold、unhold方法使用
})
.catch((err: BusinessError) => {
    console.error(`Failed to create running lock. Code: ${err.code}, message: ${err.message}`);
});
```
