# sendTouchEvent

## sendTouchEvent

```TypeScript
export declare function sendTouchEvent(event: TouchObject): boolean
```

发送触摸事件。

此接口仅用于对应用的测试。由于耗时长，不建议使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function sendTouchEvent(event: TouchObject): boolean--><!--Device-unnamed-export declare function sendTouchEvent(event: TouchObject): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [TouchObject](../arkts-components/arkts-arkui-touchobject-i.md) | Yes | 触摸事件，event参数见[TouchObject](arkts-arkui-common-touchobject-i.md)的介绍。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 事件发送失败时返回false，其余情况返回true。 |

