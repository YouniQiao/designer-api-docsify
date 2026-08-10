# getPointerStyleSync

## Modules to Import

```TypeScript
import { pointer } from 'kits/@kit.InputKit';
```

## getPointerStyleSync

```TypeScript
function getPointerStyleSync(windowId: int): PointerStyle
```

查询指定窗口的鼠标样式类型，如向东箭头、向西箭头、向南箭头、向北箭头等。此接口仅支持获取本应用进程内窗口的鼠标样式类型。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-pointer-function getPointerStyleSync(windowId: int): PointerStyle--><!--Device-pointer-function getPointerStyleSync(windowId: int): PointerStyle-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Pointer

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| windowId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | 窗口ID。取值范围为大于等于-1的整数，取值为-1时表示全局窗口。&lt;br&gt;窗口ID合法并且对应窗口存在时，返回窗口的鼠标光标样式。&lt;br&gt;窗口ID合法但窗口不存在时，默认返回全局 鼠标光标样式。&lt;br&gt;如果通过[setPointerStyleSync](arkts-input-pointer-setpointerstylesync-f.md#setpointerstylesync)接口为不存在的窗口设置了鼠标光标样式，使用本接口可以正常获取到该光标样式。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PointerStyle](../../apis-arkui/arkts-components/arkts-arkui-pointerstyle-t.md) | 返回鼠标样式类型。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## Examples

```TypeScript
import { pointer } from '@kit.InputKit';

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

