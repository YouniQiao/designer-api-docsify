# onChannelStateChange

## 导入模块

```TypeScript
import { proxyChannelManager } from 'kits/@kit.DistributedServiceKit';
```

## onChannelStateChange

```TypeScript
function onChannelStateChange(channelId: int, callback: Callback<ChannelStateInfo>): void
```

订阅通道状态事件，使用callback进行异步回调。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-proxyChannelManager-function onChannelStateChange(channelId: int, callback: Callback<ChannelStateInfo>): void--><!--Device-proxyChannelManager-function onChannelStateChange(channelId: int, callback: Callback<ChannelStateInfo>): void-End-->

**系统能力：** SystemCapability.DistributedSched.AppCollaboration

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| channelId | int | 是 | 打开代理通道时获取的channelId。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChannelStateInfo&gt; | 是 | 回调函数，返回接收到的通道状态。多次注册callback， 最后一次注册的callback生效 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 32390006 | Parameter error. |
| 201 | Permission denied. |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |

