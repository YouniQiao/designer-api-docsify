# ListFormat

**ArkTS mode:** ArkTS-Dyn only

## format

```TypeScript
format(list: Iterable<string>): string
```

Returns a string with a language-specific representation of the list.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-ListFormat-format(list: Iterable<string>): string--><!--Device-ListFormat-format(list: Iterable<string>): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| list | Iterable&lt;string&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| string | A language-specific formatted string representing the elements of the list. |

## formatToParts

```TypeScript
formatToParts(list: Iterable<string>): { type: "element" | "literal", value: string; }[]
```

Returns an Array of objects representing the different components that can be used to format a list of values in a locale-aware fashion.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-ListFormat-formatToParts(list: Iterable<string>): { type: "element" | "literal", value: string; }[]--><!--Device-ListFormat-formatToParts(list: Iterable<string>): { type: "element" | "literal", value: string; }[]-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| list | Iterable&lt;string&gt; | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| { type: "element" \| "literal", value: string; }[] | []} An Array of components which contains the formatted parts from the list. |

