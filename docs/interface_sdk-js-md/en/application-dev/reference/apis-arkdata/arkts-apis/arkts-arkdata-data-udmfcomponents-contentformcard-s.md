# ContentFormCard

Defines a content form card.

**Since:** 20

<!--Device-unnamed-declare struct ContentFormCard--><!--Device-unnamed-declare struct ContentFormCard-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { ContentFormCard, FormType } from '@kit.ArkData';
```

## contentFormData

```TypeScript
contentFormData: uniformDataStruct.ContentForm
```

Data of the form card.

**Type:** uniformDataStruct.ContentForm

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentFormCard-contentFormData: uniformDataStruct.ContentForm--><!--Device-ContentFormCard-contentFormData: uniformDataStruct.ContentForm-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## formHeight

```TypeScript
@Prop
  formHeight?: double
```

Height of the content form card. The unit of measurement is vp.

**Type:** double

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentFormCard-@Prop  formHeight?: double--><!--Device-ContentFormCard-@Prop  formHeight?: double-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## formType

```TypeScript
@Prop
  formType: FormType
```

Type of the form card.

**Type:** [FormType](../../apis-default/arkts-apis/arkts-data-udmfcomponents-formtype-e.md)

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentFormCard-@Prop  formType: FormType--><!--Device-ContentFormCard-@Prop  formType: FormType-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## formWidth

```TypeScript
@Prop
  formWidth?: double
```

Width of the content form card. The unit of measurement is vp.

**Type:** double

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentFormCard-@Prop  formWidth?: double--><!--Device-ContentFormCard-@Prop  formWidth?: double-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## handleOnClick

```TypeScript
handleOnClick?: Function
```

Callback to be invoked when the form card is tapped.

**Type:** Function

**Since:** 20

**Model restriction:** This API can be used only in the stage model.

<!--Device-ContentFormCard-handleOnClick?: Function--><!--Device-ContentFormCard-handleOnClick?: Function-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

