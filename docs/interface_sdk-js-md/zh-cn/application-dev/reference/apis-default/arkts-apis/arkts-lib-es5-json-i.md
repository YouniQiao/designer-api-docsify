# JSON

**ArkTS模式：** 仅支持ArkTS-Dyn

## parse

```TypeScript
parse(text: string, reviver?: (this: any, key: string, value: any) => any): any
```

Converts a JavaScript Object Notation (JSON) string into an object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-JSON-parse(text: string, reviver?: (this: any, key: string, value: any) => any): any--><!--Device-JSON-parse(text: string, reviver?: (this: any, key: string, value: any) => any): any-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 |  |
| reviver | (this: any, key: string, value: any) =&gt; any | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| any |  |

## stringify

```TypeScript
stringify(value: any, replacer?: (this: any, key: string, value: any) => any, space?: string | number): string
```

Converts a JavaScript value to a JavaScript Object Notation (JSON) string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-JSON-stringify(value: any, replacer?: (this: any, key: string, value: any) => any, space?: string | number): string--><!--Device-JSON-stringify(value: any, replacer?: (this: any, key: string, value: any) => any, space?: string | number): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | any | 是 |  |
| replacer | (this: any, key: string, value: any) =&gt; any | 否 |  |
| space | string \| number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## stringify

```TypeScript
stringify(value: any, replacer?: (number | string)[] | null, space?: string | number): string
```

Converts a JavaScript value to a JavaScript Object Notation (JSON) string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-JSON-stringify(value: any, replacer?: (number | string)[] | null, space?: string | number): string--><!--Device-JSON-stringify(value: any, replacer?: (number | string)[] | null, space?: string | number): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | any | 是 |  |
| replacer | (number \| string)[] \| null | 否 |  |
| space | string \| number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

