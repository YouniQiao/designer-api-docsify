# transformPoint

## Modules to Import

```TypeScript
import { matrix4 } from '@kit.ArkUI';
```

## transformPoint

```TypeScript
function transformPoint(options: [number, number]): [number, number]
```

Applies the current transformation effect to a coordinate point.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [transformPoint](arkts-arkui-matrix4-matrix4transit-i.md#transformpoint)

<!--Device-matrix4-function transformPoint(options: [number, number]): [number, number]--><!--Device-matrix4-function transformPoint(options: [number, number]): [number, number]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [number, number] | Yes | Point to be transformed. |

**Return value:**

| Type | Description |
| --- | --- |
| [number, number] | Point object after matrix transformation |

**Examples**

```TypeScript
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private originPoint: number[] = [50, 50];
  private matrix_1 = matrix4.identity().translate({ x: 150, y: -50 });
  private transformPoint = this.matrix_1.transformPoint([this.originPoint[0], this.originPoint[1]]);
  private matrix_2 = matrix4.identity().translate({ x: this.transformPoint[0], y: this.transformPoint[1] });

  build() {
    Column() {
      Text(`Coordinates before matrix transformation: [${this.originPoint}]`)
        .fontSize(16)
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r("app.media.image"))
        .width('600px')
        .height('300px')
        .margin({ top: 50 })
      Text(`Coordinates after matrix transformation: [${this.transformPoint}]`)
        .fontSize(16)
        .margin({ top: 100 })
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r("app.media.image"))
        .width('600px')
        .height('300px')
        .margin({ top: 50 })
        .transform(this.matrix_2)
    }.width("100%").padding(50)
  }
}
```

