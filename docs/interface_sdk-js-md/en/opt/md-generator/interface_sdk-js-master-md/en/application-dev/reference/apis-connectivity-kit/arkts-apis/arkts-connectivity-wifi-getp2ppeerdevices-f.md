# getP2pPeerDevices

## Modules to Import

```TypeScript
```

## getP2pPeerDevices

```TypeScript
function getP2pPeerDevices(): Promise<WifiP2pDevice[]>
```

Obtains the information about the found devices.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getP2pPeerDevices](arkts-connectivity-wifimanager-getp2ppeerdevices-f.md#getp2ppeerdevices)

**Required permissions:** ohos.permission.GET_WIFI_INFO and ohos.permission.LOCATION

<!--Device-wifi-function getP2pPeerDevices(): Promise<WifiP2pDevice[]>--><!--Device-wifi-function getP2pPeerDevices(): Promise<WifiP2pDevice[]>-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;WifiP2pDevice[] & gt; |


## getP2pPeerDevices

```TypeScript
function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void
```

Obtains the information about the found devices.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getP2pPeerDevices](arkts-connectivity-wifimanager-getp2ppeerdevices-f.md#getp2ppeerdevices)

**Required permissions:** ohos.permission.GET_WIFI_INFO and ohos.permission.LOCATION

<!--Device-wifi-function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void--><!--Device-wifi-function getP2pPeerDevices(callback: AsyncCallback<WifiP2pDevice[]>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;WifiP2pDevice[]&gt; | Yes |

**Examples**

```TypeScript
import wifi from '@ohos.wifi';

wifi.getP2pPeerDevices((err, data:wifi.WifiP2pDevice) => {
   if (err) {
       console.error("get P2P peer devices error");
       return;
   }
  console.info("get P2P peer devices: " + JSON.stringify(data));
});

wifi.getP2pPeerDevices().then(data => {
  console.info("get P2P peer devices: " + JSON.stringify(data));
});
```
