# getTouchpadScrollDirection（系统接口）

## getTouchpadScrollDirection

```TypeScript
function getTouchpadScrollDirection(callback: AsyncCallback<boolean>): void
```

获取触控板滚轴方向，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-pointer-function getTouchpadScrollDirection(callback: AsyncCallback<boolean>): void--><!--Device-pointer-function getTouchpadScrollDirection(callback: AsyncCallback<boolean>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

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
            // 获取触控板滚动方向
            pointer.getTouchpadScrollDirection((error: BusinessError, state: boolean) => {
              if (error) {
                console.error(`Failed to get touchpad scroll direction, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in getting touchpad scroll direction, state: ${JSON.stringify(state)}.`);
            });
          } catch (error) {
            console.error(`Failed to get touchpad scroll direction, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## getTouchpadScrollDirection

```TypeScript
function getTouchpadScrollDirection(): Promise<boolean>
```

获取触控板滚轴方向，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-pointer-function getTouchpadScrollDirection(): Promise<boolean>--><!--Device-pointer-function getTouchpadScrollDirection(): Promise<boolean>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

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
            // 获取触摸板滚动方向
            pointer.getTouchpadScrollDirection().then((state: boolean) => {
              console.info(`Succeeded in getting touchpad scroll direction, state: ${JSON.stringify(state)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get touchpad scroll direction, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get touchpad scroll direction, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
