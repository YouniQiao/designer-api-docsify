# FormInfo

Provides information about a form.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-formInfo-interface FormInfo--><!--Device-formInfo-interface FormInfo-End-->

**系统能力：** SystemCapability.Ability.Form

## 导入模块

```TypeScript
import { formInfo } from 'kits/@kit.FormKit';
```

## abilityName

```TypeScript
abilityName: string
```

Obtains the class name of the ability to which this form belongs.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-abilityName: string--><!--Device-FormInfo-abilityName: string-End-->

**系统能力：** SystemCapability.Ability.Form

## bundleName

```TypeScript
bundleName: string
```

Obtains the bundle name of the application to which this form belongs.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-bundleName: string--><!--Device-FormInfo-bundleName: string-End-->

**系统能力：** SystemCapability.Ability.Form

## colorMode

```TypeScript
colorMode: ColorMode
```

Obtains the color mode of this form.

**类型：** [ColorMode](../../apis-arkui/arkts-apis/arkts-arkui-storageproperty-colormode-e.md)

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

**废弃版本：** 20

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-colorMode: ColorMode--><!--Device-FormInfo-colorMode: ColorMode-End-->

**系统能力：** SystemCapability.Ability.Form

## customizeData

```TypeScript
customizeData: Record<string, string>
```

Obtains the custom data defined in this form.

**类型：** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, string&gt;

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-customizeData: Record<string, string>--><!--Device-FormInfo-customizeData: Record<string, string>-End-->

**系统能力：** SystemCapability.Ability.Form

## defaultDimension

```TypeScript
defaultDimension: int
```

Obtains the default grid style of this form.The value must be a positive integer, refer to {@link formInfo.FormDimension}.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-defaultDimension: int--><!--Device-FormInfo-defaultDimension: int-End-->

**系统能力：** SystemCapability.Ability.Form

## description

```TypeScript
description: string
```

Obtains the description of this form.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-description: string--><!--Device-FormInfo-description: string-End-->

**系统能力：** SystemCapability.Ability.Form

## descriptionId

```TypeScript
descriptionId: int
```

Obtains the description id of this form.The value must be a positive integer.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-descriptionId: int--><!--Device-FormInfo-descriptionId: int-End-->

**系统能力：** SystemCapability.Ability.Form

## displayName

```TypeScript
displayName: string
```

Obtains the display name of this form.

**类型：** string

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-displayName: string--><!--Device-FormInfo-displayName: string-End-->

**系统能力：** SystemCapability.Ability.Form

## displayNameId

```TypeScript
displayNameId: int
```

Obtains the displayName resource id of this form.The value must be a positive integer.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-displayNameId: int--><!--Device-FormInfo-displayNameId: int-End-->

**系统能力：** SystemCapability.Ability.Form

## formConfigAbility

```TypeScript
formConfigAbility: string
```

Obtains the form config ability about this form.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-formConfigAbility: string--><!--Device-FormInfo-formConfigAbility: string-End-->

**系统能力：** SystemCapability.Ability.Form

## formVisibleNotify

```TypeScript
formVisibleNotify: boolean
```

Obtains whether notify visible of this form.

**类型：** boolean

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-formVisibleNotify: boolean--><!--Device-FormInfo-formVisibleNotify: boolean-End-->

**系统能力：** SystemCapability.Ability.Form

## isDefault

```TypeScript
isDefault: boolean
```

Checks whether this form is a default form.

**类型：** boolean

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-isDefault: boolean--><!--Device-FormInfo-isDefault: boolean-End-->

**系统能力：** SystemCapability.Ability.Form

## isDynamic

```TypeScript
isDynamic: boolean
```

Obtains whether this form is a dynamic form.

**类型：** boolean

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-isDynamic: boolean--><!--Device-FormInfo-isDynamic: boolean-End-->

**系统能力：** SystemCapability.Ability.Form

## jsComponentName

```TypeScript
jsComponentName: string
```

Obtains the JS component name of this JS form.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-jsComponentName: string--><!--Device-FormInfo-jsComponentName: string-End-->

**系统能力：** SystemCapability.Ability.Form

## moduleName

```TypeScript
moduleName: string
```

Obtains the name of the application module to which this form belongs.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-moduleName: string--><!--Device-FormInfo-moduleName: string-End-->

**系统能力：** SystemCapability.Ability.Form

## name

```TypeScript
name: string
```

Obtains the name of this form.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-name: string--><!--Device-FormInfo-name: string-End-->

**系统能力：** SystemCapability.Ability.Form

## scheduledUpdateTime

```TypeScript
scheduledUpdateTime: string
```

Obtains the scheduledUpdateTime.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-scheduledUpdateTime: string--><!--Device-FormInfo-scheduledUpdateTime: string-End-->

**系统能力：** SystemCapability.Ability.Form

## supportDimensions

```TypeScript
supportDimensions: Array<int>
```

Obtains the grid styles supported by this form.The minimum length is 1, refer to {@link formInfo.FormDimension}.

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-supportDimensions: Array<int>--><!--Device-FormInfo-supportDimensions: Array<int>-End-->

**系统能力：** SystemCapability.Ability.Form

## supportedShapes

```TypeScript
supportedShapes: Array<int>
```

Obtains the shape supported by this form.The minimum length is 1, refer to {@link formInfo.FormShape}.

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-supportedShapes: Array<int>--><!--Device-FormInfo-supportedShapes: Array<int>-End-->

**系统能力：** SystemCapability.Ability.Form

## transparencyEnabled

```TypeScript
transparencyEnabled: boolean
```

Indicates whether the form can be set as a transparent background

**类型：** boolean

**默认值：** false

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-transparencyEnabled: boolean--><!--Device-FormInfo-transparencyEnabled: boolean-End-->

**系统能力：** SystemCapability.Ability.Form

## type

```TypeScript
type: FormType
```

Obtains the type of this form. Currently, JS forms are supported.

**类型：** [FormType](../../apis-arkdata/arkts-apis/arkts-arkdata-data-udmfcomponents-formtype-e.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-type: FormType--><!--Device-FormInfo-type: FormType-End-->

**系统能力：** SystemCapability.Ability.Form

## updateDuration

```TypeScript
updateDuration: int
```

Obtains the updateDuration.The value must be an integer within [0,336].

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-updateDuration: int--><!--Device-FormInfo-updateDuration: int-End-->

**系统能力：** SystemCapability.Ability.Form

## updateEnabled

```TypeScript
updateEnabled: boolean
```

Obtains the updateEnabled.

**类型：** boolean

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-updateEnabled: boolean--><!--Device-FormInfo-updateEnabled: boolean-End-->

**系统能力：** SystemCapability.Ability.Form

