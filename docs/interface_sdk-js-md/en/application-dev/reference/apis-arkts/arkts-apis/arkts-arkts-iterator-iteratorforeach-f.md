# iteratorForEach

## Modules to Import

```TypeScript
```

## iteratorForEach

```TypeScript
export function iteratorForEach<V>(x: Iterator<V>, fn: (x: V) => void): void
```

Iterates over an iterator and executes the specified callback function for each element

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | Iterator & lt;V & gt; | Yes |
| fn | (x: V) = & gt; void | Yes |
