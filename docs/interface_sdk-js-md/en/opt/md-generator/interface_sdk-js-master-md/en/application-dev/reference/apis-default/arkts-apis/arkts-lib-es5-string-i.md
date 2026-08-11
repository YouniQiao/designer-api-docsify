# String

## charAt

```TypeScript
charAt(pos: number): string
```

Returns the character at the specified index.

<!--Device-String-charAt(pos: number): string--><!--Device-String-charAt(pos: number): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pos | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## charCodeAt

```TypeScript
charCodeAt(index: number): number
```

Returns the Unicode value of the character at the specified location.

<!--Device-String-charCodeAt(index: number): number--><!--Device-String-charCodeAt(index: number): number-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| index | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## concat

```TypeScript
concat(...strings: string[]): string
```

Returns a string that contains the concatenation of two or more strings.

<!--Device-String-concat(...strings: string[]): string--><!--Device-String-concat(...strings: string[]): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strings | string[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## indexOf

```TypeScript
indexOf(searchString: string, position?: number): number
```

Returns the position of the first occurrence of a substring.

<!--Device-String-indexOf(searchString: string, position?: number): number--><!--Device-String-indexOf(searchString: string, position?: number): number-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchString | string | Yes |
| position | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## lastIndexOf

```TypeScript
lastIndexOf(searchString: string, position?: number): number
```

Returns the last occurrence of a substring in the string.

<!--Device-String-lastIndexOf(searchString: string, position?: number): number--><!--Device-String-lastIndexOf(searchString: string, position?: number): number-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchString | string | Yes |
| position | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## localeCompare

```TypeScript
localeCompare(that: string, locales?: string | string[], options?: Intl.CollatorOptions): number
```

Determines whether two strings are equivalent in the current or specified locale.

<!--Device-String-localeCompare(that: string, locales?: string | string[], options?: Intl.CollatorOptions): number--><!--Device-String-localeCompare(that: string, locales?: string | string[], options?: Intl.CollatorOptions): number-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| that | string | Yes |
| locales | string \| string[] | No |
| options | Intl.CollatorOptions | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## match

```TypeScript
match(regexp: string | RegExp): RegExpMatchArray | null
```

Matches a string with a regular expression, and returns an array containing the results of that search.

<!--Device-String-match(regexp: string | RegExp): RegExpMatchArray | null--><!--Device-String-match(regexp: string | RegExp): RegExpMatchArray | null-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| regexp | string \| RegExp | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [RegExpMatchArray](../../apis-arkts/arkts-apis/arkts-arkts-regexp-regexpmatcharray-c.md) |

## replace

```TypeScript
replace(searchValue: string | RegExp, replaceValue: string): string
```

Replaces text in a string, using a regular expression or search string.

<!--Device-String-replace(searchValue: string | RegExp, replaceValue: string): string--><!--Device-String-replace(searchValue: string | RegExp, replaceValue: string): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchValue | string \| RegExp | Yes |
| replaceValue | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## replace

```TypeScript
replace(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string
```

Replaces text in a string, using a regular expression or search string.

<!--Device-String-replace(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string--><!--Device-String-replace(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchValue | string \| RegExp | Yes |
| replacer | (substring: string, ...args: any[]) =&gt; string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## search

```TypeScript
search(regexp: string | RegExp): number
```

Finds the first substring match in a regular expression search.

<!--Device-String-search(regexp: string | RegExp): number--><!--Device-String-search(regexp: string | RegExp): number-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| regexp | string \| RegExp | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## slice

```TypeScript
slice(start?: number, end?: number): string
```

Returns a section of a string.

<!--Device-String-slice(start?: number, end?: number): string--><!--Device-String-slice(start?: number, end?: number): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | No |
| end | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## split

```TypeScript
split(separator: string | RegExp, limit?: number): string[]
```

Split a string into substrings using the specified separator and return them as an array.

<!--Device-String-split(separator: string | RegExp, limit?: number): string[]--><!--Device-String-split(separator: string | RegExp, limit?: number): string[]-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| separator | string \| RegExp | Yes |
| limit | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string[] |

## substr

```TypeScript
substr(from: number, length?: number): string
```

Gets a substring beginning at the specified location and having the specified length.

**Deprecated since:** legacy feature for browser compatibility

<!--Device-String-substr(from: number, length?: number): string--><!--Device-String-substr(from: number, length?: number): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| from | number | Yes |
| [length](#length) | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## substring

```TypeScript
substring(start: number, end?: number): string
```

Returns the substring at the specified location within a String object.

<!--Device-String-substring(start: number, end?: number): string--><!--Device-String-substring(start: number, end?: number): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| start | number | Yes |
| end | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## toLocaleLowerCase

```TypeScript
toLocaleLowerCase(locales?: string | string[]): string
```

Converts all alphabetic characters to lowercase, taking into account the host environment's current locale.

<!--Device-String-toLocaleLowerCase(locales?: string | string[]): string--><!--Device-String-toLocaleLowerCase(locales?: string | string[]): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | string \| string[] | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## toLocaleUpperCase

```TypeScript
toLocaleUpperCase(locales?: string | string[]): string
```

Returns a string where all alphabetic characters have been converted to uppercase, taking into account the host environment's current locale.

<!--Device-String-toLocaleUpperCase(locales?: string | string[]): string--><!--Device-String-toLocaleUpperCase(locales?: string | string[]): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locales | string \| string[] | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## toLowerCase

```TypeScript
toLowerCase(): string
```

Converts all the alphabetic characters in a string to lowercase.

<!--Device-String-toLowerCase(): string--><!--Device-String-toLowerCase(): string-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## toString

```TypeScript
toString(): string
```

Returns a string representation of a string.

<!--Device-String-toString(): string--><!--Device-String-toString(): string-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## toUpperCase

```TypeScript
toUpperCase(): string
```

Converts all the alphabetic characters in a string to uppercase.

<!--Device-String-toUpperCase(): string--><!--Device-String-toUpperCase(): string-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## trim

```TypeScript
trim(): string
```

Removes the leading and trailing white space and line terminator characters from a string.

<!--Device-String-trim(): string--><!--Device-String-trim(): string-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## valueOf

```TypeScript
valueOf(): string
```

Returns the primitive value of the specified object.

<!--Device-String-valueOf(): string--><!--Device-String-valueOf(): string-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

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

<!--Device-String-readonly length: number--><!--Device-String-readonly length: number-End-->
