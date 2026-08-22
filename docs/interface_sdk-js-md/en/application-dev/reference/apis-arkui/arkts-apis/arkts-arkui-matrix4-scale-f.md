# scale

## Modules to Import

```TypeScript
import { matrix4 } from '@kit.ArkUI';
```

## scale

```TypeScript
function scale(options: ScaleOption): Matrix4Transit
```

Scales this matrix object along the x, y, and z axes.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [scale](arkts-arkui-matrix4-matrix4transit-i.md#scale)

<!--Device-matrix4-function scale(options: ScaleOption): Matrix4Transit--><!--Device-matrix4-function scale(options: ScaleOption): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ScaleOption](arkts-arkui-matrix4-scaleoption-i.md) | Yes | Scaling configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| Matrix4Transit | Matrix object after scaling. |

**Examples**

```TypeScript
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity()
    .scale({
      x: 2,
      y: 3,
      z: 4,
      centerX: 50,
      centerY: 50
    });

  build() {
    Column() {
      // Replace $r("app.media.testImage") with the image resource file you use.
      Image($r("app.media.testImage")).transform(this.matrix1)
        .width("300px")
        .height("300px")
    }.width("100%").height("100%").justifyContent(FlexAlign.Center)
  }
}
```

