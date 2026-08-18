# queryTouchEvents（系统接口）

## 导入模块

```TypeScript
```

## queryTouchEvents

```TypeScript
function queryTouchEvents(count: number) : Promise<Array<TouchEvent>>
```

查询最近的触屏输入事件，最多支持查询100条事件，从API版本26.0.0开始，最多支持查询60条事件，使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.INPUT_MONITORING

<!--Device-inputMonitor-function queryTouchEvents(count: int) : Promise<Array<TouchEvent>>--><!--Device-inputMonitor-function queryTouchEvents(count: int) : Promise<Array<TouchEvent>>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputMonitor

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| count | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[TouchEvent](arkts-input-multimodalinput-touchevent-touchevent-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

```TypeScript
import { inputMonitor, TouchEvent } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 查询触屏事件数量
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
