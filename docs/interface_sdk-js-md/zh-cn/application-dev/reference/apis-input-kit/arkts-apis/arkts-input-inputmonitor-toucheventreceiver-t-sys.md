# TouchEventReceiver（系统接口）

```TypeScript
type TouchEventReceiver = (touchEvent: TouchEvent) => boolean
```

触屏输入事件的回调函数。

**起始版本：** 7

**ArkTS模式：** ArkTS-Dyn起始版本为7；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.MultimodalInput.Input.InputMonitor

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| touchEvent | [TouchEvent](arkts-input-multimodalinput-touchevent-touchevent-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
