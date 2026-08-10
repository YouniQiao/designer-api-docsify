# RunningFormInfo

The class of a running form information.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-formInfo-interface RunningFormInfo--><!--Device-formInfo-interface RunningFormInfo-End-->

**系统能力：** SystemCapability.Ability.Form

## 导入模块

```TypeScript
import { formInfo } from 'kits/@kit.FormKit';
```

## abilityName

```TypeScript
readonly abilityName: string
```

Obtains the class name of the ability to which this form belongs.

**类型：** string

**默认值：** -

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-RunningFormInfo-readonly abilityName: string--><!--Device-RunningFormInfo-readonly abilityName: string-End-->

**系统能力：** SystemCapability.Ability.Form

## bundleName

```TypeScript
readonly bundleName: string
```

Obtains the bundle name of the application to which this form belongs.

**类型：** string

**默认值：** -

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-RunningFormInfo-readonly bundleName: string--><!--Device-RunningFormInfo-readonly bundleName: string-End-->

**系统能力：** SystemCapability.Ability.Form

## dimension

```TypeScript
readonly dimension: int
```

Obtains the grid style of this form.The value must be a positive integer, refer to {@link formInfo.FormDimension}.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**默认值：** -

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-RunningFormInfo-readonly dimension: int--><!--Device-RunningFormInfo-readonly dimension: int-End-->

**系统能力：** SystemCapability.Ability.Form

## extraData

```TypeScript
readonly extraData?: Record<string, Object>
```

Obtains the extra data of the this form.

**类型：** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**默认值：** -

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-RunningFormInfo-readonly extraData?: Record<string, Object>--><!--Device-RunningFormInfo-readonly extraData?: Record<string, Object>-End-->

**系统能力：** SystemCapability.Ability.Form

## formDescription

```TypeScript
readonly formDescription: string
```

Obtains the description of this form.

**类型：** string

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-RunningFormInfo-readonly formDescription: string--><!--Device-RunningFormInfo-readonly formDescription: string-End-->

**系统能力：** SystemCapability.Ability.Form

## formId

```TypeScript
readonly formId: string
```

Obtains the id of the this form.

**类型：** string

**默认值：** -

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-RunningFormInfo-readonly formId: string--><!--Device-RunningFormInfo-readonly formId: string-End-->

**系统能力：** SystemCapability.Ability.Form

## formLocation

```TypeScript
readonly formLocation: FormLocation
```

The location of this form.

**类型：** [FormLocation](arkts-form-forminfo-formlocation-e.md)

**默认值：** -

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-RunningFormInfo-readonly formLocation: FormLocation--><!--Device-RunningFormInfo-readonly formLocation: FormLocation-End-->

**系统能力：** SystemCapability.Ability.Form

## formName

```TypeScript
readonly formName: string
```

Obtains the name of this form.

**类型：** string

**默认值：** -

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-RunningFormInfo-readonly formName: string--><!--Device-RunningFormInfo-readonly formName: string-End-->

**系统能力：** SystemCapability.Ability.Form

## formUsageState

```TypeScript
readonly formUsageState: FormUsageState
```

Obtains the stage of form use.

**类型：** [FormUsageState](arkts-form-forminfo-formusagestate-e-sys.md)

**默认值：** FormUsageState.USED

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-RunningFormInfo-readonly formUsageState: FormUsageState--><!--Device-RunningFormInfo-readonly formUsageState: FormUsageState-End-->

**系统能力：** SystemCapability.Ability.Form

## hostBundleName

```TypeScript
readonly hostBundleName: string
```

Obtains the bundle name of the form host application.

**类型：** string

**默认值：** -

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-RunningFormInfo-readonly hostBundleName: string--><!--Device-RunningFormInfo-readonly hostBundleName: string-End-->

**系统能力：** SystemCapability.Ability.Form

## moduleName

```TypeScript
readonly moduleName: string
```

Obtains the name of the application module to which this form belongs.

**类型：** string

**默认值：** -

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-RunningFormInfo-readonly moduleName: string--><!--Device-RunningFormInfo-readonly moduleName: string-End-->

**系统能力：** SystemCapability.Ability.Form

## visibilityType

```TypeScript
readonly visibilityType: VisibilityType
```

Obtains the visibility of this form.

**类型：** [VisibilityType](arkts-form-forminfo-visibilitytype-e.md)

**默认值：** -

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-RunningFormInfo-readonly visibilityType: VisibilityType--><!--Device-RunningFormInfo-readonly visibilityType: VisibilityType-End-->

**系统能力：** SystemCapability.Ability.Form

