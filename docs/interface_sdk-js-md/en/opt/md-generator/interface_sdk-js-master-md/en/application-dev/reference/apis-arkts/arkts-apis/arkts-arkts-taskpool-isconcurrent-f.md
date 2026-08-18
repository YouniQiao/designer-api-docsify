# isConcurrent

## Modules to Import

```TypeScript
```

## isConcurrent

```TypeScript
function isConcurrent(func: Function): boolean
```

Checks whether a function is a concurrent function.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-taskpool-function isConcurrent(func: Function): boolean--><!--Device-taskpool-function isConcurrent(func: Function): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| func | Function | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Examples**

```TypeScript
@Concurrent
function test() {}

let result: Boolean = taskpool.isConcurrent(test);
console.info("result is: " + result);
```
