# getSdkVersion

## getSdkVersion

```TypeScript
function getSdkVersion(options: HuksOptions): string
```

Obtains the SDK version of the current system. > **NOTE** > > This API is supported since API version 8 and deprecated since API version 11.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 11

<!--Device-huks-function getSdkVersion(options: HuksOptions): string--><!--Device-huks-function getSdkVersion(options: HuksOptions): string-End-->

**System capability:** SystemCapability.Security.Huks.Extension

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Empty object (leave this parameter empty). |

**Return value:**

| Type | Description |
| --- | --- |
| string | SDK version obtained. |

**Example**

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';

/* Set options to emptyOptions. */
let emptyOptions: huks.HuksOptions = {
  properties: []
};
let result = huks.getSdkVersion(emptyOptions);
```

