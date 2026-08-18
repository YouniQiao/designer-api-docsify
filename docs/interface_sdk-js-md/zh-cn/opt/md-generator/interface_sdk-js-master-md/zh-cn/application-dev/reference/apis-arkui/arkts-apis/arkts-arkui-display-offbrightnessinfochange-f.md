# offBrightnessInfoChange

## 导入模块

```TypeScript
```

## offBrightnessInfoChange

```TypeScript
function offBrightnessInfoChange(callback?: BrightnessCallback<number, BrightnessInfo>): void
```

Unregister the callback for brightness info changes.

**起始版本：** 23

<!--Device-display-function offBrightnessInfoChange(callback?: BrightnessCallback<long, BrightnessInfo>): void--><!--Device-display-function offBrightnessInfoChange(callback?: BrightnessCallback<long, BrightnessInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [BrightnessCallback](arkts-arkui-display-brightnesscallback-t.md)&lt;number, [BrightnessInfo](arkts-arkui-display-brightnessinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [1400004](../errorcode-display.md#1400004-参数异常) |
| [1400003](../errorcode-display.md#1400003-系统服务工作异常) |
