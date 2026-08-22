# SystemDefinedForm

Represents the service widget data defined by the system. It is a child class of [SystemDefinedRecord](arkts-arkdata-unifieddatachannel-systemdefinedrecord-c.md).

**Inheritance/Implementation:** SystemDefinedForm extends [SystemDefinedRecord](arkts-arkdata-unifieddatachannel-systemdefinedrecord-c.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-unifiedDataChannel-class SystemDefinedForm--><!--Device-unifiedDataChannel-class SystemDefinedForm-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { unifiedDataChannel } from '@kit.ArkData';
```

**Examples**

```TypeScript
let form = new unifiedDataChannel.SystemDefinedForm();
form.formId = 123456;
form.formName = 'MyFormName';
form.bundleName = 'MyBundleName';
form.abilityName = 'MyAbilityName';
form.module = 'MyModule';
let u8Array = new Uint8Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
form.details = {
  formKey1: 123,
  formKey2: 'formValue',
  formKey3: u8Array
};
let unifiedData = new unifiedDataChannel.UnifiedData(form);
```

