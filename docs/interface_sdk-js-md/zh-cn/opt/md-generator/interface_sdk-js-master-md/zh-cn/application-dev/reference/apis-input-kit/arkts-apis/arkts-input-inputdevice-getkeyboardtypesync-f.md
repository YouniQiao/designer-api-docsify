# getKeyboardTypeSync

## getKeyboardTypeSync

```TypeScript
function getKeyboardTypeSync(deviceId: number): KeyboardType
```

获取输入设备的键盘类型。

**起始版本：** 23

**废弃版本：** -1

<!--Device-inputDevice-function getKeyboardTypeSync(deviceId: int): KeyboardType--><!--Device-inputDevice-function getKeyboardTypeSync(deviceId: int): KeyboardType-End-->

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

## 示例

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
          // 示例查询设备ID为1的设备键盘类型。
          try {
            let type: inputDevice.KeyboardType = inputDevice.getKeyboardTypeSync(1);
            console.info(`Succeeded in getting keyboard type: ${JSON.stringify(type)}.`);
          } catch (error) {
            console.error(`Failed to get keyboard type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
