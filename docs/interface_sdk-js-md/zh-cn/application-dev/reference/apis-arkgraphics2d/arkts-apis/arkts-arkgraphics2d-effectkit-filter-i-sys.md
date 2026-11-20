# Filter（系统接口）

```TypeScript
interface Filter
```

图像效果类，用于通过链式调用将指定效果添加到效果链表中，适用于图片滤镜处理、视觉效果增强、图像美化等场景。在调用Filter的方法前，需要先通过[createEffect](arkts-arkgraphics2d-effectkit-createeffect-f.md)创建一个Filter实例。在添加效果后，需调用[getEffectPixelMap](arkts-arkgraphics2d-effectkit-filter-i.md#geteffectpixelmap)获取处理后的图像。

**起始版本：** 9

<!--Device-effectKit-interface Filter--><!--Device-effectKit-interface Filter-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

## 导入模块

```TypeScript
import { effectKit } from '@kit.ArkGraphics2D';
```

## ellipticalGradientBlur

```TypeScript
ellipticalGradientBlur(blurRadius: number, center: EllipticalMaskCenter,
      maskRadius: EllipticalMaskRadius, fractionStops: FractionStop[]): Filter
```

将带有椭圆形遮罩的渐变模糊效果添加到效果链表中，返回链表的头节点。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Filter-ellipticalGradientBlur(blurRadius: double, center: EllipticalMaskCenter,      maskRadius: EllipticalMaskRadius, fractionStops: FractionStop[]): Filter--><!--Device-Filter-ellipticalGradientBlur(blurRadius: double, center: EllipticalMaskCenter,      maskRadius: EllipticalMaskRadius, fractionStops: FractionStop[]): Filter-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| blurRadius | number | 是 | 模糊半径，取正整数，单位为px，模糊半径大于60px时自动截断。 模糊效果与所设置的模糊半径值成正比，值越大效果越明显。 |
| center | [EllipticalMaskCenter](arkts-arkgraphics2d-effectkit-ellipticalmaskcenter-t-sys.md) | 是 | 椭圆形遮罩的中心点坐标。 |
| maskRadius | [EllipticalMaskRadius](arkts-arkgraphics2d-effectkit-ellipticalmaskradius-t-sys.md) | 是 | 椭圆形遮罩在X轴和Y轴方向的半径。 |
| fractionStops | FractionStop[] | 是 | 渐变模糊位置与程度数组。数组元素为二元数组，第一个元素表示位置，第二个元素表示模糊程度。位置取值范围为[0, 1]，椭圆中心对应位置0，椭圆边界对应位置1。模糊程度取值范围为[0, 1]，0表示无模糊，大于1的值自动转为1。位置参数值需严格递增，数组长度不能小于2，最大为12。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](arkts-arkgraphics2d-effectkit-filter-i.md) | 返回已添加的图像效果。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-非系统应用调用系统-api) | Permission verification failed. A non-system application calls a system API. |

<!--Del-->
**示例**

```TypeScript
import { image } from '@kit.ImageKit';
import { effectKit } from '@kit.ArkGraphics2D';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
// 传入读取的图片数据
function ImageEllipticalGradientBlur(imageBuffer: ArrayBuffer): Promise<image.PixelMap> {
  return new Promise((resolve, reject) => {
    let imageSource = image.createImageSource(imageBuffer);
    let blurRadius:number = 25;
    let fractionStops:FractionStop[] = [[0, 0.2], [0.5, 0.7]];
    let maskRadius:effectKit.EllipticalMaskRadius = [1, 1];
    let center:effectKit.EllipticalMaskCenter = [0.5, 0.5];
    imageSource.createPixelMap().then((pixelMap: image.PixelMap) => {
      // 图像源使用完毕后及时释放
      imageSource.release();
      let headFilter = effectKit.createEffect(pixelMap);
      if (headFilter != null) {
        // 对图片添加效果标识
        headFilter.ellipticalGradientBlur(blurRadius, center, maskRadius, fractionStops);
        // 按照添加的效果标识对图片进行处理并且返回处理好的图片数据
        headFilter.getEffectPixelMap(false).then(imageData => {
          resolve(imageData);
        }).catch((err: BusinessError) => {
          reject(err);
        });
      } else {
        // 创建Filter实例失败，通过reject将错误传递给调用方
        reject(new Error('Failed to create filter.'));
      }
    }).catch((err: BusinessError) => {
      reject(err);
    }).finally(() => {
      imageSource.release();
    });
  });
}

@Entry
@Component
struct Index {
  @State imagePixelMap: image.PixelMap | null = null;
  private imageBuffer: ArrayBuffer | undefined = undefined;
  // 读取rawfile文件夹下的图片文件，也可根据需求更换读取方式，保证最终得到的是ArrayBuffer格式的图片数据即可
  async getFileBuffer(): Promise<ArrayBuffer | undefined> {
    try {
      const context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
      const fileData: Uint8Array = await context.resourceManager.getRawFileContent('image.png');
      const buffer: ArrayBuffer = fileData.buffer.slice(0);
      return buffer;
    } catch (err) {
      return undefined;
    }
  }

  async aboutToAppear(): Promise<void> {
    this.imageBuffer = await this.getFileBuffer();
    if (this.imageBuffer == undefined) {
      return;
    }
    // 图片处理为异步操作，可以依据是否需要拿到处理好的图片数据再进行下一步逻辑，按需添加await进行同步
    this.imagePixelMap = await ImageEllipticalGradientBlur(this.imageBuffer);
  }

  build() {
    Column() {
      Image(this.imagePixelMap)
        .width(304)
        .height(305)
    }
    .height('100%')
    .width('100%')
  }
}
```

