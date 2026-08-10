# genSessionId

## Modules to Import

```TypeScript
import { distributedDataObject } from 'kits/@kit.ArkData';
```

## genSessionId

```TypeScript
function genSessionId(): string
```

随机创建一个sessionId。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-distributedDataObject-function genSessionId(): string--><!--Device-distributedDataObject-function genSessionId(): string-End-->

**System capability:** SystemCapability.DistributedDataManager.DataObject.DistributedObject

**Return value:**

| Type | Description |
| --- | --- |
| string | 随机创建的sessionId。 |

## Examples

```TypeScript
let sessionId: string = distributedDataObject.genSessionId();
```

