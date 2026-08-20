# offReceiveData

## Modules to Import

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
```

## offReceiveData

```TypeScript
function offReceiveData(channelId: int, callback?: Callback<DataInfo>): void
```

Unsubscribes from data receive events and no longer receives data through the callback. This is applicable to scenarios where the phone-side app no longer needs to receive data from the wearable device-side app, such as when the user switches to another functional module. You must call [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md) to successfully open a proxy channel before unsubscribing. This method must be used in pair with [on('receiveData')](arkts-distributedservice-proxychannelmanager-onreceivedata-f.md) to cancel the data receive callback previously registered through **on('receiveData')**.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-proxyChannelManager-function offReceiveData(channelId: int, callback?: Callback<DataInfo>): void--><!--Device-proxyChannelManager-function offReceiveData(channelId: int, callback?: Callback<DataInfo>): void-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| channelId | int | Yes | Channel ID obtained when opening the proxy channel, with a value range of 1 to 214748 3647. Using an invalid or closed channelId returns error code 32390004, and exceeding the value range returns error code 32390006. The channelId takes effect only when the proxy channel is available, and becomes unavailable after the channel is closed or disconnected. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[DataInfo](arkts-distributedservice-proxychannelmanager-datainfo-i.md)&gt; | No | Callback for the data receive event. Default behavior: when this parameter is not passed, all data receive event subscriptions are unsubscribed. The callback passed must be the last one registered via the on method to unsubscribe that callback; passing any other callback will not take effect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [32390004](../errorcode-proxyChannelManager.md#32390004-invalid-or-unavailable-channel-id) | ChannelId is invalid or unavailable. |
| [32390006](../errorcode-proxyChannelManager.md#32390006-parameter-verification-error) | Parameter error. |
| [32390100](../errorcode-proxyChannelManager.md#32390100-internal-error) | Internal error. |
| [32390101](../errorcode-proxyChannelManager.md#32390101-call-restricted) | Call is restricted. |

