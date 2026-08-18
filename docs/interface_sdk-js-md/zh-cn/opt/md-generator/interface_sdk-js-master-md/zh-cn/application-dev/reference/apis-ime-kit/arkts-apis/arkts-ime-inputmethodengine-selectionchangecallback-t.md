# SelectionChangeCallback

```TypeScript
export type SelectionChangeCallback = (oldBegin: number, oldEnd: number, newBegin: number, newEnd: number) => void
```

文本选择范围变化（selectionChange）事件的回调函数类型，用于定义该事件触发时执行的回调函数格式。

**起始版本：** 23

<!--Device-inputMethodEngine-export type SelectionChangeCallback = (oldBegin: int, oldEnd: int, newBegin: int, newEnd: int) => void--><!--Device-inputMethodEngine-export type SelectionChangeCallback = (oldBegin: int, oldEnd: int, newBegin: int, newEnd: int) => void-End-->

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| oldBegin | number | 是 |
| oldEnd | number | 是 |
| newBegin | number | 是 |
| newEnd | number | 是 |
