# transferDynamic

## Modules to Import

```TypeScript
import { transfer } from '@kit.ArkTS';
```

## transferDynamic

```TypeScript
function transferDynamic(input: Object, inputName: string): Any
```

Converting the 1.2 object to a 1.0 object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-transfer-function transferDynamic(input: Object, inputName: string): Any--><!--Device-transfer-function transferDynamic(input: Object, inputName: string): Any-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| input | Object | Yes | The 1.2 object that needs to be converted |
| inputName | string | Yes | name registered by the subsystem. |

**Return value:**

| Type | Description |
| --- | --- |
| Any | Object |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200067 | Transfer Error. The input name is not supported! |

