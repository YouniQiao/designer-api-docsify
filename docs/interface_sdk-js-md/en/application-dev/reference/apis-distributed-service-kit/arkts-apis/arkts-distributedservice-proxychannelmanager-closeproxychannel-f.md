# closeProxyChannel

## Modules to Import

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
```

## closeProxyChannel

```TypeScript
function closeProxyChannel(channelId: int): void
```

Closes an opened proxy channel. This is applicable to scenarios where the phone-side app no longer needs to communicate with the wearable device-side app, such as actively releasing channel resources after completing a data synchronization task. This method must be used in pair with [openProxyChannel](arkts-distributedservice-proxychannelmanager-openproxychannel-f.md). Call this method to close the channel and release resources after use. After the channel is closed, the registered **receiveData** and **channelStateChange** callbacks are automatically unsubscribed, and data being transmitted is interrupted. Failure to close the proxy channel in a timely manner may cause channel resource leakage.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| channelId | ArkTS-Dyn: number<br>ArkTS-Sta：int | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [32390004](../errorcode-proxyChannelManager.md#32390004-invalid-or-unavailable-channel-id) |
| [32390006](../errorcode-proxyChannelManager.md#32390006-parameter-verification-error) |
| [32390100](../errorcode-proxyChannelManager.md#32390100-internal-error) |
| [32390101](../errorcode-proxyChannelManager.md#32390101-call-restricted) |

**Examples**

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button ('Test')
        .onClick(() => {
          // The following sample code uses try/catch as an example.
          try {
            proxyChannelManager.closeProxyChannel(1); // Assume that the channel ID is 1.
          } catch (err) {
            let error = err as BusinessError;
            console.error(`getErr: ${error.code} ${error.message}`);
            // If code:undefined message:"Cannot read property closeProxyChannel of undefined" is displayed, this API is not supported in the current image.
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
