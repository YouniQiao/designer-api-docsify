# setControlPanelQuickToggleListForAccount

## 导入模块

```TypeScript
import { deviceSettings } from '@kit.MDMKit';
```

## setControlPanelQuickToggleListForAccount

```TypeScript
function setControlPanelQuickToggleListForAccount(toggleList: Array<ControlPanelQuickToggleType>,
    accountId: number): Promise<void>
```

设置指定用户控制中心1×1区域开关项白名单。白名单仅在管控模式启用时生效，未启用时仍会保存，但不会裁剪图标。新列表会覆盖原有列表，空数组表示该区域所有可裁剪图标均隐藏。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_SETTINGS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-deviceSettings-function setControlPanelQuickToggleListForAccount(toggleList: Array<ControlPanelQuickToggleType>,    accountId: number): Promise<void>--><!--Device-deviceSettings-function setControlPanelQuickToggleListForAccount(toggleList: Array<ControlPanelQuickToggleType>,    accountId: number): Promise<void>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| toggleList | Array&lt;[ControlPanelQuickToggleType](arkts-mdm-devicesettings-controlpanelquicktoggletype-e.md)&gt; | 是 | 1×1区域开关项白名单。空数组表示该区域所有可裁剪图标均隐藏。 |
| accountId | number | 是 | 用户ID，取值大于等于0且对应用户必须存在。accountId可以通过[getOsAccountLocalId](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-osaccount-accountmanager-i.md#getosaccountlocalid)获取。跨用户设置能力取决于设备管理员类型和设备。 |

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
| [9200006](../errorcode-enterpriseDeviceManager.md#9200006-指定的用户id非法) | The specified account ID is invalid. |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) | Parameter verification failed. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-服务超时) | Service timeout. |
