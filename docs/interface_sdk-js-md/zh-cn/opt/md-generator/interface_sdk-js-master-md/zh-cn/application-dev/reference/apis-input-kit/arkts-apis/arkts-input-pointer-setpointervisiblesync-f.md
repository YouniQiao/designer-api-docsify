# setPointerVisibleSync

## setPointerVisibleSync

```TypeScript
function setPointerVisibleSync(visible: boolean): void
```

设置当前窗口鼠标光标的显示状态，使用同步方式。

**起始版本：** 10

<!--Device-pointer-function setPointerVisibleSync(visible: boolean): void--><!--Device-pointer-function setPointerVisibleSync(visible: boolean): void-End-->

**系统能力：** SystemCapability.MultimodalInput.Input.Pointer

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| visible | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

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
            // 同步设置鼠标指针可见性
            pointer.setPointerVisibleSync(false);
            console.info(`Succeeded in setting pointer cursor visible.`);
          } catch (error) {
            console.error(`Failed to set pointer cursor visible, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```
