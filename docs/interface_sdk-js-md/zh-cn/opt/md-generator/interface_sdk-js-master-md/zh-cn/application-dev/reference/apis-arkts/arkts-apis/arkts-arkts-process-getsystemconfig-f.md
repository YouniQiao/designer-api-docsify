# getSystemConfig

## getSystemConfig

```TypeScript
function getSystemConfig(name: number): number
```

获取系统配置信息。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [process.ProcessManager.getSystemConfig](arkts-arkts-process-processmanager-c.md#getsystemconfig)

<!--Device-process-function getSystemConfig(name: number): number--><!--Device-process-function getSystemConfig(name: number): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
let _SC_ARG_MAX = 0;
let pres = process.getSystemConfig(_SC_ARG_MAX);
```
