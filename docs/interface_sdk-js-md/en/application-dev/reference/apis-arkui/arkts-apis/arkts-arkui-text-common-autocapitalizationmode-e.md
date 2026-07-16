# AutoCapitalizationMode

Enumerates automatic capitalization modes. This only provides API capabilities; the specific implementation depends on the input method application.

**Since:** 20

<!--Device-unnamed-declare enum AutoCapitalizationMode--><!--Device-unnamed-declare enum AutoCapitalizationMode-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## NONE

```TypeScript
NONE = 0
```

Default state; automatic capitalization is disabled.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AutoCapitalizationMode-NONE = 0--><!--Device-AutoCapitalizationMode-NONE = 0-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## WORDS

```TypeScript
WORDS = 1
```

Automatic capitalization is applied per word: The first character of each word is capitalized, others are lowercase.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AutoCapitalizationMode-WORDS = 1--><!--Device-AutoCapitalizationMode-WORDS = 1-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## SENTENCES

```TypeScript
SENTENCES = 2
```

Automatic capitalization is applied per sentence: The first character of each sentence is capitalized, others are lowercase.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AutoCapitalizationMode-SENTENCES = 2--><!--Device-AutoCapitalizationMode-SENTENCES = 2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ALL_CHARACTERS

```TypeScript
ALL_CHARACTERS = 3
```

Automatic capitalization applied to all characters.

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AutoCapitalizationMode-ALL_CHARACTERS = 3--><!--Device-AutoCapitalizationMode-ALL_CHARACTERS = 3-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

