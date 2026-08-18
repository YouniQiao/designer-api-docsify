# transferStatic

## Modules to Import

```TypeScript
import { transfer } from '@kit.ArkTS';
```

## transferStatic

```TypeScript
function transferStatic(input: Any, inputName: string): Object
```

Converting the 1.0 object to a 1.2 object.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-transfer-function transferStatic(input: Any, inputName: string): Object--><!--Device-transfer-function transferStatic(input: Any, inputName: string): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| input | Any | Yes | The 1.0 object that needs to be converted |
| inputName | string | Yes | name registered by the subsystem. |

**Return value:**

| Type | Description |
| --- | --- |
| Object | Object |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10200067 | Transfer Error. The input name is not supported! |

