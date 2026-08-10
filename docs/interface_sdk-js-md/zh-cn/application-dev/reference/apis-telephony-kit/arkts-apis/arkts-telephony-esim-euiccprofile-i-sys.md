# EuiccProfile（系统接口）

Information about an embedded profile (subscription) on an eUICC.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-eSIM-export interface EuiccProfile--><!--Device-eSIM-export interface EuiccProfile-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## accessRules

```TypeScript
accessRules: Array<AccessRule>
```

Optional access rules that specify which apps can manage this profile. Default platform management when not set.

**类型：** Array&lt;AccessRule&gt;

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-EuiccProfile-accessRules: Array<AccessRule>--><!--Device-EuiccProfile-accessRules: Array<AccessRule>-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## iccid

```TypeScript
iccid: string
```

The iccid of the profile.

**类型：** string

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-EuiccProfile-iccid: string--><!--Device-EuiccProfile-iccid: string-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## nickName

```TypeScript
nickName: string
```

An optional nickname for the profile.

**类型：** string

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-EuiccProfile-nickName: string--><!--Device-EuiccProfile-nickName: string-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## operatorId

```TypeScript
operatorId: OperatorId
```

The operator Id of the profile.

**类型：** [OperatorId](arkts-telephony-esim-operatorid-i-sys.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-EuiccProfile-operatorId: OperatorId--><!--Device-EuiccProfile-operatorId: OperatorId-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## policyRules

```TypeScript
policyRules: PolicyRules
```

The policy rules of the profile.

**类型：** [PolicyRules](arkts-telephony-esim-policyrules-e-sys.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-EuiccProfile-policyRules: PolicyRules--><!--Device-EuiccProfile-policyRules: PolicyRules-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## profileClass

```TypeScript
profileClass: ProfileClass
```

Profile class for the profile.

**类型：** [ProfileClass](arkts-telephony-esim-profileclass-e-sys.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-EuiccProfile-profileClass: ProfileClass--><!--Device-EuiccProfile-profileClass: ProfileClass-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## profileName

```TypeScript
profileName: string
```

The profile name.

**类型：** string

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-EuiccProfile-profileName: string--><!--Device-EuiccProfile-profileName: string-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## serviceProviderName

```TypeScript
serviceProviderName: string
```

The service provider name for the profile.

**类型：** string

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-EuiccProfile-serviceProviderName: string--><!--Device-EuiccProfile-serviceProviderName: string-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

## state

```TypeScript
state: ProfileState
```

The profile state.

**类型：** [ProfileState](arkts-telephony-esim-profilestate-e-sys.md)

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-EuiccProfile-state: ProfileState--><!--Device-EuiccProfile-state: ProfileState-End-->

**系统能力：** SystemCapability.Telephony.CoreService.Esim

**系统接口：** 此接口为系统接口。

