# getKeyboardRepeatDelay（系统接口）

## getKeyboardRepeatDelay

```TypeScript
function getKeyboardRepeatDelay(callback: AsyncCallback<number>): void
```

获取键盘按键的重复时延，使用callback异步回调。

**起始版本：** 10

<!--Device-inputDevice-function getKeyboardRepeatDelay(callback: AsyncCallback<int>): void--><!--Device-inputDevice-function getKeyboardRepeatDelay(callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

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
          try {
            // 获取键盘重复延迟
            inputDevice.getKeyboardRepeatDelay((error: BusinessError, delay: number) => {
              if (error) {
                console.error(`Failed to get keyboard repeat delay, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in getting keyboard repeat delay.`);
            });
          } catch (error) {
            console.error(`Failed to get keyboard repeat delay, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## getKeyboardRepeatDelay

```TypeScript
function getKeyboardRepeatDelay(): Promise<number>
```

获取键盘按键的重复时延，使用Promise异步回调。

**起始版本：** 10

<!--Device-inputDevice-function getKeyboardRepeatDelay(): Promise<int>--><!--Device-inputDevice-function getKeyboardRepeatDelay(): Promise<int>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputDevice

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

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
          try {
            // 获取键盘重复延迟
            inputDevice.getKeyboardRepeatDelay().then((delay: number) => {
              console.info(`Succeeded in getting keyboard repeat delay.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get keyboard repeat delay, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get keyboard repeat delay, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
