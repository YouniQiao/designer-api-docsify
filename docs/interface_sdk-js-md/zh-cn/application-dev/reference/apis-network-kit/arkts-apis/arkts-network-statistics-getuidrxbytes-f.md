# getUidRxBytes

## 导入模块

```TypeScript
import { statistics } from '@kit.NetworkKit';
```

## getUidRxBytes

```TypeScript
function getUidRxBytes(uid: int, callback: AsyncCallback<long>): void
```

获取指定应用从最近一次开机开始至接口调用时刻的下行流量总和（单位：字节）。使用callback异步回调。

> **说明：**&gt;
> 若重启后该应用未产生流量消耗，则会抛出2103005错误码。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本26.0.0+：ohos.permission.GET_NETWORK_STATS

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
| [2103005](../errorcode-net-statistics.md#2103005-读取系统map失败) |
| [2103011](../errorcode-net-statistics.md#2103011-系统map创建失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

statistics.getUidRxBytes(20010038, (error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```

ArkTS-Sta示例：

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

statistics.getUidRxBytes(20010038, (error: BusinessError|null, stats: long|undefined) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```

ArkTS-Dyn示例：

```TypeScript
import { statistics } from '@kit.NetworkKit';

statistics.getUidRxBytes(20010038).then((stats: number) => {
  console.info(JSON.stringify(stats));
});
```

ArkTS-Sta示例：

```TypeScript
import { statistics } from '@kit.NetworkKit';

statistics.getUidRxBytes(20010038).then((stats: long) => {
  console.info(JSON.stringify(stats));
});
```


## getUidRxBytes

```TypeScript
function getUidRxBytes(uid: int): Promise<long>
```

获取指定应用从最近一次开机开始至接口调用时刻的下行流量总和（单位：字节）。使用Promise异步回调。

> **说明：**&gt;
> 若重启后该应用未产生流量消耗，则会抛出2103005错误码。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**需要权限：** 
- API版本26.0.0+：ohos.permission.GET_NETWORK_STATS

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uid | ArkTS-Dyn: number<br>ArkTS-Sta：int | 是 |

**返回值：**

| 类型 |
| --- |
| ArkTS-Dyn: Promise & lt;number & gt;<br>ArkTS-Sta：Promise & lt;long & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |
| [2103005](../errorcode-net-statistics.md#2103005-读取系统map失败) |
| [2103011](../errorcode-net-statistics.md#2103011-系统map创建失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

**示例**

参见 [getUidRxBytes](#getuidrxbytes)
