# px2vp

## px2vp

```TypeScript
declare function px2vp(value: number): number
```

Converts a number in units of px to a number in units of vp.By default, the virtual pixel ratio of the screen where the current UI instance is located is used for conversion.If no UI instance is available, the virtual pixel ratio of the default screen is used instead.

**Since:** 11

**Deprecated since:** 18

**Substitutes:** [px2vp](ohos.arkui.UIContext.UIContext#px2vp)

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 11.

<!--Device-unnamed-declare function px2vp(value: number): number--><!--Device-unnamed-declare function px2vp(value: number): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |
