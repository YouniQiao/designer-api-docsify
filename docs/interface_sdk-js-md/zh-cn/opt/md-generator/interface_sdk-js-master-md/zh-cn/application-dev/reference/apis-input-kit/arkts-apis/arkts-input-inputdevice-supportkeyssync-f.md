# supportKeysSync

## supportKeysSync

```TypeScript
function supportKeysSync(deviceId: number, keys: Array<KeyCode>): Array<boolean>
```

查询指定id的输入设备对指定键值的支持情况。

**起始版本：** 10

<!--Device-inputDevice-function supportKeysSync(deviceId: int, keys: Array<KeyCode>): Array<boolean>--><!--Device-inputDevice-function supportKeysSync(deviceId: int, keys: Array<KeyCode>): Array<boolean>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |
| keys | Array&lt;[KeyCode](arkts-input-multimodalinput-keycode-keycode-e.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Array&lt;boolean&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

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
          // 查询ID为1的输入设备对于17、22和2055按键的支持情况。
          try {
            let supportResult: Array<Boolean> = inputDevice.supportKeysSync(1, [17, 22, 2055]);
            console.info(`Succeeded in querying support keys, result: ${JSON.stringify(supportResult)}.`);
          } catch (error) {
            console.error(`Failed to query support key, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
