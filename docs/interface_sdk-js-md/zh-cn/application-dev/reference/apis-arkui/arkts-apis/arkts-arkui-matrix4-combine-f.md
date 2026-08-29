# combine

## 导入模块

```TypeScript
import { matrix4 } from '@kit.ArkUI';
```

## combine

```TypeScript
function combine(options: Matrix4Transit): Matrix4Transit
```

Matrix的叠加函数，可以将两个矩阵的效果叠加起来作用于当前矩阵。会改变调用该函数的原始矩阵。

> **说明：**
> 
> matrixA.combine(matrixB)与matrixB.combine(matrixA)的变换结果不同。combine()的调用顺序决定了变换的叠加顺序，例如先平移后缩放与先缩放后平移的变换效果不同。使用时需根据预期
> 的变换效果选择正确的调用顺序。如需保留原始矩阵不被修改，应先调用copy()再调用combine()，例如：matrixA.copy().combine(matrixB)。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [combine](arkts-arkui-matrix4-matrix4transit-i.md#combine)

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | Matrix4Transit | 是 | 待叠加的矩阵对象，其变换效果将与单位矩阵进行叠加。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Matrix4Transit | 叠加后的矩阵对象。 |

**示例**

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
      // 矩阵变换前
      // $r("app.media.icon")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.icon"))
        .width('40%')
        .height(100)
        .margin({ top: 50 })
      // 先平移x轴200px，再缩放两倍x轴，得到矩阵变换后的效果图
      // $r("app.media.icon")需要替换为开发者所需的图像资源文件。
      Image($r("app.media.icon"))
        .transform(this.matrix1.copy().combine(this.matrix2))
        .width("40%")
        .height(100)
        .margin({ top: 50 })
    }
  }
}
```
