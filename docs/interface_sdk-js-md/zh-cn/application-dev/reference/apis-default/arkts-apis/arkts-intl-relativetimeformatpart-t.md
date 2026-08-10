# RelativeTimeFormatPart

```TypeScript
type RelativeTimeFormatPart =
        | {
              type: "literal";
              value: string;
          }
        | {
              type: Exclude<NumberFormatPartTypes, "literal">;
              value: string;
              unit: RelativeTimeFormatUnitSingular;
          }
```

An object representing the relative time format in parts that can be used for custom locale-aware formatting.

[MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl/RelativeTimeFormat/formatToParts#Using_formatToParts).

**ArkTS模式：** 仅支持ArkTS-Dyn

<!--Device-Intl-type RelativeTimeFormatPart =        | {              type: "literal";              value: string;          }        | {              type: Exclude<NumberFormatPartTypes, "literal">;              value: string;              unit: RelativeTimeFormatUnitSingular;          }--><!--Device-Intl-type RelativeTimeFormatPart =        | {              type: "literal";              value: string;          }        | {              type: Exclude<NumberFormatPartTypes, "literal">;              value: string;              unit: RelativeTimeFormatUnitSingular;          }-End-->

| 类型 | 说明 |
| --- | --- |
| {               type: "literal"               value: string           } |  |
| {               type: Exclude&lt;NumberFormatPartTypes, "literal"&gt;               value: string               unit: RelativeTimeFormatUnitSingular           } |  |

