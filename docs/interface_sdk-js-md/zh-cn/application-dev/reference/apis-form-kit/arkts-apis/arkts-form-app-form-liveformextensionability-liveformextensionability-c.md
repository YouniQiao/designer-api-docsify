# LiveFormExtensionAbility

Interactive widget extension class. It provides APIs for the widget provider to receive notifications about widget creation and destruction.

**继承/实现关系：** LiveFormExtensionAbility extends ExtensionAbility

**起始版本：** 20

**系统能力：** SystemCapability.Ability.Form

## 导入模块

```TypeScript
import { LiveFormExtensionAbility, LiveFormInfo } from 'kits/@kit.FormKit';
```

## onLiveFormCreate

```TypeScript
onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession): void
```

Called after the UI content of **LiveFormExtensionAbility** is created.

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| liveFormInfo | [LiveFormInfo](arkts-form-app-form-liveformextensionability-liveforminfo-i.md) | 是 |
| session | [UIExtensionContentSession](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiextensioncontentsession-uiextensioncontentsession-c.md) | 是 |

## onLiveFormDestroy

```TypeScript
onLiveFormDestroy(liveFormInfo: LiveFormInfo): void
```

Called to clear resources when this **LiveFormExtensionAbility** is destroyed.

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.Form

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| liveFormInfo | [LiveFormInfo](arkts-form-app-form-liveformextensionability-liveforminfo-i.md) | 是 |

## context

```TypeScript
context: LiveFormExtensionContext
```

Context of the **LiveFormExtensionAbility**. This context is inherited from [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md).

**类型：** [LiveFormExtensionContext](arkts-form-liveformextensioncontext-c.md)

**起始版本：** 20

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Ability.Form
