# Transformer

```TypeScript
type Transformer = (this: ISendable, key: string,
      value: ISendable | undefined | null) => ISendable | undefined | null
```

The type of conversion result function.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ASON-type Transformer = (this: ISendable, key: string,      value: ISendable | undefined | null) => ISendable | undefined | null--><!--Device-ASON-type Transformer = (this: ISendable, key: string,      value: ISendable | undefined | null) => ISendable | undefined | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| this | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The ISendable to which the parsed key value pair belongs.  |
| key | string | Yes | Attribute name.  |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined \| null | Yes | The value of the parsed key value pair.  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined \| null | Return the modified ISendable or undefined or null. |

