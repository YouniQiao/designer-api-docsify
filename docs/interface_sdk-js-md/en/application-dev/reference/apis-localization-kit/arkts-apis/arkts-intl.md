# @ohos.intl

/*
 Copyright (c) 2021 Huawei Device Co., Ltd.
 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 /


**Since:** 6

<!--Device-unnamed-declare namespace intl--><!--Device-unnamed-declare namespace intl-End-->

**System capability:** SystemCapability.Global.I18n

## Modules to Import

```TypeScript
import { intl } from '@kit.LocalizationKit';
import { intl } from '@kit.LocalizationKit';
```

## Summary

### Classes

| Name | Description |
| --- | --- |
| [Collator](arkts-localization-intl-collator-c.md) | Provides the string collation capability. |
| [DateTimeFormat](arkts-localization-intl-datetimeformat-c.md) | Performs date and time formatting. |
| [Locale](arkts-localization-intl-locale-c.md) | Provides APIs for obtaining locale information. |
| [NumberFormat](arkts-localization-intl-numberformat-c.md) | Provides the API for formatting number strings. |
| [PluralRules](arkts-localization-intl-pluralrules-c.md) | Provides the capability for obtaining the plural rule type. |
| [RelativeTimeFormat](arkts-localization-intl-relativetimeformat-c.md) | Provides the relative time formatting capability. |

### Interfaces

| Name | Description |
| --- | --- |
| [CollatorOptions](arkts-localization-intl-collatoroptions-i.md) | Defines the options for creating a **Collator** object. Since API version 9, the attributes in **CollatorOptions** are optional. |
| [DateTimeOptions](arkts-localization-intl-datetimeoptions-i.md) | Defines the options for a **DateTimeOptions** object. Since API version 9, the **DateTimeOptions** attribute is changed from mandatory to optional. |
| [LocaleOptions](arkts-localization-intl-localeoptions-i.md) | Options for initializing the **Locale** object. Since API version 9, the **LocaleOptions** attribute is changed from mandatory to optional. > **NOTE：**> > - For details about **calendar**, see Table 1 in > [Calendar Setting](../../../internationalization/i18n-calendar.md). |
| [NumberOptions](arkts-localization-intl-numberoptions-i.md) | Options for creating the **NumberFormat** object. Since API version 9, the **NumberOptions** attribute is changed from mandatory to optional. |
| [PluralRulesOptions](arkts-localization-intl-pluralrulesoptions-i.md) | Defines the options for creating a **PluralRules** object. Since API version 9, the **PluralRulesOptions** attribute is changed from mandatory to optional. |
| [RelativeTimeFormatInputOptions](arkts-localization-intl-relativetimeformatinputoptions-i.md) | Defines the configuration options for a **RelativeTimeFormat** object. Since API version 9, the attributes in **RelativeTimeFormatInputOptions** are optional. |
| [RelativeTimeFormatResolvedOptions](arkts-localization-intl-relativetimeformatresolvedoptions-i.md) | Represents the formatting options for the **RelativeTimeFormat** object. |

