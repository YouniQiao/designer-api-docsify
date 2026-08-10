# InputKeyEventCallback

```TypeScript
export type InputKeyEventCallback = (event: InputKeyEvent) => boolean
```

按键事件（keyEvent）的回调函数类型，用于定义keyEvent事件触发时执行的回调函数格式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-inputMethodEngine-export type InputKeyEventCallback = (event: InputKeyEvent) => boolean--><!--Device-inputMethodEngine-export type InputKeyEventCallback = (event: InputKeyEvent) => boolean-End-->

**System capability:** SystemCapability.MiscServices.InputMethodFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | InputKeyEvent | Yes | 输入按键事件对象，包含按键编码、事件类型、触发时间等按键事件相关信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 是否消费该按键事件：返回true表示消费此事件，系统不再向下传递该事件；返回false表示不消费此事件，系统将继续处理该事件。 |

