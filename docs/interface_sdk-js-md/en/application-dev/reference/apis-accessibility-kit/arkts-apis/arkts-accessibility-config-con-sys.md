# Constants (System API)

## audioBalance

```TypeScript
const audioBalance: Config<double>
```

表示左右声道音量平衡的配置。取值范围为-1.0~1.0。默认值为0.0。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-config-const audioBalance: Config<double>--><!--Device-config-const audioBalance: Config<double>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## audioMono

```TypeScript
const audioMono: Config<boolean>
```

表示单声道音频的配置。true表示已启用单声道音频，false表示未启用单声道音频，默认值为false。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-config-const audioMono: Config<boolean>--><!--Device-config-const audioMono: Config<boolean>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## clickResponseTime

```TypeScript
const clickResponseTime: Config<ClickResponseTime>
```

表示点击持续时间功能配置。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-config-const clickResponseTime: Config<ClickResponseTime>--><!--Device-config-const clickResponseTime: Config<ClickResponseTime>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## daltonizationState

```TypeScript
const daltonizationState: Config<boolean>
```

表示颜色滤镜功能启动状态。配合daltonizationColorFilter使用。true表示已启用颜色滤镜功能，false表示未启用颜色滤镜功能，默认值为false。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-config-const daltonizationState: Config<boolean>--><!--Device-config-const daltonizationState: Config<boolean>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## ignoreRepeatClick

```TypeScript
const ignoreRepeatClick: Config<boolean>
```

表示忽略重复点击功能启用状态。配合repeatClickInterval使用。true表示已启用忽略重复点击功能，false表示未启用忽略重复点击功能，默认值为false。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-config-const ignoreRepeatClick: Config<boolean>--><!--Device-config-const ignoreRepeatClick: Config<boolean>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## repeatClickInterval

```TypeScript
const repeatClickInterval: Config<RepeatClickInterval>
```

表示忽略重复点击功能配置。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-config-const repeatClickInterval: Config<RepeatClickInterval>--><!--Device-config-const repeatClickInterval: Config<RepeatClickInterval>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## screenMagnification

```TypeScript
const screenMagnification: Config<boolean>
```

Indicates the configuration of screen magnification.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-config-const screenMagnification: Config<boolean>--><!--Device-config-const screenMagnification: Config<boolean>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

## shortkeyMultiTargets

```TypeScript
const shortkeyMultiTargets: Config<Array<string>>
```

表示辅助扩展快捷键的列表配置。取值为辅助应用的名称，格式为：['bundleName/abilityName']。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-config-const shortkeyMultiTargets: Config<Array<string>>--><!--Device-config-const shortkeyMultiTargets: Config<Array<string>>-End-->

**System capability:** SystemCapability.BarrierFree.Accessibility.Core

**System API:** This is a system API.

