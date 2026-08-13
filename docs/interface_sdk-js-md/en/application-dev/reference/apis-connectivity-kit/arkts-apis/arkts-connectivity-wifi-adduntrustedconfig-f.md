# addUntrustedConfig

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## addUntrustedConfig

```TypeScript
function addUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>
```

Adds a specified untrusted hotspot configuration. &lt;p&gt;This method adds one configuration at a time. After this configuration is added, your device will determine whether to connect to the hotspot.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [addCandidateConfig](arkts-connectivity-wifimanager-addcandidateconfig-f.md#addCandidateConfig)

**Required permissions:** ohos.permission.SET_WIFI_INFO

<!--Device-wifi-function addUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>--><!--Device-wifi-function addUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | WifiDeviceConfig | Yes | Indicates the device configuration for connection to the Wi-Fi network. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Returns { |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

try {
	let config:wifi.WifiDeviceConfig = {
		ssid : "****",
		bssid:  "****",
		preSharedKey: "****",
		isHiddenSsid: false,
		securityType: 0,
		creatorUid: 0,
		disableReason: 0,
		netId: 0,
		randomMacType: 0,
		randomMacAddr:  "****",
		ipType: 0,
		staticIp: {
			ipAddress: 0,
			gateway: 0,
			dnsServers: [],
			domains: []
		}
	}
	wifi.addUntrustedConfig(config).then(result => {
		console.info("result:" + JSON.stringify(result));
	});	
}catch(error){
	console.error("failed:" + JSON.stringify(error));
}
```


## addUntrustedConfig

```TypeScript
function addUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void
```

Adds a specified untrusted hotspot configuration. &lt;p&gt;This method adds one configuration at a time. After this configuration is added, your device will determine whether to connect to the hotspot.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [addCandidateConfig](arkts-connectivity-wifimanager-addcandidateconfig-f.md#addCandidateConfig)

**Required permissions:** ohos.permission.SET_WIFI_INFO

<!--Device-wifi-function addUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void--><!--Device-wifi-function addUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | WifiDeviceConfig | Yes | Indicates the device configuration for connection to the Wi-Fi network. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |  |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

try {
	let config:wifi.WifiDeviceConfig = {
		ssid : "****",
		bssid:  "****",
		preSharedKey: "****",
		isHiddenSsid: false,
		securityType: 0,
		creatorUid: 0,
		disableReason: 0,
		netId: 0,
		randomMacType: 0,
		randomMacAddr:  "****",
		ipType: 0,
		staticIp: {
			ipAddress: 0,
			gateway: 0,
			dnsServers: [],
			domains: []
		}
	}
	wifi.addUntrustedConfig(config,(error,result) => {
		console.info("result:" + JSON.stringify(result));
	});	
}catch(error){
	console.error("failed:" + JSON.stringify(error));
}
```

