# off

## 导入模块

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## off('change')

```TypeScript
function off(type: 'change', listener?: Callback<DeviceListener>): void
```

取消监听输入设备的热插拔事件。在应用退出前调用，取消监听。使用callback异步回调。

**起始版本：** 9

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'change' | 是 |
| listener | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DeviceListener](arkts-input-inputdevice-devicelistener-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
