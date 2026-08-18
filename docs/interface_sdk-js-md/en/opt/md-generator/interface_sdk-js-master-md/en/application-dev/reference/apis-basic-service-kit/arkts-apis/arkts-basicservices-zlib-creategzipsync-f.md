# createGZipSync

## Modules to Import

```TypeScript
```

## createGZipSync

```TypeScript
function createGZipSync(): GZip
```

Creates this **GZip** object. A **GZip** instance is returned upon a success.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-zlib-function createGZipSync(): GZip--><!--Device-zlib-function createGZipSync(): GZip-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [GZip](arkts-basicservices-zlib-gzip-i.md) |

**Examples**

```TypeScript
import { zlib } from '@kit.BasicServicesKit';

let gzip = zlib.createGZipSync();
```
