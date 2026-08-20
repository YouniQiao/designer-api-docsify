# String

**Since:** -1

<!--Device-unnamed-interface String--><!--Device-unnamed-interface String-End-->

## Modules to Import

```TypeScript
```

## replaceAll

```TypeScript
replaceAll(searchValue: string | RegExp, replaceValue: string): string
```

Replace all instances of a substring in a string, using a regular expression or search string.

**Since:** -1

<!--Device-String-replaceAll(searchValue: string | RegExp, replaceValue: string): string--><!--Device-String-replaceAll(searchValue: string | RegExp, replaceValue: string): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchValue | string \| RegExp | Yes |  |
| replaceValue | string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## replaceAll

```TypeScript
replaceAll(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string
```

Replace all instances of a substring in a string, using a regular expression or search string.

**Since:** -1

<!--Device-String-replaceAll(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string--><!--Device-String-replaceAll(searchValue: string | RegExp, replacer: (substring: string, ...args: any[]) => string): string-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| searchValue | string \| RegExp | Yes |  |
| replacer | (substring: string, ...args: any[]) =&gt; string | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
