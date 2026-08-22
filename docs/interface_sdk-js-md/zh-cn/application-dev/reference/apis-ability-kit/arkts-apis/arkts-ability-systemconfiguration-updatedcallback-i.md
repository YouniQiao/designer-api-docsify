# UpdatedCallback

UpdatedCallback是监听系统环境变化的回调函数，开发者可通过 [ApplicationContext.onSystemConfigurationUpdated](arkts-ability-applicationcontext-c.md#onsystemconfigurationupdated) 方法注册自定义的UpdatedCallback，来监听系统环境变化。

**起始版本：** 24

<!--Device-systemConfiguration-interface UpdatedCallback--><!--Device-systemConfiguration-interface UpdatedCallback-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.AbilityCore

## 导入模块

```TypeScript
import { systemConfiguration } from '@kit.AbilityKit';
```

## onColorModeUpdated

```TypeScript
onColorModeUpdated?: OnColorModeUpdatedFn
```

在注册系统环境变化的监听后，当系统深浅色模式变化时会触发回调。

**类型：** [OnColorModeUpdatedFn](arkts-ability-systemconfiguration-oncolormodeupdatedfn-t.md)

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatedCallback-onColorModeUpdated?: OnColorModeUpdatedFn--><!--Device-UpdatedCallback-onColorModeUpdated?: OnColorModeUpdatedFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onFontIdUpdated

```TypeScript
onFontIdUpdated?: OnFontIdUpdatedFn
```

在注册系统环境变化的监听后，当系统字体ID变化时触发回调。

**类型：** [OnFontIdUpdatedFn](arkts-ability-systemconfiguration-onfontidupdatedfn-t.md)

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatedCallback-onFontIdUpdated?: OnFontIdUpdatedFn--><!--Device-UpdatedCallback-onFontIdUpdated?: OnFontIdUpdatedFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onFontSizeScaleUpdated

```TypeScript
onFontSizeScaleUpdated?: OnFontSizeScaleUpdatedFn
```

在注册系统环境变化的监听后，当系统字体大小缩放比例变化时触发回调。

**类型：** [OnFontSizeScaleUpdatedFn](arkts-ability-systemconfiguration-onfontsizescaleupdatedfn-t.md)

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatedCallback-onFontSizeScaleUpdated?: OnFontSizeScaleUpdatedFn--><!--Device-UpdatedCallback-onFontSizeScaleUpdated?: OnFontSizeScaleUpdatedFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onFontWeightScaleUpdated

```TypeScript
onFontWeightScaleUpdated?: OnFontWeightScaleUpdatedFn
```

在注册系统环境变化的监听后，当系统字体粗细缩放比例变化时触发回调。

**类型：** [OnFontWeightScaleUpdatedFn](arkts-ability-systemconfiguration-onfontweightscaleupdatedfn-t.md)

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatedCallback-onFontWeightScaleUpdated?: OnFontWeightScaleUpdatedFn--><!--Device-UpdatedCallback-onFontWeightScaleUpdated?: OnFontWeightScaleUpdatedFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onHasPointerDeviceUpdated

```TypeScript
onHasPointerDeviceUpdated?: OnHasPointerDeviceUpdatedFn
```

在注册系统环境变化的监听后，当指针设备连接或者断开时触发回调。

**类型：** [OnHasPointerDeviceUpdatedFn](arkts-ability-systemconfiguration-onhaspointerdeviceupdatedfn-t.md)

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatedCallback-onHasPointerDeviceUpdated?: OnHasPointerDeviceUpdatedFn--><!--Device-UpdatedCallback-onHasPointerDeviceUpdated?: OnHasPointerDeviceUpdatedFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onLanguageUpdated

```TypeScript
onLanguageUpdated?: OnLanguageUpdatedFn
```

在注册系统环境变化的监听后，当系统语言变化时触发回调。

**类型：** [OnLanguageUpdatedFn](arkts-ability-systemconfiguration-onlanguageupdatedfn-t.md)

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatedCallback-onLanguageUpdated?: OnLanguageUpdatedFn--><!--Device-UpdatedCallback-onLanguageUpdated?: OnLanguageUpdatedFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onLocaleUpdated

```TypeScript
onLocaleUpdated?: OnLocaleUpdatedFn
```

在注册系统环境变化的监听后，当系统区域设置变化时触发回调。

**类型：** [OnLocaleUpdatedFn](arkts-ability-systemconfiguration-onlocaleupdatedfn-t.md)

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatedCallback-onLocaleUpdated?: OnLocaleUpdatedFn--><!--Device-UpdatedCallback-onLocaleUpdated?: OnLocaleUpdatedFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onMCCUpdated

```TypeScript
onMCCUpdated?: OnMCCUpdatedFn
```

在注册系统环境变化的监听后，当移动设备国家代码变化时触发回调。

**类型：** [OnMCCUpdatedFn](arkts-ability-systemconfiguration-onmccupdatedfn-t.md)

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatedCallback-onMCCUpdated?: OnMCCUpdatedFn--><!--Device-UpdatedCallback-onMCCUpdated?: OnMCCUpdatedFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

## onMNCUpdated

```TypeScript
onMNCUpdated?: OnMNCUpdatedFn
```

在注册系统环境变化的监听后，当移动设备网络代码变化时触发回调。

**类型：** [OnMNCUpdatedFn](arkts-ability-systemconfiguration-onmncupdatedfn-t.md)

**起始版本：** 24

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-UpdatedCallback-onMNCUpdated?: OnMNCUpdatedFn--><!--Device-UpdatedCallback-onMNCUpdated?: OnMNCUpdatedFn-End-->

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**示例**

```TypeScript
import { UIAbility, systemConfiguration, ConfigurationConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onForeground() {
    let callback: systemConfiguration.UpdatedCallback = {
      onColorModeUpdated: (colorMode: ConfigurationConstant.ColorMode) => {
        console.info(`system configuration updated colormode:` + colorMode);
      },
      onFontSizeScaleUpdated: (fontSizeScale: number) => {
        console.info(`system configuration updated fontSizeScale:` + fontSizeScale);
      },
      onFontWeightScaleUpdated: (fontWeightScale: number) => {
        console.info(`system configuration updated fontWeightScale:` + fontWeightScale);
      },
      onLanguageUpdated: (language: string) => {
        console.info(`system configuration updated language:` + language);
      },
      onFontIdUpdated: (fontId: string) => {
        console.info(`system configuration updated fontId:` + fontId);
      },
      onMCCUpdated: (mcc: string) => {
        console.info(`system configuration updated mcc:` + mcc);
      },
      onMNCUpdated: (mnc: string) => {
        console.info(`system configuration updated mnc:` + mnc);
      },
      onHasPointerDeviceUpdated: (hasPointerDevice: boolean) => {
        console.info(`system configuration updated hasPointerDevice:` + hasPointerDevice);
      },
      onLocaleUpdated: (locale: string) => {
        console.info(`system configuration updated locale:` + locale);
      }
    }
    // 1.通过context属性获取applicationContext
    let applicationContext = this.context.getApplicationContext();
    try {
      // 2.通过applicationContext注册监听
      applicationContext.onSystemConfigurationUpdated(callback);
    } catch (paramError) {
      console.error(`error: ${(paramError as BusinessError).code}, ${(paramError as BusinessError).message}`);
    }
    console.info(`onSystemConfigurationUpdated finish`);
  }
}
```

