# onReceiveData

## Modules to Import

```TypeScript
import { proxyChannelManager } from 'proxyChannelManager';
```

## onReceiveData

```TypeScript
function onReceiveData(channelId: int, callback: Callback<DataInfo>): void
```

Subscribes to data receive events. This API uses an asynchronous callback to return the result. This is applicable to scenarios where the phone-side app needs to continuously receive data reported by the wearable device-side app, such as receiving data from the wearable device-side app. The proxy module receives data from the peer end based on the peer UUID configured when **openProxyChannel** is called, and passes the received wearable device-side app data to the subscriber through the callback. You must call [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md#openproxychannel) to successfully open a proxy channel before subscribing to data receive events. If you need to proxy-wake the phone-side app process to receive and process peer data, configure the **action** field as **action.ohos.pull.listener** in the **module.json5** file before use. After subscribing, call [off('receiveData')](arkts-distributedservice-proxychannelmanager-offreceivedata-f.md#offreceivedata) to unsubscribe and prevent the callback from being triggered continuously.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-proxyChannelManager-function onReceiveData(channelId: int, callback: Callback<DataInfo>): void--><!--Device-proxyChannelManager-function onReceiveData(channelId: int, callback: Callback<DataInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| channelId | int | Yes | Channel ID obtained when opening a proxy channel. The value range is 1 to 2147483647. Using an invalid or closed channelId returns error code 32390004. If the value is out of range, error code 3239 0006 is returned. The channelId takes effect only when the proxy channel is available, and becomes unavailable after the channel is closed or disconnected. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataInfo](arkts-distributedservice-proxychannelmanager-datainfo-i.md)&gt; | Yes | Callback invoked to return the data received through the proxy channel. The callback parameter is a [DataInfo](arkts-distributedservice-proxychannelmanager-datainfo-i.md#datainfo) object, which contains channelId ( channel ID) and data (received byte data). Data can be received only after a proxy channel is opened by calling openProxyChannel. If registered multiple times, only the last registration takes effect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [32390006](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390006-parameter-verification-error) | Parameter error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [32390004](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390004-invalid-or-unavailable-channel-id) | ChannelId is invalid or unavailable. |
| [32390100](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390100-internal-error) | Internal error. |
| [32390101](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390101-call-restricted) | Call is restricted. |