<!--DelEnd-->

## halftone

```TypeScript
halftone(halftoneParam: HalftoneParam, outlineWidth?: number, shadowOptions?: ShadowOptions): Filter
```

将网点效果、描边和阴影效果添加至效果链表，并返回链表头节点。该效果将原图划分为规则网格，根据各网格中心的采样颜色及其亮度生成网点。每个网格以白色为背景，网点由黑色内圈和彩色圆环组成。

> **说明：** 
> 
> 输入图像应为仅包含单个主体、轮廓清晰的抠图图像，主体部分完全不透明，背景区域完全透明，不符合该标准的输入图像可能产生异常效果。
> 输入PixelMap的像素格式应为RGBA_8888、BGRA_8888、RGBA_F16或RGBA_1010102，不符合该标准的像素格式会导致输出异常。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Filter-halftone(halftoneParam: HalftoneParam, outlineWidth?: double, shadowOptions?: ShadowOptions): Filter--><!--Device-Filter-halftone(halftoneParam: HalftoneParam, outlineWidth?: double, shadowOptions?: ShadowOptions): Filter-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| halftoneParam | [HalftoneParam](arkts-arkgraphics2d-effectkit-halftoneparam-i-sys.md) | 是 | 网点配置参数。 |
| outlineWidth | number | 否 | 可选参数，描边宽度，单位为px。主体向外扩展出宽度为outlineWidth的白色边缘，超过作用图像范围自动截断。取值范围为[0, +∞)，超出取值范围时按边界值截断。默认值为0.0。 |
| shadowOptions | [ShadowOptions](arkts-arkgraphics2d-effectkit-shadowoptions-i-sys.md) | 否 | 可选参数，阴影配置参数，不传时使用默认阴影配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](arkts-arkgraphics2d-effectkit-filter-i.md) | 返回已添加效果的Filter实例，用于继续添加效果或获取处理后的图像。 |

## outline

```TypeScript
outline(outlineWidth: number, shadowOptions?: ShadowOptions): Filter
```

将描边和阴影效果添加至效果链表，并返回链表的头节点。该效果提取图像中非透明区域的轮廓生成描边，并根据阴影配置生成投影。

> **说明：** 
> 
> 输入图像应为仅包含单个主体、轮廓清晰的抠图图像，主体部分完全不透明，背景区域完全透明，不符合该标准的输入图像可能产生异常效果。
> 输入PixelMap的像素格式应为RGBA_8888、BGRA_8888、RGBA_F16或RGBA_1010102，不符合该标准的像素格式会导致输出异常。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-Filter-outline(outlineWidth: double, shadowOptions?: ShadowOptions): Filter--><!--Device-Filter-outline(outlineWidth: double, shadowOptions?: ShadowOptions): Filter-End-->

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| outlineWidth | number | 是 | 描边宽度，单位为px。主体向外扩展出宽度为outlineWidth的白色边缘，超过作用图像范围自动截断。取值范围为[0, +∞)，超出取值范围时按边界值截断。 |
| shadowOptions | [ShadowOptions](arkts-arkgraphics2d-effectkit-shadowoptions-i-sys.md) | 否 | 可选参数，阴影配置参数，不传时使用默认阴影配置。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Filter](arkts-arkgraphics2d-effectkit-filter-i.md) | 返回已添加效果的Filter实例，用于继续添加效果或获取处理后的图像。 |
