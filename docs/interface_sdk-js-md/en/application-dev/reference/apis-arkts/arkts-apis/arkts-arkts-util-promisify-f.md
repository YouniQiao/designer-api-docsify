# promisify

## promisify

```TypeScript
function promisify(original: Function): PromisifiedFunc
```

Takes a function following the common error-first callback style, i.e taking an (err, value) =>callback as the last argument, and return a function that returns promises.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-util-function promisify(original: Function): PromisifiedFunc--><!--Device-util-function promisify(original: Function): PromisifiedFunc-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| original | Function | Yes | Asynchronous Function |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Return a function that returns promises |

