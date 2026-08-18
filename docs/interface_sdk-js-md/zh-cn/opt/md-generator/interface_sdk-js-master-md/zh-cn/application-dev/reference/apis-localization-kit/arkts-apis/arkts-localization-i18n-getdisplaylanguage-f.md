# getDisplayLanguage

## 导入模块

```TypeScript
```

## getDisplayLanguage

```TypeScript
export function getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string
```

获取指定语言的本地化显示文本。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [getDisplayLanguage](arkts-localization-i18n-system-c.md#getdisplaylanguage)

<!--Device-i18n-export function getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string--><!--Device-i18n-export function getDisplayLanguage(language: string, locale: string, sentenceCase?: boolean): string-End-->

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| language | string | 是 |
| locale | string | 是 |
| sentenceCase | boolean | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let languageName: string = i18n.getDisplayLanguage('zh', 'en-GB', true); // languageName = 'Chinese'
languageName = i18n.getDisplayLanguage('zh', 'en-GB'); // languageName = 'Chinese'
```
