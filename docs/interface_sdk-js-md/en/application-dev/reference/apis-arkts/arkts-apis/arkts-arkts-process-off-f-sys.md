# off (System API)

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## off

```TypeScript
function off(type: string): boolean
```

Remove registered event

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-process-function off(type: string): boolean--><!--Device-process-function off(type: string): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | Remove the type of registered event. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Return removed result. |

