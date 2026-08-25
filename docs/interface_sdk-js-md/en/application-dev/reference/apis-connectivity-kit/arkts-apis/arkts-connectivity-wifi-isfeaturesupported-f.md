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

**Substitutes:** [isFeatureSupported](arkts-connectivity-wifimanager-isfeaturesupported-f.md)

**Required permissions:** ohos.permission.GET_WIFI_INFO

**System capability:** SystemCapability.Communication.WiFi.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| featureId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
