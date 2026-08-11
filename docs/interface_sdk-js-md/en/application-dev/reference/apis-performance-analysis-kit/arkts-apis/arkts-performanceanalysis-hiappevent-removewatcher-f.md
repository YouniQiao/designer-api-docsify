# removeWatcher

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## removeWatcher

```TypeScript
function removeWatcher(watcher: Watcher): void
```

Removes an event watcher.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-hiAppEvent-function removeWatcher(watcher: Watcher): void--><!--Device-hiAppEvent-function removeWatcher(watcher: Watcher): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| watcher | [Watcher](../../apis-core-file-kit/arkts-apis/arkts-corefile-watcher-t.md) | Yes | Event watcher. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |
| [11102001](../errorcode-hiappevent.md#11102001-invalid-watcher-name) | Invalid watcher name. Possible causes: 1. Contain invalid characters; &lt;br&gt;2. Length is invalid. |

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

