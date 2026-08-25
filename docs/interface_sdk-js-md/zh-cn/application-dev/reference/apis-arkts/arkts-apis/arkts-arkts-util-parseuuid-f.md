# parseUUID

## 导入模块

```TypeScript
import { util } from 'kits/@kit.ArkTS';
```

## parseUUID

```TypeScript
function parseUUID(uuid: string): Uint8Array
```

将generateRandomUUID生成的string类型UUID转换为[generateRandomBinaryUUID](arkts-arkts-util-generaterandombinaryuuid-f.md)生成的UUID， 符合RFC 4122版本规范。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uuid | string | 是 |

**返回值：**

| 类型 |
| --- |
| Uint8Array |

**错误码：**

| 错误码ID |
| --- |
| [10200002](../errorcode-utils.md#10200002-参数解析错误) |
