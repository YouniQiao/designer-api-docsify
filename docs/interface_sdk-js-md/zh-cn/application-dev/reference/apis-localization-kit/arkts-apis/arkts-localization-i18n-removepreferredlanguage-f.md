# removePreferredLanguage

## 导入模块

```TypeScript
import { i18n } from '@kit.LocalizationKit';
```

## removePreferredLanguage

```TypeScript
export function removePreferredLanguage(index: number): boolean
```

从系统偏好语言列表中移除指定位置的偏好语言。

**起始版本：** 8

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为8。

**废弃版本：** 9

**替代接口：** [removePreferredLanguage](arkts-localization-i18n-system-c-sys.md#removepreferredlanguage)

**需要权限：** ohos.permission.UPDATE_CONFIGURATION

**系统能力：** SystemCapability.Global.I18n

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| index | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
import { i18n } from '@kit.LocalizationKit';

// 移除系统偏好语言列表中的第一个偏好语言
let index: number = 0;
let success: boolean = i18n.removePreferredLanguage(index);
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { i18n } from '@kit.LocalizationKit';

// 删除系统偏好语言列表中的第一个偏好语言
let index = 0;
try {
  i18n.System.removePreferredLanguage(index);
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error(`call System.removePreferredLanguage failed, error code: ${err.code}, message: ${err.message}.`);
}
```
