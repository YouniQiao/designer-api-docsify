# String

## replaceAll

```TypeScript
replaceAll(searchValue: string | RegExp, replaceValue: string): string
```

Replace all instances of a substring in a string, using a regular expression or search string.

<!--Device-String-replaceAll(searchValue: string | RegExp, replaceValue: string): string--><!--Device-String-replaceAll(searchValue: string | RegExp, replaceValue: string): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchValue | string \| RegExp | Yes |
| replaceValue | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## replaceAll

```TypeScript
replaceAll(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string
```

Replace all instances of a substring in a string, using a regular expression or search string.

<!--Device-String-replaceAll(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string--><!--Device-String-replaceAll(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| searchValue | string \| RegExp | Yes |
| replacer | (substring: string, ...args: any[]) =&gt; string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |
