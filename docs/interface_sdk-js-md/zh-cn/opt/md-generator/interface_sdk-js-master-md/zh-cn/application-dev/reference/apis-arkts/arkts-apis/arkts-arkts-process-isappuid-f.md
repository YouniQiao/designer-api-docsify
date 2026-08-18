# isAppUid

## 导入模块

```TypeScript
```

## isAppUid

```TypeScript
function isAppUid(v: number): boolean
```

判断 uid 是否属于应用程序。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [isAppUid](arkts-arkts-process-processmanager-c.md#isappuid)

<!--Device-process-function isAppUid(v: number): boolean--><!--Device-process-function isAppUid(v: number): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| v | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
// uid通过process.uid获取
let pres = process.uid;
let result = process.isAppUid(pres);
```
