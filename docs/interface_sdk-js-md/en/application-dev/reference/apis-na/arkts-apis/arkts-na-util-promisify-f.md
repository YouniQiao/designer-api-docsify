# promisify

## Modules to Import

```TypeScript
```

## promisify

```TypeScript
function promisify(original: Function): PromisifiedFunc
```

Takes a function following the common error-first callback style, i.e taking an (err, value) => callback as the last argument, and return a function that returns promises.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-util-function promisify(original: Function): PromisifiedFunc--><!--Device-util-function promisify(original: Function): PromisifiedFunc-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| original | Function | Yes | Asynchronous Function |

**Return value:**

| Type | Description |
| --- | --- |
| [PromisifiedFunc](arkts-na-util-promisifiedfunc-t.md) | Return a function that returns promises |

