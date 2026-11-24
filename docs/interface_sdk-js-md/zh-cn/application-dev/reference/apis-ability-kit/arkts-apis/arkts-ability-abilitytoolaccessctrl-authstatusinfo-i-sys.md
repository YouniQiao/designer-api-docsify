# AuthStatusInfo（系统接口）

```TypeScript
interface AuthStatusInfo
```

表示授权状态信息。

**起始版本：** 26.0.0

<!--Device-abilityToolAccessCtrl-interface AuthStatusInfo--><!--Device-abilityToolAccessCtrl-interface AuthStatusInfo-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## authStatus

```TypeScript
authStatus?: AuthStatus
```

授权状态。作为入参时，该项无需传入，如果传入会被忽略；作为出参时，该项返回实际的授权状态，表示权限的授权结果。

**类型：** [AuthStatus](arkts-ability-abilitytoolaccessctrl-authstatus-e-sys.md)

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-AuthStatusInfo-authStatus?: AuthStatus--><!--Device-AuthStatusInfo-authStatus?: AuthStatus-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## flag

```TypeScript
flag?: number
```

授权标志，用于标识权限授权的相关属性（如授权类型、授权持久性等）。作为入参时无需传入，若传入将被忽略，默认值为0；作为出参时返回实际授权标志。

**类型：** number

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-AuthStatusInfo-flag?: long--><!--Device-AuthStatusInfo-flag?: long-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。
