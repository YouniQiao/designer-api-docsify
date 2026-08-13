# offDistributedSessionChange（系统接口）

## offDistributedSessionChange

```TypeScript
function offDistributedSessionChange(distributedSessionType: DistributedSessionType, callback?: Callback<Array<AVSessionController>>): void
```

Unregister distributed session changed callback

**起始版本：** 23

**废弃版本：** -1

<!--Device-avSession-function offDistributedSessionChange(distributedSessionType: DistributedSessionType, callback?: Callback<Array<AVSessionController>>): void--><!--Device-avSession-function offDistributedSessionChange(distributedSessionType: DistributedSessionType, callback?: Callback<Array<AVSessionController>>): void-End-->

**系统能力：** SystemCapability.Multimedia.AVSession.Manager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| distributedSessionType | [DistributedSessionType](arkts-avsession-avsession-distributedsessiontype-e-sys.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[AVSessionController](arkts-avsession-avsession-avsessioncontroller-i.md)&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [6600101](../errorcode-avsession.md#6600101-会话服务端异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
