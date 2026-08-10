# NotificationRequest

定义了通知请求的数据结构，用于描述一条通知的全部信息，包括通知内容、标识、展示样式、交互行为等。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-unnamed-export interface NotificationRequest--><!--Device-unnamed-export interface NotificationRequest-End-->

**System capability:** SystemCapability.Notification.Notification

## agentBundle

```TypeScript
readonly agentBundle?: BundleOption
```

创建通知的代理包信息。默认为空。

**Type:** [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NotificationRequest-readonly agentBundle?: BundleOption--><!--Device-NotificationRequest-readonly agentBundle?: BundleOption-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## appInstanceKey

```TypeScript
readonly appInstanceKey?: string
```

应用实例键值。默认为空。

**Type:** string

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-NotificationRequest-readonly appInstanceKey?: string--><!--Device-NotificationRequest-readonly appInstanceKey?: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## classification

```TypeScript
classification?: string
```

通知分类。预留能力，暂未支持。

**Type:** string

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

<!--Device-NotificationRequest-classification?: string--><!--Device-NotificationRequest-classification?: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## creatorInstanceKey

```TypeScript
readonly creatorInstanceKey?: number
```

创建者实例键值。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** 15

**Substitutes:** [NotificationRequest#appInstanceKey](arkts-notification-notificationrequest-notificationrequest-i-sys.md#appinstancekey)

<!--Device-NotificationRequest-readonly creatorInstanceKey?: number--><!--Device-NotificationRequest-readonly creatorInstanceKey?: number-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## deviceId

```TypeScript
readonly deviceId?: string
```

通知源的deviceId。预留能力，暂未支持。

**Type:** string

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-NotificationRequest-readonly deviceId?: string--><!--Device-NotificationRequest-readonly deviceId?: string-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## extendInfo

```TypeScript
extendInfo?: Record<string, Object>
```

系统应用发布通知时的自定义扩展参数。默认为空。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

<!--Device-NotificationRequest-extendInfo?: Record<string, Object>--><!--Device-NotificationRequest-extendInfo?: Record<string, Object>-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## forceDistributed

```TypeScript
forceDistributed?: boolean
```

通知是否强制进行全场景跨设备协同显示，默认为false。

**说明：**:

仅当应用在跨设备协同管控名单中且notDistributed为false时，该字段才会生效。通过读取notification_config.json文件（文件配置路径见：[notification_config_parse.h](https://gitcode.com/openharmony/notification_distributed_notification_service/blob/master/services/ans/include/notification_config_parse.h)中的NOTIFICATION_CONFIG_FILE属性）中的collaborationFilter字段，查看是否包含应用的UID或包名。如果包含，说明是在应用跨设备协同管控名单中。

- 设置为true时：通知将在所有协同设备上显示。

- 设置为false时：通知将按照协同管控名单显示。

**Type:** boolean

**Default:** false

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-NotificationRequest-forceDistributed?: boolean--><!--Device-NotificationRequest-forceDistributed?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## groupInfo

```TypeScript
groupInfo?: GroupInfo
```

组通知定制信息。默认为空。

**Type:** [GroupInfo](arkts-notification-notificationrequest-groupinfo-i-sys.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NotificationRequest-groupInfo?: GroupInfo--><!--Device-NotificationRequest-groupInfo?: GroupInfo-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## isRemoveAllowed

```TypeScript
isRemoveAllowed?: boolean
```

通知是否能被移除（点击通知下方删除按钮无法删除，左滑不出现删除按钮）。默认为true。

- true：是。  
- false：否。

**Type:** boolean

**Default:** true

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 11+: ohos.permission.SET_UNREMOVABLE_NOTIFICATION

<!--Device-NotificationRequest-isRemoveAllowed?: boolean--><!--Device-NotificationRequest-isRemoveAllowed?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## notDistributed

```TypeScript
notDistributed?: boolean
```

通知是否不进行全场景跨设备协同显示，默认为false。

**说明：**:

该字段与forceDistributed字段互斥，当两者同时为true时，仅notDistributed字段生效。

- 设置为true时：通知仅在本设备上显示。

- 设置为false时：通知将在所有协同设备上显示。

**Type:** boolean

**Default:** false

**Since:** 18

**ArkTS mode:** ArkTS-Dyn since version 18; ArkTS-Sta since version 23.

<!--Device-NotificationRequest-notDistributed?: boolean--><!--Device-NotificationRequest-notDistributed?: boolean-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## notificationControlFlags

```TypeScript
notificationControlFlags?: long
```

通知提醒方式管控。默认值为0。

可以通过此接口减少当前通知的提醒方式。与  
[NotificationControlFlagStatus](arkts-notification-notificationmanager-notificationcontrolflagstatus-e-sys.md)的枚举进行按位或运算得到该参数。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NotificationRequest-notificationControlFlags?: long--><!--Device-NotificationRequest-notificationControlFlags?: long-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## representativeBundle

```TypeScript
representativeBundle?: BundleOption
```

被代理的包信息。默认为空。

**Type:** [BundleOption](arkts-notification-notificationcommondef-bundleoption-i.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NotificationRequest-representativeBundle?: BundleOption--><!--Device-NotificationRequest-representativeBundle?: BundleOption-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## source

```TypeScript
readonly source?: int
```

通知源。预留能力，暂未支持。

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

<!--Device-NotificationRequest-readonly source?: int--><!--Device-NotificationRequest-readonly source?: int-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## trigger

```TypeScript
trigger?:Trigger
```

条件对象。默认为空。

**Type:** [Trigger](arkts-notification-notificationrequest-trigger-i-sys.md)

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-NotificationRequest-trigger?:Trigger--><!--Device-NotificationRequest-trigger?:Trigger-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

## unifiedGroupInfo

```TypeScript
unifiedGroupInfo?: UnifiedGroupInfo
```

消息智能聚合信息字段。默认为空。

**Type:** [UnifiedGroupInfo](arkts-notification-notificationmanager-unifiedgroupinfo-t-sys.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-NotificationRequest-unifiedGroupInfo?: UnifiedGroupInfo--><!--Device-NotificationRequest-unifiedGroupInfo?: UnifiedGroupInfo-End-->

**System capability:** SystemCapability.Notification.Notification

**System API:** This is a system API.

