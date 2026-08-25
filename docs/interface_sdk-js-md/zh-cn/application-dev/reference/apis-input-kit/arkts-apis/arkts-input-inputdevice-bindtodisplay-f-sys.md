# bindToDisplay（系统接口）

## 导入模块

```TypeScript
import { inputDevice } from '@kit.InputKit';
```

## bindToDisplay

```TypeScript
function bindToDisplay(inputDeviceId: int, displayId: int): Promise<void>
```

将输入设备绑定到显示器。 仅支持外接USB和蓝牙的鼠标、触摸板、键盘和游戏控手柄。 绑定后，设备将固定在指定显示器所在的显示器组上操作。 该接口使用promise返回结果。

**起始版本：** 26.1.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.1.0。

**需要权限：** ohos.permission.INPUT_DEVICE_CONTROLLER

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| inputDeviceId | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| displayId | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [3800001](../errorcode-infraredemitter.md#3800001-多模输入服务内部错误) |
| [3900001](../errorcode-inputdevice.md#3900001-指定的设备不存在) |
| [3900004](../errorcode-inputdevice.md#3900004-指定的显示器不存在) |
| [3900005](../errorcode-inputdevice.md#3900005-不支持的输入设备) |
