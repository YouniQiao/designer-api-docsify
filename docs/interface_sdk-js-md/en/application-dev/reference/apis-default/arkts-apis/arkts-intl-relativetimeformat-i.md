# RelativeTimeFormat

**ArkTS mode:** 

## Modules to Import

```TypeScript
```

## format

```TypeScript
format(value: number, unit: RelativeTimeFormatUnit): string
```

Formats a value and a unit according to the locale and formatting options of the given [`Intl.RelativeTimeFormat`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/RelativeTimeFormat) object.While this method automatically provides the correct plural forms, the grammatical form is otherwise as neutral as possible.It is the caller's responsibility to handle cut-off logic such as deciding between displaying "in 7 days" or "in 1 week". This API does not support relative dates involving compound units. e.g "in 5 days and 4 hours".

**ArkTS mode:** 

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| unit | [RelativeTimeFormatUnit](arkts-intl-relativetimeformatunit-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## formatToParts

```TypeScript
formatToParts(value: number, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]
```

Returns an array of objects representing the relative time format in parts that can be used for custom locale-aware formatting.

**ArkTS mode:** 

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |
| unit | [RelativeTimeFormatUnit](arkts-intl-relativetimeformatunit-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
## resolvedOptions

```TypeScript
resolvedOptions(): ResolvedRelativeTimeFormatOptions
```

Provides access to the locale and options computed during initialization of this `Intl.RelativeTimeFormat` object.  
[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions).

**ArkTS mode:** 

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
