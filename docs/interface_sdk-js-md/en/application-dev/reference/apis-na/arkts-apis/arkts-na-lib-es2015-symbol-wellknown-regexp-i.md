# RegExp

**Since:** -1

<!--Device-unnamed-interface RegExp--><!--Device-unnamed-interface RegExp-End-->

## Modules to Import

```TypeScript
```

## [Symbol.match]

```TypeScript
[Symbol.match](string: string): RegExpMatchArray | null
```

Matches a string with this regular expression, and returns an array containing the results of that search.

**Since:** -1

<!--Device-RegExp-[Symbol.match](string: string): RegExpMatchArray | null--><!--Device-RegExp-[Symbol.match](string: string): RegExpMatchArray | null-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| string | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## [Symbol.replace]

```TypeScript
[Symbol.replace](string: string, replaceValue: string): string
```

Replaces text in a string, using this regular expression.

**Since:** -1

<!--Device-RegExp-[Symbol.replace](string: string, replaceValue: string): string--><!--Device-RegExp-[Symbol.replace](string: string, replaceValue: string): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| string | string | Yes |  |
| replaceValue | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## [Symbol.replace]

```TypeScript
[Symbol.replace](string: string, replacer: (substring: string, ...args: any[]) => string): string
```

Replaces text in a string, using this regular expression.

**Since:** -1

<!--Device-RegExp-[Symbol.replace](string: string, replacer: (substring: string, ...args: any[]) => string): string--><!--Device-RegExp-[Symbol.replace](string: string, replacer: (substring: string, ...args: any[]) => string): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| string | string | Yes |  |
| replacer | (substring: string, ...args: any[]) =&gt; string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## [Symbol.search]

```TypeScript
[Symbol.search](string: string): number
```

Finds the position beginning first substring match in a regular expression search using this regular expression.

**Since:** -1

<!--Device-RegExp-[Symbol.search](string: string): number--><!--Device-RegExp-[Symbol.search](string: string): number-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| string | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## [Symbol.split]

```TypeScript
[Symbol.split](string: string, limit?: number): string[]
```

Returns an array of substrings that were delimited by strings in the original input that match against this regular expression. If the regular expression contains capturing parentheses, then each time this regular expression matches, the results (including any undefined results) of the capturing parentheses are spliced.

**Since:** -1

<!--Device-RegExp-[Symbol.split](string: string, limit?: number): string[]--><!--Device-RegExp-[Symbol.split](string: string, limit?: number): string[]-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| string | string | Yes |  |
| limit | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
