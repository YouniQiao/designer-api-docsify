# injectEvent

## injectEvent

```TypeScript
function injectEvent({ KeyEvent: KeyEvent }): void
```

按键(包括单个按键和组合键)注入。

**起始版本：** 8

**需要权限：** 
- API版本12+：ohos.permission.INJECT_INPUT_EVENT

<!--Device-inputEventClient-function injectEvent({ KeyEvent: KeyEvent }): void--><!--Device-inputEventClient-function injectEvent({ KeyEvent: KeyEvent }): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.InputSimulator

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| { KeyEvent: KeyEvent } | 0.0 | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { inputEventClient } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            let backKeyDown: inputEventClient.KeyEvent = {
              isPressed: true,
              keyCode: 2,
              keyDownDuration: 0,
              isIntercepted: false
            };
            // 注入事件
            inputEventClient.injectEvent({ KeyEvent: backKeyDown });

            let backKeyUp: inputEventClient.KeyEvent = {
              isPressed: false,
              keyCode: 2,
              keyDownDuration: 0,
              isIntercepted: false
            };
            // 注入事件
            inputEventClient.injectEvent({ KeyEvent: backKeyUp });
          } catch (error) {
            console.error(`Failed to inject KeyEvent, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
