# offReceiveData

## offReceiveData

```TypeScript
function offReceiveData(channelId: number, callback?: Callback<DataInfo>): void
```

取消订阅数据接收事件，停止接收数据。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-proxyChannelManager-function offReceiveData(channelId: int, callback?: Callback<DataInfo>): void--><!--Device-proxyChannelManager-function offReceiveData(channelId: int, callback?: Callback<DataInfo>): void-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| channelId | number | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataInfo](arkts-distributedservice-proxychannelmanager-datainfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [32390006](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390006-参数错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [32390004](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390004-通道id非法或者不可用) |
| [32390100](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390100-内部异常) |
| [32390101](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390101-调用受限) |
