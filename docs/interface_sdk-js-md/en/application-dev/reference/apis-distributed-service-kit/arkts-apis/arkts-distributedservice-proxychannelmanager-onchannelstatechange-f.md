# onChannelStateChange

## Modules to Import

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
```

## onChannelStateChange

```TypeScript
function onChannelStateChange(channelId: int, callback: Callback<ChannelStateInfo>): void
```

Subscribes to channel state events. This API uses an asynchronous callback to return the result. This is applicable to scenarios where the phone-side app needs to monitor the proxy channel connection state in real time, such as pausing data sending after detecting channel disconnection and automatically retrying services after channel recovery. The proxy module monitors Bluetooth BR link state changes in real time, and reports **ChannelStateInfo** through the callback when events such as connection recovery, abnormal disconnection, and pairing relationship deletion occur. You must call [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md) to successfully open a proxy channel before subscribing to channel state events. After subscribing, call [off('channelStateChange')](arkts-distributedservice-proxychannelmanager-offreceivedata-f.md) to unsubscribe and prevent the callback from being triggered continuously. After calling [closeProxyChannel](arkts-distributedservice-proxychannelmanager-closeproxychannel-f.md) to close the channel, the registered **channelStateChange** callback is automatically unsubscribed.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-proxyChannelManager-function onChannelStateChange(channelId: int, callback: Callback<ChannelStateInfo>): void--><!--Device-proxyChannelManager-function onChannelStateChange(channelId: int, callback: Callback<ChannelStateInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| channelId | int | Yes | Channel ID obtained when opening the proxy channel. The value range is 1 to 214748364 7. Using an invalid or closed channelId returns error code 32390004, and exceeding the value range returns error code 32390006. The channelId takes effect only when the proxy channel is available, and becomes unavailable after the channel is closed or disconnected. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[ChannelStateInfo](arkts-distributedservice-proxychannelmanager-channelstateinfo-i.md)&gt; | Yes | Callback invoked to return the proxy channel state change information. The callback parameter is a [ChannelStateInfo](arkts-distributedservice-proxychannelmanager-channelstateinfo-i.md) object, which contains channelId (channel ID) and state (channel connection state). The proxy channel must be opened through openProxyChannel before receiving the channel state. If registered multiple times, only the last registered callback takes effect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [32390004](../errorcode-proxyChannelManager.md#32390004-invalid-or-unavailable-channel-id) | ChannelId is invalid or unavailable. |
| [32390006](../errorcode-proxyChannelManager.md#32390006-parameter-verification-error) | Parameter error. |
| [32390100](../errorcode-proxyChannelManager.md#32390100-internal-error) | Internal error. |
| [32390101](../errorcode-proxyChannelManager.md#32390101-call-restricted) | Call is restricted. |

