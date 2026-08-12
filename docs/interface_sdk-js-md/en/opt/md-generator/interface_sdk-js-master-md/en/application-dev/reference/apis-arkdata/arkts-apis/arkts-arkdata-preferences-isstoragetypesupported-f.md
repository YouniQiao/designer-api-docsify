# isStorageTypeSupported

## Modules to Import

```TypeScript
import { preferences } from '@kit.ArkData';
```

## isStorageTypeSupported

```TypeScript
function isStorageTypeSupported(type: StorageType): boolean
```

Checks whether the specified storage type is supported. This API returns the result synchronously. If the storage type is supported, **true** is returned. Otherwise, **false** is returned.

**Since:** 18

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-preferences-function isStorageTypeSupported(type: StorageType): boolean--><!--Device-preferences-function isStorageTypeSupported(type: StorageType): boolean-End-->

**System capability:** SystemCapability.DistributedDataManager.Preferences.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [StorageType](arkts-arkdata-preferences-storagetype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
let xmlType = preferences.StorageType.XML;
let gskvType = preferences.StorageType.GSKV;
let isXmlSupported = preferences.isStorageTypeSupported(xmlType);
let isGskvSupported = preferences.isStorageTypeSupported(gskvType);
console.info("Is xml supported in current platform: " + isXmlSupported);
console.info("Is gskv supported in current platform: " + isGskvSupported);
```
