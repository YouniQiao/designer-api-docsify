# AdminType

设备管理应用的类型。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-adminManager-export enum AdminType--><!--Device-adminManager-export enum AdminType-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## ADMIN_TYPE_NORMAL

```TypeScript
ADMIN_TYPE_NORMAL = 0x00
```

普通设备管理应用，激活后应用可卸载，其[企业设备管理扩展能力](../../../mdm/mdm-kit-term.md#enterpriseadminextensionability企业设备管理扩展能力)组件将开机自启和组件进程死亡后能重新拉起。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-AdminType-ADMIN_TYPE_NORMAL = 0x00--><!--Device-AdminType-ADMIN_TYPE_NORMAL = 0x00-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## ADMIN_TYPE_SUPER

```TypeScript
ADMIN_TYPE_SUPER = 0x01
```

超级设备管理应用，激活后应用不可卸载，其[企业设备管理扩展能力](../../../mdm/mdm-kit-term.md#enterpriseadminextensionability企业设备管理扩展能力)组件将开机自启和组件进程死亡后能重新拉起。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-AdminType-ADMIN_TYPE_SUPER = 0x01--><!--Device-AdminType-ADMIN_TYPE_SUPER = 0x01-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## ADMIN_TYPE_BYOD

```TypeScript
ADMIN_TYPE_BYOD = 0x02
```

BYOD设备管理应用。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

<!--Device-AdminType-ADMIN_TYPE_BYOD = 0x02--><!--Device-AdminType-ADMIN_TYPE_BYOD = 0x02-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

