# FormLinkOptions

Defines the FormLink options.

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-unnamed-declare interface FormLinkOptions--><!--Device-unnamed-declare interface FormLinkOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## abilityName

```TypeScript
abilityName?: string
```

Name of the target UIAbility when action is **"router"** or **"call"**.

This API can be used in ArkTS widgets since API version 10.

**类型：** string

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-FormLinkOptions-abilityName?: string--><!--Device-FormLinkOptions-abilityName?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action: string
```

Action type.

- **"router"**: redirection to the specified UIAbility of the widget provider.  
- **"message"**: custom message. If this type of action is triggered, the   
[onFormEvent()](../../apis-form-kit/arkts-apis/arkts-form-app-form-formextensionability-formextensionability-c.md/arkts-form-app-form-formextensionability-formextensionability-c.md#onformevent)lifecycle callback of the provider FormExtensionAbility is called.  
- **"call"**: launch of the widget provider in the background. If this type of action is triggered, the specified   
UIAbility (whose launch type must be [singleton](../../../application-models/uiability-launch-type.md#singleton)of the widget provider is started in the background, but not displayed in the foreground. This action type requires  that the widget provider should have the   
[ohos.permission.KEEP_BACKGROUND_RUNNING](../../../security/AccessToken/permissions-for-all.md#ohospermissionkeep_background_running) permission.

**NOTE：**

Whenever possible, avoid using the router event to refresh the widget UI.

This API can be used in ArkTS widgets since API version 10.

**类型：** string

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-FormLinkOptions-action: string--><!--Device-FormLinkOptions-action: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## bundleName

```TypeScript
bundleName?: string
```

Name of the target bundle when action is **"router"** or **"call"**.

This API can be used in ArkTS widgets since API version 10.

**类型：** string

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-FormLinkOptions-bundleName?: string--><!--Device-FormLinkOptions-bundleName?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## moduleName

```TypeScript
moduleName?: string
```

Name of the target module when action is **"router"** or **"call"**.

This API can be used in ArkTS widgets since API version 10.

**类型：** string

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-FormLinkOptions-moduleName?: string--><!--Device-FormLinkOptions-moduleName?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## params

```TypeScript
params?: Object
```

Additional parameters carried in the current action. The value is a key-value pair in JSON format. For the **"call"  
** action type, the **method** parameter must be set and its value type must be string.

**NOTE：**

Whenever possible, avoid using **params** to transfer internal state variables of widgets.

This API can be used in ArkTS widgets since API version 10.

**类型：** Object

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本10开始，该接口支持在ArkTS卡片中使用。

<!--Device-FormLinkOptions-params?: Object--><!--Device-FormLinkOptions-params?: Object-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## uri

```TypeScript
uri?: string
```

URI of the target UIAbility when action is **"router"**. If both **uri** and **abilityName** are set,   
**abilityName** takes precedence.

This API can be used in ArkTS widgets since API version 11.

**类型：** string

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本11开始，该接口支持在ArkTS卡片中使用。

<!--Device-FormLinkOptions-uri?: string--><!--Device-FormLinkOptions-uri?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

