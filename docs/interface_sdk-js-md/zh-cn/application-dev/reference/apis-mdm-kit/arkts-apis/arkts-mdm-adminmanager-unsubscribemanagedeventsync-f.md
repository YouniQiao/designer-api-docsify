# unsubscribeManagedEventSync

## 导入模块

```TypeScript
import { adminManager } from 'kits/@kit.MDMKit';
```

## unsubscribeManagedEventSync

```TypeScript
function unsubscribeManagedEventSync(admin: Want, managedEvents: Array<ManagedEvent>): void
```

取消订阅系统管理事件。调用成功后，将不再收到已取消订阅的系统管理事件通知。

**起始版本：** 12

**需要权限：** ohos.permission.ENTERPRISE_SUBSCRIBE_MANAGED_EVENT

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| managedEvents | Array&lt;[ManagedEvent](arkts-mdm-adminmanager-managedevent-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200008](../errorcode-enterpriseDeviceManager.md#9200008-系统订阅事件无效) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
