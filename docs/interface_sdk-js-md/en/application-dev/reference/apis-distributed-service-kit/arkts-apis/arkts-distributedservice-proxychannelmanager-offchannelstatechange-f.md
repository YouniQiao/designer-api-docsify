# offChannelStateChange

## Modules to Import

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
```

## offChannelStateChange

```TypeScript
function offChannelStateChange(channelId: int, callback?: Callback<ChannelStateInfo>): void
```

Unsubscribes from channel state events. This is applicable to scenarios where the phone-side app no longer needs to listen for proxy channel connection state changes, such as when the user exits the relevant service page or completes the data transmission process. You must call [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md) to successfully open a proxy channel before unsubscribing. This method must be used in pair with on('channelStateChange') to cancel the channel state callback previously registered through **on('channelStateChange')**.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-proxyChannelManager-function offChannelStateChange(channelId: int, callback?: Callback<ChannelStateInfo>): void--><!--Device-proxyChannelManager-function offChannelStateChange(channelId: int, callback?: Callback<ChannelStateInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| channelId | int | Yes | Channel ID obtained when opening a proxy channel. Value range: 1 to 2147483647. Using an invalid or closed channelId returns error code 32390004, and exceeding the value range returns error code 32 390006. The channelId takes effect only when the proxy channel is available and becomes unavailable after the channel is closed or disconnected. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ChannelStateInfo](arkts-distributedservice-proxychannelmanager-channelstateinfo-i.md)&gt; | No | Registered callback. Default behavior: if this parameter is not passed, all channel state event subscriptions are unsubscribed. The callback passed must be the one last registered through the **on** method to unsubscribe from that callback; passing any other callback will not take effect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [32390006](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390006-parameter-verification-error) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [32390004](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390004-invalid-or-unavailable-channel-id) | ChannelId is invalid or unavailable. |
| [32390100](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390100-internal-error) | Internal error. |
| [32390101](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390101-call-restricted) | Call is restricted. |

