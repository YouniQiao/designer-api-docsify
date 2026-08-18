# sendData

## Modules to Import

```TypeScript
```

## sendData

```TypeScript
function sendData(channelId: number, data: ArrayBuffer): Promise<void>
```

Sends data to the peer end. This API uses a promise to return the result. This is applicable to scenarios where the phone-side app sends instructions or data to the wearable device-side app through the proxy channel, such as sending configuration updates or notification messages. This method can be called to send data only after [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md#openproxychannel) successfully opens a proxy channel. When the proxy channel is in an unavailable state (such as [ChannelState](arkts-distributedservice-proxychannelmanager-channelstate-e.md#channelstate). CHANNEL_WAIT_RESUME, CHANNEL_EXCEPTION_SOFTWARE_FAILED, or CHANNEL_BR_NO_PAIRED), calling this method will fail. It is recommended to subscribe to the [on('channelStateChange')](arkts-distributedservice-proxychannelmanager-onreceivedata-f.md#onreceivedata) event to monitor the channel state, pause data sending when the channel is unavailable, and resume sending after the channel recovers. Data is transmitted to the peer device through the established proxy channel via the Bluetooth BR link. The maximum data length is 4096 bytes. Exceeding this limit will return error code 32390103.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-proxyChannelManager-function sendData(channelId: int, data: ArrayBuffer): Promise<void>--><!--Device-proxyChannelManager-function sendData(channelId: int, data: ArrayBuffer): Promise<void>-End-->

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
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [32390104](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390104-data-sending-failed) |
| [32390006](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390006-parameter-verification-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [32390103](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390103-data-too-long) |
| [32390004](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390004-invalid-or-unavailable-channel-id) |
| [32390100](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390100-internal-error) |
| [32390101](../../apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390101-call-restricted) |

**Examples**

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button('Test')
        .onClick(() => {
          const data = new ArrayBuffer(10); // Create an ArrayBuffer with a length of 10.
          try {
            proxyChannelManager.sendData(channelId, data) // Obtain channelId from the promise returned by openProxyChannel.
              .then(() => {
              })
              .catch((error: BusinessError) => {
                console.error(`Failed to send data. Code: ${error.code}, message: ${error.message}`);
              });
          } catch (err) {
            let error = err as BusinessError;
            console.error(`Failed to send data. Code: ${error.code}, message: ${error.message}`);
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
