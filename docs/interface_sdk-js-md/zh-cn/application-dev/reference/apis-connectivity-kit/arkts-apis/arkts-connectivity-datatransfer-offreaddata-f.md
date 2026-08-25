# offReadData

## 导入模块

```TypeScript
import { dataTransfer } from 'kits/@kit.ConnectivityKit';
```

## offReadData

```TypeScript
function offReadData(callback?: Callback<DataParams>): void
```

取消订阅端口通道数据接收事件。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataParams](arkts-connectivity-datatransfer-dataparams-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
