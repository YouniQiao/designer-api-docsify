# removeWatcher

## Modules to Import

```TypeScript
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
```

## removeWatcher

```TypeScript
function removeWatcher(watcher: Watcher): void
```

Removes an event watcher.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hiAppEvent-function removeWatcher(watcher: Watcher): void--><!--Device-hiAppEvent-function removeWatcher(watcher: Watcher): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| watcher | [Watcher](../../apis-na/arkts-apis/arkts-na-watcher-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11102001](../errorcode-hiappevent.md#11102001-invalid-watcher-name) |

## Examples

```TypeScript
// 1. Define an event watcher.
let watcher: hiAppEvent.Watcher = {
  name: "watcher1",
}

// 2. Add an event watcher to subscribe to events.
hiAppEvent.addWatcher(watcher);

// 3. Remove the event watcher to unsubscribe from events.
hiAppEvent.removeWatcher(watcher);
```
