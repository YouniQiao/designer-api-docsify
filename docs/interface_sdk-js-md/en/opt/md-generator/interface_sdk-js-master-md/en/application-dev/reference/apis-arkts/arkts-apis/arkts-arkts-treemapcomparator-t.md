# TreeMapComparator

```TypeScript
export type TreeMapComparator<K> = (firstValue: K, secondValue: K) => number
```

The type of TreeMap comparator.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type TreeMapComparator<K> = (firstValue: K, secondValue: K) => double--><!--Device-unnamed-export type TreeMapComparator<K> = (firstValue: K, secondValue: K) => double-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| firstValue | K | Yes |
| secondValue | K | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |
