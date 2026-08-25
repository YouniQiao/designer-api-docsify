# ClickCallback

Defines a callback used to return whether the application started by number-pressing the function key is the application itself.

**Since:** 24

**System capability:** SystemCapability.Applications.Settings.Core.Lite

## Modules to Import

```TypeScript
import { settingsLite } from 'kits/@kit.BasicServicesKit';
```

## onResult

```TypeScript
onResult(result: boolean): void
```

Called to determine whether the application can be started by number-pressing the function key.

**Since:** 24

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.Applications.Settings.Core.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | boolean | Yes |
