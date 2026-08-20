# getInstanceFieldsRecursive

## Modules to Import

```TypeScript
```

## getInstanceFieldsRecursive

```TypeScript
export function getInstanceFieldsRecursive(targetClass: Class): Array<InstanceField>
```

Returns public instance fields of a class and its parents.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-reflect-export function getInstanceFieldsRecursive(targetClass: Class): Array<InstanceField>--><!--Device-reflect-export function getInstanceFieldsRecursive(targetClass: Class): Array<InstanceField>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetClass | [Class](arkts-arkts-class-c.md) | Yes | the target class. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;[InstanceField](arkts-arkts-reflect-instancefield-c.md)&gt; | an array of instance fields. |

