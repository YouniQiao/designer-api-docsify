# getSystemLanguage

## 导入模块

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## getSystemLanguage

```TypeScript
export function getSystemLanguage(): string
```

获取系统语言。

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为7。

**废弃版本：** 9

**替代接口：** [getSystemLanguage](arkts-localization-i18n-system-c.md#getsystemlanguage)

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let systemLanguage: string = i18n.System.getSystemLanguage(); // 如果系统语言为简体中文，systemLanguage = 'zh-Hans'
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let systemLanguage: string = i18n.getSystemLanguage();
```
