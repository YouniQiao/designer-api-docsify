# setMouseScrollRows（系统接口）

## setMouseScrollRows

```TypeScript
function setMouseScrollRows(rows: number, callback: AsyncCallback<void>): void
```

设置鼠标滚动行数，使用callback异步回调。

**起始版本：** 10

<!--Device-pointer-function setMouseScrollRows(rows: int, callback: AsyncCallback<void>): void--><!--Device-pointer-function setMouseScrollRows(rows: int, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rows | number | 是 |
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
            // 设置鼠标滚动行数
            pointer.setMouseScrollRows(1, (error: BusinessError) => {
              if (error) {
                console.error(`Failed to set mouse scroll rows, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
                return;
              }
              console.info(`Succeeded in setting mouse scroll rows.`);
            });
          } catch (error) {
            console.error(`Failed to set mouse scroll rows, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```


## setMouseScrollRows

```TypeScript
function setMouseScrollRows(rows: number): Promise<void>
```

设置鼠标滚动行数，使用Promise异步回调。

**起始版本：** 10

<!--Device-pointer-function setMouseScrollRows(rows: int): Promise<void>--><!--Device-pointer-function setMouseScrollRows(rows: int): Promise<void>-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rows | number | 是 |

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
            // 设置鼠标滚动行数
            pointer.setMouseScrollRows(20).then(() => {
              console.info(`Succeeded in setting mouse scroll rows.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to set mouse scroll rows, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to set mouse scroll rows, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
