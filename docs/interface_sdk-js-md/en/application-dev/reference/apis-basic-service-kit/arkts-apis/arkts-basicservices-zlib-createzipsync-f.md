# createZipSync

## Modules to Import

```TypeScript
import { zlib } from 'zlib';
```

## createZipSync

```TypeScript
function createZipSync(): Zip
```

Creates this **Zip** instance. A **Zip** instance is returned upon a success.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-zlib-function createZipSync(): Zip--><!--Device-zlib-function createZipSync(): Zip-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| Type | Description |
| --- | --- |
| [Zip](arkts-basicservices-zlib-zip-i.md) | The **Zip** instance created. |

## Examples

```TypeScript
import { zlib } from '@kit.BasicServicesKit';

let zip = zlib.createZipSync();
```

