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

## enableBlurBackground

```TypeScript
readonly enableBlurBackground?: boolean
```

Indicates whether the form uses a blur background provided by the form host.

**类型：** boolean

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-FormInfo-readonly enableBlurBackground?: boolean--><!--Device-FormInfo-readonly enableBlurBackground?: boolean-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## funInteractionParams

```TypeScript
readonly funInteractionParams?: FunInteractionParams
```

Indicates the fun interaction form params

**类型：** [FunInteractionParams](arkts-form-forminfo-funinteractionparams-i-sys.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-FormInfo-readonly funInteractionParams?: FunInteractionParams--><!--Device-FormInfo-readonly funInteractionParams?: FunInteractionParams-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## groupId

```TypeScript
readonly groupId?: string
```

Obtains the group id of the form.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-FormInfo-readonly groupId?: string--><!--Device-FormInfo-readonly groupId?: string-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## isFontScaleFollowSystem

```TypeScript
isFontScaleFollowSystem?: boolean
```

Obtains whether the font scaling factor follows system settings.&lt;br&gt;Default value:The default value is true.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FormInfo-isFontScaleFollowSystem?: boolean--><!--Device-FormInfo-isFontScaleFollowSystem?: boolean-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## isPrivacySensitive

```TypeScript
readonly isPrivacySensitive?: boolean
```

Obtains whether the form is privacy sensitive.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FormInfo-readonly isPrivacySensitive?: boolean--><!--Device-FormInfo-readonly isPrivacySensitive?: boolean-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## isStandbyAdapted

```TypeScript
readonly isStandbyAdapted?: boolean
```

Obtains whether the form is adapted for standby.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FormInfo-readonly isStandbyAdapted?: boolean--><!--Device-FormInfo-readonly isStandbyAdapted?: boolean-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## isStandbySupported

```TypeScript
readonly isStandbySupported?: boolean
```

Obtains whether the form supports standby.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-FormInfo-readonly isStandbySupported?: boolean--><!--Device-FormInfo-readonly isStandbySupported?: boolean-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## isTemplateForm

```TypeScript
readonly isTemplateForm?: boolean
```

Obtains whether the form is template form.

**类型：** boolean

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-FormInfo-readonly isTemplateForm?: boolean--><!--Device-FormInfo-readonly isTemplateForm?: boolean-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## previewImages

```TypeScript
readonly previewImages?: Array<int>
```

Indicates the form previewImage IDs map corresponds to the \"supportDimensions\". The maximum length is +∞, positive integer.

**类型：** ArkTS-Dyn: Array&lt;number&gt;  <br>ArkTS-Sta：Array&lt;int&gt;

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本18开始，该接口支持在原子化服务API中使用。

<!--Device-FormInfo-readonly previewImages?: Array<int>--><!--Device-FormInfo-readonly previewImages?: Array<int>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## renderingMode

```TypeScript
readonly renderingMode?: RenderingMode
```

Obtains the rendering mode of the form.

**类型：** [RenderingMode](arkts-form-forminfo-renderingmode-e-sys.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-FormInfo-readonly renderingMode?: RenderingMode--><!--Device-FormInfo-readonly renderingMode?: RenderingMode-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## resizable

```TypeScript
readonly resizable?: boolean
```

Obtains the resizable of the form.

**类型：** boolean

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-FormInfo-readonly resizable?: boolean--><!--Device-FormInfo-readonly resizable?: boolean-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## sceneAnimationParams

```TypeScript
readonly sceneAnimationParams?: SceneAnimationParams
```

Indicates the scene animation form params

**类型：** [SceneAnimationParams](arkts-form-forminfo-sceneanimationparams-i-sys.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-FormInfo-readonly sceneAnimationParams?: SceneAnimationParams--><!--Device-FormInfo-readonly sceneAnimationParams?: SceneAnimationParams-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

