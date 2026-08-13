# ArrayListReplaceCb

```TypeScript
export type ArrayListReplaceCb<T> =  (value: T, index: number, arrlist: ArrayList<T>) => T
```

The type of ArrayList callback function.

**Since:** 23

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-unnamed-export type ArrayListReplaceCb<T> =  (value: T, index: int, arrlist: ArrayList<T>) => T--><!--Device-unnamed-export type ArrayListReplaceCb<T> =  (value: T, index: int, arrlist: ArrayList<T>) => T-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | T | Yes |
| index | number | Yes |
| arrlist | [ArrayList](arkts-arkts-util-arraylist-arraylist-c.md)&lt;T&gt; | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| T |
