# getInstanceGettersRecursive

## getInstanceGettersRecursive

```TypeScript
export function getInstanceGettersRecursive(targetClass: Class): Array<InstanceMethod>
```

Returns public instance getters of a class and its parents.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-reflect-export function getInstanceGettersRecursive(targetClass: Class): Array<InstanceMethod>--><!--Device-reflect-export function getInstanceGettersRecursive(targetClass: Class): Array<InstanceMethod>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetClass | [Class](arkts-arkts-class-c.md) | Yes | the target class. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;InstanceMethod&gt; | an array of instance getters. |

