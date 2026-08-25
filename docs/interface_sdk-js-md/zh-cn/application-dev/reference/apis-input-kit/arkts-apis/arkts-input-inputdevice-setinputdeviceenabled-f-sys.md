# setInputDeviceEnabled（系统接口）

## 导入模块

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## setInputDeviceEnabled

```TypeScript
function setInputDeviceEnabled(deviceId: number, enabled: boolean): Promise<void>
```

设置输入设备的开关状态。以触摸屏为例：关闭时，点击触摸屏设备不响应；开启时，可正常操作触摸屏。使用Promise异步回调。

**起始版本：** 18

**需要权限：** ohos.permission.INPUT_DEVICE_CONTROLLER

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |
| enabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [3900001](../errorcode-inputdevice.md#3900001-指定的设备不存在) |
