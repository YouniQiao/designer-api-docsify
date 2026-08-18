# ProcessManager

提供进程管理相关接口，包括进程 UID 判断、用户信息查询、线程优先级获取、环境变量获取、进程退出和信号发送等功能。 通过 `new process.ProcessManager()` 构造 ProcessManager 对象。

**起始版本：** 9

<!--Device-process-export class ProcessManager--><!--Device-process-export class ProcessManager-End-->

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
```

## exit

```TypeScript
exit(code: number): void
```

终止程序。 请谨慎使用此接口，此接口调用后应用会退出，如果输入参数非0，可能会导致数据丢失或出现未定义的运行异常。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ProcessManager-exit(code: number): void--><!--Device-ProcessManager-exit(code: number): void-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |

**示例**

```TypeScript
let processManager = new process.ProcessManager();
processManager.exit(0);
```

## getEnvironmentVar

```TypeScript
getEnvironmentVar(name: string): string
```

获取环境变量对应的值。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ProcessManager-getEnvironmentVar(name: string): string--><!--Device-ProcessManager-getEnvironmentVar(name: string): string-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

**示例**

```TypeScript
// 创建ProcessManager实例
let processManager = new process.ProcessManager();
// 获取PATH环境变量的值
let pres = processManager.getEnvironmentVar("PATH");
```

## getSystemConfig

```TypeScript
getSystemConfig(name: number): number
```

获取系统配置信息。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ProcessManager-getSystemConfig(name: number): number--><!--Device-ProcessManager-getSystemConfig(name: number): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
// 创建ProcessManager实例
let processManager = new process.ProcessManager();
// 定义系统配置参数
let _SC_ARG_MAX = 0;
// 获取系统配置信息
let pres = processManager.getSystemConfig(_SC_ARG_MAX);
```

## getThreadPriority

```TypeScript
getThreadPriority(v: number): number
```

根据指定的 tid 获取线程优先级。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ProcessManager-getThreadPriority(v: number): number--><!--Device-ProcessManager-getThreadPriority(v: number): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| v | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
// 创建ProcessManager实例
let processManager = new process.ProcessManager();
// 获取当前线程tid
let tid = process.tid;
// 根据tid获取线程优先级
let pres = processManager.getThreadPriority(tid);
```

## getUidForName

```TypeScript
getUidForName(v: string): number
```

根据指定的用户名，从系统的用户数据库中获取该用户 uid。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ProcessManager-getUidForName(v: string): number--><!--Device-ProcessManager-getUidForName(v: string): number-End-->

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| v | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**示例**

```TypeScript
// 创建ProcessManager实例
let processManager = new process.ProcessManager();
// 根据用户名获取uid
let pres = processManager.getUidForName("tool");
```

## isAppUid

```TypeScript
isAppUid(v: number): boolean
```

判断 uid 是否属于当前应用程序。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ProcessManager-isAppUid(v: number): boolean--><!--Device-ProcessManager-isAppUid(v: number): boolean-End-->

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
// 创建ProcessManager实例
let processManager = new process.ProcessManager();
// uid通过process.uid获取
let pres = process.uid;
// 判断uid是否属于当前应用程序
let result = processManager.isAppUid(pres);
console.info("result:", result); // result: true
```

## kill

```TypeScript
kill(signal: number, pid: number): boolean
```

发送信号到指定的进程，结束指定进程（仅支持结束本进程）。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-ProcessManager-kill(signal: number, pid: number): boolean--><!--Device-ProcessManager-kill(signal: number, pid: number): boolean-End-->

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
// 创建ProcessManager实例
let processManager = new process.ProcessManager();
// 获取当前进程pid
let pres = process.pid;
// 发送信号28结束当前进程
let result = processManager.kill(28, pres);
```
