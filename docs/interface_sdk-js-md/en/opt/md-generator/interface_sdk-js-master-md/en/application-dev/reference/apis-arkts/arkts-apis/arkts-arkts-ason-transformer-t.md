# Transformer

```TypeScript
type Transformer = (this: ISendable, key: string,
      value: ISendable | undefined | null) => ISendable | undefined | null
```

The type of conversion result function.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ASON-type Transformer = (this: ISendable, key: string,      value: ISendable | undefined | null) => ISendable | undefined | null--><!--Device-ASON-type Transformer = (this: ISendable, key: string,      value: ISendable | undefined | null) => ISendable | undefined | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| this | [ISendable](../../apis-image-kit/arkts-apis/arkts-image-sendableimage-isendable-t.md) | Yes |
| key | string | Yes |
| value | ISendable \| undefined \| null | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| ISendable \| undefined \| null |
