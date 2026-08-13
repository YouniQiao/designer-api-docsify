# JSON

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-unnamed-interface JSON--><!--Device-unnamed-interface JSON-End-->

## parse

```TypeScript
parse(text: string, reviver?: (this: any, key: string, value: any) => any): any
```

Converts a JavaScript Object Notation (JSON) string into an object.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-JSON-parse(text: string, reviver?: (this: any, key: string, value: any) => any): any--><!--Device-JSON-parse(text: string, reviver?: (this: any, key: string, value: any) => any): any-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| text | string | Yes |  |
| reviver | (this: any, key: string, value: any) =&gt; any | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| any |  |

## stringify

```TypeScript
stringify(value: any, replacer?: (this: any, key: string, value: any) => any, space?: string | number): string
```

Converts a JavaScript value to a JavaScript Object Notation (JSON) string.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-JSON-stringify(value: any, replacer?: (this: any, key: string, value: any) => any, space?: string | number): string--><!--Device-JSON-stringify(value: any, replacer?: (this: any, key: string, value: any) => any, space?: string | number): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | any | Yes |  |
| replacer | (this: any, key: string, value: any) =&gt; any | No |  |
| space | string \| number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

## stringify

```TypeScript
stringify(value: any, replacer?: (number | string)[] | null, space?: string | number): string
```

Converts a JavaScript value to a JavaScript Object Notation (JSON) string.

**Since:** -1

**ArkTS mode:** ArkTS-Dyn only, since version -1.

**Deprecated since:** -1

<!--Device-JSON-stringify(value: any, replacer?: (number | string)[] | null, space?: string | number): string--><!--Device-JSON-stringify(value: any, replacer?: (number | string)[] | null, space?: string | number): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | any | Yes |  |
| replacer | (number \| string)[] \| null | No |  |
| space | string \| number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| string |  |

