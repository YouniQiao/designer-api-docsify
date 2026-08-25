# getDeviceInfoSync

## 导入模块

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## getDeviceInfoSync

```TypeScript
function getDeviceInfoSync(deviceId: number): InputDeviceData
```

获取指定输入设备的信息。

**起始版本：** 10

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [InputDeviceData](arkts-input-inputdevice-inputdevicedata-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
