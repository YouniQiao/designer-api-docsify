# ListFormat

**ArkTS模式：** 仅支持ArkTS-Dyn

## format

```TypeScript
format(list: Iterable<string>): string
```

Returns a string with a language-specific representation of the list.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ListFormat-format(list: Iterable<string>): string--><!--Device-ListFormat-format(list: Iterable<string>): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| list | Iterable&lt;string&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | A language-specific formatted string representing the elements of the list. |

## formatToParts

```TypeScript
formatToParts(list: Iterable<string>): { type: "element" | "literal", value: string; }[]
```

Returns an Array of objects representing the different components that can be used to format a list of values in a locale-aware fashion.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-ListFormat-formatToParts(list: Iterable<string>): { type: "element" | "literal", value: string; }[]--><!--Device-ListFormat-formatToParts(list: Iterable<string>): { type: "element" | "literal", value: string; }[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| list | Iterable&lt;string&gt; | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| { type: "element" \| "literal", value: string; }[] | []} An Array of components which contains the formatted parts from the list. |

