# InputEventListener

```TypeScript
declare type InputEventListener = (
  event: RawInputEventWrapper
) => InputEventInterceptResult
```

输入事件监听器回调函数类型。

> **说明：**
> 
> - RawInputEventWrapper是抽象类，开发者无法使用`new`运算符创建实例。
> 
> - 系统会在事件触发时自动创建实例并通过此参数传递给回调函数。
> 
> - 当前回调参数event仅会封装以下原始输入事件类型：
> [MouseEvent](arkts-arkui-mouseevent-i.md)、[TouchEvent](arkts-arkui-touchevent-i.md)、[KeyEvent](arkts-arkui-keyevent-i.md)。开发者可通过
> [asMouseEvent](arkts-arkui-rawinputeventwrapper-c.md#asmouseevent)、[asTouchEvent](arkts-arkui-rawinputeventwrapper-c.md#astouchevent)、
> [asKeyEvent](arkts-arkui-rawinputeventwrapper-c.md#askeyevent)获取对应事件对象。
> 
> - 请勿在回调中执行耗时操作（如复杂计算或网络请求），否则可能导致应用卡顿。
> 
> - 监听器在UI线程中同步执行会直接阻塞事件处理流程。建议只进行简单的判断和计算。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-declare type InputEventListener = (  event: RawInputEventWrapper) => InputEventInterceptResult--><!--Device-unnamed-declare type InputEventListener = (  event: RawInputEventWrapper) => InputEventInterceptResult-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [RawInputEventWrapper](arkts-arkui-rawinputeventwrapper-c.md) | Yes | 输入事件包装器，系统自动创建和传递，开发者无需手动创建。 |

**Return value:**

| Type | Description |
| --- | --- |
| [InputEventInterceptResult](arkts-arkui-inputeventinterceptresult-i.md) | 事件拦截结果。 |

