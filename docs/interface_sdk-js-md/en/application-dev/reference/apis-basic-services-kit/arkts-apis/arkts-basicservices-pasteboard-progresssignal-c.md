# ProgressSignal

Defines a function for canceling the paste task. This parameter is valid only when [ProgressIndicator](arkts-basicservices-pasteboard-progressindicator-e.md) is set to **NONE**.

**Since:** 15

**System capability:** SystemCapability.MiscServices.Pasteboard

## Modules to Import

```TypeScript
import { pasteboard } from 'kits/@kit.BasicServicesKit';
```

## cancel

```TypeScript
cancel(): void
```

Cancels an ongoing paste task.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.MiscServices.Pasteboard
