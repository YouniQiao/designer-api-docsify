# String

## Modules to Import

```TypeScript
```

## match

```TypeScript
match(matcher: { [Symbol.match](string: string): RegExpMatchArray | null; }): RegExpMatchArray | null
```

Matches a string or an object that supports being matched against, and returns an array containing the results of that search, or null if no matches are found.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| matcher | { [Symbol.match](string: string): RegExpMatchArray \| null; } | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## replace

```TypeScript
replace(searchValue: { [Symbol.replace](string: string, replaceValue: string): string; }, replaceValue: string): string
```

Passes a string and {@linkcode replaceValue} to the `[Symbol.replace]` method on {@linkcode searchValue}. This method is expected to implement its own replacement algorithm.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchValue | { [Symbol.replace](string: string, replaceValue: string): string; } | Yes |
| replaceValue | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## replace

```TypeScript
replace(searchValue: { [Symbol.replace](string: string, replacer: (substring: string, ...args: any[]) => string): string; }, replacer: (substring: string, ...args: any[]) => string): string
```

Replaces text in a string, using an object that supports replacement within a string.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchValue | { [Symbol.replace](string: string, replacer: (substring: string, ...args: any[]) =&gt; string): string; } | Yes |
| replacer | (substring: string, ...args: any[]) = & gt; string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## search

```TypeScript
search(searcher: { [Symbol.search](string: string): number; }): number
```

Finds the first substring match in a regular expression search.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searcher | { [Symbol.search](string: string): number; } | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## split

```TypeScript
split(splitter: { [Symbol.split](string: string, limit?: number): string[]; }, limit?: number): string[]
```

Split a string into substrings using the specified separator and return them as an array.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| splitter | { [Symbol.split](string: string, limit?: number): string[]; } | Yes |
| limit | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
