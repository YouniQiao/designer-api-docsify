# addWatcher

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## addWatcher

```TypeScript
function addWatcher(watcher: Watcher): AppEventPackageHolder
```

Adds an event watcher. You can use the callback of the event watcher to subscribe to events.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| watcher | [Watcher](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-watcher-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AppEventPackageHolder](arkts-performanceanalysis-hiappevent-appeventpackageholder-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11102001](../errorcode-hiappevent.md#11102001-invalid-watcher-name) |
| [11102002](../errorcode-hiappevent.md#11102002-invalid-filtering-event-domain-name) |
| [11102003](../errorcode-hiappevent.md#11102003-invalid-event-number) |
| [11102004](../errorcode-hiappevent.md#11102004-invalid-event-size) |
| [11102005](../errorcode-hiappevent.md#11102005-invalid-timeout-value) |
