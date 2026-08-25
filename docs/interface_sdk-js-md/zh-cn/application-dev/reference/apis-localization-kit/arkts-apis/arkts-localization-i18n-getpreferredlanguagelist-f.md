# getPreferredLanguageList

## 导入模块

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## getPreferredLanguageList

```TypeScript
export function getPreferredLanguageList(): Array<string>
```

获取系统偏好语言列表。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [getPreferredLanguageList](arkts-localization-i18n-system-c.md#getpreferredlanguagelist)

**系统能力：** SystemCapability.Global.I18n

**返回值：**

| 类型 |
| --- |
| Array & lt;string & gt; |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let preferredLanguageList: Array<string> = i18n.System.getPreferredLanguageList();
```

```TypeScript
import { i18n } from '@kit.LocalizationKit';

let preferredLanguageList: Array<string> = i18n.getPreferredLanguageList();
```
