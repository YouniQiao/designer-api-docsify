# ArrayFromMapFn

```TypeScript
type ArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType
```

Defines the ArkTS Array reduction function, which is used by the 'from' API of the Array class.

**Since:** 18

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-collections-type ArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType--><!--Device-collections-type ArrayFromMapFn<FromElementType, ToElementType> = (value: FromElementType, index: number) => ToElementType-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | FromElementType | Yes |
| index | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| ToElementType |
