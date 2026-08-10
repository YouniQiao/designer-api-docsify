# sendEventByKey

## Modules to Import

```TypeScript
import { inspector } from 'kits/@kit.ArkUI';
```

## sendEventByKey

```TypeScript
function sendEventByKey(id: string, action: int, params: string): boolean
```

给指定id的组件发送事件。

此接口仅用于对应用的测试。由于耗时长，不建议测试之外的场景使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-inspector-function sendEventByKey(id: string, action: int, params: string): boolean--><!--Device-inspector-function sendEventByKey(id: string, action: int, params: string): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | 要触发事件的组件id。 |
| action | int | Yes | 要触发的事件类型，当前支持取值：&lt;br/&gt;点击事件Click：10。&lt;br/&gt;长按事件LongClick：11。 |
| params | string | Yes | 事件参数，无参数时传空字符串""。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 找不到指定id的组件时返回false，其余情况返回true。 |

