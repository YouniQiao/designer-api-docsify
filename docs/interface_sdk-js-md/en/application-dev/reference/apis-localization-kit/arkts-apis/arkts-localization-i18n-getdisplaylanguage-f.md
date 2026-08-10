# getDisplayLanguage

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## getDisplayLanguage

```TypeScript
export function getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string
```

获取指定语言的本地化显示文本。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** [i18n.System.getDisplayLanguage](arkts-localization-i18n-system-c.md#getdisplaylanguage)

<!--Device-i18n-export function getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string--><!--Device-i18n-export function getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | Yes | 指定语言。 |
| locale | string | Yes | [表示区域ID的字符串](../../../internationalization/i18n-locale-culture.md#实现原理)，由语言、脚本、国家地区组成。 |
| sentenceCase | boolean | No | true表示按照首字母大写的格式显示文本，false表示按照区域默认的大小写格式显示文本。默认值：true。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 指定语言的本地化显示文本。 |

