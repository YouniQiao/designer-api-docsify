# getDnsUnicode

## 导入模块

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## getDnsUnicode

```TypeScript
function getDnsUnicode(host: string, flag?: ConversionProcess): string
```

使用Punycode编码方式，将ASCII编码形式的主机名转换为Unicode编码形式，并通过可选的conversionProcess参数控制转换行为。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为23。

**系统能力：** SystemCapability.Communication.NetManager.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| host | string | 是 |
| flag | [ConversionProcess](arkts-network-connection-conversionprocess-e.md) | 否 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| [2100001](../errorcode-net-connection.md#2100001-非法参数值) |
| [2100002](../errorcode-net-connection.md#2100002-连接服务失败) |
| [2100003](../errorcode-net-connection.md#2100003-系统内部错误) |

**示例**

```TypeScript
import { connection } from '@kit.NetworkKit';

let result = connection.getDnsUnicode("www.xn--fsq092h.com", connection.ConversionProcess.NO_CONFIGURATION);
console.info("Succeeded to getDnsUnicode: " + result);  // 预期结果：www.示例.com
let result = connection.getDnsUnicode("www.example.com", connection.ConversionProcess.NO_CONFIGURATION);
console.info("Succeeded to getDnsUnicode: " + result);  // 预期结果：www.example.com
```
