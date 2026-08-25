# subscribe (System API)

## Modules to Import

```TypeScript
import { hiSysEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## subscribe

```TypeScript
function subscribe(rules: QueryRule[]): number
```

Subscribes to real-time system events that occur occasionally or occur in a low frequency. These events are written as a file to the fixed directory of the application sandbox (that is, /data/storage/el2/base/cache/hiview/event/).

**Since:** 10

**Required permissions:** ohos.permission.READ_DFX_SYSEVENT

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rules | [QueryRule](arkts-performanceanalysis-hisysevent-queryrule-i-sys.md)[] | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [11200301](../errorcode-hisysevent-sys.md#11200301-number-of-query-rules-exceeding-the-limit) |
| [11200302](../errorcode-hisysevent-sys.md#11200302-invalid-query-rule) |
