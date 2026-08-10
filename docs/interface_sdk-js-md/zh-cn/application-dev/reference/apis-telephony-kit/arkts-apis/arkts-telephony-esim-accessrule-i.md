# AccessRule

Establishes a single UICC access rule pursuant to the GlobalPlatform Secure Element Access Control specification.

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-eSIM-export interface AccessRule--><!--Device-eSIM-export interface AccessRule-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

## 导入模块

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## accessType

```TypeScript
accessType: int
```

The type of access.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-AccessRule-accessType: int--><!--Device-AccessRule-accessType: int-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

## certificateHashHexStr

```TypeScript
certificateHashHexStr: string
```

Certificate hash hexadecimal string.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-AccessRule-certificateHashHexStr: string--><!--Device-AccessRule-certificateHashHexStr: string-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

## packageName

```TypeScript
packageName: string
```

The name of package.

**类型：** string

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-AccessRule-packageName: string--><!--Device-AccessRule-packageName: string-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

