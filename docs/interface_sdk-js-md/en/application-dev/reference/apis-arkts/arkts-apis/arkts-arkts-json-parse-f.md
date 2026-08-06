# parse

## parse

```TypeScript
function parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null
```

Parses a JSON string into an ArkTS object or null.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-json-function parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null--><!--Device-json-function parse(text: string, reviver?: Transformer, options?: ParseOptions): Object | null-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes | Valid JSON string. |
| reviver | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Conversion function. This parameter can be used to modify the value generated after parsing. The default value is undefined. |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Parsing options. This parameter is used to control the type of the parsing result. The default value is undefined. |

**Return value:**

| Type | Description |
| --- | --- |
| Object | Return an Object, array, string, number, boolean, or null value corresponding to JSON text. |

