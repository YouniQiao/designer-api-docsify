# getUidForName

## getUidForName

```TypeScript
function getUidForName(v: string): number
```

根据指定的用户名，从系统的用户数据库中获取该用户的 uid。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getUidForName](arkts-arkts-process-processmanager-c.md#getUidForName)

<!--Device-process-function getUidForName(v: string): number--><!--Device-process-function getUidForName(v: string): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| v | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
let pres = process.getUidForName("tool");
```
