# showSystemApnSettings

## 导入模块

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## showSystemApnSettings

```TypeScript
function showSystemApnSettings(context: Context): Promise<void>
```

打开当前默认移动数据卡对应的APN配置界面。使用Promise异步回调。

> **说明：**&gt;
> - 该接口仅支持查看和选择当前已添加的通用APN，不支持新建或修改。&gt;
> - 若未插入SIM卡或设备不支持APN配置，将无法打开该配置界面。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
