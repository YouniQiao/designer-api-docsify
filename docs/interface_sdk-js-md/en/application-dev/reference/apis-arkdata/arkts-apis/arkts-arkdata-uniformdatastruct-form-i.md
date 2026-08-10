# Form

系统定义的卡片类型数据，用于跨应用共享卡片信息。典型使用场景包括：卡片拖拽分享、卡片内容跨应用传输、桌面小组件数据共享等。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-uniformDataStruct-interface Form--><!--Device-uniformDataStruct-interface Form-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## Modules to Import

```TypeScript
import { uniformDataStruct } from 'kits/@kit.ArkData';
```

## abilityName

```TypeScript
abilityName: string
```

卡片对应的ability名。建议遵循Ability组件命名规范：取值为长度不超过127字节的字符串，以字母开头，可包含字母、数字、下划线（_）或点号（.）；确保该名称在整个应用中唯一。推荐使用"包名.Ability名"格式（如"com.example.myapplication.MainAbility"）。

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Form-abilityName: string--><!--Device-Form-abilityName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## bundleName

```TypeScript
bundleName: string
```

卡片所属的bundle名，格式需符合应用包名规范。

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Form-bundleName: string--><!--Device-Form-bundleName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## details

```TypeScript
details?: Record<string, int | long | double | string | Uint8Array>
```

字典类型对象，key为string类型，value可包含number（数值类型）、string（字符串类型）或Uint8Array（二进制字节数组）类型数据。非必填字段，默认值为空字典对象。

**Type:** ArkTS-Dyn: [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, number \| number \| number \| string \| Uint8Array&gt;  <br>ArkTS-Sta：[Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, int \| long \| double \| string \| Uint8Array&gt;

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Form-details?: Record<string, int | long | double | string | Uint8Array>--><!--Device-Form-details?: Record<string, int | long | double | string | Uint8Array>-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## formId

```TypeScript
formId: int
```

卡片id。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Form-formId: int--><!--Device-Form-formId: int-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## formName

```TypeScript
formName: string
```

卡片名。

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Form-formName: string--><!--Device-Form-formName: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## module

```TypeScript
module: string
```

卡片所属的module名。

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Form-module: string--><!--Device-Form-module: string-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

## uniformDataType

```TypeScript
readonly uniformDataType: 'openharmony.form'
```

统一数据类型标识为卡片类型数据，固定为“openharmony.form”，数据类型描述信息见  
[UniformDataType](arkts-arkdata-uniformtypedescriptor-uniformdatatype-e.md)。

**Type:** 'openharmony.form'

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Form-readonly uniformDataType: 'openharmony.form'--><!--Device-Form-readonly uniformDataType: 'openharmony.form'-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

