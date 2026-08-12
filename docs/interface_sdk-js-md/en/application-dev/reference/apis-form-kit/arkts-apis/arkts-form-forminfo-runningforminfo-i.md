# RunningFormInfo

The class of a running form information.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-formInfo-interface RunningFormInfo--><!--Device-formInfo-interface RunningFormInfo-End-->

**System capability:** SystemCapability.Ability.Form

## Modules to Import

```TypeScript
import { formInfo } from '@kit.FormKit';
```

## abilityName

```TypeScript
readonly abilityName: string
```

Obtains the class name of the ability to which this form belongs.

**Type:** string

**Default:** -

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-RunningFormInfo-readonly abilityName: string--><!--Device-RunningFormInfo-readonly abilityName: string-End-->

**System capability:** SystemCapability.Ability.Form

## bundleName

```TypeScript
readonly bundleName: string
```

Obtains the bundle name of the application to which this form belongs.

**Type:** string

**Default:** -

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-RunningFormInfo-readonly bundleName: string--><!--Device-RunningFormInfo-readonly bundleName: string-End-->

**System capability:** SystemCapability.Ability.Form

## dimension

```TypeScript
readonly dimension: int
```

Obtains the grid style of this form.The value must be a positive integer, refer to [FormDimension](arkts-form-forminfo-formdimension-e.md#FormDimension).

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Default:** -

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-RunningFormInfo-readonly dimension: int--><!--Device-RunningFormInfo-readonly dimension: int-End-->

**System capability:** SystemCapability.Ability.Form

## extraData

```TypeScript
readonly extraData?: Record<string, Object>
```

Obtains the extra data of the this form.

**Type:** Record&lt;string, Object&gt;

**Default:** -

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-RunningFormInfo-readonly extraData?: Record<string, Object>--><!--Device-RunningFormInfo-readonly extraData?: Record<string, Object>-End-->

**System capability:** SystemCapability.Ability.Form

## formDescription

```TypeScript
readonly formDescription: string
```

Obtains the description of this form.

**Type:** string

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-RunningFormInfo-readonly formDescription: string--><!--Device-RunningFormInfo-readonly formDescription: string-End-->

**System capability:** SystemCapability.Ability.Form

## formId

```TypeScript
readonly formId: string
```

Obtains the id of the this form.

**Type:** string

**Default:** -

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-RunningFormInfo-readonly formId: string--><!--Device-RunningFormInfo-readonly formId: string-End-->

**System capability:** SystemCapability.Ability.Form

## formLocation

```TypeScript
readonly formLocation: FormLocation
```

The location of this form.

**Type:** [FormLocation](arkts-form-forminfo-formlocation-e.md)

**Default:** -

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-RunningFormInfo-readonly formLocation: FormLocation--><!--Device-RunningFormInfo-readonly formLocation: FormLocation-End-->

**System capability:** SystemCapability.Ability.Form

## formName

```TypeScript
readonly formName: string
```

Obtains the name of this form.

**Type:** string

**Default:** -

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-RunningFormInfo-readonly formName: string--><!--Device-RunningFormInfo-readonly formName: string-End-->

**System capability:** SystemCapability.Ability.Form

## formUsageState

```TypeScript
readonly formUsageState: FormUsageState
```

Obtains the stage of form use.

**Type:** [FormUsageState](arkts-form-forminfo-formusagestate-e-sys.md)

**Default:** FormUsageState.USED

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-RunningFormInfo-readonly formUsageState: FormUsageState--><!--Device-RunningFormInfo-readonly formUsageState: FormUsageState-End-->

**System capability:** SystemCapability.Ability.Form

## hostBundleName

```TypeScript
readonly hostBundleName: string
```

Obtains the bundle name of the form host application.

**Type:** string

**Default:** -

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-RunningFormInfo-readonly hostBundleName: string--><!--Device-RunningFormInfo-readonly hostBundleName: string-End-->

**System capability:** SystemCapability.Ability.Form

## moduleName

```TypeScript
readonly moduleName: string
```

Obtains the name of the application module to which this form belongs.

**Type:** string

**Default:** -

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-RunningFormInfo-readonly moduleName: string--><!--Device-RunningFormInfo-readonly moduleName: string-End-->

**System capability:** SystemCapability.Ability.Form

## visibilityType

```TypeScript
readonly visibilityType: VisibilityType
```

Obtains the visibility of this form.

**Type:** [VisibilityType](arkts-form-forminfo-visibilitytype-e.md)

**Default:** -

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-RunningFormInfo-readonly visibilityType: VisibilityType--><!--Device-RunningFormInfo-readonly visibilityType: VisibilityType-End-->

**System capability:** SystemCapability.Ability.Form

