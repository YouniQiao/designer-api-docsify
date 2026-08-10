# sendKeyEvent

## sendKeyEvent

```TypeScript
export declare function sendKeyEvent(event: KeyEvent): boolean
```

发送按键事件。

此接口仅用于对应用的测试。由于耗时长，不建议使用。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function sendKeyEvent(event: KeyEvent): boolean--><!--Device-unnamed-export declare function sendKeyEvent(event: KeyEvent): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [KeyEvent](../arkts-components/arkts-arkui-keyevent-i.md) | Yes | 按键事件，event参数见[KeyEvent](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-keyevent-i.md/arkts-input-multimodalinput-keyevent-keyevent-i.md)介绍。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 事件发送失败时返回false，其余情况返回true。 |

