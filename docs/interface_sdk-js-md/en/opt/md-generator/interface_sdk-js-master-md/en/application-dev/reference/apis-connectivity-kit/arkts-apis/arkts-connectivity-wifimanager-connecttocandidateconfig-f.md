# connectToCandidateConfig

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## connectToCandidateConfig

```TypeScript
function connectToCandidateConfig(networkId: number): void
```

Connect to a specified candidate hotspot by networkId, only the configuration which is added by ourself is allowed to be connected. This method connect to a configuration at a time. The app must be in the foreground.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_WIFI_INFO

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-wifiManager-function connectToCandidateConfig(networkId: int): void--><!--Device-wifiManager-function connectToCandidateConfig(networkId: int): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| networkId | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2501000](../errorcode-wifi.md#2501000-sta-internal-error) |
| [2501001](../errorcode-wifi.md#2501001-sta-disabled) |

## Examples

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';

  try {
    let networkId = 0; // Candidate network ID, which is generated when a candidate network is added.
    wifiManager.connectToCandidateConfig(networkId);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```


## connectToCandidateConfig

```TypeScript
function connectToCandidateConfig(settings: ConnectSettings): Promise<void>
```

Connect to the specified candidate hotspot using connect settings.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.SET_WIFI_INFO

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-wifiManager-function connectToCandidateConfig(settings: ConnectSettings): Promise<void>--><!--Device-wifiManager-function connectToCandidateConfig(settings: ConnectSettings): Promise<void>-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| settings | [ConnectSettings](arkts-connectivity-wifimanager-connectsettings-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
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
    let setting:wifiManager.ConnectSettings = { networkId: 0 }; // Candidate network ID, which is generated when a candidate network is added.
    wifiManager.connectToCandidateConfig(setting);
  }catch(error){
    console.error("failed:" + JSON.stringify(error));
  }
```
