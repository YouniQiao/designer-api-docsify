# createChecksumSync

## Modules to Import

```TypeScript
import { zlib } from '@kit.BasicServicesKit';
```

## createChecksumSync

```TypeScript
function createChecksumSync(): Checksum
```

Creates this checksum object. A checksum instance is returned upon a success.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-zlib-function createChecksumSync(): Checksum--><!--Device-zlib-function createChecksumSync(): Checksum-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Checksum](arkts-basicservices-zlib-checksum-i.md) |

## Examples

```TypeScript
import { zlib } from '@kit.BasicServicesKit';

let checksum = zlib.createChecksumSync()
```
