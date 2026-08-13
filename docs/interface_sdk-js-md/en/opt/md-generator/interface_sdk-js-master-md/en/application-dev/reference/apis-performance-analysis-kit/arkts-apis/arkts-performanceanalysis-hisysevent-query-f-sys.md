# query (System API)

## Modules to Import

```TypeScript
import { hiSysEvent } from '@kit.PerformanceAnalysisKit';
```

## query

```TypeScript
function query(queryArg: QueryArg, rules: QueryRule[], querier: Querier): void
```

Queries system events.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_DFX_SYSEVENT

<!--Device-hiSysEvent-function query(queryArg: QueryArg, rules: QueryRule[], querier: Querier): void--><!--Device-hiSysEvent-function query(queryArg: QueryArg, rules: QueryRule[], querier: Querier): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| queryArg | [QueryArg](arkts-performanceanalysis-hisysevent-queryarg-i-sys.md) | Yes |
| [rules](arkts-performanceanalysis-hisysevent-watcher-i-sys.md) | [QueryRule](arkts-performanceanalysis-hisysevent-queryrule-i-sys.md)[] | Yes |
| querier | [Querier](../../apis-security-guard-kit/arkts-apis/arkts-securityguard-securityguard-querier-i-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11200302](../errorcode-hisysevent-sys.md#11200302-invalid-query-rule) |
| [11200303](../errorcode-hisysevent-sys.md#11200303-number-of-concurrent-queries-exceeding-the-limit) |
| [11200301](../errorcode-hisysevent-sys.md#11200301-number-of-query-rules-exceeding-the-limit) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [11200304](../errorcode-hisysevent-sys.md#11200304-query-frequency-exceeding-the-limit) |

## Examples

```TypeScript
import { hiSysEvent } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let customizedParams: Record<string, string | number> = {
    'PID': 487,
    'UID': 103,
    'PACKAGE_NAME': "com.ohos.hisysevent.test",
    'PROCESS_NAME': "syseventservice",
    'MSG': "no msg."
  };
  let eventInfo: hiSysEvent.SysEventInfo = {
    domain: "RELIABILITY",
    name: "STACK",
    eventType: hiSysEvent.EventType.FAULT,
    params: customizedParams
  };
  hiSysEvent.write(eventInfo, (err: BusinessError) => {
    // do something here.
  });

  let queryArg: hiSysEvent.QueryArg = {
    beginTime: -1,
    endTime: -1,
    maxEvents: 5,
  };
  let queryRules: hiSysEvent.QueryRule[] = [{
    domain: "RELIABILITY",
    names: ["STACK"],
    condition: '{"version":"V1","condition":{"and":[{"param":"PID","op":"=","value":487},{"param":"PROCESS_NAME","op":"=","value":"syseventservice"}]}}'
  } as hiSysEvent.QueryRule];
  let querier: hiSysEvent.Querier = {
    onQuery: (infos: hiSysEvent.SysEventInfo[]) => {
      // do something here.
    },
    onComplete: (reason: number, total: number) => {
      // do something here.
    }
  };
  hiSysEvent.query(queryArg, queryRules, querier);
} catch (err) {
  console.error(`error code: ${(err as BusinessError).code}, error msg: ${(err as BusinessError).message}`);
}
```
