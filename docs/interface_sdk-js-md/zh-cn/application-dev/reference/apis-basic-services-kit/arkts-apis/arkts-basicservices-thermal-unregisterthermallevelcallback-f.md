# unregisterThermalLevelCallback

## 导入模块

```TypeScript
import { thermal } from 'kits/@kit.BasicServicesKit';
```

## unregisterThermalLevelCallback

```TypeScript
function unregisterThermalLevelCallback(callback?: Callback<void>): void
```

取消订阅热档位变化时的回调提醒。使用callback异步回调。此方法与thermal.registerThermalLevelCallback配对使用，用于取消先前注册的热档位回调。

**起始版本：** 9

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
