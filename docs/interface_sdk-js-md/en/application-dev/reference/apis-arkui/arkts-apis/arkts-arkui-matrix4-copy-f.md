# copy

## Modules to Import

```TypeScript
import { matrix4 } from '@kit.ArkUI';
```

## copy

```TypeScript
function copy(): Matrix4Transit
```

Copies this matrix object.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [copy](arkts-arkui-matrix4-matrix4transit-i.md#copy)

<!--Device-matrix4-function copy(): Matrix4Transit--><!--Device-matrix4-function copy(): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Matrix4Transit | Copy object of the current matrix. |

**Examples**

```TypeScript
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity().translate({ x: 100 });
  // Perform the scale operation on the copy matrix of matrix1, which does not affect matrix1.
  private matrix2 = this.matrix1.copy().scale({ x: 2 });

  build() {
    Column() {
      // Replace $r("app.media.bg1") with the image resource file you use.
      Image($r("app.media.bg1"))
        .width("40%")
        .height(100)
        .transform(this.matrix1)
      // Replace $r("app.media.bg2") with the image resource file you use.
      Image($r("app.media.bg2"))
        .width("40%")
        .height(100)
        .margin({ top: 50 })
        .transform(this.matrix2)
    }
  }
}
```

