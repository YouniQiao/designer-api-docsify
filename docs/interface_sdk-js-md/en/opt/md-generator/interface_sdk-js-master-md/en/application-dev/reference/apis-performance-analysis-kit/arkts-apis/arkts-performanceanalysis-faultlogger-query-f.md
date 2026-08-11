# query

## Modules to Import

```TypeScript
import { FaultLogger } from 'kits/@kit.PerformanceAnalysisKit';
```

## query

```TypeScript
function query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>): void
```

Obtains the fault information about the current application. This API uses an asynchronous callback to return the fault information array obtained, which contains a maximum of 10 pieces of fault information.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** ohos.hiviewdfx.hiAppEvent/hiAppEvent#addWatcher

<!--Device-FaultLogger-function query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>): void--><!--Device-FaultLogger-function query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>): void-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| faultType | [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;FaultLogInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [10600001](../errorcode-faultlogger.md#10600001-service-faulty-or-not-started) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## Examples

```TypeScript
import { FaultLogger } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

function queryFaultLogCallback(error: BusinessError, value: Array<FaultLogger.FaultLogInfo>) {
    if (error) {
        console.error(`error code:${error.code}, error msg:${error.message}`);
    } else {
        console.info("value length is " + value.length);
        let len: number = value.length;
        for (let i = 0; i < len; i++) {
            console.info(`log: ${i}`);
            console.info(`Log pid: ${value[i].pid}`);
            console.info(`Log uid: ${value[i].uid}`);
            console.info(`Log type: ${value[i].type}`);
            console.info(`Log timestamp: ${value[i].timestamp}`);
            console.info(`Log reason: ${value[i].reason}`);
            console.info(`Log module: ${value[i].module}`);
            console.info(`Log summary: ${value[i].summary}`);
            console.info(`Log text: ${value[i].fullLog}`);
        }
    }
}
try {
    FaultLogger.query(FaultLogger.FaultType.JS_CRASH, queryFaultLogCallback);
} catch (err) {
    console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
}
```


## query

```TypeScript
function query(faultType: FaultType): Promise<Array<FaultLogInfo>>
```

Obtains the fault information about the current application. This API uses a promise to return the fault information array obtained, which contains a maximum of 10 pieces of fault information.

**Since:** 9

**Deprecated since:** 18

**Substitutes:** ohos.hiviewdfx.hiAppEvent/hiAppEvent#addWatcher

<!--Device-FaultLogger-function query(faultType: FaultType): Promise<Array<FaultLogInfo>>--><!--Device-FaultLogger-function query(faultType: FaultType): Promise<Array<FaultLogInfo>>-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| faultType | [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;FaultLogInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [10600001](../errorcode-faultlogger.md#10600001-service-faulty-or-not-started) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |

## Examples

```TypeScript
import { FaultLogger } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function getLog() {
  try {
    let value: Array<FaultLogger.FaultLogInfo> = await FaultLogger.query(FaultLogger.FaultType.JS_CRASH);
    if (value) {
      console.info(`value length: ${value.length}`);
      let len: number = value.length;
      for (let i = 0; i < len; i++) {
        console.info(`log: ${i}`);
        console.info(`Log pid: ${value[i].pid}`);
        console.info(`Log uid: ${value[i].uid}`);
        console.info(`Log type: ${value[i].type}`);
        console.info(`Log timestamp: ${value[i].timestamp}`);
        console.info(`Log reason: ${value[i].reason}`);
        console.info(`Log module: ${value[i].module}`);
        console.info(`Log summary: ${value[i].summary}`);
        console.info(`Log text: ${value[i].fullLog}`);
      }
    }
  } catch (err) {
    console.error(`code: ${(err as BusinessError).code}, message: ${(err as BusinessError).message}`);
  }
}
```
