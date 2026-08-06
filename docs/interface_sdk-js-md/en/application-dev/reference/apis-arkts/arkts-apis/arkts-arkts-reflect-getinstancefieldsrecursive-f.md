# getInstanceFieldsRecursive

## getInstanceFieldsRecursive

```TypeScript
export function getInstanceFieldsRecursive(targetClass: Class): Array<InstanceField>
```

Returns public instance fields of a class and its parents.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-reflect-export function getInstanceFieldsRecursive(targetClass: Class): Array<InstanceField>--><!--Device-reflect-export function getInstanceFieldsRecursive(targetClass: Class): Array<InstanceField>-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| targetClass | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | the target class. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;InstanceField&gt; | an array of instance fields. |

