# onReceiveData

## Modules to Import

```TypeScript
import { proxyChannelManager } from 'kits/@kit.DistributedServiceKit';
```

## onReceiveData

```TypeScript
function onReceiveData(channelId: int, callback: Callback<DataInfo>): void
```

Subscribes to data receiving events. This API returns the result asynchronously through a callback.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-proxyChannelManager-function onReceiveData(channelId: int, callback: Callback<DataInfo>): void--><!--Device-proxyChannelManager-function onReceiveData(channelId: int, callback: Callback<DataInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| channelId | int | Yes | Channel ID obtained when the proxy channel is opened. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataInfo&gt; | Yes | Callback used to return the received data. If the callback function is registered multiple times, only the last registered one takes effect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [32390006](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390006-parameter-verification-error) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [32390004](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390004-invalid-or-unavailable-channel-id) | ChannelId is invalid or unavailable. |
| [32390100](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390100-internal-error) | Internal error. |
| [32390101](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390101-call-restricted) | Call is restricted. |

