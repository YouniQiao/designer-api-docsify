# removePreferredLanguage

## Modules to Import

```TypeScript
import { i18n } from 'kits/@kit.LocalizationKit';
```

## removePreferredLanguage

```TypeScript
export function removePreferredLanguage(index: int): boolean
```

从系统偏好语言列表中移除指定位置的偏好语言。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [i18n.System.removePreferredLanguage](arkts-localization-i18n-system-c-sys.md#removepreferredlanguage)

**Required permissions:** ohos.permission.UPDATE_CONFIGURATION

<!--Device-i18n-export function removePreferredLanguage(index: int): boolean--><!--Device-i18n-export function removePreferredLanguage(index: int): boolean-End-->

**System capability:** SystemCapability.Global.I18n

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| index | int | Yes | 待移除偏好语言在系统偏好语言列表中的位置。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | true表示移除成功，false表示移除失败。 |

