# FontClientObserver

```TypeScript
interface FontClientObserver
```

Observer for font service death events. When the font service dies unexpectedly, the [onServiceDied](#onservicedied) callback is invoked.

**Since:** 26.0.1

**System capability:** SystemCapability.Global.FontManager

## Modules to Import

```TypeScript
import { fontManager } from '@kit.LocalizationKit';
```

## onServiceDied

```TypeScript
onServiceDied(): void
```

Called when the font service is died.

**Since:** 26.0.1

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Global.FontManager
