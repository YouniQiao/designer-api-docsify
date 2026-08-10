# ContentFormCard

内容卡片控件，用于在应用内展示标题、描述、内容图片、应用信息等。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Component

<!--Device-unnamed-declare struct ContentFormCard--><!--Device-unnamed-declare struct ContentFormCard-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { ContentFormCard, FormType } from 'kits/@kit.ArkData';
```

## build

```TypeScript
build(): void
```

构建组件的方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentFormCard-build(): void--><!--Device-ContentFormCard-build(): void-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## contentFormData

```TypeScript
contentFormData: uniformDataStruct.ContentForm
```

内容卡片数据。

**Type:** uniformDataStruct.ContentForm

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentFormCard-contentFormData: uniformDataStruct.ContentForm--><!--Device-ContentFormCard-contentFormData: uniformDataStruct.ContentForm-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## formHeight

```TypeScript
formHeight?: double
```

卡片高度，当contentFormData中的title为空字符串时，卡片高度为传入的值，否则其范围在设置的内容卡片类型默认宽度的0.8 ~ 1.2倍之间，当formType为TYPE_SMALL时，其范围在设置的内容卡片类型默认宽度的0.4 ~ 1.2倍之间。单位为vp。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentFormCard-formHeight?: double--><!--Device-ContentFormCard-formHeight?: double-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## formType

```TypeScript
formType: FormType
```

内容卡片类型，影响内容卡片的大小。

**Type:** [FormType](arkts-arkdata-data-udmfcomponents-formtype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentFormCard-formType: FormType--><!--Device-ContentFormCard-formType: FormType-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## formWidth

```TypeScript
formWidth?: double
```

卡片宽度，其范围在设置的内容卡片类型默认宽度的0.8 ~ 1.2倍之间，当formType为TYPE_SMALL时，其范围在设置的内容卡片类型默认宽度的0.4 ~ 1.2倍之间。单位为vp。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentFormCard-formWidth?: double--><!--Device-ContentFormCard-formWidth?: double-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## handleOnClick

```TypeScript
handleOnClick?: Function
```

点击事件回调函数。

**Type:** Function

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentFormCard-handleOnClick?: Function--><!--Device-ContentFormCard-handleOnClick?: Function-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

