# closeProxyChannel

## Modules to Import

```TypeScript
import { proxyChannelManager } from 'kits/@kit.DistributedServiceKit';
```

## closeProxyChannel

```TypeScript
function closeProxyChannel(channelId: number): void
```

Closes an opened proxy channel. This is applicable to scenarios where the phone-side app no longer needs to communicate with the wearable device-side app, such as actively releasing channel resources after completing a data synchronization task. This method must be used in pair with [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md). Call this method to close the channel and release resources after use. After the channel is closed, the registered **receiveData** and **channelStateChange** callbacks are automatically unsubscribed, and data being transmitted is interrupted. Failure to close the proxy channel in a timely manner may cause channel resource leakage.

**Since:** 20

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| channelId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [32390004](../errorcode-proxyChannelManager.md#32390004-invalid-or-unavailable-channel-id) |
| [32390006](../errorcode-proxyChannelManager.md#32390006-parameter-verification-error) |
| [32390100](../errorcode-proxyChannelManager.md#32390100-internal-error) |
| [32390101](../errorcode-proxyChannelManager.md#32390101-call-restricted) |
