# ButtonType

Enumerates the button types. &gt; **NOTE：**&gt; &gt; - The corner radius of the rounded rectangle button is set using the universal attribute &gt; borderRadius. &gt; &gt; - For a button of the **Capsule** type, the **borderRadius** settings do not take effect, and the radius of its &gt; rounded corner is always half of the button height or width, whichever is smaller. &gt; &gt; - For a button of the **Circle** type: (1) If both its width and height are set, **borderRadius** does not take &gt; effect, and the button radius is half of the width or height (whichever is smaller). (2) If either its width or &gt; height is set, **borderRadius** does not take effect, and the button radius is half of the set width or height. (3) &gt; If neither its width nor height is set, the button radius is as specified by **borderRadius**; if **borderRadius** &gt; is set to a negative value, the value **0** will be used. &gt; &gt; - The button text is set using [fontSize](arkts-arkui-button-attribute.md#fontsize), &gt; [fontColor](arkts-arkui-button-attribute.md#fontcolor), [fontStyle](arkts-arkui-button-attribute.md#fontstyle), &gt; [fontFamily](arkts-arkui-button-attribute.md#fontfamily), and [fontWeight](arkts-arkui-button-attribute.md#fontweight). &gt; &gt; - Before setting the gradient color, you need to set &gt; backgroundColor to transparent. &gt; &gt; - When **borderRadius** is not set, the corner radius of the rounded rectangle button remains at the default value. &gt; In this case, the corner radius does not change with the button height and is subject to the **controlSize** &gt; property. When **controlSize** is **NORMAL**, the corner radius is 20 vp; when **controlSize** is **SMALL**, the &gt; corner radius is 14 vp. &gt; &gt; - When border is set for the &gt; button, a default &gt; borderRadius value is &gt; automatically applied. When both **border** and **borderRadius** attributes are used, **borderRadius** must be &gt; specified after **border** to prevent the border radius from being overridden by the default radius value in the &gt; border style.

**Since:** 7

<!--Device-unnamed-declare enum ButtonType--><!--Device-unnamed-declare enum ButtonType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Capsule

```TypeScript
Capsule
```

Capsule-type button (the round corner is half of the height by default).

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonType-Capsule--><!--Device-ButtonType-Capsule-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Circle

```TypeScript
Circle
```

Circular button.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonType-Circle--><!--Device-ButtonType-Circle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Normal

```TypeScript
Normal
```

Normal button, with no rounded corners by default.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ButtonType-Normal--><!--Device-ButtonType-Normal-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ROUNDED_RECTANGLE

```TypeScript
ROUNDED_RECTANGLE = 3
```

Rounded rectangle button (default value: when **controlSize** is **NORMAL**, the corner radius is 20 vp; when controlSize is **SMALL**, the corner radius is 14 vp).

**Since:** 15

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

**Widget capability:** This API can be used in ArkTS widgets since API version 15.

<!--Device-ButtonType-ROUNDED_RECTANGLE = 3--><!--Device-ButtonType-ROUNDED_RECTANGLE = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

