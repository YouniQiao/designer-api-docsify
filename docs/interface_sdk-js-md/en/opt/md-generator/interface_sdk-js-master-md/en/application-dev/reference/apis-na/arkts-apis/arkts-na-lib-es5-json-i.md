# JSON

**Since:** -1

**Deprecated since:** -1

<!--Device-unnamed-interface JSON--><!--Device-unnamed-interface JSON-End-->

## parse

```TypeScript
parse(text: string, reviver?: (this: any, key: string, value: any) => any): any
```

Converts a JavaScript Object Notation (JSON) string into an object.

**Since:** -1

**Deprecated since:** -1

<!--Device-JSON-parse(text: string, reviver?: (this: any, key: string, value: any) => any): any--><!--Device-JSON-parse(text: string, reviver?: (this: any, key: string, value: any) => any): any-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| text | string | Yes |
| reviver | (this: any, key: string, value: any) = & gt; any | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| any |

## stringify

```TypeScript
stringify(value: any, replacer?: (this: any, key: string, value: any) => any, space?: string | number): string
```

Converts a JavaScript value to a JavaScript Object Notation (JSON) string.

**Since:** -1

**Deprecated since:** -1

<!--Device-JSON-stringify(value: any, replacer?: (this: any, key: string, value: any) => any, space?: string | number): string--><!--Device-JSON-stringify(value: any, replacer?: (this: any, key: string, value: any) => any, space?: string | number): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | any | Yes |
| replacer | (this: any, key: string, value: any) = & gt; any | No |
| space | string \| number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## stringify

```TypeScript
stringify(value: any, replacer?: (number | string)[] | null, space?: string | number): string
```

Converts a JavaScript value to a JavaScript Object Notation (JSON) string.

**Since:** -1

**Deprecated since:** -1

<!--Device-JSON-stringify(value: any, replacer?: (number | string)[] | null, space?: string | number): string--><!--Device-JSON-stringify(value: any, replacer?: (number | string)[] | null, space?: string | number): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | any | Yes |
| replacer | (number \| string)[] \| null | No |
| space | string \| number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |
