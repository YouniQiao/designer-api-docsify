# write (System API)

## Modules to Import

```TypeScript
import { hiSysEvent } from '@kit.PerformanceAnalysisKit';
```

## write

```TypeScript
function write(info: SysEventInfo): Promise<void>
```

Writes event information to the event file. This API uses a promise to return the result.

**Since:** 9

<!--Device-hiSysEvent-function write(info: SysEventInfo): Promise<void>--><!--Device-hiSysEvent-function write(info: SysEventInfo): Promise<void>-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [SysEventInfo](arkts-performanceanalysis-hisysevent-syseventinfo-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 11200002 |
| [11200003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hisysevent-sys.md#11200003-environment-error) |
| [11200051](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hisysevent-sys.md#11200051-invalid-event-parameter) |
| 11200001 |
| [11200054](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hisysevent-sys.md#11200054-length-of-event-parameter-values-of-the-array-type-exceeding-the-limit) |
| [11200004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hisysevent-sys.md#11200004-invalid-event-length) |
| [11200052](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hisysevent-sys.md#11200052-length-of-event-parameter-values-of-the-string-type-exceeding-the-limit) |
| [11200053](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hisysevent-sys.md#11200053-number-of-event-parameters-exceeding-the-limit) |

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
  hiSysEvent.write(eventInfo).then(
    () => {
      // do something here.
    }
  ).catch(
    (err: BusinessError) => {
      console.error(`error code: ${err.code}, error msg: ${err.message}`);
    }
  );
} catch (err) {
  console.error(`error code: ${(err as BusinessError).code}, error msg: ${(err as BusinessError).message}`);
}
```


## write

```TypeScript
function write(info: SysEventInfo, callback: AsyncCallback<void>): void
```

Writes event information to the event file. This API uses an asynchronous callback to return the result.

**Since:** 9

<!--Device-hiSysEvent-function write(info: SysEventInfo, callback: AsyncCallback<void>): void--><!--Device-hiSysEvent-function write(info: SysEventInfo, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiSysEvent

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [SysEventInfo](arkts-performanceanalysis-hisysevent-syseventinfo-i-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 11200002 |
| [11200003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hisysevent-sys.md#11200003-environment-error) |
| [11200051](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hisysevent-sys.md#11200051-invalid-event-parameter) |
| 11200001 |
| [11200054](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hisysevent-sys.md#11200054-length-of-event-parameter-values-of-the-array-type-exceeding-the-limit) |
| [11200004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hisysevent-sys.md#11200004-invalid-event-length) |
| [11200052](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hisysevent-sys.md#11200052-length-of-event-parameter-values-of-the-string-type-exceeding-the-limit) |
| [11200053](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-performance-analysis-kit/errorcode-hisysevent-sys.md#11200053-number-of-event-parameters-exceeding-the-limit) |

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
} catch (err) {
  console.error(`error code: ${(err as BusinessError).code}, error msg: ${(err as BusinessError).message}`);
}
```
