# write

## write

```TypeScript
function write(eventName: string, eventType: EventType, keyValues: object): Promise<void>
```

应用事件打点方法，将事件写入到当天的事件文件中，使用Promise方式作为异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.hiviewdfx.hiAppEvent/hiAppEvent#write

<!--Device-hiAppEvent-function write(eventName: string, eventType: EventType, keyValues: object): Promise<void>--><!--Device-hiAppEvent-function write(eventName: string, eventType: EventType, keyValues: object): Promise<void>-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventName | string | Yes | 事件名称。 |
| eventType | [EventType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-screenlock-eventtype-t-sys.md) | Yes | 事件类型。 |
| keyValues | object | Yes | 事件参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，可以在其then()、catch()方法中分别对事件写入成功、写入异常的情况进行异步处理。 |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
import { hilog } from '@kit.PerformanceAnalysisKit';

let eventParams: Record<string, number | string> = {
  "int_data": 100,
  "str_data": "strValue",
};
hiAppEvent.write("test_event", hiAppEvent.EventType.FAULT, eventParams).then(() => {
  // Event writing success
  hilog.info(0x0000, 'hiAppEvent', `success to write event`);
}).catch((err: BusinessError) => {
  // Event writing error: Write the event to the event file after the invalid parameters in the event are ignored, or stop writing the event if the event verification fails.
  hilog.error(0x0000, 'hiAppEvent', `code: ${err.code}, message: ${err.message}`);
});
```


## write

```TypeScript
function write(eventName: string, eventType: EventType, keyValues: object, callback: AsyncCallback<void>): void
```

应用事件打点方法，将事件写入到当天的事件文件中，使用callback方式作为异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

**Substitutes:** ohos.hiviewdfx.hiAppEvent/hiAppEvent#write

<!--Device-hiAppEvent-function write(eventName: string, eventType: EventType, keyValues: object, callback: AsyncCallback<void>): void--><!--Device-hiAppEvent-function write(eventName: string, eventType: EventType, keyValues: object, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| eventName | string | Yes | 事件名称。 |
| eventType | [EventType](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-screenlock-eventtype-t-sys.md) | Yes | 事件类型。 |
| keyValues | object | Yes | 事件参数。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | 事件回调函数。 |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
import { hilog } from '@kit.PerformanceAnalysisKit';

let eventParams: Record<string, number | string> = {
  "int_data": 100,
  "str_data": "strValue",
};
hiAppEvent.write("test_event", hiAppEvent.EventType.FAULT, eventParams, (err: BusinessError) => {
  if (err) {
    // Event writing error: Write the event to the event file after the invalid parameters in the event are ignored, or stop writing the event if the event verification fails.
    hilog.error(0x0000, 'hiAppEvent', `failed to write event, code: ${err.code}, message: ${err.message}`);
    return;
  }
  // Event writing success
  hilog.info(0x0000, 'hiAppEvent', `success to write event`);
});
```

