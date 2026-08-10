# DisplayNames

**ArkTS模式：** 仅支持ArkTS-Dyn

## of

```TypeScript
of(code: string): string | undefined
```

Receives a code and returns a string based on the locale and options provided when instantiating  
[`Intl.DisplayNames()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames)

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DisplayNames-of(code: string): string | undefined--><!--Device-DisplayNames-of(code: string): string | undefined-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | string | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string |  |

## resolvedOptions

```TypeScript
resolvedOptions(): ResolvedDisplayNamesOptions
```

Returns a new object with properties reflecting the locale and style formatting options computed during the construction of the current  
[`Intl/DisplayNames`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames) object.

[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/DisplayNames/resolvedOptions).

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-DisplayNames-resolvedOptions(): ResolvedDisplayNamesOptions--><!--Device-DisplayNames-resolvedOptions(): ResolvedDisplayNamesOptions-End-->

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ResolvedDisplayNamesOptions](../../apis-arkts/arkts-apis/arkts-arkts-intl-resolveddisplaynamesoptions-i.md) |  |

