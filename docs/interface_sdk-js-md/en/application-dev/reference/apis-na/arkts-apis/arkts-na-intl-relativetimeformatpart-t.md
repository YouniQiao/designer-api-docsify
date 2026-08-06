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

An object representing the relative time format in parts that can be used for custom locale-aware formatting. \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**ArkTS mode:** ArkTS-Dyn only

<!--Device-Intl-type RelativeTimeFormatPart =        | {              type: "literal";              value: string;          }        | {              type: Exclude<NumberFormatPartTypes, "literal">;              value: string;              unit: RelativeTimeFormatUnitSingular;          }--><!--Device-Intl-type RelativeTimeFormatPart =        | {              type: "literal";              value: string;          }        | {              type: Exclude<NumberFormatPartTypes, "literal">;              value: string;              unit: RelativeTimeFormatUnitSingular;          }-End-->

| Type | Description |
| --- | --- |
| {               type: "literal"               value: string           } |  |
| {               type: Exclude&lt;NumberFormatPartTypes, "literal"&gt;               value: string               unit: RelativeTimeFormatUnitSingular           } |  |

