# BrightnessCallback

```TypeScript
type BrightnessCallback<T1, T2> = (data1: T1, data2: T2) => void
```

监听屏幕亮度信息时使用的回调函数类型。

**起始版本：** 22

<!--Device-display-type BrightnessCallback<T1, T2> = (data1: T1, data2: T2) => void--><!--Device-display-type BrightnessCallback<T1, T2> = (data1: T1, data2: T2) => void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data1 | T1 | 是 |
| data2 | T2 | 是 |
