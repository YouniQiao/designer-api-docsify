# String

**ArkTS模式：** 仅支持ArkTS-Dyn

## charAt

```TypeScript
charAt(pos: number): string
```

Returns the character at the specified index.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-charAt(pos: number): string--><!--Device-String-charAt(pos: number): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pos | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## charCodeAt

```TypeScript
charCodeAt(index: number): number
```

Returns the Unicode value of the character at the specified location.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-charCodeAt(index: number): number--><!--Device-String-charCodeAt(index: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## concat

```TypeScript
concat(...strings: string[]): string
```

Returns a string that contains the concatenation of two or more strings.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-concat(...strings: string[]): string--><!--Device-String-concat(...strings: string[]): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strings | string[] | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## indexOf

```TypeScript
indexOf(searchString: string, position?: number): number
```

Returns the position of the first occurrence of a substring.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-indexOf(searchString: string, position?: number): number--><!--Device-String-indexOf(searchString: string, position?: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchString | string | 是 |  |
| position | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## lastIndexOf

```TypeScript
lastIndexOf(searchString: string, position?: number): number
```

Returns the last occurrence of a substring in the string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-lastIndexOf(searchString: string, position?: number): number--><!--Device-String-lastIndexOf(searchString: string, position?: number): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchString | string | 是 |  |
| position | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## localeCompare

```TypeScript
localeCompare(that: string, locales?: string | string[], options?: Intl.CollatorOptions): number
```

Determines whether two strings are equivalent in the current or specified locale.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-localeCompare(that: string, locales?: string | string[], options?: Intl.CollatorOptions): number--><!--Device-String-localeCompare(that: string, locales?: string | string[], options?: Intl.CollatorOptions): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| that | string | 是 |  |
| locales | string \| string[] | 否 |  |
| options | Intl.CollatorOptions | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## match

```TypeScript
match(regexp: string | RegExp): RegExpMatchArray | null
```

Matches a string with a regular expression, and returns an array containing the results of that search.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-match(regexp: string | RegExp): RegExpMatchArray | null--><!--Device-String-match(regexp: string | RegExp): RegExpMatchArray | null-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| regexp | string \| RegExp | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RegExpMatchArray](../../apis-arkts/arkts-apis/arkts-arkts-regexp-regexpmatcharray-c.md) |  |

## replace

```TypeScript
replace(searchValue: string | RegExp, replaceValue: string): string
```

Replaces text in a string, using a regular expression or search string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-replace(searchValue: string | RegExp, replaceValue: string): string--><!--Device-String-replace(searchValue: string | RegExp, replaceValue: string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchValue | string \| RegExp | 是 |  |
| replaceValue | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## replace

```TypeScript
replace(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string
```

Replaces text in a string, using a regular expression or search string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-replace(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string--><!--Device-String-replace(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| searchValue | string \| RegExp | 是 |  |
| replacer | (substring: string, ...args: any[]) =&gt; string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## search

```TypeScript
search(regexp: string | RegExp): number
```

Finds the first substring match in a regular expression search.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-search(regexp: string | RegExp): number--><!--Device-String-search(regexp: string | RegExp): number-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| regexp | string \| RegExp | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number |  |

## slice

```TypeScript
slice(start?: number, end?: number): string
```

Returns a section of a string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-slice(start?: number, end?: number): string--><!--Device-String-slice(start?: number, end?: number): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 否 |  |
| end | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## split

```TypeScript
split(separator: string | RegExp, limit?: number): string[]
```

Split a string into substrings using the specified separator and return them as an array.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-split(separator: string | RegExp, limit?: number): string[]--><!--Device-String-split(separator: string | RegExp, limit?: number): string[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| separator | string \| RegExp | 是 |  |
| limit | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string[] |  |

## substr

```TypeScript
substr(from: number, length?: number): string
```

Gets a substring beginning at the specified location and having the specified length.

**ArkTS模式：** 仅支持ArkTS-Dyn

**废弃版本：** legacy feature for browser compatibility

<!--Device-String-substr(from: number, length?: number): string--><!--Device-String-substr(from: number, length?: number): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | number | 是 |  |
| length | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## substring

```TypeScript
substring(start: number, end?: number): string
```

Returns the substring at the specified location within a String object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-substring(start: number, end?: number): string--><!--Device-String-substring(start: number, end?: number): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| start | number | 是 |  |
| end | number | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## toLocaleLowerCase

```TypeScript
toLocaleLowerCase(locales?: string | string[]): string
```

Converts all alphabetic characters to lowercase, taking into account the host environment's current locale.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-toLocaleLowerCase(locales?: string | string[]): string--><!--Device-String-toLocaleLowerCase(locales?: string | string[]): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## toLocaleUpperCase

```TypeScript
toLocaleUpperCase(locales?: string | string[]): string
```

Returns a string where all alphabetic characters have been converted to uppercase, taking into account the host environment's current locale.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-toLocaleUpperCase(locales?: string | string[]): string--><!--Device-String-toLocaleUpperCase(locales?: string | string[]): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| locales | string \| string[] | 否 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## toLowerCase

```TypeScript
toLowerCase(): string
```

Converts all the alphabetic characters in a string to lowercase.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-toLowerCase(): string--><!--Device-String-toLowerCase(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## toString

```TypeScript
toString(): string
```

Returns a string representation of a string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-toString(): string--><!--Device-String-toString(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## toUpperCase

```TypeScript
toUpperCase(): string
```

Converts all the alphabetic characters in a string to uppercase.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-toUpperCase(): string--><!--Device-String-toUpperCase(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## trim

```TypeScript
trim(): string
```

Removes the leading and trailing white space and line terminator characters from a string.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-trim(): string--><!--Device-String-trim(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## valueOf

```TypeScript
valueOf(): string
```

Returns the primitive value of the specified object.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-valueOf(): string--><!--Device-String-valueOf(): string-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## [index: number]

```TypeScript
readonly [index: number]: string
```

**类型：** string

**ArkTS模式：** 仅支持ArkTS-Dyn

## length

```TypeScript
readonly length: number
```

Returns the length of a String object.

**类型：** number

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-String-readonly length: number--><!--Device-String-readonly length: number-End-->

