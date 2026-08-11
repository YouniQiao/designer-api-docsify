# DisplayNames

## of

```TypeScript
of(code: string): string | undefined
```

Receives a code and returns a string based on the locale and options provided when instantiating  
[`Intl.DisplayNames()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames)

<!--Device-DisplayNames-of(code: string): string | undefined--><!--Device-DisplayNames-of(code: string): string | undefined-End-->

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| code | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## resolvedOptions

```TypeScript
resolvedOptions(): ResolvedDisplayNamesOptions
```

Returns a new object with properties reflecting the locale and style formatting options computed during the construction of the current  
[`Intl/DisplayNames`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames) object.

[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/resolvedOptions).

<!--Device-DisplayNames-resolvedOptions(): ResolvedDisplayNamesOptions--><!--Device-DisplayNames-resolvedOptions(): ResolvedDisplayNamesOptions-End-->

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ResolvedDisplayNamesOptions](../../apis-arkts/arkts-apis/arkts-arkts-intl-resolveddisplaynamesoptions-i.md) |
