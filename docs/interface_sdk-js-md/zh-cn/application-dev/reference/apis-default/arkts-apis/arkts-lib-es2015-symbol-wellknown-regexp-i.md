# RegExp

**ArkTS模式：** 仅支持ArkTS-Dyn

## [Symbol.match]

```TypeScript
[Symbol.match](string: string): RegExpMatchArray | null
```

Matches a string with this regular expression, and returns an array containing the results of that search.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-RegExp-[Symbol.match](string: string): RegExpMatchArray | null--><!--Device-RegExp-[Symbol.match](string: string): RegExpMatchArray | null-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| string | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RegExpMatchArray](../../apis-arkts/arkts-apis/arkts-arkts-regexp-regexpmatcharray-c.md) |  |

## [Symbol.replace]

```TypeScript
[Symbol.replace](string: string, replaceValue: string): string
```

Replaces text in a string, using this regular expression.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-RegExp-[Symbol.replace](string: string, replaceValue: string): string--><!--Device-RegExp-[Symbol.replace](string: string, replaceValue: string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| string | string | 是 |  |
| replaceValue | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## [Symbol.replace]

```TypeScript
[Symbol.replace](string: string, replacer: (substring: string, ...args: any[]) => string): string
```

Replaces text in a string, using this regular expression.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-RegExp-[Symbol.replace](string: string, replacer: (substring: string, ...args: any[]) => string): string--><!--Device-RegExp-[Symbol.replace](string: string, replacer: (substring: string, ...args: any[]) => string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| string | string | 是 |  |
| replacer | (substring: string, ...args: any[]) =&gt; string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## [Symbol.search]

```TypeScript
[Symbol.search](string: string): number
```

Finds the position beginning first substring match in a regular expression search using this regular expression.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-RegExp-[Symbol.search](string: string): number--><!--Device-RegExp-[Symbol.search](string: string): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| string | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## [Symbol.split]

```TypeScript
[Symbol.split](string: string, limit?: number): string[]
```

Returns an array of substrings that were delimited by strings in the original input that match against this regular expression.

If the regular expression contains capturing parentheses, then each time this regular expression matches, the results (including any undefined results) of the capturing parentheses are spliced.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-RegExp-[Symbol.split](string: string, limit?: number): string[]--><!--Device-RegExp-[Symbol.split](string: string, limit?: number): string[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| string | string | 是 |  |
| limit | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] |  |

