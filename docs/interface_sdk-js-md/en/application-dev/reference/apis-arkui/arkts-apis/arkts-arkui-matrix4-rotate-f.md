# rotate

## Modules to Import

```TypeScript
import { matrix4 } from '@kit.ArkUI';
```

## rotate

```TypeScript
function rotate(options: RotateOption): Matrix4Transit
```

Rotates this matrix object along the x, y, and z axes.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [rotate](arkts-arkui-matrix4-matrix4transit-i.md#rotate)

<!--Device-matrix4-function rotate(options: RotateOption): Matrix4Transit--><!--Device-matrix4-function rotate(options: RotateOption): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RotateOption](arkts-arkui-matrix4-rotateoption-i.md) | Yes | Rotation configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| Matrix4Transit | Matrix object after rotation. |

**Examples**

```TypeScript
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity()
    .rotate({
      x: 1,
      y: 1,
      z: 2,
      angle: 30
    });

  build() {
    Column() {
      // Replace $r("app.media.bg1") with the image resource file you use.
      Image($r("app.media.bg1")).transform(this.matrix1)
        .width("40%")
        .height(100)
    }.width("100%").margin({ top: 50 })
  }
}
```

