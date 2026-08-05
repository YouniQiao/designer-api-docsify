# hasCallSync

## hasCallSync

```TypeScript
function hasCallSync(): boolean
```

Checks whether a call is ongoing.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-call-function hasCallSync(): boolean--><!--Device-call-function hasCallSync(): boolean-End-->

**System capability:** SystemCapability.Telephony.CallManager

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returns { |

**Example**

```TypeScript
let hasCall: boolean = call.hasCallSync();
console.info(`hasCallSync success, has call is ` + hasCall);
```

