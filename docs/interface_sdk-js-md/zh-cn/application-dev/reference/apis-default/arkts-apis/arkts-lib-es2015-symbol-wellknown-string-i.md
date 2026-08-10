# String

**ArkTS模式：** 仅支持ArkTS-Dyn

## match

```TypeScript
match(matcher: { [Symbol.match](string: string): RegExpMatchArray | null; }): RegExpMatchArray | null
```

Matches a string or an object that supports being matched against, and returns an array containing the results of that search, or null if no matches are found.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-match(matcher: { [Symbol.match](string: string): RegExpMatchArray | null; }): RegExpMatchArray | null--><!--Device-String-match(matcher: { [Symbol.match](string: string): RegExpMatchArray | null; }): RegExpMatchArray | null-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| matcher | { [Symbol.match](string: string): RegExpMatchArray \| null; } | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RegExpMatchArray](../../apis-arkts/arkts-apis/arkts-arkts-regexp-regexpmatcharray-c.md) |  |

## replace

```TypeScript
replace(searchValue: { [Symbol.replace](string: string, replaceValue: string): string; }, replaceValue: string): string
```

Passes a string and {@linkcode replaceValue} to the `[Symbol.replace]` method on {@linkcode searchValue}. This method is expected to implement its own replacement algorithm.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-replace(searchValue: { [Symbol.replace](string: string, replaceValue: string): string; }, replaceValue: string): string--><!--Device-String-replace(searchValue: { [Symbol.replace](string: string, replaceValue: string): string; }, replaceValue: string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchValue | { [Symbol.replace](string: string, replaceValue: string): string; } | 是 |  |
| replaceValue | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## replace

```TypeScript
replace(searchValue: { [Symbol.replace](string: string, replacer: (substring: string, ...args: any[]) => string): string; }, replacer: (substring: string, ...args: any[]) => string): string
```

Replaces text in a string, using an object that supports replacement within a string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-replace(searchValue: { [Symbol.replace](string: string, replacer: (substring: string, ...args: any[]) => string): string; }, replacer: (substring: string, ...args: any[]) => string): string--><!--Device-String-replace(searchValue: { [Symbol.replace](string: string, replacer: (substring: string, ...args: any[]) => string): string; }, replacer: (substring: string, ...args: any[]) => string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchValue | { [Symbol.replace](string: string, replacer: (substring: string, ...args: any[]) =&gt; string): string; } | 是 |  |
| replacer | (substring: string, ...args: any[]) =&gt; string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## search

```TypeScript
search(searcher: { [Symbol.search](string: string): number; }): number
```

Finds the first substring match in a regular expression search.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-search(searcher: { [Symbol.search](string: string): number; }): number--><!--Device-String-search(searcher: { [Symbol.search](string: string): number; }): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searcher | { [Symbol.search](string: string): number; } | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## split

```TypeScript
split(splitter: { [Symbol.split](string: string, limit?: number): string[]; }, limit?: number): string[]
```

Split a string into substrings using the specified separator and return them as an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-split(splitter: { [Symbol.split](string: string, limit?: number): string[]; }, limit?: number): string[]--><!--Device-String-split(splitter: { [Symbol.split](string: string, limit?: number): string[]; }, limit?: number): string[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| splitter | { [Symbol.split](string: string, limit?: number): string[]; } | 是 |  |
| limit | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] |  |

