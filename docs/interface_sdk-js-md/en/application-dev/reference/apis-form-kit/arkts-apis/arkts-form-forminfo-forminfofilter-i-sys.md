# FormInfoFilter

The optional options used as filters to ask getFormsInfo to return formInfos from only forms that match the options.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-formInfo-interface FormInfoFilter--><!--Device-formInfo-interface FormInfoFilter-End-->

**System capability:** SystemCapability.Ability.Form

## Modules to Import

```TypeScript
import { formInfo } from 'kits/@kit.FormKit';
```

## bundleName

```TypeScript
bundleName?: string
```

optional bundleName that used to ask getFormsInfo to return form infos with the same bundleName.

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-FormInfoFilter-bundleName?: string--><!--Device-FormInfoFilter-bundleName?: string-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

## supportedDimensions

```TypeScript
supportedDimensions?: Array<int>
```

optional supportedDimensions that used to ask getFormsInfo to return form infos with the same supportedDimensions.The minimum length is 1, refer to {@link formInfo.FormDimension}.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-FormInfoFilter-supportedDimensions?: Array<int>--><!--Device-FormInfoFilter-supportedDimensions?: Array<int>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

## supportedShapes

```TypeScript
supportedShapes?: Array<int>
```

optional supportedShapes that used to ask getFormsInfo to return form infos with the same supportedShapes.The minimum length is 1, Refer to {@link formInfo.FormShape}.

**Type:** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-FormInfoFilter-supportedShapes?: Array<int>--><!--Device-FormInfoFilter-supportedShapes?: Array<int>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

