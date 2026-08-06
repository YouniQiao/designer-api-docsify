# Transformer

```TypeScript
type Transformer = (this: Object, key: string, value: Object) => Object | undefined | null
```

Defines the type of the conversion result function.

When used as a parameter of [JSON.parse]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_, the function is called by each member of the object,allowing for custom data processing or conversion during parsing.

When used as a parameter of  
[JSON.stringify]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, the function is used to transfer and handle each property during serialization.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-json-type Transformer = (this: Object, key: string, value: Object) => Object | undefined | null--><!--Device-json-type Transformer = (this: Object, key: string, value: Object) => Object | undefined | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| this | Object | Yes | Object to which the key-value pair to parse belongs.  |
| key | string | Yes | Key to parse.  |
| value | Object | Yes | Value of the key.  |

**Return value:**

| Type | Description |
| --- | --- |
| Object \| undefined \| null | Return an Object, undefined or null value  |

