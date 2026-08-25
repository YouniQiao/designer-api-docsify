# sendData

## Modules to Import

```TypeScript
import { proxyChannelManager } from 'kits/@kit.DistributedServiceKit';
```

## sendData

```TypeScript
function sendData(channelId: number, data: ArrayBuffer): Promise<void>
```

Sends data to the peer end. This API uses a promise to return the result. This is applicable to scenarios where the phone-side app sends instructions or data to the wearable device-side app through the proxy channel, such as sending configuration updates or notification messages. This method can be called to send data only after [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md) successfully opens a proxy channel. When the proxy channel is in an unavailable state (such as [ChannelState](arkts-distributedservice-proxychannelmanager-channelstate-e.md). CHANNEL_WAIT_RESUME, CHANNEL_EXCEPTION_SOFTWARE_FAILED, or CHANNEL_BR_NO_PAIRED), calling this method will fail. It is recommended to subscribe to the on('channelStateChange') event to monitor the channel state, pause data sending when the channel is unavailable, and resume sending after the channel recovers. Data is transmitted to the peer device through the established proxy channel via the Bluetooth BR link. The maximum data length is 4096 bytes. Exceeding this limit will return error code 32390103.

**Since:** 20

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| channelId | number | Yes |
| data | ArrayBuffer | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [32390004](../errorcode-proxyChannelManager.md#32390004-invalid-or-unavailable-channel-id) |
| [32390006](../errorcode-proxyChannelManager.md#32390006-parameter-verification-error) |
| [32390100](../errorcode-proxyChannelManager.md#32390100-internal-error) |
| [32390101](../errorcode-proxyChannelManager.md#32390101-call-restricted) |
| [32390103](../errorcode-proxyChannelManager.md#32390103-data-too-long) |
| [32390104](../errorcode-proxyChannelManager.md#32390104-data-sending-failed) |
