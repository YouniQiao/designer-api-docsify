# sendMouseEvent

## sendMouseEvent

```TypeScript
export declare function sendMouseEvent(event: MouseEvent): boolean
```

发送鼠标事件。

此接口仅用于对应用的测试。由于耗时长，不建议使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function sendMouseEvent(event: MouseEvent): boolean--><!--Device-unnamed-export declare function sendMouseEvent(event: MouseEvent): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [MouseEvent](../arkts-components/arkts-arkui-mouseevent-i.md) | Yes | 鼠标事件，event参数见[MouseEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-mouseevent-mouseevent-i.md/arkts-input-multimodalinput-mouseevent-mouseevent-i.md)介绍。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 事件发送失败时返回false，其余情况返回true。 |

