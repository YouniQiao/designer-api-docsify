# AttestResultInfo（系统接口）

Device attest result information.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-deviceAttest-export interface AttestResultInfo--><!--Device-deviceAttest-export interface AttestResultInfo-End-->

**系统能力：** SystemCapability.XTS.DeviceAttest

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { deviceAttest } from 'kits/@kit.BasicServicesKit';
```

## authResult

```TypeScript
authResult: number
```

Result of the device hardware information authentication.

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-AttestResultInfo-authResult: number--><!--Device-AttestResultInfo-authResult: number-End-->

**系统能力：** SystemCapability.XTS.DeviceAttest

**系统接口：** 此接口为系统接口。

## softwareResult

```TypeScript
softwareResult: number
```

Result of the device software information authentication.

**类型：** number

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-AttestResultInfo-softwareResult: number--><!--Device-AttestResultInfo-softwareResult: number-End-->

**系统能力：** SystemCapability.XTS.DeviceAttest

**系统接口：** 此接口为系统接口。

## softwareResultDetail

```TypeScript
softwareResultDetail: Array<number>
```

Software result detail array that includes versionId, patchLevel,rootHash and a reserved space.

**类型：** Array&lt;number&gt;

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-AttestResultInfo-softwareResultDetail: Array<number>--><!--Device-AttestResultInfo-softwareResultDetail: Array<number>-End-->

**系统能力：** SystemCapability.XTS.DeviceAttest

**系统接口：** 此接口为系统接口。

## ticket

```TypeScript
ticket: string
```

Credential sent from the cloud.

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-AttestResultInfo-ticket: string--><!--Device-AttestResultInfo-ticket: string-End-->

**系统能力：** SystemCapability.XTS.DeviceAttest

**系统接口：** 此接口为系统接口。

