# getKeyboardTypeSync

## 导入模块

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## getKeyboardTypeSync

```TypeScript
function getKeyboardTypeSync(deviceId: number): KeyboardType
```

获取输入设备的键盘类型。

**起始版本：** 10

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [KeyboardType](arkts-input-inputdevice-keyboardtype-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
