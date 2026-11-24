# TicketInfo（系统接口）

```TypeScript
interface TicketInfo
```

表示ticket信息。

**起始版本：** 26.0.0

<!--Device-abilityToolAccessCtrl-interface TicketInfo--><!--Device-abilityToolAccessCtrl-interface TicketInfo-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## challenge

```TypeScript
challenge: string
```

挑战值，用于验证ticket的合法性。

**类型：** string

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-TicketInfo-challenge: string--><!--Device-TicketInfo-challenge: string-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## message

```TypeScript
message: string
```

ticket消息，用于传递授权信息、提示信息和状态描述。

**类型：** string

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-TicketInfo-message: string--><!--Device-TicketInfo-message: string-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。

## ticket

```TypeScript
ticket: string
```

ticket字符串，用于权限验证。

**类型：** string

**起始版本：** 26.0.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-TicketInfo-ticket: string--><!--Device-TicketInfo-ticket: string-End-->

**系统能力：** SystemCapability.Security.Asset

**系统接口：** 此接口为系统接口。
