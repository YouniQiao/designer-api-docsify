# EnterpriseAdminExtensionContext

EnterpriseAdminExtensionContext是  
[EnterpriseAdminExtensionAbility](../../apis-default/arkts-apis/arkts-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md/arkts-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md)的上下文环境，继承自[ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)。

每个EnterpriseAdminExtensionAbility组件实例化时，系统都会自动创建对应的EnterpriseAdminExtensionContext。开发者可以通过EnterpriseAdminExtensionContext获取应用的沙箱路径、启动其他的组件。该上下文环境只能在当前EnterpriseAdminExtensionAbility中使用，不能传递到其他组件中使用。

> **说明：**
> 
> 本模块接口仅可在Stage模型下使用。
> 
> 本模块接口仅对设备管理应用开放，且调用接口前需激活设备管理应用，具体请参考[MDM Kit开发指南](../../../mdm/mdm-kit-guide.md)。

**Inheritance/Implementation:** EnterpriseAdminExtensionContext extends [ExtensionContext](../../apis-ability-kit/arkts-apis/arkts-ability-extensioncontext-c.md/arkts-ability-extensioncontext-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-declare class EnterpriseAdminExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class EnterpriseAdminExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## startAbilityByAdmin

```TypeScript
startAbilityByAdmin(admin: Want, want: Want): Promise<void>
```

在  
[EnterpriseAdminExtensionAbility](../../apis-default/arkts-apis/arkts-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md/arkts-enterprise-enterpriseadminextensionability-enterpriseadminextensionability-c.md)组件中直接启动另外一个组件（页面没有弹窗提醒），目前支持[UIAbility](../../apis-ability-kit/arkts-apis/arkts-app-ability-uiability.md/arkts-app-ability-uiability.md)，  
[AppServiceExtensionAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-appserviceextensionability-appserviceextensionability-c.md/arkts-ability-app-ability-appserviceextensionability-appserviceextensionability-c.md)。使用Promise异步回调。

> **说明：**
> 
> 仅支持启动三方应用组件，不支持系统应用组件。
> 
> 被启动的组件需要对外可见，即module.json5中的exported字段需要为true。
> 
> 不支持[隐式Want启动](../../../application-models/ability-terminology.md#隐式want启动)。
> 
> 如果被启动的UIAbility有权限保护，需要额外申请对应的权限。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Required permissions:** ohos.permission.ENTERPRISE_START_ABILITIES

**Model restriction:** This API can be used only in the stage model.

<!--Device-EnterpriseAdminExtensionContext-startAbilityByAdmin(admin: Want, want: Want): Promise<void>--><!--Device-EnterpriseAdminExtensionContext-startAbilityByAdmin(admin: Want, want: Want): Promise<void>-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 企业设备管理扩展组件。Want中必须包含企业设备管理扩展能力的abilityName和所在应用的bundleName。 |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | 启动组件的必要信息，Want中必须包含被启动组件的abilityName和所在应用的bundleName。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。当启动组件失败时，会抛出错误对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | Capability not supported. Failed to call the API due to limited device capabilities. |
| 9200014 | Failed to start the ability. |
| 9200015 | The ability does not exist. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 9200001 | The application is not an administrator application of the device. |

