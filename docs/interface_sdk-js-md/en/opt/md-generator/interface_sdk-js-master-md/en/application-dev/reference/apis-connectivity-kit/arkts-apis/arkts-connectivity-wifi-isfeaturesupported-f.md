# isFeatureSupported

## Modules to Import

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## isFeatureSupported

```TypeScript
function isFeatureSupported(featureId: number): boolean
```

Checks whether this device supports a specified feature.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** ohos.wifiManager/wifiManager.isFeatureSupported

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifi-function isFeatureSupported(featureId: number): boolean--><!--Device-wifi-function isFeatureSupported(featureId: number): boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| featureId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
import wifi from '@ohos.wifi';

try {
  let featureId = 0;
  let ret = wifi.isFeatureSupported(featureId);
  console.info("isFeatureSupported:" + ret);
}catch(error){
  console.error("failed:" + JSON.stringify(error));
}
```
