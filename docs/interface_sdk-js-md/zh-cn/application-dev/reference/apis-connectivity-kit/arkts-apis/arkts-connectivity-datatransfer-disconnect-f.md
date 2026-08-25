# disconnect

## 导入模块

```TypeScript
import { dataTransfer } from 'kits/@kit.ConnectivityKit';
```

## disconnect

```TypeScript
function disconnect(params: ConnectionParams): Promise<void>
```

断连远端设备。需在通过[dataTransfer.connect](arkts-connectivity-datatransfer-connect-f.md)成功建立连接后调用，用于断开已建立的远端设备连接。使用Promise异步回调。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.ACCESS_NEARLINK

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| params | [ConnectionParams](arkts-connectivity-datatransfer-connectionparams-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [36100003](../errorcode-nearlink-service.md#36100003-星闪关闭) |
| [36100041](../errorcode-nearlink-service.md#36100041-无效地址) |
| [36100043](../errorcode-nearlink-service.md#36100043-无效uuid) |
| [36100044](../errorcode-nearlink-service.md#36100044-禁止使用星闪标准服务uuid) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
