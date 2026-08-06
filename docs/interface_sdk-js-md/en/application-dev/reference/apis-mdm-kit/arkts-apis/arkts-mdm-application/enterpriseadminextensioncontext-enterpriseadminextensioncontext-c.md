# EnterpriseAdminExtensionContext

EnterpriseAdminExtensionContext** is the context of  
[EnterpriseAdminExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_and inherits from [ExtensionContext]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_.

When an **EnterpriseAdminExtensionAbility** component is instantiated, the system automatically creates the corresponding **EnterpriseAdminExtensionContext**. You can use this **EnterpriseAdminExtensionContext** to obtain the sandbox path of the app and start other components. This context can only be used within the current  
**EnterpriseAdminExtensionAbility** and cannot be transferred to other components.
    **NOTE**  
    
    - The APIs of this module can be used only in the stage model.  
    
    - The APIs of this module can be called only by a device administrator application that is enabled. For details,  
    see \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Inheritance/Implementation:** EnterpriseAdminExtensionContext extends [ExtensionContext](../../../apis-ability-kit/arkts-apis/arkts-ability-application/extensioncontext-extensioncontext-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-declare class EnterpriseAdminExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class EnterpriseAdminExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## startAbilityByAdmin

```TypeScript
startAbilityByAdmin(admin: Want, want: Want): Promise<void>
```

Directly starts another component within the  
[EnterpriseAdminExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_component (without pop-up prompts on the page). Currently, [UIAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ and  
[AppServiceExtensionAbility]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_are supported. This API uses a promise to return the result.
    **NOTE**  
    
    - Only third-party app components are supported; system app components are not supported.  
    
    - The component to start must be visible to external parties, that is, the **exported** field in the  
    **module.json5** file must be set to **true**.  
    
    - \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_ is not supported.  
    
    - If the **UIAbility** to start has permission protection, you need to apply for the corresponding permission.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Required permissions:** ohos.permission.ENTERPRISE_START_ABILITIES

**Model restriction:** This API can be used only in the stage model.

<!--Device-EnterpriseAdminExtensionContext-startAbilityByAdmin(admin: Want, want: Want): Promise<void>--><!--Device-EnterpriseAdminExtensionContext-startAbilityByAdmin(admin: Want, want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | EnterpriseAdminExtensionAbility. **Want** must contain the ability name of **EnterpriseAdminExtensionAbility** and the app bundle name. |
| want | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Mandatory information for starting a component. The **Want** must contain the ability name of the component to be started and the bundle name of the app where the component is located. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. If the component fails to be started, an error object is thrown. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [9200001](../../errorcode-enterpriseDeviceManager.md#9200001-deviceadmin-not-enabled) | The application is not an administrator application of the device. |
| [9200014](../../errorcode-enterpriseDeviceManager.md#9200014-failed-to-start-the-component) | Failed to start the ability. |
| [9200015](../../errorcode-enterpriseDeviceManager.md#9200015-component-not-exist) | The ability does not exist. |
| [201](../../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Failed to call the API due to limited device capabilities. |

