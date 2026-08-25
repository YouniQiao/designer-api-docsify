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

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [targetClass](../../apis-ability-kit/arkts-apis/arkts-ability-shortcutinfo-shortcutwant-depr-i-sys.md) | [Class](arkts-arkts-class-c.md) | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Array&lt;[InstanceField](arkts-arkts-reflect-instancefield-c.md)&gt; |
