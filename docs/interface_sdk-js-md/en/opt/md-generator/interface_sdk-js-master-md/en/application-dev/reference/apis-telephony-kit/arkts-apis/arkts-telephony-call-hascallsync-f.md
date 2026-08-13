# hasCallSync

## Modules to Import

```TypeScript
import { call } from '@kit.TelephonyKit';
```

## hasCallSync

```TypeScript
function hasCallSync(): boolean
```

Checks whether a call is in progress.

**Since:** 10

<!--Device-call-function hasCallSync(): boolean--><!--Device-call-function hasCallSync(): boolean-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

## Examples

```TypeScript
let hasCall: boolean = call.hasCallSync();
console.info(`hasCallSync success, has call is ` + hasCall);
```
