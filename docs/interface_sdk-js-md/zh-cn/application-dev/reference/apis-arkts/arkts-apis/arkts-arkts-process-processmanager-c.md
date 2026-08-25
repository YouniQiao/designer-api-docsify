# ProcessManager

提供进程管理相关接口，包括进程 UID 判断、用户信息查询、线程优先级获取、环境变量获取、进程退出和信号发送等功能。通过 `new process.ProcessManager()` 构造 ProcessManager 对象。

**起始版本：** 9

**系统能力：** SystemCapability.Utils.Lang

## 导入模块

```TypeScript
import { process } from 'kits/@kit.ArkTS';
```

## exit

```TypeScript
exit(code: number): void
```

终止程序。请谨慎使用此接口，此接口调用后应用会退出，如果输入参数非0，可能会导致数据丢失或出现未定义的运行异常。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| code | number | 是 |

## getEnvironmentVar

```TypeScript
getEnvironmentVar(name: string): string
```

获取环境变量对应的值。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | string | 是 |

**返回值：**

| 类型 |
| --- |
| string |

## getSystemConfig

```TypeScript
getSystemConfig(name: number): number
```

获取系统配置信息。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| name | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getThreadPriority

```TypeScript
getThreadPriority(v: number): number
```

根据指定的 tid 获取线程优先级。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| v | number | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getUidForName

```TypeScript
getUidForName(v: string): number
```

根据指定的用户名，从系统的用户数据库中获取该用户 uid。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| v | string | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## isAppUid

```TypeScript
isAppUid(v: number): boolean
```

判断 uid 是否属于当前应用程序。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Utils.Lang

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| v | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## kill

```TypeScript
kill(signal: number, pid: number): boolean
```

发送信号到指定的进程，结束指定进程（仅支持结束本进程）。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

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
