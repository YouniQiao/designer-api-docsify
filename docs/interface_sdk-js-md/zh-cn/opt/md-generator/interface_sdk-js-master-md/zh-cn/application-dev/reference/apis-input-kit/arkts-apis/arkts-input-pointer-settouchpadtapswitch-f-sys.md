# setTouchpadTapSwitch（系统接口）

## setTouchpadTapSwitch

```TypeScript
function setTouchpadTapSwitch(state: boolean, callback: AsyncCallback<void>): void
```

设置触控板轻触功能开关，使用callback异步回调。

**起始版本：** 10

<!--Device-pointer-function setTouchpadTapSwitch(state: boolean, callback: AsyncCallback<void>): void--><!--Device-pointer-function setTouchpadTapSwitch(state: boolean, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| state | boolean | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // 设置触控板点击开关
            pointer.setTouchpadTapSwitch(true, (error: BusinessError) => {
              if (error) {
                console.error(`Failed to set touchpad tap switch, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in setting touchpad tap switch.`);
            });
          } catch (error) {
            console.error(`Failed to set touchpad tap switch, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`); 
          }
        })
    }
  }
}
```


## setTouchpadTapSwitch

```TypeScript
function setTouchpadTapSwitch(state: boolean): Promise<void>
```

设置触控板轻触功能开关，使用Promise异步回调。

**起始版本：** 10

<!--Device-pointer-function setTouchpadTapSwitch(state: boolean): Promise<void>--><!--Device-pointer-function setTouchpadTapSwitch(state: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| state | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Text()
        .onClick(() => {
          try {
            // 设置触摸板点击开关
            pointer.setTouchpadTapSwitch(false).then(() => {
              console.info(`Succeeded in setting touchpad tap switch.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to set touchpad tap switch, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to set touchpad tap switch, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
