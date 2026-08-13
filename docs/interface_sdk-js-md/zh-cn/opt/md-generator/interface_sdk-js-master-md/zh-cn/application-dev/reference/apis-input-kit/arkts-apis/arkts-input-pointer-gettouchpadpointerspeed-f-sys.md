# getTouchpadPointerSpeed（系统接口）

## getTouchpadPointerSpeed

```TypeScript
function getTouchpadPointerSpeed(callback: AsyncCallback<number>): void
```

获取触控板光标移动速度，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-pointer-function getTouchpadPointerSpeed(callback: AsyncCallback<int>): void--><!--Device-pointer-function getTouchpadPointerSpeed(callback: AsyncCallback<int>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

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
            // 获取触控板光标速度
            pointer.getTouchpadPointerSpeed((error: BusinessError, speed: number) => {
              if (error) {
                console.error(`Failed to get touchpad pointer speed, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
              } else {
                console.info(`Succeeded in getting touchpad pointer speed, speed: ${JSON.stringify(speed)}.`);
              }
            });
          } catch (error) {
            console.error(`Failed to get touchpad pointer speed, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## getTouchpadPointerSpeed

```TypeScript
function getTouchpadPointerSpeed(): Promise<number>
```

获取触控板光标移动速度，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-pointer-function getTouchpadPointerSpeed(): Promise<int>--><!--Device-pointer-function getTouchpadPointerSpeed(): Promise<int>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

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
            // 获取触摸板指针速度
            pointer.getTouchpadPointerSpeed().then((speed: number) => {
              console.info(`Succeeded in getting touchpad pointer speed, speed: ${JSON.stringify(speed)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get touchpad pointer speed, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get touchpad pointer speed, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
