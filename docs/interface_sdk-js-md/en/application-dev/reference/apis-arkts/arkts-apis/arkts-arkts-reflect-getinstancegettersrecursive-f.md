# getInstanceGettersRecursive

## Modules to Import

```TypeScript
```

## getInstanceGettersRecursive

```TypeScript
export function getInstanceGettersRecursive(targetClass: Class): Array<InstanceMethod>
```

Returns public instance getters of a class and its parents.

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
| Array&lt;[InstanceMethod](arkts-arkts-reflect-instancemethod-c.md)&gt; |
