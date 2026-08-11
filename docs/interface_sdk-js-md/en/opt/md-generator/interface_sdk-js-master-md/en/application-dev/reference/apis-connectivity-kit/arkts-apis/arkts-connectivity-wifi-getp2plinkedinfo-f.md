# getP2pLinkedInfo

## Modules to Import

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## getP2pLinkedInfo

```TypeScript
function getP2pLinkedInfo(): Promise<WifiP2pLinkedInfo>
```

Obtains information about a P2P connection.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.wifiManager/wifiManager.getP2pLinkedInfo

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function getP2pLinkedInfo(): Promise<WifiP2pLinkedInfo>--><!--Device-wifi-function getP2pLinkedInfo(): Promise<WifiP2pLinkedInfo>-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;WifiP2pLinkedInfo&gt; |


## getP2pLinkedInfo

```TypeScript
function getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void
```

Obtains information about a P2P connection.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** ohos.wifiManager/wifiManager.getP2pLinkedInfo

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void--><!--Device-wifi-function getP2pLinkedInfo(callback: AsyncCallback<WifiP2pLinkedInfo>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.P2P

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;WifiP2pLinkedInfo&gt; | Yes |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

wifi.getP2pLinkedInfo((err, data:wifi.WifiP2pLinkedInfo) => {
   if (err) {
       console.error("get p2p linked info error");
       return;
   }
  console.info("get wifi p2p linked info: " + JSON.stringify(data));
});

wifi.getP2pLinkedInfo().then(data => {
  console.info("get wifi p2p linked info: " + JSON.stringify(data));
});
```
