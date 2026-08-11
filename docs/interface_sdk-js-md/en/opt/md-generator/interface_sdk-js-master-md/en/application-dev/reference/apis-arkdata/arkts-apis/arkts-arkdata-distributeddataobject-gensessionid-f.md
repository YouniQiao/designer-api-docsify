# genSessionId

## Modules to Import

```TypeScript
import { distributedDataObject } from 'kits/@kit.ArkData';
```

## genSessionId

```TypeScript
function genSessionId(): string
```

Creates a random session ID.

**Since:** 8

<!--Device-distributedDataObject-function genSessionId(): string--><!--Device-distributedDataObject-function genSessionId(): string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
let sessionId: string = distributedDataObject.genSessionId();
```
