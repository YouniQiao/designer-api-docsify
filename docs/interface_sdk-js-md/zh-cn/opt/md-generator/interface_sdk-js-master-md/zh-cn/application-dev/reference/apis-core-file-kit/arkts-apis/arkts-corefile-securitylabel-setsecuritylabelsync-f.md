# setSecurityLabelSync

## setSecurityLabelSync

```TypeScript
function setSecurityLabelSync(path: string, type: DataLevel): void
```

以同步方法设置文件或目录的数据安全等级。数据安全等级仅可由低向高或平级设置。

**起始版本：** 9

<!--Device-securityLabel-function setSecurityLabelSync(path: string, type: DataLevel): void--><!--Device-securityLabel-function setSecurityLabelSync(path: string, type: DataLevel): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| type | [DataLevel](arkts-corefile-securitylabel-datalevel-t.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 13900037 |
| 13900007 |
| 13900001 |
| 13900015 |
| 13900025 |
| 13900041 |
| 13900042 |

## 示例

```TypeScript
let filePath = pathDir + '/test.txt';
securityLabel.setSecurityLabelSync(filePath, "s0");
```
