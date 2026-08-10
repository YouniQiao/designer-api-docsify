# LocaleItem (System API)

语言或国家地区的组合信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-i18n-export interface LocaleItem--><!--Device-i18n-export interface LocaleItem-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## displayName

```TypeScript
displayName: string
```

id在SystemLocaleManager的指定区域下的表示。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-LocaleItem-displayName: string--><!--Device-LocaleItem-displayName: string-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## id

```TypeScript
id: string
```

语言代码或国家地区代码，如"zh"、"CN"。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-LocaleItem-id: string--><!--Device-LocaleItem-id: string-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## localName

```TypeScript
localName?: string
```

id的本地名称。只有在表示语言相关信息时才存在该选项。

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-LocaleItem-localName?: string--><!--Device-LocaleItem-localName?: string-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

## suggestionType

```TypeScript
suggestionType: SuggestionType
```

语言或国家地区推荐类型。

**Type:** [SuggestionType](arkts-localization-i18n-suggestiontype-e-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-LocaleItem-suggestionType: SuggestionType--><!--Device-LocaleItem-suggestionType: SuggestionType-End-->

**System capability:** SystemCapability.Global.I18n

**System API:** This is a system API.

