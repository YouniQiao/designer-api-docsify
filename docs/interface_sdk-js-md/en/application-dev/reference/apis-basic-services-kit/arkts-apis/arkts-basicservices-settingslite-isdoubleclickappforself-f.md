# isDoubleClickAppForSelf

## Modules to Import

```TypeScript
import { settingsLite } from '@kit.BasicServicesKit';
```

## isDoubleClickAppForSelf

```TypeScript
function isDoubleClickAppForSelf(callback: ClickCallback): void
```

1. Checks whether the application started by double-pressing the function key is the application itself.
2. This API is triggered to check whether double-pressing the function key starts the application itself.

**Since:** 24

**ArkTS mode:** Supports only ArkTS-Dyn, since version 24.

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Applications.Settings.Core.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [ClickCallback](arkts-basicservices-settingslite-clickcallback-i.md) | Yes |
