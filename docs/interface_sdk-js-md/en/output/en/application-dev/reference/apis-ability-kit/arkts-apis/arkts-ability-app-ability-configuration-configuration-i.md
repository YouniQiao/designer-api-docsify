# Configuration

The module defines the environment variables for the application runtime, including language, dark/light color mode, screen orientation, and font size. You can subscribe to these environment variables to adapt to different user preferences and enhance the interaction experience.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface Configuration--><!--Device-unnamed-export interface Configuration-End-->

**System capability:** SystemCapability.Ability.AbilityBase

## colorMode

```TypeScript
colorMode?: ConfigurationConstant.ColorMode
```

Dark/Light color mode of the application. The light color mode is used by default. You can \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ . The options are as follows: - **COLOR\_MODE\_NOT\_SET**: The color mode is not set. - **COLOR\_MODE\_LIGHT**: light mode. - **COLOR\_MODE\_DARK**: dark mode.

**Type:** ConfigurationConstant.ColorMode

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Configuration-colorMode?: ConfigurationConstant.ColorMode--><!--Device-Configuration-colorMode?: ConfigurationConstant.ColorMode-End-->

**System capability:** SystemCapability.Ability.AbilityBase

## direction

```TypeScript
direction?: ConfigurationConstant.Direction
```

Screen orientation of the application. The options are as follows: - **DIRECTION\_NOT\_SET**: The screen orientation is not set. - **DIRECTION\_HORIZONTAL**: horizontal direction. - **DIRECTION\_VERTICAL**: vertical direction. You can subscribe to changes to this environment variable in the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ and \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_, but not in the \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ or \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_.

**Type:** ConfigurationConstant.Direction

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Configuration-direction?: ConfigurationConstant.Direction--><!--Device-Configuration-direction?: ConfigurationConstant.Direction-End-->

**System capability:** SystemCapability.Ability.AbilityBase

## displayId

```TypeScript
displayId?: long
```

ID of the display where the application is located. You can subscribe to changes to this environment variable in the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ and \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_, but not in the \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ or \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_.

**Type:** long

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Configuration-displayId?: long--><!--Device-Configuration-displayId?: long-End-->

**System capability:** SystemCapability.Ability.AbilityBase

## fontId

```TypeScript
fontId?: string
```

Unique ID of the font.

**Type:** string

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-Configuration-fontId?: string--><!--Device-Configuration-fontId?: string-End-->

**System capability:** SystemCapability.Ability.AbilityBase

## fontSizeScale

```TypeScript
fontSizeScale?: double
```

Font size scale ratio. The value is a non-negative number. The default value is **1**. You can \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ .

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Configuration-fontSizeScale?: double--><!--Device-Configuration-fontSizeScale?: double-End-->

**System capability:** SystemCapability.Ability.AbilityBase

## fontWeightScale

```TypeScript
fontWeightScale?: double
```

Font weight scale ratio. The value is a non-negative number. The default value is **1**.

**Type:** double

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Configuration-fontWeightScale?: double--><!--Device-Configuration-fontWeightScale?: double-End-->

**System capability:** SystemCapability.Ability.AbilityBase

## hasPointerDevice

```TypeScript
hasPointerDevice?: boolean
```

Whether a pointer device, such as a keyboard, mouse, or touchpad, is connected. **true** if connected, **false** otherwise.

**Type:** boolean

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Configuration-hasPointerDevice?: boolean--><!--Device-Configuration-hasPointerDevice?: boolean-End-->

**System capability:** SystemCapability.Ability.AbilityBase

## language

```TypeScript
language?: string
```

Current language of the application, for example, **zh** (Chinese) or **en** (English). You can \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ . For details about the value range, see \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_.

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Configuration-language?: string--><!--Device-Configuration-language?: string-End-->

**System capability:** SystemCapability.Ability.AbilityBase

## locale

```TypeScript
locale?: Intl.Locale
```

Locale. The application automatically adjusts its behavior based on the current locale to meet the localization requirements of users. This property can be set by configuring the system language, system region, and application preferred language.

**Type:** Intl.Locale

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-Configuration-locale?: Intl.Locale--><!--Device-Configuration-locale?: Intl.Locale-End-->

**System capability:** SystemCapability.Ability.AbilityBase

## mcc

```TypeScript
mcc?: string
```

Mobile country code.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Configuration-mcc?: string--><!--Device-Configuration-mcc?: string-End-->

**System capability:** SystemCapability.Ability.AbilityBase

## mnc

```TypeScript
mnc?: string
```

Mobile network code.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Configuration-mnc?: string--><!--Device-Configuration-mnc?: string-End-->

**System capability:** SystemCapability.Ability.AbilityBase

## screenDensity

```TypeScript
screenDensity?: ConfigurationConstant.ScreenDensity
```

Screen density. The options are as follows: - **SCREEN\_DENSITY\_NOT\_SET**: The pixel density is not set. - **SCREEN\_DENSITY\_SDPI**: 120. - **SCREEN\_DENSITY\_MDPI**: 160. - **SCREEN\_DENSITY\_LDPI**: 240. - **SCREEN\_DENSITY\_XLDPI**: 320. - **SCREEN\_DENSITY\_XXLDPI**: 480. - **SCREEN\_DENSITY\_XXXLDPI**: 640. The font size is positively correlated with the screen pixel density. By monitoring changes in the screen pixel density, you can detect adjustments in the font size. Typically, for the same physical size, the higher the screen pixel density, the larger the font display effect. You can subscribe to changes to this environment variable in the \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ and \_\_\_MD\_LINK\_DESC\_USD\_1\_\_\_, but not in the \_\_\_MD\_LINK\_DESC\_USD\_2\_\_\_ or \_\_\_MD\_LINK\_DESC\_USD\_3\_\_\_.

**Type:** ConfigurationConstant.ScreenDensity

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Configuration-screenDensity?: ConfigurationConstant.ScreenDensity--><!--Device-Configuration-screenDensity?: ConfigurationConstant.ScreenDensity-End-->

**System capability:** SystemCapability.Ability.AbilityBase

