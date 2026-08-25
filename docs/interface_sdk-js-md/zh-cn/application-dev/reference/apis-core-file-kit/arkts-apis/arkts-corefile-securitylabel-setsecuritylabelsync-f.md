# setSecurityLabelSync

## 导入模块

```TypeScript
import { securityLabel } from 'kits/@kit.CoreFileKit';
```

## setSecurityLabelSync

```TypeScript
function setSecurityLabelSync(path: string, type: DataLevel): void
```

以同步方法设置文件或目录的数据安全等级，用于实现文件的分级管理和访问控制。

**起始版本：** 9

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| type | [DataLevel](arkts-corefile-securitylabel-datalevel-t.md) | 是 |

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
