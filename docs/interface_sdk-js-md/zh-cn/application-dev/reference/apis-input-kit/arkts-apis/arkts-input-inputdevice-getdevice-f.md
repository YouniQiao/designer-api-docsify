# getDevice

## 导入模块

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## getDevice

```TypeScript
function getDevice(deviceId: number, callback: AsyncCallback<InputDeviceData>): void
```

获取指定id的输入设备信息，使用callback异步回调。

> **说明：**

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getDeviceInfo

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[InputDeviceData](arkts-input-inputdevice-inputdevicedata-i.md)&gt; | 是 |


## getDevice

```TypeScript
function getDevice(deviceId: number): Promise<InputDeviceData>
```

获取指定id的输入设备信息，使用Promise异步回调。

> **说明：**

**起始版本：** 8

**废弃版本：** 9

**替代接口：** getDeviceInfo

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[InputDeviceData](arkts-input-inputdevice-inputdevicedata-i.md)&gt; |
