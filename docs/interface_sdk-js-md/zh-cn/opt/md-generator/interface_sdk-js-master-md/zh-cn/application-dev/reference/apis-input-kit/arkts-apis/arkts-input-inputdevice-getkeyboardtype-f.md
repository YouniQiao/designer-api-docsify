# getKeyboardType

## getKeyboardType

```TypeScript
function getKeyboardType(deviceId: number, callback: AsyncCallback<KeyboardType>): void
```

获取输入设备的键盘类型，如全键盘、小键盘等。输入设备的键盘类型以接口返回结果为准。使用callback异步回调。

**起始版本：** 9

<!--Device-inputDevice-function getKeyboardType(deviceId: int, callback: AsyncCallback<KeyboardType>): void--><!--Device-inputDevice-function getKeyboardType(deviceId: int, callback: AsyncCallback<KeyboardType>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[KeyboardType](arkts-input-inputdevice-keyboardtype-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

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
          // 查询ID为1的输入设备的键盘类型。
          try {
            // 获取键盘类型
            inputDevice.getKeyboardType(1, (error: BusinessError, type: inputDevice.KeyboardType) => {
              if (error) {
                console.error(`Failed to get keyboard type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in getting keyboard type: ${JSON.stringify(type)}.`);
            });
          } catch (error) {
            console.error(`Failed to get keyboard type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## getKeyboardType

```TypeScript
function getKeyboardType(deviceId: number): Promise<KeyboardType>
```

获取输入设备的键盘类型，使用Promise异步回调。

**起始版本：** 9

<!--Device-inputDevice-function getKeyboardType(deviceId: int): Promise<KeyboardType>--><!--Device-inputDevice-function getKeyboardType(deviceId: int): Promise<KeyboardType>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| deviceId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[KeyboardType](arkts-input-inputdevice-keyboardtype-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |

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
            // 获取键盘类型
            inputDevice.getKeyboardType(1).then((type: inputDevice.KeyboardType) => {
              console.info(`Succeeded in getting keyboard type: ${JSON.stringify(type)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get keyboard type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get keyboard type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
