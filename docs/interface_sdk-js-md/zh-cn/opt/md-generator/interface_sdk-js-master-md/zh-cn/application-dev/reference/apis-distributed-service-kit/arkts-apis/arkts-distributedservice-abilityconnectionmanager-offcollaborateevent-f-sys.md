# offCollaborateEvent（系统接口）

## offCollaborateEvent

```TypeScript
function offCollaborateEvent(sessionId: number,
        callback?: Callback<CollaborateEventInfo>): void
```

Unregisters collaborateEvent event.

**起始版本：** 23

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-abilityConnectionManager-function offCollaborateEvent(sessionId: int,        callback?: Callback<CollaborateEventInfo>): void--><!--Device-abilityConnectionManager-function offCollaborateEvent(sessionId: int,        callback?: Callback<CollaborateEventInfo>): void-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sessionId | number | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CollaborateEventInfo](arkts-distributedservice-abilityconnectionmanager-collaborateeventinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
