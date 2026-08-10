# queryTouchEvents (System API)

## Modules to Import

```TypeScript
import { inputMonitor } from 'kits/@kit.InputKit';
```

## queryTouchEvents

```TypeScript
function queryTouchEvents(count: int) : Promise<Array<TouchEvent>>
```

查询最近的触屏输入事件，最多支持查询100条事件，从API版本26.0.0开始，最多支持查询60条事件，使用Promise异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function queryTouchEvents(count: int) : Promise<Array<TouchEvent>>--><!--Device-inputMonitor-function queryTouchEvents(count: int) : Promise<Array<TouchEvent>>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.InputMonitor

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| count | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 需要查询的触屏输入事件数量，取值范围为0到100的整数。小于0时取值为0、大于100时取值为100。从API版本26.0.0开始，大于60时取值为60。如果实际触屏输入事件只有30个， 但该参数取值为50 ，则仅支持查询到30个触屏输入事件。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[TouchEvent](arkts-input-multimodalinput-touchevent-touchevent-i-sys.md)&gt;&gt; | Promise对象，返回查询到的触屏输入事件。包含以下有效信息，其余均为无效信息：&lt;br/&gt;- actionTime：触屏输入事件发生的时间，表示系统 启动运行至今逝去的微秒数，单位为微秒（μs）。&lt;br/&gt;- [SourceType]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |

## Examples

```TypeScript
import { inputMonitor, TouchEvent } from '@kit.InputKit'
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // Querying the Number of Touchscreen Events
  inputMonitor.queryTouchEvents(10).then((events: Array<TouchEvent>) => {
    events.forEach((event, index) => {
      console.info(`Succeeded in querying touch event ${index}, actionTime=${event.actionTime}, sourceType=${event.sourceType}.`);
    });
  }).catch((error: BusinessError) => {
    console.error(`Failed to query touch events promise, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
  });
} catch (error) {
  const code = (error as BusinessError).code;
  const message = (error as BusinessError).message;
  console.error(`Failed to query touch events, Code: ${code}, message: ${message}.`);
}
```

