# write

## 导入模块

```TypeScript
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';
```

## write

```TypeScript
function write(info: AppEventInfo): Promise<void>
```

应用事件打点方法，将AppEventInfo类型的事件进行存储，使用Promise方式作为异步回调。通过此接口写入的事件对象是开发者自定义的对象，为了避免与系统事件产生冲突混淆，不建议写入 系统事件（[Event](arkts-performanceanalysis-hiappevent-event-n.md)中定义的系统事件名称常量）。此接口写入的事件可通过订阅事件观察者（[addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md)）进行处理。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [AppEventInfo](arkts-performanceanalysis-hiappevent-appeventinfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11100001](../errorcode-hiappevent.md#11100001-打点功能被关闭) |
| [11101001](../errorcode-hiappevent.md#11101001-非法的事件领域名称) |
| [11101002](../errorcode-hiappevent.md#11101002-非法的事件名称) |
| [11101003](../errorcode-hiappevent.md#11101003-非法的事件参数数量) |
| [11101004](../errorcode-hiappevent.md#11101004-非法的事件参数字符串长度) |
| [11101005](../errorcode-hiappevent.md#11101005-非法的事件参数名称) |
| [11101006](../errorcode-hiappevent.md#11101006-非法的事件参数数组长度) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let eventParams: Record<string, number | string> = {
  "int_data": 100,
  "str_data": "strValue",
};

// 应用事件打点，使用callback方式作为异步回调
hiAppEvent.write({
  domain: "test_domain",
  name: "test_event",
  eventType: hiAppEvent.EventType.FAULT,
  params: eventParams,
}, (err: BusinessError) => {
  if (err) {
    hilog.error(0x0000, 'hiAppEvent', `code: ${err.code}, message: ${err.message}`);
    return;
  }
  hilog.info(0x0000, 'hiAppEvent', `success to write event`);
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@ohos.base';
import { hilog } from '@kit.PerformanceAnalysisKit';

let eventParams: Record<string, int | string> = {
  "int_data": 100,
  "str_data": "strValue",
};

// 应用事件打点，使用callback方式作为异步回调
hiAppEvent.write({
  domain: "test_domain",
  name: "test_event",
  eventType: hiAppEvent.EventType.FAULT,
  params: eventParams,
}, (err: BusinessError<void>|null) => {
  if (err?.code != 0) {
    hilog.error(0x0000, 'hiAppEvent', `code: ${err?.code}, message: ${err?.message}`);
    return;
  }
  hilog.info(0x0000, 'hiAppEvent', `success to write event`);
});
```

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let eventParams: Record<string, number | string> = {
  "int_data": 100,
  "str_data": "strValue",
};

// 应用事件打点，使用Promise方式作为异步回调
hiAppEvent.write({
  domain: "test_domain",
  name: "test_event",
  eventType: hiAppEvent.EventType.FAULT,
  params: eventParams,
}).then(() => {
  hilog.info(0x0000, 'hiAppEvent', `success to write event`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'hiAppEvent', `code: ${err.code}, message: ${err.message}`);
});
```

ArkTS-Sta示例：

```TypeScript
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@ohos.base';

let eventParams: Record<String, int | string> = {
  "int_data": 100,
  "str_data": "strValue",
};
// 应用事件打点，使用Promise方式作为异步回调
hiAppEvent.write({
  domain: "test_domain",
  name: "test_event",
  eventType: hiAppEvent.EventType.FAULT,
  params: eventParams,
}).then(() => {
  hilog.info(0x0000, 'hiAppEvent', `success to write event`);
}).catch((err: Error) => {
  const bErr = err as BusinessError;
  hilog.error(0x0000, 'hiAppEvent', `code: ${bErr.code}, message: ${bErr.message}`);
});
```


## write

```TypeScript
function write(info: AppEventInfo, callback: AsyncCallback<void>): void
```

应用事件打点方法，将AppEventInfo类型的事件进行存储，使用callback方式作为异步回调。通过此接口写入的事件对象是开发者自定义的对象，为了避免与系统事件产生冲突混淆，不建议写入 系统事件（[Event](arkts-performanceanalysis-hiappevent-event-n.md)中定义的系统事件名称常量）。此接口写入的事件可通过订阅事件观察者（[addWatcher](arkts-performanceanalysis-hiappevent-addwatcher-f.md)）进行订阅。

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.HiviewDFX.HiAppEvent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| info | [AppEventInfo](arkts-performanceanalysis-hiappevent-appeventinfo-i.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [11100001](../errorcode-hiappevent.md#11100001-打点功能被关闭) |
| [11101001](../errorcode-hiappevent.md#11101001-非法的事件领域名称) |
| [11101002](../errorcode-hiappevent.md#11101002-非法的事件名称) |
| [11101003](../errorcode-hiappevent.md#11101003-非法的事件参数数量) |
| [11101004](../errorcode-hiappevent.md#11101004-非法的事件参数字符串长度) |
| [11101005](../errorcode-hiappevent.md#11101005-非法的事件参数名称) |
| [11101006](../errorcode-hiappevent.md#11101006-非法的事件参数数组长度) |

**示例**

参见 [write](#write)
