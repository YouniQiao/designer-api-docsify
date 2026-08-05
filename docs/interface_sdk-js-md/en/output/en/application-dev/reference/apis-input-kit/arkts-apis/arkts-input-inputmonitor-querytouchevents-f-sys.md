# queryTouchEvents (System API)

## queryTouchEvents

```TypeScript
function queryTouchEvents(count: int) : Promise<Array<TouchEvent>>
```

Queries recent touchscreen input events. A maximum of 100 events can be queried. Since API version 26.0.0, a maximum of 60 events can be queried. This API uses a promise to return the result.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function queryTouchEvents(count: int) : Promise<Array<TouchEvent>>--><!--Device-inputMonitor-function queryTouchEvents(count: int) : Promise<Array<TouchEvent>>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Number of touchscreen input events to query. The value range is an integer from 0 to 100. If the value is less than 0, the value **0** is used. If the value is greater than 100, the value **100** is used.Since API version 26.0.0, if the value is greater than 60, the value **60** is used. If there are only 30actual touchscreen input events but this parameter is set to **50**, only 30 touchscreen input events can be queried. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt;&gt; | Promise used to return the queried touchscreen input events. It contains |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |

**Example**

```TypeScript
import { inputMonitor, TouchEvent } from '@kit.InputKit'
import { BusinessError } from '@kit.BasicServicesKit';

try {
  inputMonitor.queryTouchEvents(10).then((events: Array<TouchEvent>) => {
    events.forEach((event, index) => {
      console.info(`Touch event ${index}: actionTime=${event.actionTime}, sourceType=${event.sourceType}`);
    });
  }).catch((error: BusinessError) => {
    console.error('queryTouchEvents promise error: ' + JSON.stringify(error));
  });
} catch (error) {
  const code = (error as BusinessError).code;
  const message = (error as BusinessError).message;
  console.error(`queryTouchEvents failed, error code: ${code}, message: ${message}.`);
}
```

