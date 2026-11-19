# ControlComponentClickResult

```TypeScript
interface ControlComponentClickResult
```

模拟点击操作结果。

**起始版本：** 26.1.0

<!--Device-abilityToolAccessCtrl-interface ControlComponentClickResult--><!--Device-abilityToolAccessCtrl-interface ControlComponentClickResult-End-->

**系统能力：** SystemCapability.Security.Asset

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## appInfo

```TypeScript
appInfo: AppInfo
```

模拟点击的目标应用信息。

**类型：** [AppInfo](arkts-ability-abilitytoolaccessctrl-appinfo-i.md)

**起始版本：** 26.1.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-ControlComponentClickResult-appInfo: AppInfo--><!--Device-ControlComponentClickResult-appInfo: AppInfo-End-->

**系统能力：** SystemCapability.Security.Asset

## code

```TypeScript
code: number
```

模拟点击操作结果码。0表示成功，其他表示失败。

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-ControlComponentClickResult-code: number--><!--Device-ControlComponentClickResult-code: number-End-->

**系统能力：** SystemCapability.Security.Asset

## componentId

```TypeScript
componentId: string
```

被模拟点击的组件ID。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-ControlComponentClickResult-componentId: string--><!--Device-ControlComponentClickResult-componentId: string-End-->

**系统能力：** SystemCapability.Security.Asset

## isAllowed

```TypeScript
isAllowed: boolean
```

模拟点击是否被允许。true表示允许， false表示被拒绝。

**类型：** boolean

**起始版本：** 26.1.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-ControlComponentClickResult-isAllowed: boolean--><!--Device-ControlComponentClickResult-isAllowed: boolean-End-->

**系统能力：** SystemCapability.Security.Asset

## reason

```TypeScript
reason: string
```

模拟点击操作结果的原因描述。

**类型：** string

**起始版本：** 26.1.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-ControlComponentClickResult-reason: string--><!--Device-ControlComponentClickResult-reason: string-End-->

**系统能力：** SystemCapability.Security.Asset
