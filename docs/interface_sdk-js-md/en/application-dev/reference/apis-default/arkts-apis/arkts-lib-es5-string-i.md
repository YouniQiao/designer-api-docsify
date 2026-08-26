# String

## Modules to Import

```TypeScript
```

## charAt

```TypeScript
charAt(pos: number): string
```

Returns the character at the specified index.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| pos | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## charCodeAt

```TypeScript
charCodeAt(index: number): number
```

Returns the Unicode value of the character at the specified location.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | number | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## concat

```TypeScript
concat(...strings: string[]): string
```

Returns a string that contains the concatenation of two or more strings.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| strings | string[] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## indexOf

```TypeScript
indexOf(searchString: string, position?: number): number
```

Returns the position of the first occurrence of a substring.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchString | string | Yes |  |
| position | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## lastIndexOf

```TypeScript
lastIndexOf(searchString: string, position?: number): number
```

Returns the last occurrence of a substring in the string.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchString | string | Yes |  |
| position | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## localeCompare

```TypeScript
localeCompare(that: string, locales?: string | string[], options?: Intl.CollatorOptions): number
```

Determines whether two strings are equivalent in the current or specified locale.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| that | string | Yes |  |
| locales | string \| string[] | No |  |
| options | [Intl.CollatorOptions](arkts-intl-collatoroptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## match

```TypeScript
match(regexp: string | RegExp): RegExpMatchArray | null
```

Matches a string with a regular expression, and returns an array containing the results of that search.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| regexp | string \| RegExp | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## replace

```TypeScript
replace(searchValue: string | RegExp, replaceValue: string): string
```

Replaces text in a string, using a regular expression or search string.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchValue | string \| RegExp | Yes |  |
| replaceValue | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## replace

```TypeScript
replace(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string
```

Replaces text in a string, using a regular expression or search string.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchValue | string \| RegExp | Yes |  |
| replacer | (substring: string, ...args: any[]) = & gt; string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## search

```TypeScript
search(regexp: string | RegExp): number
```

Finds the first substring match in a regular expression search.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| regexp | string \| RegExp | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## slice

```TypeScript
slice(start?: number, end?: number): string
```

Returns a section of a string.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | number | No |  |
| end | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## split

```TypeScript
split(separator: string | RegExp, limit?: number): string[]
```

Split a string into substrings using the specified separator and return them as an array.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| separator | string \| RegExp | Yes |  |
| limit | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## substr

```TypeScript
substr(from: number, length?: number): string
```

Gets a substring beginning at the specified location and having the specified length.

**Deprecated since:** legacy feature for browser compatibility

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| from | number | Yes |  |
| length | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## substring

```TypeScript
substring(start: number, end?: number): string
```

Returns the substring at the specified location within a String object.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| start | number | Yes |  |
| end | number | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## toLocaleLowerCase

```TypeScript
toLocaleLowerCase(locales?: string | string[]): string
```

Converts all alphabetic characters to lowercase, taking into account the host environment's current locale.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | string \| string[] | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## toLocaleUpperCase

```TypeScript
toLocaleUpperCase(locales?: string | string[]): string
```

Returns a string where all alphabetic characters have been converted to uppercase, taking into account the host environment's current locale.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| locales | string \| string[] | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## toLowerCase

```TypeScript
toLowerCase(): string
```

Converts all the alphabetic characters in a string to lowercase.

**Return value:**

| Type | Description |
| --- | --- |
## toString

```TypeScript
toString(): string
```

Returns a string representation of a string.

**Return value:**

| Type | Description |
| --- | --- |
## toUpperCase

```TypeScript
toUpperCase(): string
```

Converts all the alphabetic characters in a string to uppercase.

**Return value:**

| Type | Description |
| --- | --- |
## trim

```TypeScript
trim(): string
```

Removes the leading and trailing white space and line terminator characters from a string.

**Return value:**

| Type | Description |
| --- | --- |
## valueOf

```TypeScript
valueOf(): string
```

Returns the primitive value of the specified object.

**Return value:**

| Type | Description |
| --- | --- |
## [index: number]

```TypeScript
readonly [index: number]: string
```

**Type:** string

## length

```TypeScript
readonly length: number
```

Returns the length of a String object.

**Type:** number
