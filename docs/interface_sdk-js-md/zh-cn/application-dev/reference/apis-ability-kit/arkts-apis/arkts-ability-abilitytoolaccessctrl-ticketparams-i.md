# TicketParams

```TypeScript
interface TicketParams
```

表示生成ticket的参数。各字段均为可选，未传入的字段使用默认值。

**起始版本：** 26.1.0

<!--Device-abilityToolAccessCtrl-interface TicketParams--><!--Device-abilityToolAccessCtrl-interface TicketParams-End-->

**系统能力：** SystemCapability.Security.Asset

## 导入模块

```TypeScript
import { abilityToolAccessCtrl } from '@kit.AbilityKit';
```

## ticketExpireTimeMs

```TypeScript
ticketExpireTimeMs?: number
```

ticket过期时间，单位为毫秒。取值范围：1~60000（60秒）。默认值：10000

**类型：** number

**起始版本：** 26.1.0

**模型约束：** 此接口可在Stage模型和FA模型下使用。

<!--Device-TicketParams-ticketExpireTimeMs?: long--><!--Device-TicketParams-ticketExpireTimeMs?: long-End-->

**系统能力：** SystemCapability.Security.Asset
