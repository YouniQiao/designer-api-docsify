# ProxyData

Defines the form proxy data.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-formBindingData-interface ProxyData--><!--Device-formBindingData-interface ProxyData-End-->

**系统能力：** SystemCapability.Ability.Form

## 导入模块

```TypeScript
import { formBindingData } from 'kits/@kit.FormKit';
```

## key

```TypeScript
key: string
```

Key for proxy. The value depends on the data publisher.

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ProxyData-key: string--><!--Device-ProxyData-key: string-End-->

**系统能力：** SystemCapability.Ability.Form

## subscriberId

```TypeScript
subscriberId?: string
```

SubscriberId. The value depends on the data publisher. The default value is current formId.

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ProxyData-subscriberId?: string--><!--Device-ProxyData-subscriberId?: string-End-->

**系统能力：** SystemCapability.Ability.Form

