# getAllowedHotspotClientList

## 导入模块

```TypeScript
import { wifiManager } from '@kit.MDMKit';
```

## getAllowedHotspotClientList

```TypeScript
function getAllowedHotspotClientList(queryPolicy?: common.QueryPolicy): Array<string>
```

获取网络共享MAC地址可用名单。

**起始版本：** 26.1.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_WIFI

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-wifiManager-function getAllowedHotspotClientList(queryPolicy?: common.QueryPolicy): Array<string>--><!--Device-wifiManager-function getAllowedHotspotClientList(queryPolicy?: common.QueryPolicy): Array<string>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| queryPolicy | [common.QueryPolicy](arkts-mdm-common-querypolicy-e.md) | 否 | 查询策略。通过queryPolicy指定查询策略，默认值为[SELF](arkts-mdm-common-querypolicy-e.md#self)，表示查询当前设备管理应用设置的策略；传入[ALL](arkts-mdm-common-querypolicy-e.md#all)时，可查询当前设备设置的策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;string&gt; | 网络共享MAC地址可用名单。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) | The application is not an administrator application of the device. |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) | The administrator application does not have permission to manage the device. |
| [9200016](../errorcode-enterpriseDeviceManager.md#9200016-服务超时) | Service timeout. |
