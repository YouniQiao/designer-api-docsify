# showAppNetPolicySettings

## 导入模块

```TypeScript
import { policy } from 'kits/@kit.NetworkKit';
```

## showAppNetPolicySettings

```TypeScript
function showAppNetPolicySettings(context: Context): Promise<void>
```

当需要设置当前应用能否使用Wi-Fi/蜂窝联网时，调用该接口可以打开当前应用的联网设置界面，以设置应用的联网权限。使用Promise异步回调。

**起始版本：** 22

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |
