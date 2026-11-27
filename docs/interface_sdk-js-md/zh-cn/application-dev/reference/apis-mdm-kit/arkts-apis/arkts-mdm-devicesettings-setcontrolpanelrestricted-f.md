# setControlPanelRestricted

## 导入模块

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## setControlPanelRestricted

```TypeScript
function setControlPanelRestricted(restricted: boolean): Promise<void>
```

设置是否启用控制中心图标裁剪管控模式。启用后，控制中心仅显示白名单中的开关项，未配置白名单时，该区域所有可裁剪图标均隐藏。关闭后，白名单不生效。

本接口为设备级设置，对所有用户生效并在重启后保持，多个管理员调用时以最后一次成功设置为准。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-deviceSettings-function setControlPanelRestricted(restricted: boolean): Promise<void>--><!--Device-deviceSettings-function setControlPanelRestricted(restricted: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| restricted | boolean | 是 | 是否启用控制中心图标裁剪管控模式。**true**表示启用；**false**表示关闭。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | 无返回结果的Promise对象。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) | The administrator application does not have permission to manage the device. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-服务超时) | Service timeout. |
