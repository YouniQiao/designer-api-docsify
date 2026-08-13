# getTouchpadRightClickType（系统接口）

## getTouchpadRightClickType

```TypeScript
function getTouchpadRightClickType(callback: AsyncCallback<RightClickType>): void
```

获取触控板右键菜单类型，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-pointer-function getTouchpadRightClickType(callback: AsyncCallback<RightClickType>): void--><!--Device-pointer-function getTouchpadRightClickType(callback: AsyncCallback<RightClickType>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[RightClickType](arkts-input-pointer-rightclicktype-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
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
            // 获取触控板右键点击类型
            pointer.getTouchpadRightClickType((error: BusinessError, type: pointer.RightClickType) => {
              if (error) {
                console.error(`Failed to get touchpad right click type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in getting touchpad right click type, type: ${JSON.stringify(type)}.`);
            });
          } catch (error) {
            console.error(`Failed to get touchpad right click type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## getTouchpadRightClickType

```TypeScript
function getTouchpadRightClickType(): Promise<RightClickType>
```

获取触控板右键菜单类型，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-pointer-function getTouchpadRightClickType(): Promise<RightClickType>--><!--Device-pointer-function getTouchpadRightClickType(): Promise<RightClickType>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[RightClickType](arkts-input-pointer-rightclicktype-e.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
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
            // 获取触摸板右键点击类型
            pointer.getTouchpadRightClickType().then((type: pointer.RightClickType) => {
              console.info(`Succeeded in getting touchpad right click type, type: ${JSON.stringify(type)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get touchpad right click type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get touchpad right click type, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
