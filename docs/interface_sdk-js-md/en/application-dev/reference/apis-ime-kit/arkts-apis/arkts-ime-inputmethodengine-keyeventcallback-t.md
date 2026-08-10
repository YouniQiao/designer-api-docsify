# KeyEventCallback

```TypeScript
export type KeyEventCallback = (event: KeyEvent) => boolean
```

按键按下（keyDown）或按键抬起（keyUp）事件的回调函数类型，用于定义这两类按键事件触发时执行的回调函数格式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputMethodEngine-export type KeyEventCallback = (event: KeyEvent) => boolean--><!--Device-inputMethodEngine-export type KeyEventCallback = (event: KeyEvent) => boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [KeyEvent](arkts-ime-inputmethodengine-keyevent-i.md) | Yes | 按键事件对象，包含按键码、按键类型、事件时间等按键相关信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否消费该按键事件：返回true表示消费，系统不再向下传递该事件；返回false表示不消费，系统继续处理该事件。 |

