# SharingCode (System API)

端云共享错误码。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-sharing-enum SharingCode--><!--Device-sharing-enum SharingCode-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## SUCCESS

```TypeScript
SUCCESS = 0
```

成功。请使用枚举名称而非枚举值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SharingCode-SUCCESS = 0--><!--Device-SharingCode-SUCCESS = 0-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## REPEATED_REQUEST

```TypeScript
REPEATED_REQUEST = 1
```

重复邀请，表示当前参与者已被邀请。请使用枚举名称而非枚举值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SharingCode-REPEATED_REQUEST = 1--><!--Device-SharingCode-REPEATED_REQUEST = 1-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## NOT_INVITER

```TypeScript
NOT_INVITER = 2
```

非端云共享的邀请者，表示当前参与者不是端云共享的邀请者。请使用枚举名称而非枚举值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SharingCode-NOT_INVITER = 2--><!--Device-SharingCode-NOT_INVITER = 2-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## NOT_INVITER_OR_INVITEE

```TypeScript
NOT_INVITER_OR_INVITEE = 3
```

非法参与者，表示当前参与者既不是共享的邀请者，也不是共享的被邀请者。请使用枚举名称而非枚举值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SharingCode-NOT_INVITER_OR_INVITEE = 3--><!--Device-SharingCode-NOT_INVITER_OR_INVITEE = 3-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## OVER_QUOTA

```TypeScript
OVER_QUOTA = 4
```

端云共享次数达到上限，表示当前账号可共享的次数达到上限。请使用枚举名称而非枚举值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SharingCode-OVER_QUOTA = 4--><!--Device-SharingCode-OVER_QUOTA = 4-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## TOO_MANY_PARTICIPANTS

```TypeScript
TOO_MANY_PARTICIPANTS = 5
```

端云共享参与者数量达到上限。请使用枚举名称而非枚举值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SharingCode-TOO_MANY_PARTICIPANTS = 5--><!--Device-SharingCode-TOO_MANY_PARTICIPANTS = 5-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## INVALID_ARGS

```TypeScript
INVALID_ARGS = 6
```

无效的参数。请使用枚举名称而非枚举值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SharingCode-INVALID_ARGS = 6--><!--Device-SharingCode-INVALID_ARGS = 6-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## NETWORK_ERROR

```TypeScript
NETWORK_ERROR = 7
```

网络错误。请使用枚举名称而非枚举值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SharingCode-NETWORK_ERROR = 7--><!--Device-SharingCode-NETWORK_ERROR = 7-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## CLOUD_DISABLED

```TypeScript
CLOUD_DISABLED = 8
```

云开关未打开。请使用枚举名称而非枚举值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SharingCode-CLOUD_DISABLED = 8--><!--Device-SharingCode-CLOUD_DISABLED = 8-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## SERVER_ERROR

```TypeScript
SERVER_ERROR = 9
```

服务端发生错误。请使用枚举名称而非枚举值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SharingCode-SERVER_ERROR = 9--><!--Device-SharingCode-SERVER_ERROR = 9-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## INNER_ERROR

```TypeScript
INNER_ERROR = 10
```

系统发生内部错误。请使用枚举名称而非枚举值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SharingCode-INNER_ERROR = 10--><!--Device-SharingCode-INNER_ERROR = 10-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## INVALID_INVITATION

```TypeScript
INVALID_INVITATION = 11
```

无效的邀请，表示当前邀请已失效或不存在。请使用枚举名称而非枚举值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SharingCode-INVALID_INVITATION = 11--><!--Device-SharingCode-INVALID_INVITATION = 11-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## RATE_LIMIT

```TypeScript
RATE_LIMIT = 12
```

速率限制，表示单次同步的数据量达到上限。请使用枚举名称而非枚举值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SharingCode-RATE_LIMIT = 12--><!--Device-SharingCode-RATE_LIMIT = 12-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

## CUSTOM_ERROR

```TypeScript
CUSTOM_ERROR = 1000
```

定制错误，小于该枚举值的错误码用于定义系统内部的标准错误码，大于该枚举值的错误码用于使用者自定义错误码。请使用枚举名称而非枚举值。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-SharingCode-CUSTOM_ERROR = 1000--><!--Device-SharingCode-CUSTOM_ERROR = 1000-End-->

**System capability:** SystemCapability.DistributedDataManager.CloudSync.Client

**System API:** This is a system API.

