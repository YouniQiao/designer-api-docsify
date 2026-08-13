# getPowerMode

## Modules to Import

```TypeScript
import { wifiManagerExt } from '@kit.ConnectivityKit';
```

## getPowerMode

```TypeScript
function getPowerMode(): Promise<PowerMode>
```

Obtains the current Wi-Fi power mode.

**Since:** 9

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManagerExt-function getPowerMode(): Promise<PowerMode>--><!--Device-wifiManagerExt-function getPowerMode(): Promise<PowerMode>-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Extension

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PowerMode](arkts-connectivity-wifimanagerext-powermode-e.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2701000](../errorcode-wifi.md#2701000-ap-extension-module-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { wifiManagerExt } from '@kit.ConnectivityKit';

  try {
      let model = wifiManagerExt.getPowerMode();
      console.info("model info:" + model);
  }catch(error){
      console.error("failed: " + JSON.stringify(error));
  }
```


## getPowerMode

```TypeScript
function getPowerMode(callback: AsyncCallback<PowerMode>): void
```

Obtains the current Wi-Fi power mode.

**Since:** 9

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiManagerExt-function getPowerMode(callback: AsyncCallback<PowerMode>): void--><!--Device-wifiManagerExt-function getPowerMode(callback: AsyncCallback<PowerMode>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PowerMode](arkts-connectivity-wifimanagerext-powermode-e.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [2701000](../errorcode-wifi.md#2701000-ap-extension-module-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { wifiManagerExt } from '@kit.ConnectivityKit';

  wifiManagerExt.getPowerMode((err, data:wifiManagerExt.PowerMode) => {
      if (err) {
          console.error("Failed to get linked information");
          return;
      }
      console.info("get power mode info: " + JSON.stringify(data));
  });

  wifiManagerExt.getPowerMode().then(data => {
      console.info("get power mode info: " + JSON.stringify(data));
  }).catch((error:number) => {
      console.error("get power mode error");
  });
```
