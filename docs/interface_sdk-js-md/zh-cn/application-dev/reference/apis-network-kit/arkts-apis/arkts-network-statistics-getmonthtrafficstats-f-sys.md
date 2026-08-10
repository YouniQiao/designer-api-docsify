# getMonthTrafficStats（系统接口）

## 导入模块

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## getMonthTrafficStats

```TypeScript
function getMonthTrafficStats(simId: int): Promise<long>
```

Get this month traffic data of the cellular network.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.GET_NETWORK_STATS

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-statistics-function getMonthTrafficStats(simId: int): Promise<long>--><!--Device-statistics-function getMonthTrafficStats(simId: int): Promise<long>-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| simId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | The id of the specified sim card. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | The statistics of the simId in this month. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2100001 | Invalid parameter value. |
| 2100002 | Failed to connect to the service. |
| 201 | Permission denied. |
| 202 | Nonsystem applications use system APIs. |

