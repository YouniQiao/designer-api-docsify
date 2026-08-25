# setFunctionKeyEnabled

## 导入模块

```TypeScript
import { inputDevice } from 'kits/@kit.InputKit';
```

## setFunctionKeyEnabled

```TypeScript
function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>
```

设置功能键（如：CapsLock键）使能状态。使用Promise异步回调。

**起始版本：** 15

**需要权限：** ohos.permission.INPUT_KEYBOARD_CONTROLLER

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| functionKey | [FunctionKey](arkts-input-inputdevice-functionkey-e.md) | 是 |
| enabled | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [3900002](../errorcode-inputdevice.md#3900002-键盘设备没有连接) |
| [3900003](../errorcode-inputdevice.md#3900003-非输入法应用调用) |
