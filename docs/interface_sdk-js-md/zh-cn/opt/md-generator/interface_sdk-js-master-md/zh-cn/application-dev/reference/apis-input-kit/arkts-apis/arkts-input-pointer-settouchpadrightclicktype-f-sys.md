# setTouchpadRightClickType（系统接口）

## 导入模块

```TypeScript
```

## setTouchpadRightClickType

```TypeScript
function setTouchpadRightClickType(type: RightClickType, callback: AsyncCallback<void>): void
```

设置触控板右键菜单类型，使用callback异步回调。

**起始版本：** 23

<!--Device-pointer-function setTouchpadRightClickType(type: RightClickType, callback: AsyncCallback<void>): void--><!--Device-pointer-function setTouchpadRightClickType(type: RightClickType, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [RightClickType](arkts-input-pointer-rightclicktype-e.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

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
            // 设置触控板右键点击类型
            pointer.setTouchpadRightClickType(pointer.RightClickType.TOUCHPAD_RIGHT_BUTTON, (error: BusinessError) => {
              if (error) {
                console.error(`Failed to set touchpad right click type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in setting touchpad right click type.`);
            });
          } catch (error) {
            console.error(`Failed to set touchpad right click type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## setTouchpadRightClickType

```TypeScript
function setTouchpadRightClickType(type: RightClickType): Promise<void>
```

设置触控板右键菜单类型，使用Promise异步回调。

**起始版本：** 23

<!--Device-pointer-function setTouchpadRightClickType(type: RightClickType): Promise<void>--><!--Device-pointer-function setTouchpadRightClickType(type: RightClickType): Promise<void>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [RightClickType](arkts-input-pointer-rightclicktype-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

**示例**

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
            // 设置触摸板右键点击类型
            pointer.setTouchpadRightClickType(pointer.RightClickType.TOUCHPAD_RIGHT_BUTTON).then(() => {
              console.info(`Succeeded in setting touchpad right click type.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to set touchpad right click type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to set touchpad right click type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
