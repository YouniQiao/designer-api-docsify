# removeUntrustedConfig

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
import { wifiext } from '@kit.ConnectivityKit';
import { wifiManager } from '@kit.ConnectivityKit';
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## removeUntrustedConfig

```TypeScript
function removeUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>
```

Removes a specified untrusted hotspot configuration.

<p>This method removes one configuration at a time.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [removeCandidateConfig](arkts-connectivity-wifimanager-removecandidateconfig-f.md)

**Required permissions:** ohos.permission.SET_WIFI_INFO

<!--Device-wifi-function removeUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>--><!--Device-wifi-function removeUntrustedConfig(config: WifiDeviceConfig): Promise<boolean>-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | WifiDeviceConfig | Yes | Indicates the device configuration for connection to the Wi-Fi network. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Returns { |

**Examples**

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
	wifi.removeUntrustedConfig(config).then(result => {
		console.info("result:" + JSON.stringify(result));
	});	
}catch(error){
	console.error("failed:" + JSON.stringify(error));
}
```


## removeUntrustedConfig

```TypeScript
function removeUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void
```

Removes a specified untrusted hotspot configuration.

<p>This method removes one configuration at a time.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [removeCandidateConfig](arkts-connectivity-wifimanager-removecandidateconfig-f.md)

**Required permissions:** ohos.permission.SET_WIFI_INFO

<!--Device-wifi-function removeUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void--><!--Device-wifi-function removeUntrustedConfig(config: WifiDeviceConfig, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | WifiDeviceConfig | Yes | Indicates the device configuration for connection to the Wi-Fi network. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes |  |

**Examples**

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
	wifi.removeUntrustedConfig(config,(error,result) => {
	console.info("result:" + JSON.stringify(result));
	});	
}catch(error){
	console.error("failed:" + JSON.stringify(error));
}
```

