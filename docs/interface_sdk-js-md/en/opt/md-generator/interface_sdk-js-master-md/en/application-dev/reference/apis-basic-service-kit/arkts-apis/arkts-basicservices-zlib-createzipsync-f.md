# createZipSync

## Modules to Import

```TypeScript
import { zlib } from '@kit.BasicServicesKit';
```

## createZipSync

```TypeScript
function createZipSync(): Zip
```

Creates this **Zip** instance. A **Zip** instance is returned upon a success.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-zlib-function createZipSync(): Zip--><!--Device-zlib-function createZipSync(): Zip-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Zip](arkts-basicservices-zlib-zip-i.md) |

## Examples

```TypeScript
import { zlib } from '@kit.BasicServicesKit';

let zip = zlib.createZipSync();
```
