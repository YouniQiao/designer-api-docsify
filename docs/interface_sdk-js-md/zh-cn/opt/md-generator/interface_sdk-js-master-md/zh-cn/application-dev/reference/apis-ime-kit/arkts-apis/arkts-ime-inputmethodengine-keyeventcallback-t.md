# KeyEventCallback

```TypeScript
export type KeyEventCallback = (event: KeyEvent) => boolean
```

按键按下（keyDown）或按键抬起（keyUp）事件的回调函数类型，用于定义这两类按键事件触发时执行的回调函数格式。

**起始版本：** 23

**废弃版本：** -1

<!--Device-inputMethodEngine-export type KeyEventCallback = (event: KeyEvent) => boolean--><!--Device-inputMethodEngine-export type KeyEventCallback = (event: KeyEvent) => boolean-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| event | [KeyEvent](../../apis-na/arkts-apis/arkts-na-common-keyevent-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
