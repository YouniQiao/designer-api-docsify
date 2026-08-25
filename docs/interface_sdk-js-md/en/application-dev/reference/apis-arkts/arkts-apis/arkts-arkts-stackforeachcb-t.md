# StackForEachCb

```TypeScript
export type StackForEachCb<T> = (value: T, index: int, stack: Stack<T>) => void
```

The type of Stack callback function.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |
| index | int | Yes |
| stack | [Stack](arkts-arkts-util-stack-stack-c.md)&lt;T&gt; | Yes |
