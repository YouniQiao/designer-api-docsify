# unsubscribe (System API)

## Modules to Import

```TypeScript
import { hiSysEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## unsubscribe

```TypeScript
function unsubscribe(): void
```

Unsubscribes from system events.

**Since:** 10

**Required permissions:** ohos.permission.READ_DFX_SYSEVENT

<!--Device-hiSysEvent-function unsubscribe(): void--><!--Device-hiSysEvent-function unsubscribe(): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [11200305](../errorcode-hisysevent-sys.md#11200305-unsubscription-failed) |

## Examples

```TypeScript
import { hiSysEvent } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let rules: hiSysEvent.QueryRule[] = [{
    domain: "RELIABILITY",
    names: ["STACK"],
  } as hiSysEvent.QueryRule,
  {
    domain: "BUNDLE_MANAGER",
    names: ["BUNDLE_UNINSTALL"],
  } as hiSysEvent.QueryRule];
  hiSysEvent.subscribe(rules);
  hiSysEvent.unsubscribe();
} catch (err) {
  console.error(`error code: ${(err as BusinessError).code}, error msg: ${(err as BusinessError).message}`);
}
```
