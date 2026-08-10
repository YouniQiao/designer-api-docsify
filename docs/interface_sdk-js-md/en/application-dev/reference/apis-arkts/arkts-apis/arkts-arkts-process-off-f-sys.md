# off (System API)

## Modules to Import

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## off

```TypeScript
function off(type: string): boolean
```

移除已注册的事件。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-process-function off(type: string): boolean--><!--Device-process-function off(type: string): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | string | Yes | 要移除的已注册事件类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回移除结果。 |

