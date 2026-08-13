# getPointerStyleSync

## getPointerStyleSync

```TypeScript
function getPointerStyleSync(windowId: number): PointerStyle
```

查询指定窗口的鼠标样式类型，如向东箭头、向西箭头、向南箭头、向北箭头等。此接口仅支持获取本应用进程内窗口的鼠标样式类型。

**起始版本：** 23

**废弃版本：** -1

<!--Device-pointer-function getPointerStyleSync(windowId: int): PointerStyle--><!--Device-pointer-function getPointerStyleSync(windowId: int): PointerStyle-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| windowId | number | 是 |

**返回值：**

| 类型 |
| --- |
| [PointerStyle](../../apis-na/arkts-apis/arkts-na-pointerstyle-t.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

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
          let windowId = -1;
          try {
            let style: pointer.PointerStyle = pointer.getPointerStyleSync(windowId);
            console.info(`Succeeded in getting pointer style, style: ${JSON.stringify(style)}.`);
          } catch (error) {
            console.error(`Failed to get pointer style, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
