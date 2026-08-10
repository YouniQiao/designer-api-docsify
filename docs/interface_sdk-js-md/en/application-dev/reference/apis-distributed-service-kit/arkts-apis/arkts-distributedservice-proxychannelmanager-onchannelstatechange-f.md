# onChannelStateChange

## Modules to Import

```TypeScript
import { proxyChannelManager } from 'kits/@kit.DistributedServiceKit';
```

## onChannelStateChange

```TypeScript
function onChannelStateChange(channelId: int, callback: Callback<ChannelStateInfo>): void
```

订阅通道状态事件，使用callback进行异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-proxyChannelManager-function onChannelStateChange(channelId: int, callback: Callback<ChannelStateInfo>): void--><!--Device-proxyChannelManager-function onChannelStateChange(channelId: int, callback: Callback<ChannelStateInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| channelId | int | Yes | 打开代理通道时获取的channelId。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChannelStateInfo&gt; | Yes | 回调函数，返回接收到的通道状态。多次注册callback， 最后一次注册的callback生效 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 32390006 | Parameter error. |
| 201 | Permission denied. |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |

