# getSecurityLabelSync

## 导入模块

```TypeScript
import { securityLabel } from 'kits/@kit.CoreFileKit';
```

## getSecurityLabelSync

```TypeScript
function getSecurityLabelSync(path: string): string
```

以同步方法获取文件或目录的数据安全等级。若未设置过数据安全等级则默认返回“s3”。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**错误码：**

| 错误码ID |
| --- |
| 13900001 |
| 13900007 |
| 13900015 |
| 13900020 |
| 13900025 |
| 13900037 |
| 13900041 |
| 13900042 |
