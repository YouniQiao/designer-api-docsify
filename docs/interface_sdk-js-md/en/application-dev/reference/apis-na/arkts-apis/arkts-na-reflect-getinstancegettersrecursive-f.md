# getInstanceGettersRecursive

## getInstanceGettersRecursive

```TypeScript
export function getInstanceGettersRecursive(targetClass: Class): Array<InstanceMethod>
```

Returns public instance getters of a class and its parents.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-reflect-export function getInstanceGettersRecursive(targetClass: Class): Array<InstanceMethod>--><!--Device-reflect-export function getInstanceGettersRecursive(targetClass: Class): Array<InstanceMethod>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetClass | [Class](arkts-na-class-c.md) | Yes | the target class. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[InstanceMethod](arkts-na-reflect-instancemethod-c.md)&gt; | an array of instance getters. |

