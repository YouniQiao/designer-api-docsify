# getLinkedInfo

## getLinkedInfo

```TypeScript
function getLinkedInfo(): Promise<WifiLinkedInfo>
```

Obtains information about a Wi-Fi connection.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.wifiManager/wifiManager.getLinkedInfo

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function getLinkedInfo(): Promise<WifiLinkedInfo>--><!--Device-wifi-function getLinkedInfo(): Promise<WifiLinkedInfo>-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;WifiLinkedInfo&gt; | Returns Wi-Fi linked information. |


## getLinkedInfo

```TypeScript
function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void
```

Obtains information about a Wi-Fi connection.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn only, since version 6.

**Deprecated since:** 9

**Substitutes:** ohos.wifiManager/wifiManager.getLinkedInfo

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void--><!--Device-wifi-function getLinkedInfo(callback: AsyncCallback<WifiLinkedInfo>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;WifiLinkedInfo&gt; | Yes |  |

**Example**

```TypeScript
import wifi from '@ohos.wifi';

wifi.getLinkedInfo((err, data:wifi.WifiLinkedInfo) => {
    if (err) {
        console.error("get linked info error");
        return;
    }
    console.info("get wifi linked info: " + JSON.stringify(data));
});

wifi.getLinkedInfo().then(data => {
    console.info("get wifi linked info: " + JSON.stringify(data));
}).catch((error:number) => {
    console.info("get linked info error");
});
```

