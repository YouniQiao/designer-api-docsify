# getRunningProcessInformationByBundleType（系统接口）

## 导入模块

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## getRunningProcessInformationByBundleType

```TypeScript
function getRunningProcessInformationByBundleType(
    bundleType: bundleManager.BundleType): Promise<Array<ProcessInformation>>
```

根据包类型获取当前运行进程的有关信息。使用Promise异步回调。

**起始版本：** 12

**需要权限：** ohos.permission.GET_RUNNING_INFO

**系统能力：** SystemCapability.Ability.AbilityRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bundleType | bundleManager.BundleType | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;ProcessInformation & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [16000050](../errorcode-ability.md#16000050-内部错误) |
