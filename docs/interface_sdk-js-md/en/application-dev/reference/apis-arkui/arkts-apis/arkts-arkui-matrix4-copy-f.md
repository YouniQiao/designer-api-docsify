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

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 10

**Substitutes:** [copy](arkts-arkui-matrix4-matrix4transit-i.md#copy)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Matrix4Transit](arkts-arkui-matrix4transit-t.md) |

**Examples**

```TypeScript
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity().scale({ x: 1.5 });
  private matrix2 = this.matrix1.copy().translate({ x: 200 });
  imageSize: Length = '300px';

  build() {
    Column({ space: "50px" }) {
      // Replace $r("app.media.testImage") with the image resource file you use.
      Image($r("app.media.testImage"))
        .width(this.imageSize)
        .height(this.imageSize)
      // Replace $r("app.media.testImage") with the image resource file you use.
      Image($r("app.media.testImage"))
        .width(this.imageSize)
        .height(this.imageSize)
        .transform(this.matrix1)
      // Replace $r("app.media.testImage") with the image resource file you use.
      Image($r("app.media.testImage"))
        .width(this.imageSize)
        .height(this.imageSize)
        .transform(this.matrix2)
    }.alignItems(HorizontalAlign.Center)
    .height('100%').width("100%")
    .justifyContent(FlexAlign.Center)
  }
}
```

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
