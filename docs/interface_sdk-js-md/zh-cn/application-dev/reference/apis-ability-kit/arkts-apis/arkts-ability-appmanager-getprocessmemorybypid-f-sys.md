# getProcessMemoryByPid（系统接口）

## 导入模块

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## getProcessMemoryByPid

```TypeScript
function getProcessMemoryByPid(pid: number): Promise<number>
```

通过pid查询对应进程占用的内存大小。使用Promise异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pid | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |


## getProcessMemoryByPid

```TypeScript
function getProcessMemoryByPid(pid: number, callback: AsyncCallback<number>): void
```

通过pid查询对应进程占用的内存大小。使用callback异步回调。

**起始版本：** 10

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pid | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
