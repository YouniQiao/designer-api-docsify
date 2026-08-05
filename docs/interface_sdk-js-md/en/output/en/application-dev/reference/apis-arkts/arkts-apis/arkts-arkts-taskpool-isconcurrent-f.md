# isConcurrent

## isConcurrent

```TypeScript
function isConcurrent(func: Function): boolean
```

Checks whether a function is a concurrent function.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-taskpool-function isConcurrent(func: Function): boolean--><!--Device-taskpool-function isConcurrent(func: Function): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| func | Function | Yes | Function to check. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Check result. The value **true** is returned if the function is a concurrent function, that is |

**Example**

```TypeScript
@Concurrent
function test() {}

let result: Boolean = taskpool.isConcurrent(test);
console.info("result is: " + result);
```

