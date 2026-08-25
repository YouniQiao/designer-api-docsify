# EnterpriseAdminExtensionContext

**EnterpriseAdminExtensionContext** is the context of [EnterpriseAdminExtensionAbility](arkts-mdm-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md) and inherits from [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md).When an **EnterpriseAdminExtensionAbility** component is instantiated, the system automatically creates the corresponding **EnterpriseAdminExtensionContext**. You can use this **EnterpriseAdminExtensionContext** to obtain the sandbox path of the app and start other components. This context can only be used within the current **EnterpriseAdminExtensionAbility** and cannot be transferred to other components.

> **NOTE：**&gt;
> - The APIs of this module can be used only in the stage model.&gt;
> - The APIs of this module can be called only by a device administrator application that is enabled. For details,
> see [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Inheritance/Implementation:** EnterpriseAdminExtensionContext extends ExtensionContext

**Since:** 23

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## startAbilityByAdmin

```TypeScript
startAbilityByAdmin(admin: Want, want: Want): Promise<void>
```

Directly starts another component within the [EnterpriseAdminExtensionAbility](arkts-mdm-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md) component (without pop-up prompts on the page). Currently, [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md) and [AppServiceExtensionAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-appserviceextensionability-appserviceextensionability-c.md) are supported. This API uses a promise to return the result.

> **NOTE：**&gt;
> - Only third-party app components are supported; system app components are not supported.&gt;
> - The component to start must be visible to external parties, that is, the **exported** field in the
> **module.json5** file must be set to **true**.&gt;
> - [Implicit Want launch](../../../application-models/ability-terminology.md) is not supported.&gt;
> - If the **UIAbility** to start has permission protection, you need to apply for the corresponding permission.

**Since:** 23

**Required permissions:** ohos.permission.ENTERPRISE_START_ABILITIES

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) |
| [9200014](../errorcode-enterpriseDeviceManager.md#9200014-failed-to-start-the-component) |
| [9200015](../errorcode-enterpriseDeviceManager.md#9200015-component-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
