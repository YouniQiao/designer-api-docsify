# FormInfoFilter

The optional options used as filters to ask getFormsInfo to return formInfos from only forms that match the options.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-formInfo-interface FormInfoFilter--><!--Device-formInfo-interface FormInfoFilter-End-->

**系统能力：** SystemCapability.Ability.Form

## 导入模块

```TypeScript
import { formInfo } from 'kits/@kit.FormKit';
```

## bundleName

```TypeScript
bundleName?: string
```

optional bundleName that used to ask getFormsInfo to return form infos with the same bundleName.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-FormInfoFilter-bundleName?: string--><!--Device-FormInfoFilter-bundleName?: string-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## supportedDimensions

```TypeScript
supportedDimensions?: Array<int>
```

optional supportedDimensions that used to ask getFormsInfo to return form infos with the same supportedDimensions.The minimum length is 1, refer to {@link formInfo.FormDimension}.

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-FormInfoFilter-supportedDimensions?: Array<int>--><!--Device-FormInfoFilter-supportedDimensions?: Array<int>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## supportedShapes

```TypeScript
supportedShapes?: Array<int>
```

optional supportedShapes that used to ask getFormsInfo to return form infos with the same supportedShapes.The minimum length is 1, Refer to {@link formInfo.FormShape}.

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-FormInfoFilter-supportedShapes?: Array<int>--><!--Device-FormInfoFilter-supportedShapes?: Array<int>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

