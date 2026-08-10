# onBrightnessInfoChange

## 导入模块

```TypeScript
import { display } from 'kits/@kit.ArkUI';
```

## onBrightnessInfoChange

```TypeScript
function onBrightnessInfoChange(callback: BrightnessCallback<long, BrightnessInfo>): void
```

Register the callback for brightness info changes.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-display-function onBrightnessInfoChange(callback: BrightnessCallback<long, BrightnessInfo>): void--><!--Device-display-function onBrightnessInfoChange(callback: BrightnessCallback<long, BrightnessInfo>): void-End-->

**系统能力：** SystemCapability.Window.SessionManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [BrightnessCallback](arkts-arkui-display-brightnesscallback-t.md)&lt;long, BrightnessInfo&gt; | 是 | Callback used to return the display if and corresponding brightness info. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 1400004 | Parameter error. Possible cause: 1. Invalid parameter range. |
| 1400003 | This display manager service works abnormally. |

