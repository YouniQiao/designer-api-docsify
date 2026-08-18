# onChannelStateChange

## Modules to Import

```TypeScript
```

## onChannelStateChange

```TypeScript
function onChannelStateChange(channelId: number, callback: Callback<ChannelStateInfo>): void
```

Subscribes to channel state events. This API uses an asynchronous callback to return the result. This is applicable to scenarios where the phone-side app needs to monitor the proxy channel connection state in real time, such as pausing data sending after detecting channel disconnection and automatically retrying services after channel recovery. The proxy module monitors Bluetooth BR link state changes in real time, and reports **ChannelStateInfo** through the callback when events such as connection recovery, abnormal disconnection, and pairing relationship deletion occur. You must call [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md#openproxychannel) to successfully open a proxy channel before subscribing to channel state events. After subscribing, call [off('channelStateChange')](arkts-distributedservice-proxychannelmanager-offreceivedata-f.md#offreceivedata) to unsubscribe and prevent the callback from being triggered continuously. After calling [closeProxyChannel](arkts-distributedservice-proxychannelmanager-closeproxychannel-f.md#closeproxychannel) to close the channel, the registered **channelStateChange** callback is automatically unsubscribed.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-proxyChannelManager-function onChannelStateChange(channelId: int, callback: Callback<ChannelStateInfo>): void--><!--Device-proxyChannelManager-function onChannelStateChange(channelId: int, callback: Callback<ChannelStateInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| channelId | number | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ChannelStateInfo](arkts-distributedservice-proxychannelmanager-channelstateinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [32390006](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390006-parameter-verification-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [32390004](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390004-invalid-or-unavailable-channel-id) |
| [32390100](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390100-internal-error) |
| [32390101](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390101-call-restricted) |
