# isFunctionKeyEnabled

## 导入模块

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## isFunctionKeyEnabled

```TypeScript
function isFunctionKeyEnabled(functionKey: FunctionKey): Promise<boolean>
```

检查功能键（如：CapsLock键）是否使能。使用Promise异步回调。

**起始版本：** 15

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| functionKey | [FunctionKey](arkts-input-inputdevice-functionkey-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [3900002](../errorcode-inputdevice.md#3900002-键盘设备没有连接) |
