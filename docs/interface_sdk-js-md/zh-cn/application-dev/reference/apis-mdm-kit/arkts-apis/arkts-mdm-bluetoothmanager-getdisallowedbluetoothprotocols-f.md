# getDisallowedBluetoothProtocols

## 导入模块

```TypeScript
import { bluetoothManager } from 'kits/@kit.MDMKit';
```

## getDisallowedBluetoothProtocols

```TypeScript
function getDisallowedBluetoothProtocols(admin: Want, accountId: number): Array<Protocol>
```

获取指定用户的蓝牙协议禁用名单。

**起始版本：** 20

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| accountId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;Protocol & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [201](../../errorcode-universal.md#201-权限校验失败) |


## getDisallowedBluetoothProtocols

```TypeScript
function getDisallowedBluetoothProtocols(admin: Want | null, accountId: number, policy: TransferPolicy): Array<Protocol>
```

获取指定用户指定传输策略下已禁用的蓝牙协议列表。

> **说明：**&gt;
> 1. 本接口与[getDisallowedBluetoothProtocols&lt;sup&gt;20+&lt;/sup&gt;](#getdisallowedbluetoothprotocols)接口为
> 重载接口。本接口增加了policy参数，用于按传输策略查询对应的禁用配置。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) \| null | 是 |
| accountId | number | 是 |
| policy | [TransferPolicy](arkts-mdm-bluetoothmanager-transferpolicy-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;Protocol & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
