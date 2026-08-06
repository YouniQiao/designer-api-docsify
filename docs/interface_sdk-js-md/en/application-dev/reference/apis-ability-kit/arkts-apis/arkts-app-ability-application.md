# @ohos.app.ability.application

You can use this module to create a \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace application--><!--Device-unnamed-declare namespace application-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Summary

### Functions

| Name | Description |
| --- | --- |
| [createModuleContext](arkts-ability-application-createmodulecontext-f.md#createmodulecontext) | Creates the context for a module. The  [resourceManager.Configuration]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ in the created module context inherits from the input context, making it convenient for you to access  \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_. This API uses a promise to return the result. |
| [createModuleContextSync](arkts-ability-application-createmodulecontextsync-f.md#createmodulecontextsync) | Creates the context for a module. The  [resourceManager.Configuration]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ in the created module context inherits from the input context, making it convenient for you to access  \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ |
| [createPluginModuleContext](arkts-ability-application-createpluginmodulecontext-f.md#createpluginmodulecontext) | Creates the context of a plugin under the current application based on the context, plugin bundle name, and plugin module name, so as to obtain the basic information about the plugin. This API uses a promise to return the result. |
| [demoteCurrentFromCandidateMasterProcess](arkts-ability-application-demotecurrentfromcandidatemasterprocess-f.md#demotecurrentfromcandidatemasterprocess) | Removes the current process from the candidate master process list. This API uses a promise to return the result.This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 801is returned.  **System capability**: SystemCapability.Ability.AbilityRuntime.Core |
| [exitMasterProcessRole](arkts-ability-application-exitmasterprocessrole-f.md#exitmasterprocessrole) | Relinquishes the \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ role from the current process. This API uses a promise to return the result.This API can be properly called only on 2-in-1 devices and tablets. If it is called on other device types, error code 801 is returned. |
| [getAppPreloadType](arkts-ability-application-getapppreloadtype-f.md#getapppreloadtype) | Obtains the preloading type of the current application process. |
| [getApplicationContext](arkts-ability-application-getapplicationcontext-f.md#getapplicationcontext) | Obtains the application context. This API provides context access independent of the base class **Context**.Repeated calls to this API generate a new ApplicationContext object. |
| [getApplicationContextInstance](arkts-ability-application-getapplicationcontextinstance-f.md#getapplicationcontextinstance) | Obtains the application context. This API provides context access independent of the base class **Context**.Repeated calls to this API obtain the same ApplicationContext instance. |
| [promoteCurrentToCandidateMasterProcess](arkts-ability-application-promotecurrenttocandidatemasterprocess-f.md#promotecurrenttocandidatemasterprocess) | Adds the current process into the  \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ list. This API uses a promise to return the result.When the \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ is destroyed and a UIAbility or UIExtensionAbility with **isolationProcess** set to **true** is restarted, the system takes corresponding actions based on whether there is a candidate master process.  - If a candidate master process exists, the system sets the process at the head of the candidate master process  list as the new master process and triggers the  [onNewProcessRequest]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_4\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ callback.  - If no candidate master process exists, the system performs the following operations based on the component type:   - For a UIAbility, the system creates an empty process as the master process.   - For a UIExtensionAbility, the system first tries to reuse an existing UIExtensionAbility process as the new  master process. If no available process exists, it creates an empty process as the master process.This API can be properly called on PCs/2-in-1 devices and tablets. If it is called on other devices, error code 801is returned. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [createBundleContext](arkts-ability-application-createbundlecontext-f-sys.md#createbundlecontext) | Creates the context for an application. This API uses a promise to return the result. |
| [createModuleContext](arkts-ability-application-createmodulecontext-f-sys.md#createmodulecontext-1) | Creates the context for a module. This API uses a promise to return the result. |
| [createPluginModuleContextForHostBundle](arkts-ability-application-createpluginmodulecontextforhostbundle-f-sys.md#createpluginmodulecontextforhostbundle) | Creates the context for a plugin based on a given context, plugin bundle name, plugin module name, and application bundle name to obtain the basic information about the plugin. This API uses a promise to return the result. |
<!--DelEnd-->

### Enums

| Name | Description |
| --- | --- |
| [AppPreloadType](arkts-ability-application-apppreloadtype-e.md) | Enumerates the preloading types of the current application process. |

