# openProxyChannel

## Modules to Import

```TypeScript
import { proxyChannelManager } from '@kit.DistributedServiceKit';
```

## openProxyChannel

```TypeScript
function openProxyChannel(channelInfo: ChannelInfo): Promise<number>
```

Opens a proxy channel. This API uses a promise to return the result.

**Since:** 20

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-proxyChannelManager-function openProxyChannel(channelInfo: ChannelInfo): Promise<int>--><!--Device-proxyChannelManager-function openProxyChannel(channelInfo: ChannelInfo): Promise<int>-End-->

**System capability:** SystemCapability.DistributedSched.AppCollaboration

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| channelInfo | [ChannelInfo](arkts-distributedservice-proxychannelmanager-channelinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [32390006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390006-parameter-verification-error) |
| [32390102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390102-operation-failed-or-connection-timed-out) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [32390100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390100-internal-error) |
| [32390101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390101-call-restricted) |
| [32390002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390002-bluetooth-unpaired) |
| [32390001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-distributedservice-kit/errorcode-proxyChannelManager.md#32390001-bluetooth-disabled) |

## Examples

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
          let channelInfo: proxyChannelManager.ChannelInfo = {
            linkType: proxyChannelManager.LinkType.LINK_BR,
            peerDevAddr: 'xx:xx:xx:xx:xx:xx', // Bluetooth MAC address of the wearable device.
            peerUuid: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', // UUID listened on by the wearable side.
          };
          // The following sample code uses try/catch as an example.
          try {
            proxyChannelManager.openProxyChannel(channelInfo)
              .then((channelId: number) => {
                // Obtain the channel ID.
              })
              .catch((error: BusinessError) => {
                console.error(`Failed to open proxy channel. Code: ${error.code}, message: ${error.message}`);
              });
          } catch (err) {
            let error = err as BusinessError;
            console.error(`Failed to open proxy channel. Code: ${error.code}, message: ${error.message}`);
            // If the returned error.code is undefined and error.message is "Cannot read property openProxyChannel of undefined", the current image does not support this API.
          }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
