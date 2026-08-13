# exportSysEvents (System API)

## Modules to Import

```TypeScript
import { hiSysEvent } from '@kit.PerformanceAnalysisKit';
```

## exportSysEvents

```TypeScript
function exportSysEvents(queryArg: QueryArg, rules: QueryRule[]): number
```

Exports system events in batches and writes them as a file to the fixed directory of the application sandbox (that is, /data/storage/el2/base/cache/hiview/event/).

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_DFX_SYSEVENT

<!--Device-hiSysEvent-function exportSysEvents(queryArg: QueryArg, rules: QueryRule[]): long--><!--Device-hiSysEvent-function exportSysEvents(queryArg: QueryArg, rules: QueryRule[]): long-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| queryArg | [QueryArg](arkts-performanceanalysis-hisysevent-queryarg-i-sys.md) | Yes |
| [rules](arkts-performanceanalysis-hisysevent-watcher-i-sys.md) | [QueryRule](arkts-performanceanalysis-hisysevent-queryrule-i-sys.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11200302](../errorcode-hisysevent-sys.md#11200302-invalid-query-rule) |
| [11200301](../errorcode-hisysevent-sys.md#11200301-number-of-query-rules-exceeding-the-limit) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [11200304](../errorcode-hisysevent-sys.md#11200304-query-frequency-exceeding-the-limit) |

## Examples

```TypeScript
import { fileIo } from '@kit.CoreFileKit';
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
    maxEvents: 1,
  };
  let queryRules: hiSysEvent.QueryRule[] = [{
    domain: "RELIABILITY",
    names: ["STACK"],
  } as hiSysEvent.QueryRule];
  let time = hiSysEvent.exportSysEvents(queryArg, queryRules);
  console.info(`receive export task time is : ${time}`);

  // Postpone reading of exported events.
  setTimeout(() => {
    let eventDir = '/data/storage/el2/base/cache/hiview/event';
    let filenames = fileIo.listFileSync(eventDir);
    for (let i = 0; i < filenames.length; i++) {
      if (filenames[i].indexOf(time.toString()) != -1) {
        let res = fileIo.readTextSync(eventDir + '/' + filenames[i]);
        let events: string = JSON.parse('[' + res.slice(0, res.length - 1) + ']');
        console.info("read file end, events is :" + JSON.stringify(events));
      }
    }
  }, 10000);
} catch (err) {
  console.error(`error code: ${(err as BusinessError).code}, error msg: ${(err as BusinessError).message}`);
}
```
