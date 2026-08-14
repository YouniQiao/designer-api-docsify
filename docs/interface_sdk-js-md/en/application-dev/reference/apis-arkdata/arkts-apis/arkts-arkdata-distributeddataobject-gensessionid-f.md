# genSessionId

## Modules to Import

```TypeScript
import { distributedDataObject } from 'distributedDataObject';
```

## genSessionId

```TypeScript
function genSessionId(): string
```

Creates a random session ID.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-distributedDataObject-function genSessionId(): string--><!--Device-distributedDataObject-function genSessionId(): string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Return value:**

| Type | Description |
| --- | --- |
| string | Session ID created. |

## Examples

```TypeScript
let sessionId: string = distributedDataObject.genSessionId();
```

