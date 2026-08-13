# getSecurityLabelSync

## getSecurityLabelSync

```TypeScript
function getSecurityLabelSync(path: string): string
```

以同步方法获取文件或目录的数据安全等级。若未设置过数据安全等级则默认返回“s3”。

**起始版本：** 23

**废弃版本：** -1

<!--Device-securityLabel-function getSecurityLabelSync(path: string): string--><!--Device-securityLabel-function getSecurityLabelSync(path: string): string-End-->

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
let type = securityLabel.getSecurityLabelSync(filePath);
console.info("Succeeded in getting security label, Label: " + type);
```
