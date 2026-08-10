# addPreferredLanguage

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## addPreferredLanguage

```TypeScript
export function addPreferredLanguage(language: string, index?: int): boolean
```

在系统偏好语言列表的指定位置添加偏好语言。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [i18n.System.addPreferredLanguage](arkts-localization-i18n-system-c-sys.md#addpreferredlanguage)

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-i18n-export function addPreferredLanguage(language: string, index?: int): boolean--><!--Device-i18n-export function addPreferredLanguage(language: string, index?: int): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| language | string | Yes | 待添加的偏好语言。 |
| index | int | No | 偏好语言的添加位置。默认值：系统偏好语言列表长度。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示添加成功，false表示添加失败。 |

