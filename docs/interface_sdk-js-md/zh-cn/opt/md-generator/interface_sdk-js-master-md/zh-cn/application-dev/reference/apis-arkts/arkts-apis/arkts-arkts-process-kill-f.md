# kill

## 导入模块

```TypeScript
```

## kill

```TypeScript
function kill(signal: number, pid: number): boolean
```

发送信号到指定进程，结束该进程。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** [kill](arkts-arkts-process-processmanager-c.md#kill)

<!--Device-process-function kill(signal: number, pid: number): boolean--><!--Device-process-function kill(signal: number, pid: number): boolean-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [signal](arkts-arkts-locks-asynclockoptions-c.md) | number | 是 |
| pid | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**示例**

```TypeScript
let pid = process.pid;
let result = process.kill(28, pid);
```
