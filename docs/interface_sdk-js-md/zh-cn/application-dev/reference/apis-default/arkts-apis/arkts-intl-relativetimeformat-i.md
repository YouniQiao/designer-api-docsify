# RelativeTimeFormat

**ArkTS模式：** 仅支持ArkTS-Dyn

## format

```TypeScript
format(value: number, unit: RelativeTimeFormatUnit): string
```

Formats a value and a unit according to the locale and formatting options of the given  
[`Intl.RelativeTimeFormat`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/RelativeTimeFormat)object.

While this method automatically provides the correct plural forms,the grammatical form is otherwise as neutral as possible.

It is the caller's responsibility to handle cut-off logic such as deciding between displaying "in 7 days" or "in 1 week".This API does not support relative dates involving compound units.e.g "in 5 days and 4 hours".

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-RelativeTimeFormat-format(value: number, unit: RelativeTimeFormatUnit): string--><!--Device-RelativeTimeFormat-format(value: number, unit: RelativeTimeFormatUnit): string-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 |  |
| unit | [RelativeTimeFormatUnit](arkts-intl-relativetimeformatunit-t.md) | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | Internationalized relative time message as string |

## formatToParts

```TypeScript
formatToParts(value: number, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]
```

Returns an array of objects representing the relative time format in parts that can be used for custom locale-aware formatting.

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-RelativeTimeFormat-formatToParts(value: number, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]--><!--Device-RelativeTimeFormat-formatToParts(value: number, unit: RelativeTimeFormatUnit): RelativeTimeFormatPart[]-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 |  |
| unit | [RelativeTimeFormatUnit](arkts-intl-relativetimeformatunit-t.md) | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RelativeTimeFormatPart](arkts-intl-relativetimeformatpart-t.md)[] |  |

## resolvedOptions

```TypeScript
resolvedOptions(): ResolvedRelativeTimeFormatOptions
```

Provides access to the locale and options computed during initialization of this `Intl.RelativeTimeFormat` object.

[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/resolvedOptions).

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-RelativeTimeFormat-resolvedOptions(): ResolvedRelativeTimeFormatOptions--><!--Device-RelativeTimeFormat-resolvedOptions(): ResolvedRelativeTimeFormatOptions-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedRelativeTimeFormatOptions](arkts-intl-resolvedrelativetimeformatoptions-i.md) |  |

