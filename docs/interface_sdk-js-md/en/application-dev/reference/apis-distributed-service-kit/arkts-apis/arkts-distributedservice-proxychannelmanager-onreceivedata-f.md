# onReceiveData

## Modules to Import

```TypeScript
import { proxyChannelManager } from 'kits/@kit.DistributedServiceKit';
```

## onReceiveData

```TypeScript
function onReceiveData(channelId: int, callback: Callback<DataInfo>): void
```

订阅数据接收事件，使用异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-proxyChannelManager-function onReceiveData(channelId: int, callback: Callback<DataInfo>): void--><!--Device-proxyChannelManager-function onReceiveData(channelId: int, callback: Callback<DataInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| channelId | int | Yes | 打开代理通道时获取的channelId。 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataInfo&gt; | Yes | 回调函数，返回接收到的数据。多次注册回调函数，最后一次注册的回调函数生效。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 32390006 | Parameter error. |
| 201 | Permission denied. |
| 32390004 | ChannelId is invalid or unavailable. |
| 32390100 | Internal error. |
| 32390101 | Call is restricted. |

