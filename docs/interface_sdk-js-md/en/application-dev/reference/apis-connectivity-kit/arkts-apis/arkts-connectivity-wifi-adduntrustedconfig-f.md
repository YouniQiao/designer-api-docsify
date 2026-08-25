# addUntrustedConfig

## Modules to Import

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## addUntrustedConfig

```TypeScript
function addUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>
```

Adds a specified untrusted hotspot configuration.<p>This method adds one configuration at a time. After this configuration is added, your device will determine whether to connect to the hotspot.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [addCandidateConfig](arkts-connectivity-wifimanager-addcandidateconfig-f.md)

**Required permissions:** ohos.permission.SET_WIFI_INFO

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |


## addUntrustedConfig

```TypeScript
function addUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void
```

Adds a specified untrusted hotspot configuration.<p>This method adds one configuration at a time. After this configuration is added, your device will determine whether to connect to the hotspot.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [addCandidateConfig](arkts-connectivity-wifimanager-addcandidateconfig-f.md)

**Required permissions:** ohos.permission.SET_WIFI_INFO

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| config | [WifiDeviceConfig](arkts-connectivity-wifi-wifideviceconfig-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |
