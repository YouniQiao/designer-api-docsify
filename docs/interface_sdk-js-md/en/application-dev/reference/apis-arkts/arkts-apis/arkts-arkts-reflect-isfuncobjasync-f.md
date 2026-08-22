# isFuncObjAsync

## Modules to Import

```TypeScript
```

## isFuncObjAsync

```TypeScript
export function isFuncObjAsync(target: Function): boolean
```

Determines if a functional object was lowered from an async function.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-reflect-export function isFuncObjAsync(target: Function): boolean--><!--Device-reflect-export function isFuncObjAsync(target: Function): boolean-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | Function | Yes | the functional object. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true if the functional object was lowered from an async function. |

