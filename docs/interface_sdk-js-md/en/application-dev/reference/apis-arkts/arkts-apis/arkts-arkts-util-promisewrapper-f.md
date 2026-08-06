# promiseWrapper

## promiseWrapper

```TypeScript
function promiseWrapper(original: (err: Object, value: Object) => void): Object
```

Receives a function that uses the error-first callback mode, that is, uses \_\_\_INLINE\_CODE\_DESC\_USD\_0\_\_\_ as the last  
parameter, and uses a promise to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [util.promisify](arkts-arkts-util-promisify-f.md#promisify)

<!--Device-util-function promiseWrapper(original: (err: Object, value: Object) => void): Object--><!--Device-util-function promiseWrapper(original: (err: Object, value: Object) => void): Object-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| original | (err: Object, value: Object) =&gt; void | Yes | Asynchronous function. |

**Return value:**

| Type | Description |
| --- | --- |
| Object | Promise in the error-first style (that is, (err, value) =       ... is called as the last parameter) . |

