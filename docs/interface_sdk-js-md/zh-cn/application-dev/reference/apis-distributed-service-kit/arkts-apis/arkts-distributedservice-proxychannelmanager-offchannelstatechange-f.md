# offChannelStateChange

## 导入模块

```TypeScript
import { proxyChannelManager } from 'kits/@kit.DistributedServiceKit';
```

## offChannelStateChange

```TypeScript
function offChannelStateChange(channelId: int, callback?: Callback<ChannelStateInfo>): void
```

取消订阅通道状态事件。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-proxyChannelManager-function offChannelStateChange(channelId: int, callback?: Callback<ChannelStateInfo>): void--><!--Device-proxyChannelManager-function offChannelStateChange(channelId: int, callback?: Callback<ChannelStateInfo>): void-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| channelId | int | 是 | 打开代理通道时获取的channelId。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChannelStateInfo&gt; | 否 | 注册的回调函数。如果为空、undefined、null， 则取消订阅所有的数据接收事件。如果不为空，传入最后一次注册的回调函数。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 32390006 | Parameter error. |
| 201 | Permission denied. |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |

