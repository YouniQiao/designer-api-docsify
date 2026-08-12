# getThreadPriority

## getThreadPriority

```TypeScript
function getThreadPriority(v: number): number
```

根据指定的 tid 获取线程优先级，优先级顺序取决于当前操作系统。

**起始版本：** 8

**废弃版本：** 9

**替代接口：** [getThreadPriority](arkts-arkts-process-processmanager-c.md#getThreadPriority)

<!--Device-process-function getThreadPriority(v: number): number--><!--Device-process-function getThreadPriority(v: number): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| v | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## 示例

```TypeScript
let tid = process.tid;
let pres = process.getThreadPriority(tid);
```
