# ClickCallback

Defines a callback used to return whether the application started by double-pressing the function key is the application itself.

**Since:** 24

<!--Device-settingsLite-interface ClickCallback--><!--Device-settingsLite-interface ClickCallback-End-->

**System capability:** SystemCapability.Applications.Settings.Core.Lite

## Modules to Import

```TypeScript
import { settingsLite } from '@kit.BasicServicesKit';
```

## onResult

```TypeScript
onResult(result: boolean): void
```

Called to determine whether the application can be started by double-pressing the function key.

**Since:** 24

**Model restriction:** This API can be used only in the FA model.

<!--Device-ClickCallback-onResult(result: boolean): void--><!--Device-ClickCallback-onResult(result: boolean): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | boolean | Yes |
