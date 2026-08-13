# StackForEachCb

```TypeScript
export type StackForEachCb<T> = (value: T, index: number, stack: Stack<T>) => void
```

The type of Stack callback function.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type StackForEachCb<T> = (value: T, index: int, stack: Stack<T>) => void--><!--Device-unnamed-export type StackForEachCb<T> = (value: T, index: int, stack: Stack<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |
| index | number | Yes |
| [stack](../../apis-na/arkts-apis/arkts-na-lib-es5-error-i.md) | [Stack](arkts-arkts-util-stack-stack-c.md)&lt;T&gt; | Yes |
