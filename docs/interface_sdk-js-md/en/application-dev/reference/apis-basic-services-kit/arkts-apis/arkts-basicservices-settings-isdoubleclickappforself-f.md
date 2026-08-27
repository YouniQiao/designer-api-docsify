# isDoubleClickAppForSelf

## Modules to Import

```TypeScript
import { settings } from '@kit.BasicServicesKit';
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

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Check result. { |

**Examples**

```TypeScript
import { settings } from '@kit.BasicServicesKit';

settings.isDoubleClickAppForSelf().then((result: boolean) => {
  console.info(`isDoubleClickAppForSelf result: ${result}`);
})
```
