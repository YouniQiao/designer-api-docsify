# on

## Modules to Import

```TypeScript
import { proxyChannelManager } from 'kits/@kit.DistributedServiceKit';
```

## on('receiveData')

```TypeScript
function on(type: 'receiveData', channelId: number, callback: Callback<DataInfo>): void
```

Subscribes to data receive events. This API uses an asynchronous callback to return the result. This is applicable to scenarios where the phone-side app needs to continuously receive data reported by the wearable device-side app, such as receiving data from the wearable device-side app. The proxy module receives data from the peer end based on the peer UUID configured when **openProxyChannel** is called, and passes the received wearable device-side app data to the subscriber through the callback. You must call [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md) to successfully open a proxy channel before subscribing to data receive events. If you need to proxy-wake the phone-side app process to receive and process peer data, configure the **action** field as **action.ohos.pull.listener** in the **module.json5** file before use. After subscribing, call off('receiveData') to unsubscribe and prevent the callback from being triggered continuously.

**Since:** 20

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'receiveData' | Yes |
| channelId | number | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataInfo](arkts-distributedservice-proxychannelmanager-datainfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [32390004](../errorcode-proxyChannelManager.md#32390004-invalid-or-unavailable-channel-id) |
| [32390006](../errorcode-proxyChannelManager.md#32390006-parameter-verification-error) |
| [32390100](../errorcode-proxyChannelManager.md#32390100-internal-error) |
| [32390101](../errorcode-proxyChannelManager.md#32390101-call-restricted) |


## on('channelStateChange')

```TypeScript
function on(type: 'channelStateChange', channelId: number, callback: Callback<ChannelStateInfo>): void
```

Subscribes to channel state events. This API uses an asynchronous callback to return the result. This is applicable to scenarios where the phone-side app needs to monitor the proxy channel connection state in real time, such as pausing data sending after detecting channel disconnection and automatically retrying services after channel recovery. The proxy module monitors Bluetooth BR link state changes in real time, and reports **ChannelStateInfo** through the callback when events such as connection recovery, abnormal disconnection, and pairing relationship deletion occur. You must call [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md) to successfully open a proxy channel before subscribing to channel state events. After subscribing, call off('channelStateChange') to unsubscribe and prevent the callback from being triggered continuously. After calling [closeProxyChannel](arkts-distributedservice-proxychannelmanager-closeproxychannel-f.md) to close the channel, the registered **channelStateChange** callback is automatically unsubscribed.

**Since:** 20

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'channelStateChange' | Yes |
| channelId | number | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ChannelStateInfo](arkts-distributedservice-proxychannelmanager-channelstateinfo-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [32390004](../errorcode-proxyChannelManager.md#32390004-invalid-or-unavailable-channel-id) |
| [32390006](../errorcode-proxyChannelManager.md#32390006-parameter-verification-error) |
| [32390100](../errorcode-proxyChannelManager.md#32390100-internal-error) |
| [32390101](../errorcode-proxyChannelManager.md#32390101-call-restricted) |
