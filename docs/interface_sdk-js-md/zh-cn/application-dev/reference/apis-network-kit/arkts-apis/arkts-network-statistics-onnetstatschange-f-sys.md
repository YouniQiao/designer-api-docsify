# onNetStatsChange（系统接口）

## 导入模块

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## onNetStatsChange

```TypeScript
function onNetStatsChange(callback: Callback<NetStatsChangeInfo>): void
```

Register notifications of network traffic updates.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**需要权限：** ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function onNetStatsChange(callback: Callback<NetStatsChangeInfo>): void--><!--Device-statistics-function onNetStatsChange(callback: Callback<NetStatsChangeInfo>): void-End-->

**系统能力：** SystemCapability.Communication.NetManager.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetStatsChangeInfo&gt; | 是 | The callback of on. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |

