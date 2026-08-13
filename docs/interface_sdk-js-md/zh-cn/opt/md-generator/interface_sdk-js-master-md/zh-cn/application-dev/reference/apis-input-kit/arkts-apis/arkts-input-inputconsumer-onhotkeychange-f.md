# onHotkeyChange

## onHotkeyChange

```TypeScript
function onHotkeyChange(hotkeyOptions: HotkeyOptions, callback: Callback<HotkeyOptions>): void
```

订阅应用快捷键。获取满足条件的组合按键输入事件，使用Callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-inputConsumer-function onHotkeyChange(hotkeyOptions: HotkeyOptions, callback: Callback<HotkeyOptions>): void--><!--Device-inputConsumer-function onHotkeyChange(hotkeyOptions: HotkeyOptions, callback: Callback<HotkeyOptions>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputConsumer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| hotkeyOptions | [HotkeyOptions](arkts-input-inputconsumer-hotkeyoptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HotkeyOptions](arkts-input-inputconsumer-hotkeyoptions-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [4200002](../errorcode-inputconsumer.md#4200002-快捷键被系统注册) |
| [4200003](../errorcode-inputconsumer.md#4200003-快捷键已经被其他应用注册) |
