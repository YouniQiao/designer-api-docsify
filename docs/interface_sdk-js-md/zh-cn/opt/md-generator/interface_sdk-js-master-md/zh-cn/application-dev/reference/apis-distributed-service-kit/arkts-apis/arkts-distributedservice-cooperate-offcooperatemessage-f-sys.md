# offCooperateMessage（系统接口）

## offCooperateMessage

```TypeScript
function offCooperateMessage(callback?: Callback<CooperateMessage>): void
```

Disables listening for screen hopping status change events.

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.COOPERATE_MANAGER

<!--Device-cooperate-function offCooperateMessage(callback?: Callback<CooperateMessage>): void--><!--Device-cooperate-function offCooperateMessage(callback?: Callback<CooperateMessage>): void-End-->

**系统能力：** SystemCapability.Msdp.DeviceStatus.Cooperate

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CooperateMessage](arkts-distributedservice-cooperate-cooperatemessage-i-sys.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
