# queryBundleStatsInfos

## queryBundleStatsInfos

```TypeScript
function queryBundleStatsInfos(admin: Want, startTime: number, endTime: number, accountId: number): Array<BundleStatsInfo>
```

查询指定用户账户在给定时间段内，各应用在前台运行的累计时长统计信息。查询的最小粒度是天，调用时需要传入起始时间（startTime）、结束时间（endTime）以及目标用户账户ID（accountId）。请求参数startTime 和endTime为毫秒级时间戳，支持调用方传入自定义值，startTime默认取当天的00:00:00.000，endTime默认取当天的24:00:00.000（即次日零点）。请求参数接口返回BundleStatsInfo数组， 每个元素包含一个应用的包名，其分身索引值及其对应时间段内的前台使用时长（毫秒级时间戳）。若startTime为0，则表示从设备首次开机的时间开始查询。若起始时间晚于结束时间，接口将返回错误码9200012。

**起始版本：** 26.0.0

**废弃版本：** -1

**需要权限：** ohos.permission.ENTERPRISE_MANAGE_APPLICATION

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-applicationManager-function queryBundleStatsInfos(admin: Want, startTime: number, endTime: number, accountId: number): Array<BundleStatsInfo>--><!--Device-applicationManager-function queryBundleStatsInfos(admin: Want, startTime: number, endTime: number, accountId: number): Array<BundleStatsInfo>-End-->

**系统能力：** SystemCapability.Customization.EnterpriseDeviceManager

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| admin | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | 是 |
| startTime | number | 是 |
| endTime | number | 是 |
| accountId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;BundleStatsInfo & gt; |

**错误码：**

| 错误码ID |
| --- |
| [9200012](../errorcode-enterpriseDeviceManager.md#9200012-参数校验失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [9200001](../errorcode-enterpriseDeviceManager.md#9200001-应用没有激活成设备管理器) |
| [9200002](../errorcode-enterpriseDeviceManager.md#9200002-设备管理器权限不够) |

## 示例

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 查询2026/4/15 00:00:00.000 ~ 2026/4/16 23:59:59.999的数据（月份从0开始计算）
  let startTime: number = new Date(2026, 3, 15, 0, 0, 0, 0).getTime();
  let endTime: number = new Date(2026, 3, 16, 23, 59, 59, 999).getTime();
  let accountId: number = 100;
  let result: Array<applicationManager.BundleStatsInfo> = applicationManager.queryBundleStatsInfos(wantTemp, startTime, endTime, accountId);
  console.info(`Succeeded in querying bundle stats infos, result : ${JSON.stringify(result)}`);
} catch(err) {
  console.error(`Failed to query bundle stats infos. Code: ${err.code}, message: ${err.message}`);
}
```

```TypeScript
import { applicationManager } from '@kit.MDMKit';
import { Want } from '@kit.AbilityKit';

let wantTemp: Want = {
  // 需根据实际情况进行替换
  bundleName: 'com.example.myapplication',
  abilityName: 'EnterpriseAdminAbility'
};

try {
  // 查询上个月的一个月的数据
  // 获取当前日期
  let currentDate: Date = new Date();
  // 计算上个月的第一天（月份从0开始，所以当前月份减1）
  let lastMonthFirstDay: Date = new Date(currentDate.getFullYear(), currentDate.getMonth() - 1, 1, 0, 0, 0, 0);
  // 计算上个月的最后一天（下个月第0天即为本月最后一天）
  let lastMonthLastDay: Date = new Date(currentDate.getFullYear(), currentDate.getMonth(), 0, 23, 59, 59, 999);
  
  let startTime: number = lastMonthFirstDay.getTime();
  let endTime: number = lastMonthLastDay.getTime();
  let accountId: number = 100;
  let result: Array<applicationManager.BundleStatsInfo> = applicationManager.queryBundleStatsInfos(wantTemp, startTime, endTime, accountId);
  console.info(`Succeeded in querying bundle stats infos, result : ${JSON.stringify(result)}`);
} catch(err) {
  console.error(`Failed to query bundle stats infos. Code: ${err.code}, message: ${err.message}`);
}
```
