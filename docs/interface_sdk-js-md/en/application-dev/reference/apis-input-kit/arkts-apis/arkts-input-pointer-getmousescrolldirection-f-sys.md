# getMouseScrollDirection (System API)

## Modules to Import

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## getMouseScrollDirection

```TypeScript
function getMouseScrollDirection(): Promise<boolean>
```

获取鼠标滚轮滚动方向，使用Promise异步回调。

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.INPUT_DEVICE_CONTROLLER

<!--Device-pointer-function getMouseScrollDirection(): Promise<boolean>--><!--Device-pointer-function getMouseScrollDirection(): Promise<boolean>-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象。返回true表示鼠标滚轮滚动方向与手指方向一致；返回false表示鼠标滚轮滚动方向与手指方向相反。默认为true。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 3800001 | Input service exception. |
| 201 | permission denied. |
| 202 | SystemAPI permission error. |

## Examples

```TypeScript
import { pointer } from '@kit.InputKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  build() {
    RelativeContainer() {
      Button("getMouseScrollDirection")
        .onClick(() => {
          try {
            // Obtain the mouse scroll direction.
            pointer.getMouseScrollDirection().then((state: boolean) => {
              console.info(`Succeeded in getting mouse scroll direction, state: ${JSON.stringify(state)}.`);
            }).catch((error: BusinessError) => {
              console.error(`Failed to get mouse scroll direction, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
            })
          } catch (error) {
            console.error(`Failed to get mouse scroll direction, Code: ${(error as BusinessError).code}, message: ${(error as BusinessError).message}.`);
          }
        })
    }
  }
}
```

