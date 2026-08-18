# setFunctionKeyEnabled

## 导入模块

```TypeScript
```

## setFunctionKeyEnabled

```TypeScript
function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>
```

设置功能键（如：CapsLock键）使能状态。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.INPUT_KEYBOARD_CONTROLLER

<!--Device-inputDevice-function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>--><!--Device-inputDevice-function setFunctionKeyEnabled(functionKey: FunctionKey, enabled: boolean): Promise<void>-End-->

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
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [3900003](../errorcode-inputdevice.md#3900003-非输入法应用调用) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [3900002](../errorcode-inputdevice.md#3900002-键盘设备没有连接) |

**示例**

```TypeScript
import { inputDevice } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // 设置功能键使能状态
            inputDevice.setFunctionKeyEnabled(inputDevice.FunctionKey.CAPS_LOCK, true).then(() => {
              console.info(`Succeeded in setting capslock state.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to set capslock state, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            });
          } catch (error) {
            console.error(`Failed to set capslock enable, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
