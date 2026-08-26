# combine

## Modules to Import

```TypeScript
import matrix4 from '@kit.ArkUI';
```

## combine

```TypeScript
function combine(options: Matrix4Transit): Matrix4Transit
```

Combines the effects of two matrices to generate a new matrix object.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [combine](arkts-arkui-matrix4-matrix4transit-i.md#combine)

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) | Yes | Matrix object to be combined. |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) | Matrix object after combination. |

**Examples**

```TypeScript
// xxx.ets
import { matrix4 } from '@kit.ArkUI';

@Entry
@Component
struct Test {
  private matrix1 = matrix4.identity().translate({ x: 200 });
  private matrix2 = matrix4.identity().scale({ x: 2 });

  build() {
    Column() {
      // Before matrix transformation
      // Replace $r("app.media.icon") with the image resource file you use.
      Image($r("app.media.icon"))
        .width('40%')
        .height(100)
        .margin({ top: 50 })
      // Translate the x-axis by 200px, and then scale it twice to obtain the resultant matrix.
      // Replace $r("app.media.icon") with the image resource file you use.
      Image($r("app.media.icon"))
        .transform(this.matrix1.copy().combine(this.matrix2))
        .width("40%")
        .height(100)
        .margin({ top: 50 })
    }
  }
}
```
