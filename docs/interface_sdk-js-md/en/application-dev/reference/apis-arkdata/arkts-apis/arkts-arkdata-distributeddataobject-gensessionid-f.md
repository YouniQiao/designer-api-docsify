# genSessionId

## Modules to Import

```TypeScript
import { distributedDataObject } from '@kit.ArkData';
```

## genSessionId

```TypeScript
function genSessionId(): string
```

Creates a random session ID.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Examples**

```TypeScript
let sessionId: string = distributedDataObject.genSessionId();
```
