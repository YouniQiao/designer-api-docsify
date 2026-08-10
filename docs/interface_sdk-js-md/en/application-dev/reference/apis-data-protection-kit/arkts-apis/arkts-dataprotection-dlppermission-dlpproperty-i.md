# DLPProperty

表示授权相关信息。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-dlpPermission-export interface DLPProperty--><!--Device-dlpPermission-export interface DLPProperty-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## Modules to Import

```TypeScript
import { dlpPermission } from 'kits/@kit.DataProtectionKit';
```

## actionUponExpiry

```TypeScript
actionUponExpiry?: ActionType
```

表示到期后文件是否允许打开（打开后拥有编辑权限），仅在expireTime不为空时生效，默认为空。

**Type:** [ActionType](../../apis-avsession-kit/arkts-apis/arkts-avsession-avmusictemplate-actiontype-t.md)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-DLPProperty-actionUponExpiry?: ActionType--><!--Device-DLPProperty-actionUponExpiry?: ActionType-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## allowedOpenCount

```TypeScript
allowedOpenCount?: number
```

表示允许打开的次数，默认为0。无范围限制。

**Type:** number

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-DLPProperty-allowedOpenCount?: number--><!--Device-DLPProperty-allowedOpenCount?: number-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## authUserList

```TypeScript
authUserList?: Array<AuthUser>
```

表示授权用户列表，默认为空。

**Type:** Array&lt;AuthUser&gt;

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DLPProperty-authUserList?: Array<AuthUser>--><!--Device-DLPProperty-authUserList?: Array<AuthUser>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## contactAccount

```TypeScript
contactAccount: string
```

表示联系人账号。长度不超过255字节，超出此范围抛出错误码401。

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DLPProperty-contactAccount: string--><!--Device-DLPProperty-contactAccount: string-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## countdown

```TypeScript
countdown?: number
```

表示文件可被查看的有效时间，超时后打开的文件将自动关闭，默认为0，单位：s。取值范围为[-2&lt;sup&gt;31&lt;/sup&gt;, 2&lt;sup&gt;31&lt;/sup&gt;-1]。

**Type:** number

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DLPProperty-countdown?: number--><!--Device-DLPProperty-countdown?: number-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## everyoneAccessList

```TypeScript
everyoneAccessList?: Array<DLPFileAccess>
```

表示授予所有人的权限，默认为空。

**Type:** Array&lt;DLPFileAccess&gt;

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DLPProperty-everyoneAccessList?: Array<DLPFileAccess>--><!--Device-DLPProperty-everyoneAccessList?: Array<DLPFileAccess>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## expireTime

```TypeScript
expireTime?: number
```

表示文件权限到期时间戳，默认为空。取值范围大于等于0，超出此范围抛出错误码。单位：s。

**Type:** number

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-DLPProperty-expireTime?: number--><!--Device-DLPProperty-expireTime?: number-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## extensionFields

```TypeScript
extensionFields?: Record<string, Object>
```

表示DLP文件的扩展属性，默认为空。

**Type:** [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt;

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DLPProperty-extensionFields?: Record<string, Object>--><!--Device-DLPProperty-extensionFields?: Record<string, Object>-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## fileId

```TypeScript
fileId?: string
```

表示文件的标识，默认为空。长度不超过255字节，超出此范围抛出错误码401。

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

<!--Device-DLPProperty-fileId?: string--><!--Device-DLPProperty-fileId?: string-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## offlineAccess

```TypeScript
offlineAccess: boolean
```

表示是否是离线打开。true表示允许离线打开，false表示不可离线打开。

**Type:** boolean

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DLPProperty-offlineAccess: boolean--><!--Device-DLPProperty-offlineAccess: boolean-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## ownerAccount

```TypeScript
ownerAccount: string
```

表示权限设置者账号。长度不超过255字节，超出此范围抛出错误码401。

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DLPProperty-ownerAccount: string--><!--Device-DLPProperty-ownerAccount: string-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## ownerAccountID

```TypeScript
ownerAccountID: string
```

表示权限设置者账号的ID。长度不超过255字节，超出此范围抛出错误码401。

**Type:** string

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DLPProperty-ownerAccountID: string--><!--Device-DLPProperty-ownerAccountID: string-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## ownerAccountType

```TypeScript
ownerAccountType: AccountType
```

表示权限设置者账号类型。

**Type:** [AccountType](arkts-dataprotection-dlppermission-accounttype-e.md)

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-DLPProperty-ownerAccountType: AccountType--><!--Device-DLPProperty-ownerAccountType: AccountType-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

## waterMarkConfig

```TypeScript
waterMarkConfig?: boolean
```

表示是否要求添加水印。true表示要求添加水印，false表示不要求添加水印，默认为空。

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-DLPProperty-waterMarkConfig?: boolean--><!--Device-DLPProperty-waterMarkConfig?: boolean-End-->

**System capability:** SystemCapability.Security.DataLossPrevention

