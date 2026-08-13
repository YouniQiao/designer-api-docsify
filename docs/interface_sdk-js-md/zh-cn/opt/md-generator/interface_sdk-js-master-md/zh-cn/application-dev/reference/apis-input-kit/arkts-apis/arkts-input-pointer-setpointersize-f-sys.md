# setPointerSize（系统接口）

## setPointerSize

```TypeScript
function setPointerSize(size: number, callback: AsyncCallback<void>): void
```

设置鼠标光标大小，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-pointer-function setPointerSize(size: int, callback: AsyncCallback<void>): void--><!--Device-pointer-function setPointerSize(size: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

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
            // 设置鼠标光标大小
            pointer.setPointerSize(1, (error: BusinessError) => {
              if (error) {
                console.error(`Failed to set pointer size, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in setting pointer size.`);
            });
          } catch (error) {
            console.error(`Failed to set pointer size, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## setPointerSize

```TypeScript
function setPointerSize(size: number): Promise<void>
```

设置鼠标光标大小，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-pointer-function setPointerSize(size: int): Promise<void>--><!--Device-pointer-function setPointerSize(size: int): Promise<void>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

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
            // 设置鼠标指针大小
            pointer.setPointerSize(3).then(() => {
              console.info(`Succeeded in setting pointer size.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to set pointer size, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to set pointer size, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
