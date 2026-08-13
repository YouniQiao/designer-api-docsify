# getSupportedPowerMode

## Modules to Import

```TypeScript
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## getSupportedPowerMode

```TypeScript
function getSupportedPowerMode(): Promise<Array<PowerMode>>
```

Obtains the supported power Mode.

**Since:** 9

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManagerExt-function getSupportedPowerMode(): Promise<Array<PowerMode>>--><!--Device-wifiManagerExt-function getSupportedPowerMode(): Promise<Array<PowerMode>>-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Extension

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[PowerMode](arkts-connectivity-wifimanagerext-powermode-e.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2701000](../errorcode-wifi.md#2701000-ap-extension-module-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |


## getSupportedPowerMode

```TypeScript
function getSupportedPowerMode(callback: AsyncCallback<Array<PowerMode>>): void
```

Obtains the supported power Mode.

**Since:** 9

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManagerExt-function getSupportedPowerMode(callback: AsyncCallback<Array<PowerMode>>): void--><!--Device-wifiManagerExt-function getSupportedPowerMode(callback: AsyncCallback<Array<PowerMode>>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[PowerMode](arkts-connectivity-wifimanagerext-powermode-e.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2701000](../errorcode-wifi.md#2701000-ap-extension-module-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { wifiManagerExt } from '@kit.ConnectivityKit';

wifiManagerExt.getSupportedPowerMode((err, data: wifiManagerExt.PowerMode[]) => {
    if (err) {
        console.error("get supported power mode info error: ", err);
        return;
    }
    console.info("get supported power mode info: " + JSON.stringify(data));
});
```
