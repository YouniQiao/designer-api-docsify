# EnterpriseAdminExtensionContext

**EnterpriseAdminExtensionContext** is the context of  
[EnterpriseAdminExtensionAbility](arkts-mdm-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md#EnterpriseAdminExtensionAbility)and inherits from [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md#ExtensionContext).

When an **EnterpriseAdminExtensionAbility** component is instantiated, the system automatically creates the corresponding **EnterpriseAdminExtensionContext**. You can use this **EnterpriseAdminExtensionContext** to obtain the sandbox path of the app and start other components. This context can only be used within the current  
**EnterpriseAdminExtensionAbility** and cannot be transferred to other components.

> **NOTE：**
> 
> - The APIs of this module can be used only in the stage model.
> 
> - The APIs of this module can be called only by a device administrator application that is enabled. For details,
> see [MDM Kit Development](../../../mdm/mdm-kit-guide.md).

**Inheritance/Implementation:** EnterpriseAdminExtensionContext extends [ExtensionContext](ExtensionContext)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-declare class EnterpriseAdminExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class EnterpriseAdminExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## startAbilityByAdmin

```TypeScript
startAbilityByAdmin(admin: Want, want: Want): Promise<void>
```

Directly starts another component within the  
[EnterpriseAdminExtensionAbility](arkts-mdm-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md#EnterpriseAdminExtensionAbility)component (without pop-up prompts on the page). Currently, [UIAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-uiability-uiability-c.md#UIAbility) and  
[AppServiceExtensionAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-appserviceextensionability-appserviceextensionability-c.md#AppServiceExtensionAbility)are supported. This API uses a promise to return the result.

> **NOTE：**
> 
> - Only third-party app components are supported; system app components are not supported.
> 
> - The component to start must be visible to external parties, that is, the **exported** field in the
> **module.json5** file must be set to **true**.
> 
> - [Implicit Want launch](../../../application-models/ability-terminology.md) is not supported.
> 
> - If the **UIAbility** to start has permission protection, you need to apply for the corresponding permission.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Required permissions:** ohos.permission.ENTERPRISE_START_ABILITIES

**Model restriction:** This API can be used only in the stage model.

<!--Device-EnterpriseAdminExtensionContext-startAbilityByAdmin(admin: Want, want: Want): Promise<void>--><!--Device-EnterpriseAdminExtensionContext-startAbilityByAdmin(admin: Want, want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of **EnterpriseAdminExtensionAbility** and the app bundle name. |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Mandatory information for starting a component. The **Want** must contain the ability name of the component to be started and the bundle name of the app where the component is located. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. If the component fails to be started, an error object is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call the API due to limited device capabilities. |
| [9200014](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200014-failed-to-start-the-component) | Failed to start the ability. |
| [9200015](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200015-component-not-exist) | The ability does not exist. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-mdm-kit/errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |

