# getSuperAdmin（系统接口）

## 导入模块

```TypeScript
import { adminManager } from 'kits/@kit.MDMKit';
```

## getSuperAdmin

```TypeScript
function getSuperAdmin(): Promise<Want>
```

查询首用户（u100）下的超级设备管理应用。使用Promise异步回调。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
