# PlainArrayForEachCb

```TypeScript
export type PlainArrayForEachCb<T> = (value: T, key: number, PlainArray: PlainArray<T>) => void
```

The type of PlainArray callback function.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type PlainArrayForEachCb<T> = (value: T, key: int, PlainArray: PlainArray<T>) => void--><!--Device-unnamed-export type PlainArrayForEachCb<T> = (value: T, key: int, PlainArray: PlainArray<T>) => void-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |
| key | number | Yes |
| [PlainArray](arkts-arkts-util-plainarray-plainarray-c.md) | [PlainArray](arkts-arkts-util-plainarray-plainarray-c.md)&lt;T&gt; | Yes |
