# DLPPermissionInfo

表示DLP文件的权限信息。

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.Security.DataLossPrevention

## 导入模块

```TypeScript
import { dlpPermission } from '@kit.DataProtectionKit';
```

## dlpFileAccess

```TypeScript
dlpFileAccess: DLPFileAccess
```

表示DLP文件针对用户的授权类型，例如：只读。

**类型：** [DLPFileAccess](arkts-dataprotection-dlppermission-dlpfileaccess-e.md)

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.Security.DataLossPrevention

## flags

```TypeScript
flags: number
```

表示DLP文件的详细操作权限，取值范围由不同[ActionFlagType](arkts-dataprotection-dlppermission-actionflagtype-e.md)的组合决定。

**类型：** number

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为10。

**系统能力：** SystemCapability.Security.DataLossPrevention
