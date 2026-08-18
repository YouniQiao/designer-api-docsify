# offChannelStateChange

## 导入模块

```TypeScript
```

## offChannelStateChange

```TypeScript
function offChannelStateChange(channelId: number, callback?: Callback<ChannelStateInfo>): void
```

取消订阅通道状态事件。适用于手机侧应用不再需要监听代理通道连接状态变化的场景，例如用户退出相关业务页面、完成数据传输流程后等。必须在 [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md#openproxychannel)成功打开代理通道后才能取消订阅。此方法必须与 [on('channelStateChange')](arkts-distributedservice-proxychannelmanager-onreceivedata-f.md#onreceivedata) 配对使用，用于取消之前通过on('channelStateChange')注册的通道状态回调。

**起始版本：** 23

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-proxyChannelManager-function offChannelStateChange(channelId: int, callback?: Callback<ChannelStateInfo>): void--><!--Device-proxyChannelManager-function offChannelStateChange(channelId: int, callback?: Callback<ChannelStateInfo>): void-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| channelId | number | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ChannelStateInfo](arkts-distributedservice-proxychannelmanager-channelstateinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [32390006](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390006-参数错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [32390004](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390004-通道id非法或者不可用) |
| [32390100](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390100-内部异常) |
| [32390101](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390101-调用受限) |
