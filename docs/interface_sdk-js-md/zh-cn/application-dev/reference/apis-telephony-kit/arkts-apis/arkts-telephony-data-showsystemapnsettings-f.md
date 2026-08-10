# showSystemApnSettings

## 导入模块

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## showSystemApnSettings

```TypeScript
function showSystemApnSettings(context: Context): Promise<void>
```

Open the system APN selection menu, which is presented in a semi-modal form and can be used to select a specific APN. This API uses a promise to return the result.If there is no SIM card or the device does not support the APN menu, the menu cannot be displayed.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-data-function showSystemApnSettings(context: Context): Promise<void>--><!--Device-data-function showSystemApnSettings(context: Context): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 | Indicates Context instance. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## 示例

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需在页面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../../application-models/uiability-usage.md#获取uiability的上下文信息)。

```TypeScript
import { data } from '@kit.TelephonyKit';
import { common } from '@kit.AbilityKit';

let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
data.showSystemApnSettings(context).then(() => {
  console.info("showSystemApnSettings success");
}).catch(() => {
  console.error("showSystemApnSettings failed");
});
```

