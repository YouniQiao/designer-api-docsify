# setEventParam

## Modules to Import

```TypeScript
import { hiAppEvent } from 'kits/@kit.PerformanceAnalysisKit';
```

## setEventParam

```TypeScript
function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>
```

事件自定义参数设置方法，使用Promise方式作为异步回调。在同一生命周期中，可以通过事件领域和事件名称关联系统事件和应用事件。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-hiAppEvent-function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>--><!--Device-hiAppEvent-function setEventParam(params: Record<string, ParamType>, domain: string, name?: string): Promise<void>-End-->

**System capability:** SystemCapability.HiviewDFX.HiAppEvent

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, ParamType&gt; | Yes | 事件自定义参数对象。参数名和参数值规格定义如下：&lt;br&gt;- 参数名为string类型，首字符必须为字母字符或\\$字符。中间字符必须为 数字字符、字母字符或下划线字符。结尾字符必须为数字字符或字母字符。长度非空且不超过32个字符。&lt;br&gt;- 参数值为[ParamType](arkts-performanceanalysis-hiappevent-paramtype-t.md)类型，参数值长度需在 1024个字符以内。&lt;br&gt;- 参数个数需在64个以内。 |
| domain | string | Yes | 事件领域。事件领域可支持关联应用事件和系统事件（hiAppEvent.domain.OS）。 |
| name | string | No | 事件名称。默认为空字符串，空字符串表示关联事件领域下的所有事件名称。事件名称可支持关联应用事件和系统事件，其中系统事件仅支持关联：&lt;br&gt;- [崩溃事件](../../../dfx/hiappevent-watcher-crash-events.md)（hiAppEvent.event.APP_CRASH）&lt;br&gt;- [应用冻屏事件](../../../dfx/hiappevent-watcher-freeze-events.md)（hiAppEvent.event.APP_FREEZE）&lt;br&gt;- [资源泄漏事件](../../../dfx/hiappevent-watcher-resourceleak-events.md)（hiAppEvent.event.RESOURCE_OVERLIMIT）。&lt;br&gt; **注意**：从API version 20开始，支持[资源泄漏事件](../../../dfx/hiappevent-watcher-resourceleak-events.md)。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 11101001 | Invalid event domain. Possible causes: 1. Contain invalid characters; &lt;br&gt;2. Length is invalid. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types. |
| 11101002 | Invalid event name. Possible causes: 1. Contain invalid characters; &lt;br&gt;2. Length is invalid. |
| 11101005 | Invalid event parameter name. Possible causes: 1. Contain invalid characters; &lt;br&gt;2. Length is invalid. |
| 11101004 | Invalid string length of the event parameter. |
| 11101007 | The number of parameter keys exceeds the limit. |
| 11100001 | Function disabled. Possibly caused by the param disable in ConfigOption is true. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let params: Record<string, hiAppEvent.ParamType> = {
  "int_data": 100,
  "str_data": "strValue",
};

// Add custom parameters to the application event.
hiAppEvent.setEventParam(params, "test_domain", "test_event").then(() => {
  hilog.info(0x0000, 'hiAppEvent', `success to set event param`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'hiAppEvent', `code: ${err.code}, message: ${err.message}`);
});
```

