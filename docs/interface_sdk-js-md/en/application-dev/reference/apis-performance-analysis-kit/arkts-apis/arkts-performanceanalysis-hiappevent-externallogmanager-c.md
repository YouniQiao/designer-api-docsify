# ExternalLogManager

Defines an external log manager for external log management.

**Since:** 26.1.0

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## onCapacityReached

```TypeScript
onCapacityReached(container: ExternalLogContainer): void
```

This function is called when external log directory capacity is reached

**Since:** 26.1.0

**Atomic service API:** This API can be used in atomic services since API version 26.1.0.

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| container | [ExternalLogContainer](arkts-performanceanalysis-hiappevent-externallogcontainer-c.md) | Yes |
