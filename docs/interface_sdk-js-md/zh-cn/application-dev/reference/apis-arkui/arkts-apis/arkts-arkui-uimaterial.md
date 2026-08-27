# @ohos.arkui.uiMaterial

本模块提供系统材质的接口定义。不同的系统材质对应不同的UI效果，包括背景色backgroundColor、边框颜色borderColor、边框宽度borderWidth、阴影shadow效果。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { uiMaterial } from '@kit.ArkUI';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [getMaterialInfo](arkts-arkui-uimaterial-getmaterialinfo-f.md) | 获取当前应用的材质配置信息。返回的配置信息来自应用在[module.json5](../../../quick-start/module-configuration-file.md)中配置的metadata。 |

### 类

| 名称 | 说明 |
| --- | --- |
| [ImmersiveMaterial](arkts-arkui-uimaterial-immersivematerial-c.md) | 沉浸式材质类，继承自[Material](arkts-arkui-uimaterial-materialtype-e.md)。 |
| [Material](arkts-arkui-uimaterial-material-c.md) | 系统材质对象基类。 |

<!--Del-->
### 类（系统接口）

| 名称 | 说明 |
| --- | --- |
| [Material](arkts-arkui-uimaterial-material-c-sys.md) | 系统材质对象基类。 |
<!--DelEnd-->

### 接口

| 名称 | 说明 |
| --- | --- |
| [ImmersiveOptions](arkts-arkui-uimaterial-immersiveoptions-i.md) | 沉浸式材质参数。 |
| [LightEffectOptions](arkts-arkui-uimaterial-lighteffectoptions-i.md) | 沉浸式材质的光感交互反馈配置。用于自定义反馈光感的颜色。 |
| [MaterialInfo](arkts-arkui-uimaterial-materialinfo-i.md) | 材质配置信息，包含材质使能状态和材质类型。 |

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [MaterialOptions](arkts-arkui-uimaterial-materialoptions-i-sys.md) | 系统材质选项。 |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [ImmersiveStyle](arkts-arkui-uimaterial-immersivestyle-e.md) | 沉浸式材质样式枚举。不同的材质样式对应不同的材质参数，主要包括材质的模糊程度、高光效果等。 |
| [MaterialState](arkts-arkui-uimaterial-materialstate-e.md) | 材质使能状态枚举，表示应用级沉浸式系统材质配置的状态。 |
| [MaterialType](arkts-arkui-uimaterial-materialtype-e.md) | 系统材质类型枚举。 |

<!--Del-->
### 枚举（系统接口）

| 名称 | 说明 |
| --- | --- |
| [MaterialType](arkts-arkui-uimaterial-materialtype-e-sys.md) | 系统材质类型枚举。 |
<!--DelEnd-->

## 示例

本示例介绍如何将半透明材质的Material对象通过[systemMaterial](../arkui-ts/ts-universal-attributes-image-effect-sys.md#systemmaterial23)属性设置给组件。

```TypeScript
import { uiMaterial } from '@kit.ArkUI';

@Entry
@Component
struct SystemMaterialPage {
  build() {
    Column() {
      Stack() {
        Image($r('app.media.bg1')) // $r('app.media.bg1')需要替换为开发者所需的图像资源文件
          .width('100%')
          .height('100%')

        Column()
          .width(100)
          .height(50)
          .position({ x: 50, y: 350 })
          .systemMaterial(new uiMaterial.Material({ type: uiMaterial.MaterialType.SEMI_TRANSPARENT })) // 使用半透明的系统材质效果
      }
      .height('90%')
      .width('90%')
    }
    .height('100%')
    .width('100%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
```

从API版本26.0.0开始，新增uiMaterial.convertToECMaterial、uiMaterial.convertToECSubMaterial接口。

```TypeScript
import { uiMaterial } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State myMaterialBase: uiMaterial.ImmersiveMaterial | undefined = new uiMaterial.ImmersiveMaterial({
    style: uiMaterial.ImmersiveStyle.ULTRA_THIN,
  });
  @State myMaterialEC: uiMaterial.ImmersiveMaterial | undefined = new uiMaterial.ImmersiveMaterial({
    style: uiMaterial.ImmersiveStyle.ULTRA_THIN_EC,
  });
  @State myMaterialECSub: uiMaterial.ImmersiveMaterial | undefined = new uiMaterial.ImmersiveMaterial({
    style: uiMaterial.ImmersiveStyle.ULTRA_THIN_EC_SUB,
  });

  build() {
    Stack() {
      // 请将$r('app.media.startIcon')替换为实际资源文件
      Image($r('app.media.startIcon'))
      Row() {
        // 推荐使用不同style为EffectComponent及其子组件设置材质
        EffectComponent() {
          Row() {
            Column()
              .width(100)
              .height(100)
              .systemMaterial(this.myMaterialECSub)
              .margin(5)
          }
        }
        .systemMaterial(this.myMaterialEC)

        EffectComponent() {
          Row() {
            Column()
              .width(100)
              .height(100)
              .systemMaterial(uiMaterial.convertToECSubMaterial(this.myMaterialBase))
              .margin(5)

            Column()
              .width(100)
              .height(100)
              .systemMaterial(uiMaterial.convertToECSubMaterial(this.myMaterialBase))
              .margin(5)
          }
        }
        .systemMaterial(uiMaterial.convertToECMaterial(this.myMaterialBase))
      }.height('100%').width('100%').justifyContent(FlexAlign.Center)
    }
  }
}
```
