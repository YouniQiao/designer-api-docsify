# printf

## 导入模块

```TypeScript
```

## printf

```TypeScript
function printf(format: string, ...args: Object[]): string
```

通过式样化字符串对输入的内容按特定格式输出。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [format](arkts-arkts-util-format-f.md#format)

<!--Device-util-function printf(format: string, ...args: Object[]): string--><!--Device-util-function printf(format: string, ...args: Object[]): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| format | string | 是 |
| [args](../../apis-arkdata/arkts-apis/arkts-arkdata-relationalstore-sqlinfo-i.md) | Object[] | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
let res = util.printf("%s", "hello world!");
console.info(res);
// 输出结果：hello world!
```
