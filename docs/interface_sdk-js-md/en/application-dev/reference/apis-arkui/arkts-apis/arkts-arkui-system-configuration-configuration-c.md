# Configuration

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-export default class Configuration--><!--Device-unnamed-export default class Configuration-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## Modules to Import

```TypeScript
import { LocaleResponse } from 'kits/@kit.ArkUI';
```

## getLocale

```TypeScript
static getLocale(): LocaleResponse
```

获取应用当前的语言和地区。默认与系统的语言和地区同步。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Configuration-static getLocale(): LocaleResponse--><!--Device-Configuration-static getLocale(): LocaleResponse-End-->

**Return value:**

| Type | Description |
| --- | --- |
| [LocaleResponse](arkts-arkui-system-configuration-localeresponse-i.md) | 应用当前Locale相关信息。 |

