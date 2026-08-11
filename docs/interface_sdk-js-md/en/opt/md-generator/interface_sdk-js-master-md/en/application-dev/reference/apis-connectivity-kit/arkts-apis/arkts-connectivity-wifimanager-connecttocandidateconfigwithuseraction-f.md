# connectToCandidateConfigWithUserAction

## Modules to Import

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## connectToCandidateConfigWithUserAction

```TypeScript
function connectToCandidateConfigWithUserAction(networkId: number): Promise<void>
```

Connect to a specified candidate hotspot by networkId, and wait for user respond result.Only the configuration which is added by ourself is allowed to be connected.This method connect to a configuration at a time.The app must be in the foreground.

**Since:** 20

**Required permissions:** ohos.permission.SET_WIFI_INFO

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-wifiManager-function connectToCandidateConfigWithUserAction(networkId: int): Promise<void>--><!--Device-wifiManager-function connectToCandidateConfigWithUserAction(networkId: int): Promise<void>-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| networkId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [2501006](../errorcode-wifi.md#2501006-connection-request-rejected) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2501007](../errorcode-wifi.md#2501007-parameter-verification-failed) |
| [2501005](../errorcode-wifi.md#2501005-no-user-response-to-the-connection-request) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |
| [2501001](../errorcode-wifi.md#2501001-sta-disabled) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
  
  try {
    let networkId = 0; // Candidate network ID, which is generated when a candidate network is added.
    wifiManager.connectToCandidateConfigWithUserAction(networkId).then(result => {
      console.info("result:" + JSON.stringify(result));
    }).catch((err:number) => {
      console.error("failed:" + JSON.stringify(err));
    });
  }catch(error){  
    console.error("failed:" + JSON.stringify(error));
  }
```
