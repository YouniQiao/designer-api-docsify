# query

## Modules to Import

```TypeScript
import { FaultLogger } from 'kits/@kit.PerformanceAnalysisKit';
```

## query

```TypeScript
function query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>): void
```

获取当前应用故障信息，该方法通过回调方式获取故障信息数组，故障信息数组内最多上报10份故障信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** ohos.hiviewdfx.hiAppEvent/hiAppEvent#addWatcher

<!--Device-FaultLogger-function query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>): void--><!--Device-FaultLogger-function query(faultType: FaultType, callback: AsyncCallback<Array<FaultLogInfo>>): void-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| faultType | [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) | Yes | 输入要查询的故障类型。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;FaultLogInfo&gt;&gt; | Yes | 回调函数，在回调函数中获取故障信息数组。 &lt;br&gt;value拿到故障信息数组；value为undefined表示获取过程中出现异常，error返回错误提示字符串。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10600001 | The service is not started or is faulty |
| 401 | The parameter check failed, Parameter type error |
| 801 | The specified SystemCapability name was not found |

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

获取当前应用故障信息，该方法通过Promise方式返回故障信息数组，故障信息数组内最多上报10份故障信息。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 18

**Substitutes:** ohos.hiviewdfx.hiAppEvent/hiAppEvent#addWatcher

<!--Device-FaultLogger-function query(faultType: FaultType): Promise<Array<FaultLogInfo>>--><!--Device-FaultLogger-function query(faultType: FaultType): Promise<Array<FaultLogInfo>>-End-->

**System capability:** SystemCapability.HiviewDFX.Hiview.FaultLogger

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| faultType | [FaultType](arkts-performanceanalysis-faultlogger-faulttype-e.md) | Yes | 输入要查询的故障类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;FaultLogInfo&gt;&gt; | Promise实例，可以在其then()方法中获取故障信息实例，也可以使用await。 &lt;br&gt;value拿到故障信息数组；value为undefined表示获取过程中出现异常。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 10600001 | The service is not started or is faulty |
| 401 | The parameter check failed, Parameter type error |
| 801 | The specified SystemCapability name was not found |

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

