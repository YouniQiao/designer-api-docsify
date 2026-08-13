# getMouseScrollRows（系统接口）

## getMouseScrollRows

```TypeScript
function getMouseScrollRows(callback: AsyncCallback<number>): void
```

获取鼠标滚动行数，使用callback异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-pointer-function getMouseScrollRows(callback: AsyncCallback<int>): void--><!--Device-pointer-function getMouseScrollRows(callback: AsyncCallback<int>): void-End-->

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
            // 获取鼠标滚动行数
            pointer.getMouseScrollRows((error: BusinessError, rows: number) => {
              if (error) {
                console.error(`Failed to get mouse scroll rows, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
              } else {
                console.info(`Succeeded in getting mouse scroll rows, rows: ${JSON.stringify(rows)}.`);
              }
            });
          } catch (error) {
            console.error(`Failed to get mouse scroll rows, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## getMouseScrollRows

```TypeScript
function getMouseScrollRows(): Promise<number>
```

获取当前鼠标滚动行数，使用Promise异步回调。

**起始版本：** 23

**废弃版本：** -1

<!--Device-pointer-function getMouseScrollRows(): Promise<int>--><!--Device-pointer-function getMouseScrollRows(): Promise<int>-End-->

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
            // 获取鼠标滚动行数
            pointer.getMouseScrollRows().then((rows: number) => {
              console.info(`Succeeded in getting mouse scroll rows, rows: ${JSON.stringify(rows)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get mouse scroll rows, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get mouse scroll rows, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
