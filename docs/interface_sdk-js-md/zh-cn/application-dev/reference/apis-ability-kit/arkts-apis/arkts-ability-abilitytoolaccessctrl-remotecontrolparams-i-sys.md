# RemoteControlParams（系统接口）

```TypeScript
interface RemoteControlParams
```

表示远程控制交互参数。

**起始版本：** 26.0.1

<!--Device-abilityToolAccessCtrl-interface RemoteControlParams--><!--Device-abilityToolAccessCtrl-interface RemoteControlParams-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## challenge

```TypeScript
challenge?: string
```

防重放挑战值，用于防止重放攻击。合法的挑战值由generateControlledDevicePackage接口获取。默认值：空字符串。

**类型：** string

**起始版本：** 26.0.1

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-RemoteControlParams-challenge?: string--><!--Device-RemoteControlParams-challenge?: string-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## controlledDeviceName

```TypeScript
controlledDeviceName?: string
```

被控设备的设备名称。默认值：空字符串。

**类型：** string

**起始版本：** 26.0.1

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-RemoteControlParams-controlledDeviceName?: string--><!--Device-RemoteControlParams-controlledDeviceName?: string-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## controllerDeviceName

```TypeScript
controllerDeviceName?: string
```

主控设备的设备名称。默认值：空字符串。

**类型：** string

**起始版本：** 26.0.1

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-RemoteControlParams-controllerDeviceName?: string--><!--Device-RemoteControlParams-controllerDeviceName?: string-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## remoteControlTicket

```TypeScript
remoteControlTicket?: string
```

可信设备的远程控制凭证，用于远程控制场景同账号下可信设备的身份验证。默认值：空字符串。

**类型：** string

**起始版本：** 26.0.1

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-RemoteControlParams-remoteControlTicket?: string--><!--Device-RemoteControlParams-remoteControlTicket?: string-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## signVerifyMsg

```TypeScript
signVerifyMsg?: string
```

签名认证需要的额外信息，如调用方包名、模块名等。默认值：空字符串。

**类型：** string

**起始版本：** 26.0.1

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-RemoteControlParams-signVerifyMsg?: string--><!--Device-RemoteControlParams-signVerifyMsg?: string-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。
