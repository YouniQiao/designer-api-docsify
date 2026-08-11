# addWatcher (System API)

## Modules to Import

```TypeScript
import { hiSysEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## addWatcher

```TypeScript
function addWatcher(watcher: Watcher): void
```

Adds a watcher for event subscription.

**Since:** 9

**Required permissions:** ohos.permission.READ_DFX_SYSEVENT

<!--Device-hiSysEvent-function addWatcher(watcher: Watcher): void--><!--Device-hiSysEvent-function addWatcher(watcher: Watcher): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| watcher | [Watcher](../../apis-core-file-kit/arkts-apis/arkts-corefile-file-fs-watcher-i.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [11200102](../errorcode-hisysevent-sys.md#11200102-number-of-event-watcher-rules-exceeding-the-limit) |
| [11200101](../errorcode-hisysevent-sys.md#11200101-number-of-event-watchers-exceeding-the-limit) |

## Examples

```TypeScript
import { hiSysEvent } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let watchRules: hiSysEvent.WatchRule[] = [{
    domain: "RELIABILITY",
    name: "STACK",
    tag: "STABILITY",
    ruleType: hiSysEvent.RuleType.WHOLE_WORD,
  } as hiSysEvent.WatchRule];
let watcher: hiSysEvent.Watcher = {
  rules: watchRules,
  onEvent: (info: hiSysEvent.SysEventInfo) => {
    // do something here.
  },
  onServiceDied: () => {
    // do something here.
  }
};
try {
  hiSysEvent.addWatcher(watcher);
} catch (err) {
  console.error(`error code: ${(err as BusinessError).code}, error msg: ${(err as BusinessError).message}`);
}
```
