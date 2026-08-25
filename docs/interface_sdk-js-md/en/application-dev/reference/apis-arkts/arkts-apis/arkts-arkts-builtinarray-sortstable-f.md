# sort_stable

## Modules to Import

```TypeScript
```

## sort_stable

```TypeScript
export function sort_stable<T>(arr: FixedArray<T>, startIndex: int, endIndex: int, comp: (lhs: T, rhs: T) => int): 
    void
```

Sorts elements of `arr` using stable sort algorithm.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| arr | FixedArray & lt;T & gt; | Yes |
| startIndex | int | Yes |
| endIndex | int | Yes |
| comp | (lhs: T, rhs: T) = & gt; int | Yes |
