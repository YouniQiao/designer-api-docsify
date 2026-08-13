# CursorContextChangeCallback

```TypeScript
export type CursorContextChangeCallback = (x: number, y: number, height: number) => void
```

光标上下文变化（cursorContextChange）事件的回调函数类型，用于定义该事件触发时执行的回调函数格式。

**起始版本：** 23

**废弃版本：** -1

<!--Device-inputMethodEngine-export type CursorContextChangeCallback = (x: double, y: double, height: double) => void--><!--Device-inputMethodEngine-export type CursorContextChangeCallback = (x: double, y: double, height: double) => void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| height | number | 是 |
