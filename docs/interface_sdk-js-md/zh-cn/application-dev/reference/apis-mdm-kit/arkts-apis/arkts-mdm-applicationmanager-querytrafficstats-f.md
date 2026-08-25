# queryTrafficStats

## 导入模块

```TypeScript
import { applicationManager } from 'kits/@kit.MDMKit';
```

## queryTrafficStats

```TypeScript
function queryTrafficStats(
    admin: Want,
    bundleName: string,
    appIndex: number,
    accountId: number,
    networkInfo: statistics.NetworkInfo
  ): Promise<statistics.NetStatsInfo>
```

查询当前用户下指定应用在特定时间段内使用流量情况。使用Promise异步回调。

> **说明：**&gt;
> 传入的网络类型（networkInfo.type）仅支持蜂窝网络（connection.NetBearType.BEARER_CELLULAR）和Wi-Fi网络（
> connection.NetBearType.BEARER_WIFI）。若传入其他值，接口会返回错误码9200012。&gt;
> 传入的起始时间（networkInfo.startTime）、结束时间（networkInfo.endTime）为秒级时间戳。若传入的起始时间、结束时间为负数，或起始时间大于结束时间，接口会返回错误码9200012。&gt;
> 传入的用户ID（accountId）非当前用户时，接口会返回错误码9200012。&gt;
> 建议查询的时间间隔（结束时间-起始时间）最小为1天，最大为30天。时间间隔太小，查询结果可能不准确。时间间隔太大，查询耗时会很长。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| bundleName | string | 是 |
| appIndex | number | 是 |
| accountId | number | 是 |
| networkInfo | statistics.NetworkInfo | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;statistics.NetStatsInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
