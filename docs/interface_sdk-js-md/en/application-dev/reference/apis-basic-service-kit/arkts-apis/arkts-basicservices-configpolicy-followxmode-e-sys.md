# FollowXMode (System API)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-configPolicy-export enum FollowXMode--><!--Device-configPolicy-export enum FollowXMode-End-->

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

## DEFAULT

```TypeScript
DEFAULT = 0
```

默认模式，会根据各配置层级下的followx_file_list.cfg文件配置的跟随规则进行文件查找。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-FollowXMode-DEFAULT = 0--><!--Device-FollowXMode-DEFAULT = 0-End-->

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

## NO_RULE_FOLLOWED

```TypeScript
NO_RULE_FOLLOWED = 1
```

不跟随模式，不会使用任何跟随规则，即使存在followx_file_list.cfg文件。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-FollowXMode-NO_RULE_FOLLOWED = 1--><!--Device-FollowXMode-NO_RULE_FOLLOWED = 1-End-->

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

## SIM_DEFAULT

```TypeScript
SIM_DEFAULT = 10
```

跟随默认卡模式，会根据默认卡的opkey在各配置层级下的etc/carrier/\${opkey}下查找文件。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-FollowXMode-SIM_DEFAULT = 10--><!--Device-FollowXMode-SIM_DEFAULT = 10-End-->

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

## SIM_1

```TypeScript
SIM_1 = 11
```

跟随卡1模式，会根据卡1的opkey在各配置层级下的etc/carrier/\${opkey}下查找文件。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-FollowXMode-SIM_1 = 11--><!--Device-FollowXMode-SIM_1 = 11-End-->

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

## SIM_2

```TypeScript
SIM_2 = 12
```

跟随卡2模式，会根据卡2的opkey在各配置层级下的etc/carrier/\${opkey}下查找文件。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-FollowXMode-SIM_2 = 12--><!--Device-FollowXMode-SIM_2 = 12-End-->

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

## USER_DEFINED

```TypeScript
USER_DEFINED = 100
```

用户自定义模式，会根据入参extra提供的跟随规则进行配置文件获取，忽略各配置层级下的followx_file_list.cfg文件。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-FollowXMode-USER_DEFINED = 100--><!--Device-FollowXMode-USER_DEFINED = 100-End-->

**System capability:** SystemCapability.Customization.ConfigPolicy

**System API:** This is a system API.

