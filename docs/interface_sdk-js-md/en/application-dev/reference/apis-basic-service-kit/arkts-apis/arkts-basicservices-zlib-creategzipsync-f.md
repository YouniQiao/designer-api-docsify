# createGZipSync

## Modules to Import

```TypeScript
import { zlib } from 'zlib';
```

## createGZipSync

```TypeScript
function createGZipSync(): GZip
```

Creates this **GZip** object. A **GZip** instance is returned upon a success.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-zlib-function createGZipSync(): GZip--><!--Device-zlib-function createGZipSync(): GZip-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| Type | Description |
| --- | --- |
| [GZip](arkts-basicservices-zlib-gzip-i.md) | gzip object instance. |

## Examples

```TypeScript
import { zlib } from '@kit.BasicServicesKit';

let gzip = zlib.createGZipSync();
```

