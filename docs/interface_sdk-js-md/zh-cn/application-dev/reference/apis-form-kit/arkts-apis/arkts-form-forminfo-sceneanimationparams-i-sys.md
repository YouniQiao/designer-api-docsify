# SceneAnimationParams（系统接口）

The scene animation form params.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-formInfo-interface SceneAnimationParams--><!--Device-formInfo-interface SceneAnimationParams-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { formInfo } from 'kits/@kit.FormKit';
```

## abilityName

```TypeScript
abilityName: string
```

Ability name of the scene animation form.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-SceneAnimationParams-abilityName: string--><!--Device-SceneAnimationParams-abilityName: string-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## disabledDesktopBehaviors

```TypeScript
disabledDesktopBehaviors?: string
```

Indicates disabled desktop behaviors, only takes effect for system app.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-SceneAnimationParams-disabledDesktopBehaviors?: string--><!--Device-SceneAnimationParams-disabledDesktopBehaviors?: string-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

## triggerTypes

```TypeScript
triggerTypes?: Array<SceneAnimationTriggerType>
```

The trigger types of the scene animation.

**类型：** Array&lt;SceneAnimationTriggerType&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SceneAnimationParams-triggerTypes?: Array<SceneAnimationTriggerType>--><!--Device-SceneAnimationParams-triggerTypes?: Array<SceneAnimationTriggerType>-End-->

**系统能力：** SystemCapability.Ability.Form

**系统接口：** 此接口为系统接口。

