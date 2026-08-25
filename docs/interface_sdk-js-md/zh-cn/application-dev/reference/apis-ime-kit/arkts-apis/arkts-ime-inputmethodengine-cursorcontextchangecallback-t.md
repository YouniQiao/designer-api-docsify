# CursorContextChangeCallback

```TypeScript
export type CursorContextChangeCallback = (x: double, y: double, height: double) => void
```

光标上下文变化（cursorContextChange）事件的回调函数类型，用于定义该事件触发时执行的回调函数格式。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |
| height | double | 是 |
