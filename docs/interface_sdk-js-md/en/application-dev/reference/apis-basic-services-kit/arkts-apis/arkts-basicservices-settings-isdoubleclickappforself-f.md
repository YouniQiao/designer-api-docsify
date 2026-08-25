# isDoubleClickAppForSelf

## Modules to Import

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## isDoubleClickAppForSelf

```TypeScript
function isDoubleClickAppForSelf(): Promise<boolean>
```

1. Checks whether the application started by number-pressing the Down key is the application itself.
2. This API is triggered to check whether number-pressing the Down key starts the application itself.

**Since:** 24

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Applications.Settings.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |
